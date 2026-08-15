#!/usr/bin/env python3
"""Converte o script T-SQL da Northwind em CSVs por tabela (formato Databricks/Neon)."""
import re
import csv
import sys
from datetime import datetime
from pathlib import Path

SRC = sys.argv[1]
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

text = Path(SRC).read_text(encoding="utf-8", errors="replace")

# ---------- util ----------

def skip_ws(s, i):
    while i < len(s) and s[i].isspace():
        i += 1
    return i

def read_balanced(s, pos, o, c):
    depth = 0
    in_str = False
    i = pos
    start = pos
    while i < len(s):
        ch = s[i]
        if in_str:
            if ch == "'":
                if i + 1 < len(s) and s[i + 1] == "'":
                    i += 2
                    continue
                in_str = False
            i += 1
            continue
        if ch == "'":
            in_str = True
            i += 1
            continue
        if ch == o:
            depth += 1
            if depth == 1:
                start = i
            i += 1
            continue
        if ch == c:
            depth -= 1
            if depth == 0:
                return s[start + 1:i], i + 1
        i += 1
    raise ValueError("unbalanced")

def split_values(body):
    """Divide o conteúdo de um tuple em valores (respeitando aspas)."""
    vals = []
    cur = []
    in_str = False
    depth = 0
    i = 0
    while i < len(body):
        ch = body[i]
        if in_str:
            cur.append(ch)
            if ch == "'":
                if i + 1 < len(body) and body[i + 1] == "'":
                    cur.append(body[i + 1])
                    i += 2
                    continue
                in_str = False
            i += 1
            continue
        if ch == "'":
            in_str = True
            cur.append(ch)
            i += 1
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            vals.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    vals.append("".join(cur))
    return vals

# ---------- CREATE TABLE ----------

CREATE_RE = re.compile(
    r'CREATE\s+TABLE\s+("(?P<n1>[^"]+)"|\[dbo\]\.\[(?P<n2>[^\]]+)\])',
    re.IGNORECASE,
)

def parse_create(body):
    """Retorna lista de (coluna, tipo) a partir do corpo do CREATE TABLE."""
    cols = []
    # divide por vírgula no nível 0
    segs = []
    cur = []
    in_str = False
    depth = 0
    i = 0
    while i < len(body):
        ch = body[i]
        if in_str:
            if ch == "'":
                if i + 1 < len(body) and body[i + 1] == "'":
                    cur.append("''")
                    i += 2
                    continue
                in_str = False
            cur.append(ch)
            i += 1
            continue
        if ch == "'":
            in_str = True
            cur.append(ch)
            i += 1
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            segs.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    segs.append("".join(cur))

    name_re = re.compile(r'^"?\[?([A-Za-z_][A-Za-z0-9_ ]*)\]?"?')
    for seg in segs:
        seg = seg.strip()
        if not seg:
            continue
        if re.match(r'CONSTRAINT\b|PRIMARY\b|FOREIGN\b|CHECK\s*\(', seg, re.I):
            continue
        if seg.startswith(')') or seg in (')', ''):
            continue
        m = name_re.match(seg)
        if not m:
            continue
        col = m.group(1).strip()
        rest = seg[m.end():].strip()
        # tipo = tokens até NULL/NOT/IDENTITY/CONSTRAINT/CHECK/DEFAULT
        tm = re.match(
            r'([^A-Za-z]?\[?"?[A-Za-z_]+\]?"?\s*(?:\([^)]*\))?)',
            rest,
        )
        typ = tm.group(1).strip() if tm else rest.split()[0] if rest else ''
        typ = re.sub(r'\s+', '', typ)
        typ = re.sub(r'["\[\]]', '', typ)
        cols.append((col, typ))
    return cols

def find_col_types(table):
    """Busca o CREATE TABLE de `table` e devolve dict col->tipo."""
    for m in CREATE_RE.finditer(text):
        name = m.group("n1") or m.group("n2")
        if name.strip().lower() != table.lower():
            continue
        body, _ = read_balanced(text, m.end(), "(", ")")
        return parse_create(body)
    return []

# ---------- INSERT ----------

INSERT_RE = re.compile(
    r'INSERT\s+(?:INTO\s+)?("(?P<n1>[^"]+)"|\[dbo\]\.\[(?P<n2>[^\]]+)\]|(?P<n3>[A-Za-z_][A-Za-z_]*))\s*',
    re.IGNORECASE,
)

