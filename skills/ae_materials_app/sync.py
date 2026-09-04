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
    {"num": 9,  "sort": 9,   "title": "Curso SQL Completo (YouTube)"},
]

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
        cat = f"Módulo {num}" + (f" - {title}" if title else "")

        # Encontra a pasta do módulo
        folder = find_module_folder(num)
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


def find_module_folder(num) -> Path | None:
    """Encontra a pasta do módulo pelo número (aceita 'IV' ou '4', com/sem acento)."""
    pattern = re.compile(rf'^[Mm][óo]dulo\s+{re.escape(str(num))}\b')
    for d in ROOT.iterdir():
        if not d.is_dir():
            continue
        if pattern.match(d.name):
            return d
    return None


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
    """Gera version.json com commit atual para o banner de atualizações."""
    import subprocess
    info = {"sha": "", "short": "", "date": "", "message": "", "repo": ""}
    try:
        info["sha"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
        info["short"] = info["sha"][:7]
        info["date"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%ad", "--date=short"],
            cwd=ROOT, text=True,
        ).strip()
        info["message"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%s"], cwd=ROOT, text=True
        ).strip()
        remote = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], cwd=ROOT, text=True
        ).strip()
        # https://github.com/owner/repo.git -> owner/repo
        m = re.search(r'github\.com[:/](.+?)(?:\.git)?$', remote)
        if m:
            info["repo"] = m.group(1)
    except Exception as e:
        print(f"   [SYNC] Aviso: sem info git ({e})")
    VERSION_JSON.write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    return info


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
