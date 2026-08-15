# Banco de Dados BanVic — Visão Geral

Banco fictício da Indicium usado no curso de Analytics Engineering. Simula o
banco de dados de um banco digital (clientes, contas, agências, colaboradores,
transações e propostas de crédito). Os dados vêm de 8 seeds CSV no repositório
`banvic-dbt` (pasta `seeds/banvic/`).

## Tabelas

| Tabela | Linhas | Descrição | PK |
|--------|-------:|-----------|----|
| `agencias` | 10 | Agências físicas e digitais do banco | `cod_agencia` |
| `localidades` | 1.024 | Cidades + UF de referência | `cod_localidade` |
| `clientes` | 999 | Clientes PF/PJ | `cod_cliente` |
| `contas` | 999 | Contas correntes | `num_conta` |
| `transacoes` | 10.999 | Movimentações das contas | `cod_transacao` |
| `colaboradores` | 100 | Funcionários (gerência hierárquica) | `cod_colaborador` |
| `colaborador_agencia` | 100 | Alocação de colaboradores em agências (N:N) | `cod_colaborador` + `cod_agencia` |
| `propostas_credito` | 2.000 | Propostas de crédito enviadas a clientes | `cod_proposta` |

## Relacionamentos (ER)

```
localidades 1──N agencias
localidades 1──N clientes
localidades 1──N colaboradores

clientes 1──N contas
agencias 1──N contas
colaboradores 1──N contas

contas 1──N transacoes

clientes 1──N propostas_credito
colaboradores 1──N propostas_credito

colaboradores N──N agencias  (via colaborador_agencia)
colaboradores 1──N colaboradores  (auto-ref: cod_gerente)
```

## Convenções

- **Colunas**: `snake_case` na modelagem final; seeds brutas em `UPPER_SNAKE`.
- **Schemas (dbt)**: `erp_banvic` (seeds), `staging`, `intermediate`, `marts`.
- **Valores negativos em `transacoes.valor_transacao`** = saída de dinheiro (débito).
- **CEP**: string de 8 dígitos (zeros à esquerda).
- **Datas**: `DATA_*` em `timestamp`/`date`; normalizar para `America/Sao_Paulo`.

## Campos de referência

| Campo | Valores válidos |
|-------|-----------------|
| `clientes.tipo_cliente` | `PF`, `PJ` |
| `agencias.tipo_agencia` | `Física`, `Digital` |
| `contas.tipo_conta` | `PF`, `PJ` |
| `propostas_credito.status_proposta` | `Enviada`, `Aprovada`, `Em análise`, `Validação documentos` |
| `transacoes.nome_transacao` | `Saque`, `Depósito em espécie`, `Pix - Realizado/Recebido/Saque`, `TED - Realizado/Recebido`, `DOC - Realizado/Recebido`, `Pagamento de boleto`, `Compra Crédito`, `Compra Débito`, `Estorno de Debito`, `Transferência entre CC - Crédito/Débito` |

> Dica: consulte os arquivos `*_tabelas.md` (schema coluna a coluna) e
> `*_queries.md` (exemplos prontos de SQL) deste módulo.
