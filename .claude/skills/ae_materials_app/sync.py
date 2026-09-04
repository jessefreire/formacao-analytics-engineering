#!/usr/bin/env python3
"""
ae-materials-app — Sincroniza arquivos de módulo no index.html
Uso: python .opencode/skill/ae_materials_app/sync.py
"""
import re
import json
from pathlib import Path
from typing import List, Dict, Any

# Encontra raiz do projeto (procura AGENTS.md como marcador)
def find_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path(__file__).resolve().parent.parent.parent.parent

ROOT = find_root()
INDEX = ROOT / "index.html"
TEMPLATE = Path(__file__).parent / "templates" / "index.html.j2"
FILES_JSON = ROOT / "files.json"
VERSION_JSON = ROOT / "version.json"

# Módulos na ordem do curso. `sort` controla ordenação (IV=3.5 fica entre 3 e 4)
MODULES = [
    {"num": 0,  "sort": 0.5, "title": "Banco de Dados BanVic"},
    {"num": 1,  "sort": 1,   "title": "Introdução à Análise de Dados"},
    {"num": 2,  "sort": 2,   "title": "SQL"},
    {"num": 3,  "sort": 3,   "title": "Modelagem de dados"},
    {"num": "IV", "sort": 3.5, "title": "Engenharia de Dados com dbt e Snowflake"},
    {"num": 4,  "sort": 4,   "title": "Storytelling com Dados"},
    {"num": 5,  "sort": 5,   "title": "Design de Experiência"},
    {"num": 6,  "sort": 6,   "title": "Dashboards com Power BI"},
    {"num": 7,  "sort": 7,   "title": "Estatística aplicada à análise de dados"},
    {"num": 8,  "sort": 8,   "title": "Python"},
    {"num": 9,  "sort": 9,   "title": "AI-Powered Productivity"},
    # Material extra (fora da grade oficial): pasta e rotulo explicitos, porque
    # o regex ^Modulo N nao casa e o numero 9 ja e do modulo oficial acima.
    {
        "num": "Extra", "sort": 9.5,
        "title": "Curso SQL Completo (YouTube)",
        "folder": "Extra - Curso SQL Completo (YouTube)",
        "cat": "Extra - Curso SQL Completo (YouTube)",
    },
]

# Padrão de nome de pasta de módulo (usado por find_module_folder)
MODULE_FOLDER_RE = r"^[Mm][óo]dulo\s+{num}\b"

# Mapa sort -> módulo para lookup
MODULE_BY_SORT = {m["sort"]: m for m in MODULES}

# Regex para detectar versão em inglês
EN_RE = re.compile(r'(English|EN-US|Copy of|Asynchronous)', re.IGNORECASE)

# Regex para detectar resumos/decorebas pessoais (não são material oficial)
PERSONAL_RE = re.compile(r'(resumo|decoreba|aprofundamento)', re.IGNORECASE)

# Heading genéricos de fechamento de apresentação (não são títulos reais)
GENERIC_HEADINGS = {
    "thank you", "thanks", "obrigado", "obrigada",
    "questions", "q&a", "perguntas", "dúvidas", "duvidas", "fim", "the end",
}

# Arquivos de config (raiz, não-módulo)
CONFIG_FILES = {
    "AGENTS.md": ("agents", True),
    "INDICE_MODULOS.md": ("indice", True),
    "Analytics Engineer Training 2026.md": ("diario", True),
    "GUIA_DBT_BANVIC.md": ("guia", True),
    "SETUP_AMBIENTE_AULAS.md": ("setup", True),
    "CONVENCOES_GIT.md": ("convencoes", True),
}


