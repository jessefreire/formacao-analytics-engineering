# -*- coding: utf-8 -*-
"""Exporta os 4 marts do Databricks para CSV (treino do dashboard do Modulo 6).

Uso (no PowerShell, segredos via variaveis de ambiente — nada de token no codigo):
    $env:DATABRICKS_HOST="xxxx.cloud.databricks.com"   # sem https://
    $env:DATABRICKS_HTTP_PATH="/sql/1.0/warehouses/xxxx"
    $env:DATABRICKS_TOKEN="dapi..."
    # Opcionais (tem padrao sensato / autodescoberta):
    # $env:DATABRICKS_CATALOG="dev"
    # $env:DATABRICKS_MARTS_SCHEMA="seu_schema_marts"
    python export_marts_csv.py
"""
import os
import sys
from pathlib import Path

import pandas as pd
from databricks import sql

TABLES = ["dim_agencias", "dim_clientes", "dim_datas", "fact_transacoes"]
OUT_DIR = Path(__file).resolve().parent / "dados_treino"


def get_env(name, default=None, required=False):
    value = os.environ.get(name, default)
    if required and not value:
        sys.exit(f"[ERRO] Defina a variavel de ambiente {name} antes de rodar.")
    return value


def discover_marts_schema(cursor, catalog):
    cursor.execute(
        f"SELECT table_schema FROM {catalog}.information_schema.tables "
        "WHERE lower(table_name) = 'dim_agencias'"
    )
    schemas = [row[0] for row in cursor.fetchall()]
    if not schemas:
        sys.exit(
            "[ERRO] Tabela dim_agencias nao encontrada no catalogo "
            f"'{catalog}'. Confira DATABRICKS_CATALOG ou defina "
            "DATABRICKS_MARTS_SCHEMA manualmente."
        )
    if len(schemas) > 1:
        print(f"[AVISO] dim_agencias em varios schemas {schemas}; usando '{schemas[0]}'.")
    return schemas[0]


def main():
    host = get_env("DATABRICKS_HOST", required=True)
    http_path = get_env("DATABRICKS_HTTP_PATH", required=True)
    token = get_env("DATABRICKS_TOKEN", required=True)
    catalog = get_env("DATABRICKS_CATALOG", default="dev")

    OUT_DIR.mkdir(exist_ok=True)
    print(f"[INFO] Conectando em {host} ...")
    with sql.connect(server_hostname=host, http_path=http_path, access_token=token) as conn:
        with conn.cursor() as cursor:
            schema = os.environ.get("DATABRICKS_MARTS_SCHEMA") or discover_marts_schema(cursor, catalog)
            print(f"[INFO] Schema dos marts: {catalog}.{schema}")
            for table in TABLES:
                fqn = f"{catalog}.{schema}.{table}"
                print(f"[INFO] Lendo {fqn} ...")
                df = pd.read_sql(f"SELECT * FROM {fqn}", conn)
                out = OUT_DIR / f"{table}.csv"
                df.to_csv(out, index=False, encoding="utf-8-sig")
                print(f"[OK] {out.name}: {len(df)} linhas x {len(df.columns)} colunas")
    print(f"[PRONTO] CSVs em {OUT_DIR}")


if __name__ == "__main__":
    main()
