---
name: pbi-raio-x
description: Gera o Raio-X de um modelo Power BI (PBIP/TMDL) — tabelas classificadas (fato, dimensão, ponte, calendário, field parameter, auxiliar), medidas com DAX e descrição, árvore de dependência e impacto de cada medida, uso no relatório, e achados de boas práticas com nota 0–100 — para ver na tela Raio-X da plataforma da formação. Use quando o usuário pedir "raio-x do modelo", "audita o modelo", "o modelo está pronto pra produção?", "onde essa medida é usada?", "o que quebra se eu mudar essa medida?", "quais medidas não são usadas", ou apontar uma pasta .SemanticModel.
---

# /pbi-raio-x

Autoria: Jessé Freire · Indicium AI.

Lê o TMDL de um PBIP e gera um JSON que a plataforma mostra na tela **Raio-X**: nota,
achados, tabelas, medidas e o grafo de dependências. Só biblioteca padrão do Python;
não precisa do Power BI Desktop aberto.

## Uso

```bash
# Na raiz do repositório da formação
python ~/.claude/skills/pbi-raio-x/scripts/raio_x.py "<pasta X.SemanticModel>" \
  --saida raio-x/<nome-em-ascii>.json --nome "Rótulo na plataforma"
python .claude/skills/ae_materials_app/sync.py
```

- Se existir a pasta `X.Report` ao lado, o script lê o relatório e marca medidas órfãs.
- `raio-x/` é versionada **só para modelos de treino** (BanVic, desafio). Modelo de
  projeto real: gerar com `--saida` fora do repositório — o repo é público.

## O que o JSON traz

| Campo | Conteúdo |
|---|---|
| `nota`, `contagem` | nota 0–100 e achados por severidade |
| `tabelas` | tipo, descrição, colunas (tipo de dado, chave, oculta, calculada, agregação, ordenação) |
| `medidas` | DAX, descrição, formato, `usa_medidas`, `usa_colunas`, `impacta` (quem depende, direta ou indiretamente), `usada_no_relatorio` |
| `relacionamentos` | de/para, cardinalidade, bidirecional, ativo |
| `achados` | id, severidade, título, onde, por que importa, como corrigir |
| `dependencias` | nós e ligações para o grafo |

## Classificação das tabelas

Field parameter (partição com `NAMEOF`) → calendário (`dataCategory: Time` ou nome de
datas) → ponte (`bridge_`/`ponte_`) → fato (lado "muitos" de 2+ relacionamentos) →
dimensão (lado "um") → auxiliar (o resto: tabela de medidas, tabela calculada).

## Checks

| Id | Severidade | O que procura |
|---|---|---|
| `rel-bidirecional` | crítico (leve se envolve ponte) | `crossFilteringBehavior: bothDirections` |
| `rel-inativo-sem-uso` | médio | relacionamento inativo sem `USERELATIONSHIP` no modelo |
| `coluna-somavel` | médio | chave, ano, mês ou status numérico com agregação ≠ none |
| `mes-sem-ordenacao` | médio | nome do mês em texto sem `sortByColumn` |
| `coluna-calculada` | médio na fato, leve fora | coluna calculada — avaliar se vira medida |
| `divisao-com-barra` | médio | `/` em vez de `DIVIDE` (nomes entre aspas e colchetes ignorados) |
| `filter-tabela-inteira` | médio na fato/ponte, leve fora | `FILTER(tabela, …)` |
| `dimensao-sem-chave` | leve | dimensão sem coluna `isKey` |
| `tabela-sem-descricao` | leve | fato, dimensão, ponte ou calendário sem `///` |
| `medida-sem-descricao` | leve | medida sem `///` |
| `medida-sem-formato` | leve | razão, % ou valor sem `formatString` (medida de texto não conta) |
| `medida-orfa` | leve | não usada por visual, filtro, outra medida nem field parameter |

**Nota** = 100 − (8 × crítico + 3 × médio + 1 × leve), cada check contando no máximo 3
ocorrências (repetição é hábito a corrigir, não erro multiplicado). Mínimo 0.

## Leitura do resultado

- Achado é **ponto de atenção**, não sentença: bidirecional em ponte muitos-para-muitos e
  `FILTER` numa dimensão pequena costumam ser escolhas conscientes. Registre o motivo.
- Antes de apagar medida órfã, confirme que não é usada em outro relatório conectado ao
  mesmo modelo.
- Para conferir número depois de corrigir, use a skill `reconciliacao-numeros`.
