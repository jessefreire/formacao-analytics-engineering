# Como Carregar os Bancos do Curso (Databricks / Neon)

Os arquivos originais são **formato SQL Server** e **não carregam direto** nem no
Databricks nem no Neon (Postgres). Este módulo já resolve isso:

- **Northwind** → já convertido para **11 CSVs** prontos (pasta `northwind_csv/`)
- **AdventureWorks** → o `.bak` precisa de uma etapa de extração (guia abaixo)

> Ambiente alvo: **Databricks** (prioridade) ou **Neon** (Postgres serverless).

## O que tem em `northwind_csv/`

| Arquivo | Tabela | Linhas |
|---------|--------|-------:|
| `customers.csv` | Customers | 91 |
| `orders.csv` | Orders | 830 |
| `order_details.csv` | Order Details | 2.155 |
| `products.csv` | Products | 77 |
| `categories.csv` | Categories | 8 |
| `suppliers.csv` | Suppliers | 29 |
| `employees.csv` | Employees | 9 |
| `shippers.csv` | Shippers | 3 |
| `region.csv` | Region | 4 |
| `territories.csv` | Territories | 53 |
| `employee_territories.csv` | EmployeeTerritories | 49 |
| `northwind_schema_databricks.sql` | DDL + COPY INTO (Databricks) | — |

Os CSVs usam **snake_case**, **UTF-8** e **datas ISO** (`1996-07-04 00:00:00`),
então o infer de tipos funciona de cara.

---

## 1. Northwind no Databricks (prioridade)

### 1.1 Enviar os CSVs para o lakehouse

1. No Databricks, crie (ou use) um **Volume** externo/gerenciado, ex.:
   `/Volumes/main/datalake/raw/northwind/`.
2. Faça upload dos 11 CSVs para essa pasta (UI: Catalog → volume → Upload).
   > Alternativa: `Auto Loader` / notebook Python lendo os mesmos CSVs.

### 1.2 Criar as tabelas Delta + carga

Abra o arquivo `northwind_schema_databricks.sql` e rode num **SQL warehouse**.
Ele cria o schema e faz `CREATE TABLE ... USING DELTA` + `COPY INTO` para cada
tabela. Só ajuste o caminho do volume no `COPY INTO`:

```sql
CREATE SCHEMA IF NOT EXISTS northwind;

CREATE TABLE northwind.orders (
    order_id INT,
    customer_id STRING,
    employee_id INT,
    order_date TIMESTAMP,
    -- ... (o resto está no .sql pronto)
) USING DELTA;

COPY INTO northwind.orders
FROM '/Volumes/main/datalake/raw/northwind/orders.csv'
FILEFORMAT = CSV
FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');
```

### 1.3 Validar

```sql
SELECT COUNT(*) FROM northwind.orders;          -- 830
SELECT * FROM northwind.orders WHERE order_id = 10248;
SELECT p.product_name, SUM(od.quantity * od.unit_price) AS receita
FROM northwind.order_details od
JOIN northwind.products p ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY receita DESC;
```

---

## 2. Northwind no Neon (Postgres)

1. Crie um banco (ex.: `northwind`) na sua instância Neon.
2. Abra o SQL Editor e rode o `CREATE TABLE` equivalente (tipos Postgres).
   Exemplo do padrão para as tabelas principais:

```sql
CREATE TABLE orders (
    order_id       int PRIMARY KEY,
    customer_id    char(5),
    employee_id    int,
    order_date     timestamp,
    required_date  timestamp,
    shipped_date   timestamp,
    ship_via       int,
    freight        numeric(19,4),
    ship_name      text,
    ship_address   text,
    ship_city      text,
    ship_region    text,
    ship_postal_code text,
    ship_country   text
);
```

> Use `text` no lugar de `nvarchar`, `numeric(19,4)` no lugar de `money` e
> `boolean` no lugar de `bit`. Os tipos originais estão no
> `northwind_banco_referencia.md`.

3. Carga via `psql` (cliente local) apontando a connection string do Neon:

```bash
psql "$NEON_CONNECTION_STRING" -c "\copy orders FROM 'northwind_csv/orders.csv' WITH (FORMAT csv, HEADER true)"
```

> No SQL Editor do Neon você pode usar `\copy` também, mas o caminho do arquivo
> é do seu computador — mais simples via `psql` local.

---

## 3. AdventureWorks (o `.bak`)

> ⚠️ **Este `.bak` (~48 MB) NÃO está no git** (ignorado via `.gitignore` — `*.bak`).
> `bancoNorthwind.txt` e os CSVs já estão versionados; só o `.bak` precisa ser
> copiado manualmente ao trocar de máquina (pendrive/Drive). Se você ainda não o
> tem na máquina atual, procure-o em `Módulo 9 - Curso SQL Completo (YouTube)/`.

O `AdventureWorks2017.bak` é um **backup binário do SQL Server** — não há como
ler sem um SQL Server. O caminho prático é extrair as tabelas para CSV usando um
SQL Server em container (você já tem Docker instalado):

### 3.1 Subir o SQL Server (Docker)

```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourStrong@Pass1" \
  -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2022-latest
```

> Você precisa abrir o **Docker Desktop** antes (o daemon estava parado).

### 3.2 Restaurar o backup

```bash
docker cp "AdventureWorks2017.bak" sqlserver:/tmp/
docker exec -it sqlserver /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa \
  -P "YourStrong@Pass1" -C -Q \
  "RESTORE DATABASE AdventureWorks2017 FROM DISK='/tmp/AdventureWorks2017.bak' WITH REPLACE, MOVE 'AdventureWorks2017' TO '/var/opt/mssql/data/AdventureWorks2017.mdf', MOVE 'AdventureWorks2017_log' TO '/var/opt/mssql/data/AdventureWorks2017_log.ldf'"
```

### 3.3 Exportar tabelas para CSV

Para cada tabela (ex.: `Person.Person`, `Sales.SalesOrderHeader`,
`Production.Product`):

```bash
docker exec -it sqlserver /opt/mssql-tools18/bin/bcp \
  "AdventureWorks2017.Person.Person" out /tmp/person.csv -S localhost -U sa \
  -P "YourStrong@Pass1" -c -t, -C 65001
docker cp sqlserver:/tmp/person.csv .
```

Repita para as tabelas que quiser usar. Depois é o mesmo fluxo do item 1/2:
subir os CSVs no Databricks (ou `\copy` no Neon) e criar as tabelas.

> **Alternativa rápida:** a Microsoft publica datasets de exemplo do
> AdventureWorks em outros formatos; se preferir, baixe uma versão CSV/Parquet
> oficial e pule o passo do container.

---

## Referências deste módulo

- `northwind_banco_referencia.md` — schema SQL Server da Northwind
- `adventureworks_banco_referencia.md` — schema da AdventureWorks
- `curso_sql_completo_2025.md` — conteúdo do curso
