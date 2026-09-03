# -*- coding: utf-8 -*-
"""Exporta os 4 marts do DuckDB local para CSV (treino do dashboard do Modulo 6).

Pre-requisito (uma vez): dbt build --target local dentro de banvic-dbt/
Uso: python export_marts_local.py
Saida: dados_treino/{dim_agencias,dim_clientes,dim_datas,fact_transacoes}.csv
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DUCKDB_FILE = ROOT / "banvic-dbt" / "dev.duckdb"
OUT_DIR = ROOT / "dados_treino"
TABLES = ["dim_agencias", "dim_clientes", "dim_datas", "fact_transacoes"]


def main():
    if not DUCKDB_FILE.exists():
        sys.exit("[ERRO] dev.duckdb nao encontrado. Rode 'dbt build --target local' em banvic-dbt/ primeiro.")
    import duckdb
    import pandas as pd

    OUT_DIR.mkdir(exist_ok=True)
    con = duckdb.connect(str(DUCKDB_FILE), read_only=True)
    for table in TABLES:
        df = con.execute(f"SELECT * FROM main.{table}").fetchdf()
        out = OUT_DIR / f"{table}.csv"
        df.to_csv(out, index=False, encoding="utf-8-sig")
        print(f"[OK] {out.name}: {len(df)} linhas x {len(df.columns)} colunas | colunas: {list(df.columns)}")
    con.close()
    print(f"[PRONTO] CSVs em {OUT_DIR}")


if __name__ == "__main__":
    main()
