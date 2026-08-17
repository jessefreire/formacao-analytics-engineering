# Banco BanVic — Queries de Referência

Exemplos prontos para usar como referência. Assumem as seeds já carregadas
(`dbt seed`) no schema raw `erp_banvic` ou nas views `staging`.

> Convenção: colunas em MAIÚSCULAS (igual ao schema em `banvic_tabelas.md`).
> Sintaxe Databricks/Spark SQL (usa `- INTERVAL n UNIT` em vez de `DATEADD`).

## Joins básicos

```sql
-- Contas com nome do cliente e UF
SELECT
    c.NUM_CONTA,
    cl.PRIMEIRO_NOME || ' ' || cl.ULTIMO_NOME AS NOME_CLIENTE,
    l.UF
FROM erp_banvic.contas c
JOIN erp_banvic.clientes cl ON cl.COD_CLIENTE = c.COD_CLIENTE
JOIN erp_banvic.localidades l ON l.COD_LOCALIDADE = cl.COD_LOCALIDADE;
```

```sql
-- Transações enriquecidas com cliente e agência
SELECT
    t.COD_TRANSACAO,
    t.DATA_TRANSACAO,
    t.NOME_TRANSACAO,
    t.VALOR_TRANSACAO,
    c.NUM_CONTA,
    a.NOME AS AGENCIA
FROM erp_banvic.transacoes t
JOIN erp_banvic.contas c ON c.NUM_CONTA = t.NUM_CONTA
JOIN erp_banvic.agencias a ON a.COD_AGENCIA = c.COD_AGENCIA;
```

## Filtros e agregações

```sql
-- Saldo médio por UF
SELECT
    l.UF,
    COUNT(*)                       AS NUM_CONTAS,
    ROUND(AVG(c.SALDO_TOTAL), 2)   AS SALDO_MEDIO
FROM erp_banvic.contas c
JOIN erp_banvic.clientes cl ON cl.COD_CLIENTE = c.COD_CLIENTE
JOIN erp_banvic.localidades l ON l.COD_LOCALIDADE = cl.COD_LOCALIDADE
GROUP BY l.UF
ORDER BY SALDO_MEDIO DESC;
```

```sql
-- Volume de transações por tipo (últimos 30 dias da base)
SELECT
    NOME_TRANSACAO,
    COUNT(*)                        AS QTD,
    ROUND(SUM(VALOR_TRANSACAO), 2)  AS TOTAL
FROM erp_banvic.transacoes
WHERE DATA_TRANSACAO >= (SELECT MAX(DATA_TRANSACAO) FROM erp_banvic.transacoes) - INTERVAL 30 DAYS
GROUP BY NOME_TRANSACAO
ORDER BY QTD DESC;
```

```sql
-- Propostas aprovadas por mês
SELECT
    DATE_TRUNC('month', DATA_ENTRADA_PROPOSTA) AS MES,
    COUNT(*)                            AS PROPOSTAS_APROVADAS,
    ROUND(SUM(VALOR_FINANCIAMENTO), 2)  AS VALOR_TOTAL
FROM erp_banvic.propostas_credito
WHERE STATUS_PROPOSTA = 'Aprovada'
GROUP BY 1
ORDER BY 1;
```

## Top N e ranking

```sql
-- Clientes com maior saldo total (top 10)
SELECT
    cl.COD_CLIENTE,
    cl.PRIMEIRO_NOME || ' ' || cl.ULTIMO_NOME AS NOME_CLIENTE,
    c.SALDO_TOTAL
FROM erp_banvic.contas c
JOIN erp_banvic.clientes cl ON cl.COD_CLIENTE = c.COD_CLIENTE
ORDER BY c.SALDO_TOTAL DESC
LIMIT 10;
```

```sql
-- Agências por movimentação (ranking com window function)
SELECT
    a.NOME,
    SUM(t.VALOR_TRANSACAO)                    AS MOVIMENTACAO,
    RANK() OVER (ORDER BY SUM(t.VALOR_TRANSACAO) DESC) AS POSICAO
FROM erp_banvic.transacoes t
JOIN erp_banvic.contas c ON c.NUM_CONTA = t.NUM_CONTA
JOIN erp_banvic.agencias a ON a.COD_AGENCIA = c.COD_AGENCIA
GROUP BY a.NOME
ORDER BY POSICAO;
```

## Conversão de tipos / tratamento

```sql
-- CEP como string de 8 dígitos (importante para joins com clientes)
SELECT COD_CLIENTE, LPAD(CEP, 8, '0') AS CEP_8 FROM erp_banvic.clientes;

-- Data em fuso local (se o raw vier em UTC)
SELECT
    DATA_TRANSACAO,
    DATA_TRANSACAO - INTERVAL 3 HOURS AS DATA_LOCAL
FROM erp_banvic.transacoes;
```

## Testes de qualidade típicos (dbt)

```sql
-- PK duplicada
SELECT COD_CLIENTE, COUNT(*) AS QTD
FROM erp_banvic.clientes
GROUP BY 1
HAVING COUNT(*) > 1;

-- FK órfã (transação apontando para conta inexistente)
SELECT t.*
FROM erp_banvic.transacoes t
LEFT JOIN erp_banvic.contas c ON c.NUM_CONTA = t.NUM_CONTA
WHERE c.NUM_CONTA IS NULL;
```

> Lembre-se: nos models `staging` do dbt, use `{{ source('erp_banvic', 'clientes') }}`
> em vez de `erp_banvic.clientes` direto. As queries acima servem para exploração
> rápida no Databricks/jupyter.
