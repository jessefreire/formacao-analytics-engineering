# Banco BanVic — Queries de Referência

Exemplos prontos para usar como referência. Assumem as seeds já carregadas
(`dbt seed`) no schema raw `erp_banvic` ou nas views `staging`.

## Joins básicos

```sql
-- Contas com nome do cliente e UF
SELECT
    c.num_conta,
    cl.primeiro_nome || ' ' || cl.ultimo_nome AS nome_cliente,
    l.uf
FROM erp_banvic.contas c
JOIN erp_banvic.clientes cl ON cl.cod_cliente = c.cod_cliente
JOIN erp_banvic.localidades l ON l.cod_localidade = cl.cod_localidade;
```

```sql
-- Transações enriquecidas com cliente e agência
SELECT
    t.cod_transacao,
    t.data_transacao,
    t.nome_transacao,
    t.valor_transacao,
    c.num_conta,
    a.nome AS agencia
FROM erp_banvic.transacoes t
JOIN erp_banvic.contas c ON c.num_conta = t.num_conta
JOIN erp_banvic.agencias a ON a.cod_agencia = c.cod_agencia;
```

## Filtros e agregações

```sql
-- Saldo médio por UF
SELECT
    l.uf,
    COUNT(*)              AS num_contas,
    ROUND(AVG(c.saldo_total), 2) AS saldo_medio
FROM erp_banvic.contas c
JOIN erp_banvic.clientes cl ON cl.cod_cliente = c.cod_cliente
JOIN erp_banvic.localidades l ON l.cod_localidade = cl.cod_localidade
GROUP BY l.uf
ORDER BY saldo_medio DESC;
```

```sql
-- Volume de transações por tipo (últimos 30 dias da base)
SELECT
    nome_transacao,
    COUNT(*)                       AS qtd,
    ROUND(SUM(valor_transacao), 2) AS total
FROM erp_banvic.transacoes
WHERE data_transacao >= DATEADD(DAY, -30, (SELECT MAX(data_transacao) FROM erp_banvic.transacoes))
GROUP BY nome_transacao
ORDER BY qtd DESC;
```

```sql
-- Propostas aprovadas por mês
SELECT
    DATE_TRUNC('month', data_entrada_proposta) AS mes,
    COUNT(*)                                   AS propostas_aprovadas,
    ROUND(SUM(valor_financiamento), 2)         AS valor_total
FROM erp_banvic.propostas_credito
WHERE status_proposta = 'Aprovada'
GROUP BY 1
ORDER BY 1;
```

## Top N e ranking

```sql
-- Clientes com maior saldo total (top 10)
SELECT
    cl.cod_cliente,
    cl.primeiro_nome || ' ' || cl.ultimo_nome AS nome_cliente,
    c.saldo_total
FROM erp_banvic.contas c
JOIN erp_banvic.clientes cl ON cl.cod_cliente = c.cod_cliente
ORDER BY c.saldo_total DESC
LIMIT 10;
```

```sql
-- Agências por movimentação (ranking com window function)
SELECT
    a.nome,
    SUM(t.valor_transacao) AS movimentacao,
    RANK() OVER (ORDER BY SUM(t.valor_transacao) DESC) AS posicao
FROM erp_banvic.transacoes t
JOIN erp_banvic.contas c ON c.num_conta = t.num_conta
JOIN erp_banvic.agencias a ON a.cod_agencia = c.cod_agencia
GROUP BY a.nome
ORDER BY posicao;
```

## Conversão de tipos / tratamento

```sql
-- CEP como string de 8 dígitos (importante para joins com clientes)
SELECT cod_cliente, LPAD(CEP, 8, '0') AS cep_8 FROM erp_banvic.clientes;

-- Data em fuso local (se o raw vier em UTC)
SELECT
    data_transacao,
    DATEADD(HOUR, -3, data_transacao) AS data_local
FROM erp_banvic.transacoes;
```

## Testes de qualidade típicos (dbt)

```sql
-- PK duplicada
SELECT cod_cliente, COUNT(*) AS qtd
FROM erp_banvic.clientes
GROUP BY 1
HAVING COUNT(*) > 1;

-- FK órfã (transação apontando para conta inexistente)
SELECT t.*
FROM erp_banvic.transacoes t
LEFT JOIN erp_banvic.contas c ON c.num_conta = t.num_conta
WHERE c.num_conta IS NULL;
```

> Lembre-se: nos models `staging` do dbt, use `{{ source('erp_banvic', 'clientes') }}`
> em vez de `erp_banvic.clientes` direto. As queries acima servem para exploração
> rápida no Databricks/jupyter.
