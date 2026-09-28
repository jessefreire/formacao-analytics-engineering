---
name: databricks-ingestao
description: Carrega arquivos brutos (CSV/TSV, inclusive sem cabeçalho) num schema do Databricks a partir do DDL de origem, com tipos corretos, carga idempotente e conferências de contagem, órfãos, nulos e valor de aceite. Use quando o usuário pedir "sobe esses dados no Databricks", "ingestão", "carga da camada bruta", "criar as tabelas raw", ou mencionar install.sql/DDL + arquivos de dados.
---

# /databricks-ingestao

Camada bruta confiável antes de qualquer análise. Se a carga não for conferida, todo número
depois dela é suspeito.

## Setup

1. Schema com o nome que o projeto exige (ex.: `adventure_works`) — não inventar.
2. **Managed Volume** no Unity Catalog, nome `raw_<fonte>`; subir a pasta inteira com
   *Select folder* (preserva estrutura) e *Overwrite files* marcado.
3. SQL warehouse pequeno. Rodar pelo **SQL Editor** — compute errado dá `RESOURCE_EXHAUSTED`
   disfarçado de erro do cliente.

## Carga: uma instrução por tabela, idempotente

```sql
-- Cria e carrega em uma instrução: repetir substitui, nunca duplica
create or replace table workspace.<schema>.<tabela> as
select cast(_c0 as int) as <col0>, cast(_c1 as decimal(19, 4)) as <col1>, ...
from read_files('/Volumes/workspace/<schema>/raw_<fonte>/.../<Tabela>.csv',
  format => 'csv', sep => '\t', header => false,
  nullValue => '', quote => '"', mode => 'FAILFAST')
```

- **Gere o SQL a partir do DDL** (script, não à mão): sem cabeçalho, a ordem das colunas do
  DDL é a única fonte da verdade. Nomes e casts por posição.
- `sep => '\t'` quando a extensão é `.csv` mas o separador é tab.
- `nullValue => ''` — sem ele, vazio em `int` vira **0** ("sem vendedor" vira "vendedor 0").
- `quote => '"'` para campos com aspas internas duplicadas (XML, texto livre).
- `mode => 'FAILFAST'` — linha ruim derruba a carga em vez de virar NULL silencioso.
- Dinheiro em `decimal(19,4)`, nunca `double`.
- **Evite `COPY INTO` + `force = true`**: acrescenta linhas em recarga → duplica. Assinatura
  do problema: contagem = múltiplo exato do esperado.

## Antes de rodar

- Compare a contagem de colunas do DDL com a de campos de cada arquivo (todas as tabelas).
- Simule os casts no dado real antes (um auditor de tipos evita erro na célula 36 de 80).
- Priorize as tabelas do escopo de análise primeiro (cota da Free Edition).

## Conferências (rodar antes de qualquer análise)

1. **Contagem por tabela** = linhas do arquivo de origem (medidas localmente e embutidas no SQL).
2. **Junções da análise com zero órfão** (pedido→cliente, item→produto...).
3. **NULL sobreviveu** onde deveria (ex.: pedidos sem vendedor = NULL, e zero com vendedor 0).
4. **Valor de aceite do negócio** batendo (ex.: receita bruta de um ano, comparado em centavos).
5. **Identidades de campo** preservadas (ex.: `linetotal` = qtd × preço × (1 − desconto), ±1 centavo).

Cada conferência com comentário: o que confere e o valor esperado.

## Linter

- sqlfluff 1.4.5 pula em silêncio arquivos > 20.000 bytes e não parseia `group by all` —
  conferir que o arquivo foi de fato lintado.