def discover_files() -> List[Dict[str, Any]]:
    files = []
    seen = set()

    # --- Configs (raiz) ---
    for name, (prefix, done) in CONFIG_FILES.items():
        path = ROOT / name
        if not path.exists():
            continue
        seen.add(name)
        title = extract_title(path) or name
        files.append({
            "id": prefix,
            "label": name,
            "title": title,
            "path": path.relative_to(ROOT).as_posix(),
            "cat": "Config",
            "done": done,
            "module": 0,
            "sort": 0,
            "size": path.stat().st_size,
        })

    # --- Módulos (pastas) ---
    for mod in MODULES:
        sort = mod["sort"]
        num = mod["num"]
        title = mod["title"]
        cat = mod.get("cat") or (f"Módulo {num}" + (f" - {title}" if title else ""))

        # Encontra a pasta do módulo: `folder` explícito ganha do regex por número
        if mod.get("folder"):
            folder = ROOT / mod["folder"]
            if not folder.is_dir():
                print(f"   [SYNC] Aviso: pasta declarada '{mod['folder']}' nao existe.")
                continue
        else:
            folder = find_module_folder(num, title)
        if not folder:
            continue

        # Coleta .md e .txt da pasta (ignora PDFs e outros)
        md_files = sorted(folder.glob("*.md")) + sorted(folder.glob("*.txt"))
        for md_file in md_files:
            name = md_file.name
            if name in seen:
                continue
            seen.add(name)

            is_en = bool(EN_RE.search(name))
            is_personal = bool(PERSONAL_RE.search(name)) if not is_en else False
            file_title = extract_title(md_file) or name

            # ID único e tipo
            name_part = re.sub(r'[^a-z0-9]+', '_', md_file.stem.lower())[:30]
            if is_en:
                kind = "en"
            elif is_personal:
                kind = "personal"
            else:
                kind = "oficial"
            fid = f"{kind}_{num}_{name_part}"
            fid = re.sub(r'[^a-z0-9_]+', '_', fid.lower()).strip('_')

            files.append({
                "id": fid,
                "label": name,
                "title": file_title,
                "path": md_file.relative_to(ROOT).as_posix(),
                "cat": cat,
                "done": True,
                "module": str(num),
                "sort": sort,
                "size": md_file.stat().st_size,
            })

    # Ordena: Config primeiro, depois por sort do módulo, depois tipo (oficial > pessoal > EN), depois label
    def type_order(fid):
        if fid.startswith("oficial"):
            return 0
        if fid.startswith("personal"):
            return 1
        return 2  # en
    files.sort(key=lambda f: (
        f["cat"] != "Config",
        f["sort"],
        type_order(f["id"]),
        f["label"],
    ))
    return files


def find_module_folder(num, title="") -> Path | None:
    """Encontra a pasta do módulo pelo número (aceita 'IV' ou '4', com/sem acento).

    Pode existir mais de uma pasta com o mesmo número (ex: "Módulo 9 - AI-Powered
    Productivity" e "Módulo 9 - Curso SQL Completo (YouTube)"). Nesse caso desempata
    pelo título declarado em MODULES — nunca pela ordem alfabética do disco, que já
    fez o sync descartar em silêncio os 5 materiais do Curso SQL. Pasta que sobrar
    sem dono vira aviso no console, nunca descarte silencioso.
    """
    pattern = re.compile(MODULE_FOLDER_RE.format(num=re.escape(str(num))))
    matches = sorted(d for d in ROOT.iterdir() if d.is_dir() and pattern.match(d.name))
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]

    # Desempate 1: pasta cujo nome contém o título declarado do módulo
    if title:
        for d in matches:
            if title.lower() in d.name.lower():
                _warn_unclaimed(num, [o for o in matches if o != d])
                return d

    # Desempate 2: sem título, fica com a que tem material (não perde arquivo)
    with_files = [d for d in matches if any(d.glob("*.md")) or any(d.glob("*.txt"))]
    chosen = with_files[0] if with_files else matches[0]
    _warn_unclaimed(num, [o for o in matches if o != chosen])
    return chosen


