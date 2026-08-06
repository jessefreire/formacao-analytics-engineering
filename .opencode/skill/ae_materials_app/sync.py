#!/usr/bin/env python3
"""
ae-materials-app — Sincroniza arquivos de módulo no index.html
Uso: python -m ae_materials_app.sync
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
    # Fallback: assume estrutura padrão .opencode/skill/... -> sobe 4 níveis
    return Path(__file__).resolve().parent.parent.parent.parent

ROOT = find_root()
INDEX = ROOT / "index.html"
TEMPLATE = Path(__file__).parent / "templates" / "index.html.j2"
FILES_JSON = ROOT / "files.json"

# Padrões de arquivo por categoria
# (glob, categoria_base, prefixo_id, done_default)
PATTERNS = [
    # Configs (raiz)
    ("AGENTS.md", "Config", "agents", True),
    ("INDICE_MODULOS.md", "Config", "indice", True),
    ("Analytics Engineer Training 2026.md", "Config", "diario", True),
    ("GUIA_DBT_BANVIC.md", "Config", "guia", True),
    # Módulo 1 - Resumos/Decorebas
    ("Módulo 1 -  Introdução à Análise de Dados/resumo_modulo1.md", "Módulo 1", "resumo", True),
    ("Módulo 1 -  Introdução à Análise de Dados/decoreba_modulo1.txt", "Módulo 1", "decoreba", True),
    # Módulo 2 - Resumos/Decorebas
    ("Modulo 2 - SQL para Análise de Dados/Resumo_Modulo_2_SQL.md", "Módulo 2", "resumo", True),
    ("Modulo 2 - SQL para Análise de Dados/Decoreba_SQL.txt", "Módulo 2", "decoreba", True),
    # Materiais Oficiais - Módulo 1 (só .md)
    ("Módulo 1 -  Introdução à Análise de Dados/*FADA*Módulo*01*Introdução*Análise*Dados*.md", "Módulo 1", "oficial", True),
    ("Módulo 1 -  Introdução à Análise de Dados/*FADA*English*Slides*Introduction*data*analysis*.md", "Módulo 1 (EN)", "oficial", True),
    # Materiais Oficiais - Módulo 2 (só .md)
    ("Modulo 2 - SQL para Análise de Dados/*Academy*Querying*data*SQL*Slides*.md", "Módulo 2 (SQL)", "oficial", True),
    ("Modulo 2 - SQL para Análise de Dados/*Conteúdo*Módulo*2*SQL*.md", "Módulo 2 (SQL)", "oficial", True),
]

# Arquivos que NÃO são de módulo (configs fixos)
NON_MODULE_FILES = {
    "AGENTS.md", "INDICE_MODULOS.md", 
    "Analytics Engineer Training 2026.md", "GUIA_DBT_BANVIC.md",
}

# Títulos dos módulos (para label completo)
MODULE_TITLES = {
    1: "Introdução à Análise de Dados",
    2: "SQL",
}

# Regex para extrair número do módulo (várias formas)
MODULE_RE = re.compile(r'(?:modulo|modulo_|modulo[-_])?(\d+)', re.IGNORECASE)

def discover_files() -> List[Dict[str, Any]]:
    files = []
    seen = set()
    
    for pattern, cat_base, prefix, done in PATTERNS:
        for path in sorted(ROOT.glob(pattern)):
            if path.name in seen:
                continue
            seen.add(path.name)
            
            # Verifica se é arquivo de config (não módulo)
            is_config = path.name in NON_MODULE_FILES
            
            # Extrai número do módulo
            m = MODULE_RE.search(path.stem)
            module_num = int(m.group(1)) if m else 0
            
            # Se cat_base já tem "Módulo N", extrai o número dela
            if module_num == 0:
                m2 = re.search(r'Módulo\s+(\d+)', cat_base)
                if m2:
                    module_num = int(m2.group(1))
            
            if is_config or module_num == 0:
                module_label = cat_base
            else:
                title = MODULE_TITLES.get(module_num)
                module_label = f"Módulo {module_num}" + (f" - {title}" if title else "")
            
            # Título legível a partir do primeiro heading no markdown
            title = extract_title(path)
            if not title:
                title = path.stem.replace('_', ' ').replace('-', ' ').title()
            
            # ID único
            if is_config:
                fid = prefix
            elif module_num:
                # Inclui parte única do nome para evitar colisão
                name_part = re.sub(r'[^a-z0-9]+', '_', path.stem.lower())[:30]
                fid = f"{prefix}_{module_num}_{name_part}"
            else:
                fid = f"{prefix}_{path.stem}"
            fid = re.sub(r'[^a-z0-9_]+', '_', fid.lower()).strip('_')
            
            files.append({
                "id": fid,
                "label": path.name,
                "title": title,
                "path": path.name,
                "cat": module_label,
                "done": done,
                "module": module_num if not is_config else 0,
                "size": path.stat().st_size,
            })
    
    # Ordena: Config primeiro, depois por módulo, depois por label
    files.sort(key=lambda f: (f["cat"] != "Config", f["module"], f["label"]))
    return files

def extract_title(path: Path) -> str:
    """Extrai o primeiro heading # do arquivo markdown/txt."""
    try:
        text = path.read_text(encoding="utf-8")
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
            if line.startswith("## "):
                return line[3:].strip()
    except Exception:
        pass
    return ""

def render_index(files: List[Dict[str, Any]]) -> str:
    # Lê template
    if not TEMPLATE.exists():
        raise RuntimeError(f"Template não encontrado: {TEMPLATE}")
    
    tpl = TEMPLATE.read_text(encoding="utf-8")
    
    # Gera array FILES como string JS
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
    
    # Substitui entre marcadores
    start_marker = "// ========== FILES AUTO-GENERATED =========="
    end_marker = "// ========== END FILES =========="
    
    if start_marker in tpl and end_marker in tpl:
        before, rest = tpl.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        return before + start_marker + "\n" + files_js + "\n" + end_marker + "\n" + after
    
    # Fallback: substitui const FILES = [...];
    pattern = r'const FILES\s*=\s*\[[\s\S]*?\n\];'
    if re.search(pattern, tpl):
        return re.sub(pattern, files_js, tpl)
    
    raise RuntimeError("Não foi possível injetar FILES: marcadores não encontrados e fallback falhou")

def escape_js(s: str) -> str:
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')

def write_files_json(files: List[Dict[str, Any]]):
    FILES_JSON.write_text(json.dumps(files, ensure_ascii=False, indent=2), encoding="utf-8")

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
    
    print("[SYNC] Pronto! Rode `python server.py` para ver.")

if __name__ == "__main__":
    main()