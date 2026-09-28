#!/usr/bin/env python3
"""Raio-X de um modelo semântico do Power BI (PBIP/TMDL).

Uso:
  python raio_x.py "<pasta X.SemanticModel>" --saida "<raiz>/raio-x/<nome>.json" [--nome "Rótulo"]

Lê o TMDL (tabelas, colunas, medidas, partições, relacionamentos), classifica as tabelas,
monta a árvore de dependência das medidas, cruza com o uso no relatório (.Report irmão,
se existir) e roda os checks de boas práticas. Saída: um JSON para a tela Raio-X da
plataforma da formação. Só biblioteca padrão.

Autoria: Jessé Freire · Indicium AI
"""
import argparse
import datetime
import json
import re
import sys
import urllib.parse
from pathlib import Path

AUTORIA = "Jessé Freire · Indicium AI"
OBJETOS = {"column", "measure", "partition", "hierarchy", "calculationGroup", "calculationItem"}
PESO = {"critico": 8, "medio": 3, "leve": 1}
LIMITE_REPETICAO = 3
NUMERICOS = {"int64", "decimal", "double"}


# ---------------------------------------------------------------- leitura do TMDL
def _tabs(linha):
    return len(linha) - len(linha.lstrip("\t"))


def _desaspear(nome):
    nome = nome.strip()
    if len(nome) >= 2 and nome[0] == "'" and nome[-1] == "'":
        return nome[1:-1].replace("''", "'")
    return nome


CABECALHO = re.compile(r"^(\w+)\s+('(?:[^']|'')*'|[^\s=]+)\s*(?:=\s*(.*))?$")


def _bloco_expressao(linhas, i, nivel_min):
    """Lê linhas seguintes com indentação >= nivel_min (expressão multilinha).
    Suporta o bloco cercado por ``` que o TMDL usa para expressões com linhas em branco."""
    corpo = []
    if i < len(linhas) and linhas[i].strip() == "```":
        i += 1
        while i < len(linhas) and linhas[i].strip() != "```":
            corpo.append(linhas[i].strip("\t"))
            i += 1
        return "\n".join(corpo), i + 1
    while i < len(linhas):
        l = linhas[i]
        if l.strip() and _tabs(l) < nivel_min:
            break
        corpo.append(l[nivel_min:] if l.startswith("\t" * nivel_min) else l.strip())
        i += 1
    while corpo and not corpo[-1].strip():
        corpo.pop()
    return "\n".join(corpo), i


def ler_tabela(caminho):
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    tabela = {"nome": None, "descricao": "", "props": {}, "colunas": [], "medidas": [],
              "particoes": [], "hierarquias": []}
    descricao, atual, i = [], None, 0
    while i < len(linhas):
        l = linhas[i]
        s = l.strip()
        n = _tabs(l)
        if not s:
            i += 1
            continue
        if s.startswith("///"):
            descricao.append(s[3:].strip())
            i += 1
            continue
        m = CABECALHO.match(s)
        if n == 0 and m and m.group(1) == "table":
            tabela["nome"] = _desaspear(m.group(2))
            tabela["descricao"] = " ".join(descricao)
            descricao, atual = [], None
            i += 1
            continue
        if n == 1 and m and m.group(1) in OBJETOS:
            tipo, nome, resto = m.group(1), _desaspear(m.group(2)), m.group(3)
            atual = {"tipo": tipo, "nome": nome, "descricao": " ".join(descricao), "props": {},
                     "expressao": None}
            descricao = []
            i += 1
            if resto is not None:
                resto = resto.strip()
                if resto and resto != "```":
                    atual["expressao"] = resto
                else:
                    if resto == "```":
                        i -= 1
                        linhas[i] = "\t" * 3 + "```"
                    atual["expressao"], i = _bloco_expressao(linhas, i, 3)
            destino = {"column": "colunas", "measure": "medidas", "partition": "particoes",
                       "hierarchy": "hierarquias"}.get(tipo)
            if destino:
                tabela[destino].append(atual)
            continue
        if n == 1:
            # propriedade da própria tabela
            atual = None
            _ler_prop(tabela["props"], s)
            i += 1
            continue
        if n >= 2 and atual is not None:
            if re.match(r"^(source|expression)\s*=\s*$", s):
                chave = s.split("=")[0].strip()
                atual["props"][chave], i = _bloco_expressao(linhas, i + 1, n + 1)
                continue
            _ler_prop(atual["props"], s)
            i += 1
            continue
        i += 1
    return tabela