def parse_inserts():
    """Extrai {tabela: [rows]} onde cada row é lista de valores (strings)."""
    data = {}
    for m in INSERT_RE.finditer(text):
        table = m.group("n1") or m.group("n2") or m.group("n3")
        table = table.strip()
        i = skip_ws(text, m.end())
        cols = None
        if i < len(text) and text[i] == "(":
            # pode ser coluna list
            j = i
            depth = 0
            in_str = False
            while j < len(text):
                ch = text[j]
                if in_str:
                    if ch == "'":
                        if j + 1 < len(text) and text[j + 1] == "'":
                            j += 2
                            continue
                        in_str = False
                    j += 1
                    continue
                if ch == "'":
                    in_str = True
                elif ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            colbody = text[i + 1:j]
            if re.match(r'\s*["\[]?[A-Za-z_]', colbody) and 'VALUES' not in text[i:j].upper():
                cols = [c.strip().strip('"[]') for c in split_values(colbody)]
            i = skip_ws(text, j + 1)
        if text[i:i + 6].upper() != "VALUES":
            continue
        i = skip_ws(text, i + 6)
        rows = data.setdefault(table, [])
        while i < len(text) and text[i] == "(":
            body, i = read_balanced(text, i, "(", ")")
            rows.append(split_values(body))
            i = skip_ws(text, i)
    return data

# ---------- datas ----------

DATE_FMTS = [
    "%m/%d/%Y", "%m/%d/%y",
    "%m/%d/%Y %H:%M:%S", "%m/%d/%y %H:%M:%S",
    "%m/%d/%Y %I:%M:%S %p", "%m/%d/%y %I:%M:%S %p",
    "%m/%d/%Y %I:%M %p", "%m/%d/%y %I:%M %p",
    "%Y-%m-%d %H:%M:%S",
]

def iso_date(v, coltype):
    if coltype.lower() not in ("datetime", "date", "smalldatetime", "datetime2"):
        return v
    for fmt in DATE_FMTS:
        try:
            return datetime.strptime(v, fmt).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    return v

def clean_value(v, coltype):
    v = v.strip()
    if v.upper() == "NULL":
        return ""
    if v.startswith("N'") or v.startswith("n'"):
        s = v[1:]
        s = s[1:-1] if s.startswith("'") and s.endswith("'") else s
        s = s.replace("''", "'")
        return iso_date(s, coltype)
    if v.startswith("'"):
        s = v[1:-1] if v.endswith("'") else v[1:]
        s = s.replace("''", "'")
        return iso_date(s, coltype)
    if v.lower().startswith("0x"):
        return v
    return v

def snake(name):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")

def databricks_type(t):
    t = t.lower()
    if any(k in t for k in ("nvarchar", "varchar", "char", "ntext", "text", "uniqueidentifier")):
        return "STRING"
    if "tinyint" in t: return "TINYINT"
    if "smallint" in t: return "SMALLINT"
    if "bigint" in t: return "BIGINT"
    if "int" in t: return "INT"
    if "money" in t or "decimal" in t or "numeric" in t: return "DECIMAL(19,4)"
    if "real" in t: return "FLOAT"
    if "float" in t or "double" in t: return "DOUBLE"
    if "bit" in t: return "BOOLEAN"
    if "datetime" in t or "date" in t or "time" in t: return "TIMESTAMP"
    return "STRING"

def write_databricks_ddl(schemas, out_path):
    lines = []
    lines.append("-- Northwind para Databricks (Delta). Gerado automaticamente.")
    lines.append("-- 1) Crie o schema:  CREATE SCHEMA IF NOT EXISTS northwind;")
    lines.append("-- 2) Ajuste o caminho /Volumes/... no COPY INTO e rode num SQL warehouse.")
    lines.append("")
    lines.append("CREATE SCHEMA IF NOT EXISTS northwind;")
    lines.append("")
    for table, cols in schemas.items():
        fname = snake(table) + ".csv"
        col_defs = ",\n    ".join(f"{c} {databricks_type(t)}" for c, t in cols)
        lines.append(f"DROP TABLE IF EXISTS northwind.{snake(table)};")
        lines.append("CREATE TABLE northwind." + snake(table) + " (\n    " + col_defs + "\n) USING DELTA;")
        lines.append(
            f"COPY INTO northwind.{snake(table)} FROM '/Volumes/main/datalake/raw/northwind/{fname}' "
            "FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');"
        )
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"DDL Databricks: {out_path.name}")

# ---------- main ----------

tables = parse_inserts()
total = 0
schemas = {}
for table in sorted(tables):
    rows = tables[table]
    types = dict(find_col_types(table))
    col_names = list(types.keys()) if types else None
    type_by_snake = {snake(c): t for c, t in types.items()}
    # determina colunas
    if col_names:
        columns = [snake(c) for c in col_names]
    else:
        width = max(len(r) for r in rows)
        columns = [f"col{i}" for i in range(width)]
    fname = snake(table) + ".csv"
    schemas[table] = [(snake(c), types[c]) for c in col_names] if col_names else [(c, "") for c in columns]
    out_path = OUT / fname
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(columns)
        for row in rows:
            cleaned = []
            for idx, v in enumerate(row):
                col = columns[idx] if idx < len(columns) else "col"
                cleaned.append(clean_value(v, type_by_snake.get(col, "")))
            w.writerow(cleaned)
    total += len(rows)
    print(f"{len(rows):6d} linhas  {table:22s} -> {out_path.name}")

write_databricks_ddl(schemas, OUT / "northwind_schema_databricks.sql")

print(f"\nTOTAL: {total} linhas em {len(tables)} tabelas")