def _warn_unclaimed(num, others):
    """Avisa sobre pastas do mesmo número que ficaram fora do sync."""
    for d in others:
        n = len(list(d.glob("*.md"))) + len(list(d.glob("*.txt")))
        detail = f"{n} material(is) NAO sincronizado(s)" if n else "vazia"
        print(f"   [SYNC] Aviso: '{d.name}' tambem casa com Modulo {num} - {detail}."
              f" Declare-a em MODULES com num/titulo proprios.")


def extract_title(path: Path) -> str:
    """Extrai o melhor título do arquivo (heading real ou primeira linha)."""
    try:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("# "):
                t = line[2:].strip()
                if t.lower().strip(" !?.,:;-") not in GENERIC_HEADINGS:
                    return t
            elif line.startswith("## "):
                t = line[3:].strip()
                if t.lower().strip(" !?.,:;-") not in GENERIC_HEADINGS:
                    return t
        # Fallback: primeira linha não-vazia não-heading (ignora separadores ===/---)
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#") and not re.match(r'^[-=_*#]{3,}$', line):
                return line[:120]
    except Exception:
        pass
    return ""


def render_index(files: List[Dict[str, Any]]) -> str:
    if not TEMPLATE.exists():
        raise RuntimeError(f"Template não encontrado: {TEMPLATE}")

    tpl = TEMPLATE.read_text(encoding="utf-8")

    lines = ["const FILES = ["]
    for f in files:
        done = "true" if f["done"] else "false"
        lines.append(
            f'  {{ id: "{f["id"]}", label: "{escape_js(f["label"])}", '
            f'title: "{escape_js(f["title"])}", path: "{escape_js(f["path"])}", '
            f'cat: "{escape_js(f["cat"])}", done: {done} }},'
        )
    lines.append("];")
    files_js = "\n".join(lines)

    start_marker = "// ========== FILES AUTO-GENERATED =========="
    end_marker = "// ========== END FILES =========="

    if start_marker in tpl and end_marker in tpl:
        before, rest = tpl.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        return before + start_marker + "\n" + files_js + "\n" + end_marker + "\n" + after

    pattern = r'const FILES\s*=\s*\[[\s\S]*?\n\];'
    if re.search(pattern, tpl):
        return re.sub(pattern, files_js, tpl)

    raise RuntimeError("Não foi possível injetar FILES: marcadores não encontrados e fallback falhou")


def escape_js(s: str) -> str:
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')


def write_files_json(files: List[Dict[str, Any]]):
    FILES_JSON.write_text(json.dumps(files, ensure_ascii=False, indent=2), encoding="utf-8")


def write_version_json():
    """Gera version.json com o commit atual para o banner de atualizações.

    Delega para `update_version.py` na raiz do repo — fonte única da lógica de
    versão, também usada pelo `server.py` no startup. Evita as duas
    implementações divergirem (foi assim que o badge ficou defasado).
    """
    import sys as _sys
    if str(ROOT) not in _sys.path:
        _sys.path.insert(0, str(ROOT))
    try:
        import update_version
        info = update_version.write_version(quiet=True)
    except Exception as e:
        print(f"   [SYNC] Aviso: version.json nao gerado ({e})")
        info = None
    return info or {"sha": "", "short": "", "date": "", "message": "", "repo": ""}


def main():
    print("[SYNC] Descobrindo arquivos...")
    files = discover_files()
    print(f"   Encontrados: {len(files)}")
    for f in files:
        status = "[OK]" if f["done"] else "[ ]"
        print(f"   {status} {f['label']} ({f['cat']})")

    print("[SYNC] Atualizando index.html...")
    html = render_index(files)
    INDEX.write_text(html, encoding="utf-8")

    print("[SYNC] Gerando files.json...")
    write_files_json(files)

    print("[SYNC] Gerando version.json...")
    ver = write_version_json()
    if ver["short"]:
        print(f"   Versao: {ver['short']} ({ver['date']}) {ver['message'][:60]}")

    print("[SYNC] Pronto! Rode `python server.py` para ver.")


if __name__ == "__main__":
    main()