def _ler_prop(props, s):
    if s.startswith(("annotation ", "extendedProperty ", "changedProperty")):
        props.setdefault("_extras", []).append(s)
        return
    m = re.match(r"^(\w+)\s*:\s*(.*)$", s)
    if m:
        props[m.group(1)] = m.group(2).strip()
        return
    m = re.match(r"^(\w+)\s*=\s*(.*)$", s)
    if m:
        props[m.group(1)] = m.group(2).strip()
        return
    props[s] = True  # flag sem valor: isHidden, isKey...


REF_COLUNA = re.compile(r"^('(?:[^']|'')*'|[^.]+)\.('(?:[^']|'')*'|.+)$")


def ler_relacionamentos(caminho):
    rels, atual = [], None
    if not caminho.exists():
        return rels
    for l in caminho.read_text(encoding="utf-8").splitlines():
        s = l.strip()
        if not s:
            continue
        if _tabs(l) == 0 and s.startswith("relationship "):
            atual = {"id": s.split(" ", 1)[1], "props": {}}
            rels.append(atual)
        elif atual is not None:
            _ler_prop(atual["props"], s)
    saida = []
    for r in rels:
        p = r["props"]
        def parte(v):
            m = REF_COLUNA.match(v or "")
            return (_desaspear(m.group(1)), _desaspear(m.group(2))) if m else (v, "")
        de_t, de_c = parte(p.get("fromColumn"))
        para_t, para_c = parte(p.get("toColumn"))
        saida.append({
            "de_tabela": de_t, "de_coluna": de_c, "para_tabela": para_t, "para_coluna": para_c,
            "bidirecional": p.get("crossFilteringBehavior") == "bothDirections",
            "ativo": p.get("isActive", "true") != "false",
            "cardinalidade": f"{p.get('fromCardinality', 'many')}:{p.get('toCardinality', 'one')}",
        })
    return saida


# ---------------------------------------------------------------- DAX
def limpar_dax(dax):
    """Tira comentários e strings, para as referências não virem de texto."""
    dax = re.sub(r"/\*.*?\*/", " ", dax, flags=re.S)
    dax = re.sub(r'"(?:[^"]|"")*"', '""', dax)
    dax = re.sub(r"(//|--)[^\n]*", " ", dax)
    return dax


REF_QUALIFICADA = re.compile(r"('(?:[^']|'')*'|\b[A-Za-z_]\w*)\s*\[([^\]]+)\]")
REF_SOLTA = re.compile(r"\[([^\]]+)\]")


def referencias(dax, medidas):
    limpo = limpar_dax(dax or "")
    usa_m, usa_c, ambiguas = set(), set(), set()
    for tab, nome in REF_QUALIFICADA.findall(limpo):
        t = _desaspear(tab)
        if nome in medidas:
            usa_m.add(nome)
        else:
            usa_c.add(f"{t}[{nome}]")
    sem_qualificadas = REF_QUALIFICADA.sub(" ", limpo)
    for nome in REF_SOLTA.findall(sem_qualificadas):
        if nome in medidas:
            usa_m.add(nome)
        else:
            ambiguas.add(nome)
    return sorted(usa_m), sorted(usa_c), sorted(ambiguas)


# ---------------------------------------------------------------- relatório
def usos_no_relatorio(pasta_modelo):
    rel = pasta_modelo.with_name(pasta_modelo.name.replace(".SemanticModel", ".Report")) / "definition"
    if not rel.is_dir():
        return None
    usadas = set()

    def andar(no):
        if isinstance(no, dict):
            med = no.get("Measure")
            if isinstance(med, dict) and "Property" in med:
                usadas.add(med["Property"])
            for v in no.values():
                andar(v)
        elif isinstance(no, list):
            for v in no:
                andar(v)

    for arq in rel.rglob("*.json"):
        try:
            andar(json.loads(arq.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
    return usadas


# ---------------------------------------------------------------- classificação
def classificar(tabelas, rels):
    lado_muitos, lado_um = {}, {}
    for r in rels:
        lado_muitos[r["de_tabela"]] = lado_muitos.get(r["de_tabela"], 0) + 1
        lado_um[r["para_tabela"]] = lado_um.get(r["para_tabela"], 0) + 1
    for t in tabelas:
        nome = t["nome"]
        fontes = " ".join(str(p["props"].get("source", "")) + " " + str(p.get("expressao") or "")
                          for p in t["particoes"])
        calculada = any((p.get("expressao") or "").strip().startswith("calculated") for p in t["particoes"])
        extras = " ".join(" ".join(c["props"].get("_extras", [])) for c in t["colunas"])
        if "NAMEOF" in fontes or "ParameterMetadata" in extras:
            tipo = "field parameter"
        elif t["props"].get("dataCategory") == "Time" or re.search(r"(^|_)(dim_)?(date|dates|data|datas|calend)", nome, re.I):
            tipo = "calendário"
        elif nome.lower().startswith(("bridge", "ponte")):
            tipo = "ponte"
        elif lado_muitos.get(nome, 0) >= 2:
            tipo = "fato"
        elif lado_um.get(nome, 0) >= 1:
            tipo = "dimensão"
        elif calculada or not t["colunas"] or all(c["props"].get("isHidden") for c in t["colunas"]):
            tipo = "auxiliar"
        else:
            tipo = "auxiliar"
        t["tipo"] = tipo


# ---------------------------------------------------------------- checks
def checks(tabelas, medidas, rels, usadas_relatorio):
    achados = []

    def achado(id_, sev, titulo, onde, por_que, como):
        achados.append({"id": id_, "severidade": sev, "titulo": titulo, "onde": onde,
                        "por_que": por_que, "como_corrigir": como})

    tipo_de = {t["nome"]: t["tipo"] for t in tabelas}
    dax_total = " ".join(m["dax"] or "" for m in medidas)

    for r in rels:
        onde = f"{r['de_tabela']}[{r['de_coluna']}] → {r['para_tabela']}[{r['para_coluna']}]"
        if r["bidirecional"]:
            ponte = "ponte" in (tipo_de.get(r["de_tabela"]), tipo_de.get(r["para_tabela"]))
            achado("rel-bidirecional", "leve" if ponte else "critico",
                   "Relacionamento com filtro nos dois sentidos", onde,
                   "Filtro bidirecional cria caminhos ambíguos entre tabelas e deixa o motor mais lento. "
                   + ("Em ponte muitos-para-muitos costuma ser intencional — só confirme que é." if ponte
                      else "Fora de uma ponte, raramente é necessário."),
                   "Troque para filtro único e, onde precisar do outro sentido, use CROSSFILTER dentro da medida.")
        if not r["ativo"] and "USERELATIONSHIP" not in dax_total.upper():
            achado("rel-inativo-sem-uso", "medio", "Relacionamento inativo que nenhuma medida usa", onde,
                   "Relacionamento inativo só tem efeito via USERELATIONSHIP; sem isso, é peso morto e confunde quem mantém.",
                   "Remova o relacionamento ou crie a medida que o ativa com USERELATIONSHIP.")

    for t in tabelas:
        if t["tipo"] == "dimensão" and not any(c["props"].get("isKey") for c in t["colunas"]):
            achado("dimensao-sem-chave", "leve", "Dimensão sem coluna marcada como chave", t["nome"],
                   "Marcar a chave (isKey) documenta a unicidade da linha e ajuda recursos de IA e de "
                   "relacionamento a entenderem o modelo.",
                   "No TMDL, acrescente `isKey` na coluna de chave primária da tabela.")
        if t["tipo"] in ("fato", "dimensão", "ponte", "calendário") and not t["descricao"]:
            achado("tabela-sem-descricao", "leve", "Tabela sem descrição", t["nome"],
                   "Quem abre o modelo não sabe o grão nem o papel da tabela sem ler o código.",
                   "Acrescente `///` acima de `table` com grão e papel (ex.: 'fato no grão do item do pedido').")
        for c in t["colunas"]:
            p = c["props"]
            onde = f"{t['nome']}[{c['nome']}]"
            chave_ou_atributo = re.search(r"(_key|_id|key|id|^year|^month|^quarter|^ano|^mes|^trimestre|status)$",
                                          c["nome"], re.I)
            if p.get("dataType") in NUMERICOS and chave_ou_atributo and p.get("summarizeBy", "none") != "none":
                achado("coluna-somavel", "medio", "Chave ou atributo numérico com agregação automática", onde,
                       f"Com summarizeBy: {p.get('summarizeBy')}, arrastar a coluna soma códigos ou anos — número sem sentido.",
                       "Defina `summarizeBy: none`.")
            if (re.search(r"(month|mes)[\s_]*(name|nome)?$", c["nome"], re.I) and p.get("dataType") == "string"
                    and not p.get("sortByColumn")):
                achado("mes-sem-ordenacao", "medio", "Nome do mês sem coluna de ordenação", onde,
                       "Sem sortByColumn o mês ordena em ordem alfabética (abril, agosto, dezembro…).",
                       "Defina `sortByColumn` apontando para o número do mês.")
            if c.get("expressao"):
                achado("coluna-calculada", "medio" if t["tipo"] == "fato" else "leve",
                       "Coluna calculada — avaliar se vira medida", onde,
                       "Coluna calculada é gravada em memória a cada atualização e aumenta o modelo; "
                       "se ela só é agregada, uma medida faz o mesmo sem custo de armazenamento.",
                       "Se não é usada como filtro ou eixo, converta em medida e troque as referências.")

    for m in medidas:
        onde = f"{m['tabela']}[{m['nome']}]"
        limpo = limpar_dax(m["dax"] or "")
        if not m["descricao"]:
            achado("medida-sem-descricao", "leve", "Medida sem descrição", onde,
                   "A descrição aparece no painel de campos e documenta a regra de negócio dentro do arquivo.",
                   "Acrescente `///` acima da medida explicando o que ela calcula.")
        # Tira nomes de tabela/coluna/medida antes: 'Métrica (Receita/Pedidos)' não é divisão.
        sem_nomes = re.sub(r"'(?:[^']|'')*'|\[[^\]]*\]", " X ", limpo)
        if re.search(r"[\w)]\s*/\s*[\w(]", sem_nomes):
            achado("divisao-com-barra", "medio", "Divisão com / em vez de DIVIDE", onde,
                   "Divisão por zero ou BLANK com / devolve erro ou infinito no visual.",
                   "Use DIVIDE(numerador, denominador) — trata zero e BLANK.")
        if re.search(r"FILTER\s*\(\s*('(?:[^']|'')*'|[A-Za-z_]\w*)\s*,", limpo, re.I):
            alvo = re.search(r"FILTER\s*\(\s*('(?:[^']|'')*'|[A-Za-z_]\w*)\s*,", limpo, re.I).group(1)
            if _desaspear(alvo) in tipo_de:
                sev = "medio" if tipo_de[_desaspear(alvo)] in ("fato", "ponte") else "leve"
                achado("filter-tabela-inteira", sev, "FILTER sobre a tabela inteira", onde,
                       f"FILTER({_desaspear(alvo)}, …) percorre a tabela linha a linha e costuma ser o gargalo da medida.",
                       "Filtre só a coluna: CALCULATE([m], tabela[coluna] = valor) ou FILTER(VALUES(tabela[coluna]), …).")
        # Medida de texto (título, nome do destaque, rótulo) não precisa de formatString.
        texto = (re.search(r"\b(FORMAT|CONCATENATEX|UNICHAR)\s*\(|&", limpo)
                 or '"' in (m["dax"] or "")
                 or re.search(r"(texto|legenda|t[ií]tulo|predominante|destaque|maior)", m["nome"], re.I))
        numero_sensivel = ("DIVIDE" in limpo.upper() or re.search(r"[\w)]\s*/\s*[\w(]", sem_nomes)
                           or re.search(r"(%|receita|valor|ticket|taxa|pre[cç]o|custo)", m["nome"], re.I))
        if not m["formato"] and not texto and numero_sensivel:
            achado("medida-sem-formato", "leve", "Medida sem formato definido", onde,
                   "Sem formatString cada visual mostra o número de um jeito (casas, moeda, %).",
                   "Defina `formatString` na medida.")
        if usadas_relatorio is not None and not m["impacta"] and m["nome"] not in usadas_relatorio \
                and not m.get("usada_por_parametro"):
            achado("medida-orfa", "leve", "Medida que nenhum visual nem outra medida usa", onde,
                   "Medida sem uso aumenta a lista de campos e o custo de manutenção.",
                   "Confirme se é resto de teste; se for, remova.")
    return achados


# ---------------------------------------------------------------- montagem
def raio_x(pasta, nome=None):
    definicao = pasta / "definition"
    tabelas = [ler_tabela(p) for p in sorted((definicao / "tables").glob("*.tmdl"))]
    for t, p in zip(tabelas, sorted((definicao / "tables").glob("*.tmdl"))):
        t["nome"] = t["nome"] or urllib.parse.unquote(p.stem)
    rels = ler_relacionamentos(definicao / "relationships.tmdl")
    classificar(tabelas, rels)

    nomes_medidas = {m["nome"] for t in tabelas for m in t["medidas"]}
    fontes_parametros = " ".join(str(p["props"].get("source", "")) for t in tabelas
                                 if t["tipo"] == "field parameter" for p in t["particoes"])
    medidas = []
    for t in tabelas:
        for m in t["medidas"]:
            usa_m, usa_c, amb = referencias(m["expressao"], nomes_medidas)
            medidas.append({
                "nome": m["nome"], "tabela": t["nome"], "descricao": m["descricao"],
                "dax": m["expressao"] or "", "formato": m["props"].get("formatString", ""),
                "pasta": m["props"].get("displayFolder", ""), "usa_medidas": usa_m,
                "usa_colunas": usa_c, "ambiguas": amb,
                "usada_por_parametro": f"[{m['nome']}]" in fontes_parametros,
            })

    # impacto: quem depende de cada medida, direta ou indiretamente
    dependentes = {m["nome"]: set() for m in medidas}
    for m in medidas:
        for u in m["usa_medidas"]:
            dependentes.setdefault(u, set()).add(m["nome"])
    for m in medidas:
        vistos, pilha = set(), list(dependentes.get(m["nome"], ()))
        while pilha:
            x = pilha.pop()
            if x not in vistos:
                vistos.add(x)
                pilha.extend(dependentes.get(x, ()))
        m["impacta"] = sorted(vistos)

    usadas = usos_no_relatorio(pasta)
    for m in medidas:
        m["usada_no_relatorio"] = None if usadas is None else m["nome"] in usadas

    achados = checks(tabelas, medidas, rels, usadas)
    contagem = {s: sum(1 for a in achados if a["severidade"] == s) for s in PESO}
    # O mesmo problema repetido pesa no máximo LIMITE vezes: onze tabelas sem descrição são
    # um hábito a corrigir, não onze erros graves.
    por_check = {}
    for a in achados:
        chave = (a["id"], a["severidade"])
        por_check[chave] = por_check.get(chave, 0) + 1
    nota = max(0, 100 - sum(PESO[sev] * min(n, LIMITE_REPETICAO) for (_, sev), n in por_check.items()))

    nos, ligacoes = [], []
    for m in medidas:
        nos.append({"id": "m:" + m["nome"], "tipo": "medida", "rotulo": m["nome"], "tabela": m["tabela"]})
        for u in m["usa_medidas"]:
            ligacoes.append(["m:" + m["nome"], "m:" + u])
        for c in m["usa_colunas"]:
            ligacoes.append(["m:" + m["nome"], "c:" + c])
    for c in sorted({c for m in medidas for c in m["usa_colunas"]}):
        nos.append({"id": "c:" + c, "tipo": "coluna", "rotulo": c})

    por_tipo = {}
    for t in tabelas:
        por_tipo[t["tipo"]] = por_tipo.get(t["tipo"], 0) + 1

    return {
        "modelo": nome or pasta.name.replace(".SemanticModel", ""),
        "gerado_em": datetime.datetime.now().isoformat(timespec="seconds"),
        "autoria": AUTORIA,
        "nota": nota, "contagem": contagem,
        "pesos": PESO, "limite_repeticao": LIMITE_REPETICAO,
        "resumo": {"tabelas": len(tabelas), "colunas": sum(len(t["colunas"]) for t in tabelas),
                   "medidas": len(medidas), "relacionamentos": len(rels), "por_tipo": por_tipo,
                   "relatorio_lido": usadas is not None},
        "tabelas": [{
            "nome": t["nome"], "tipo": t["tipo"], "descricao": t["descricao"],
            "oculta": bool(t["props"].get("isHidden")), "medidas": len(t["medidas"]),
            "colunas": [{"nome": c["nome"], "tipo_dado": c["props"].get("dataType", ""),
                         "chave": bool(c["props"].get("isKey")), "oculta": bool(c["props"].get("isHidden")),
                         "calculada": bool(c.get("expressao")), "agregacao": c["props"].get("summarizeBy", ""),
                         "ordenar_por": c["props"].get("sortByColumn", "")} for c in t["colunas"]],
        } for t in tabelas],
        "medidas": medidas,
        "relacionamentos": rels,
        "achados": sorted(achados, key=lambda a: -PESO[a["severidade"]]),
        "dependencias": {"nos": nos, "ligacoes": ligacoes},
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("pasta", help="pasta X.SemanticModel do PBIP")
    p.add_argument("--saida", required=True, help="arquivo .json de saída (ex.: raio-x/modelo.json)")
    p.add_argument("--nome", help="rótulo do modelo na plataforma")
    args = p.parse_args()

    pasta = Path(args.pasta)
    if not (pasta / "definition" / "tables").is_dir():
        print(f"erro: {pasta} não tem definition/tables — aponte para a pasta .SemanticModel de um PBIP")
        return 1
    resultado = raio_x(pasta, args.nome)
    saida = Path(args.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    r = resultado["resumo"]
    print(f"ok: {saida}")
    print(f"   {r['tabelas']} tabelas, {r['colunas']} colunas, {r['medidas']} medidas, "
          f"{r['relacionamentos']} relacionamentos · {r['por_tipo']}")
    print(f"   nota {resultado['nota']}/100 · {resultado['contagem']} · relatório lido: {r['relatorio_lido']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
