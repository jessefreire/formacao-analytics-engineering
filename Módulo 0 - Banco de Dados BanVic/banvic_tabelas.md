# Banco BanVic — Schema das Tabelas

Referência coluna a coluna para escrever queries. Tipos aproximados do CSV/raw.

## `localidades`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_LOCALIDADE` | int | **PK** — código da cidade |
| `CIDADE` | string | Nome da cidade |
| `UF` | string | Unidade federativa (2 letras) |

## `agencias`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_AGENCIA` | int | **PK** |
| `NOME` | string | Nome da agência |
| `ENDERECO` | string | Endereço completo |
| `COD_LOCALIDADE` | int | **FK** → `localidades.cod_localidade` |
| `DATA_ABERTURA` | date | Data de abertura |
| `TIPO_AGENCIA` | string | `Física` ou `Digital` |

## `clientes`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_CLIENTE` | int | **PK** |
| `PRIMEIRO_NOME` | string | Primeiro nome |
| `ULTIMO_NOME` | string | Sobrenome |
| `EMAIL` | string | E-mail |
| `TIPO_CLIENTE` | string | `PF` ou `PJ` |
| `DATA_INCLUSAO` | datetime | Quando entrou no banco |
| `CPFCNPJ` | string | CPF ou CNPJ (formatado) |
| `DATA_NASCIMENTO` | date | Data de nascimento/fundação |
| `ENDERECO` | string | Endereço completo |
| `CEP` | string | CEP (8 dígitos, zeros à esquerda) |
| `COD_LOCALIDADE` | int | **FK** → `localidades.cod_localidade` |

## `contas`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `NUM_CONTA` | int | **PK** — número da conta |
| `COD_CLIENTE` | int | **FK** → `clientes.cod_cliente` |
| `COD_AGENCIA` | int | **FK** → `agencias.cod_agencia` |
| `COD_COLABORADOR` | int | **FK** → `colaboradores.cod_colaborador` (gerente da conta) |
| `TIPO_CONTA` | string | `PF` ou `PJ` |
| `DATA_ABERTURA` | datetime | Abertura da conta |
| `SALDO_TOTAL` | decimal | Saldo total (inclui aplicações) |
| `SALDO_DISPONIVEL` | decimal | Saldo disponível para uso |
| `DATA_ULTIMO_LANCAMENTO` | datetime | Última movimentação |

## `transacoes`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_TRANSACAO` | int | **PK** |
| `NUM_CONTA` | int | **FK** → `contas.num_conta` |
| `DATA_TRANSACAO` | datetime | Momento da transação |
| `NOME_TRANSACAO` | string | Tipo da transação (ver valores válidos) |
| `VALOR_TRANSACAO` | decimal | Valor (negativo = saída/débito) |

## `colaboradores`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_COLABORADOR` | int | **PK** |
| `PRIMEIRO_NOME` | string | Primeiro nome |
| `ULTIMO_NOME` | string | Sobrenome |
| `EMAIL` | string | E-mail |
| `CPF` | string | CPF formatado |
| `DATA_NASCIMENTO` | date | Data de nascimento |
| `ENDERECO` | string | Endereço completo |
| `CEP` | string | CEP (8 dígitos) |
| `COD_GERENTE` | int | **FK** → `colaboradores.cod_colaborador` (auto-ref; gerente do colaborador) |
| `COD_LOCALIDADE` | int | **FK** → `localidades.cod_localidade` |

## `colaborador_agencia`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_COLABORADOR` | int | **FK** → `colaboradores.cod_colaborador` |
| `COD_AGENCIA` | int | **FK** → `agencias.cod_agencia` |

Relacionamento **N:N** — um colaborador pode trabalhar em várias agências e uma
agência tem vários colaboradores.

## `propostas_credito`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `COD_PROPOSTA` | int | **PK** |
| `COD_CLIENTE` | int | **FK** → `clientes.cod_cliente` |
| `COD_COLABORADOR` | int | **FK** → `colaboradores.cod_colaborador` (proponente) |
| `DATA_ENTRADA_PROPOSTA` | datetime | Quando a proposta entrou |
| `TAXA_JUROS_MENSAL` | decimal | Taxa mensal (ex: `0.0151` = 1,51%) |
| `VALOR_PROPOSTA` | decimal | Valor total da proposta |
| `VALOR_FINANCIAMENTO` | decimal | Valor financiado |
| `VALOR_ENTRADA` | decimal | Valor de entrada |
| `VALOR_PRESTACAO` | decimal | Valor da parcela |
| `QUANTIDADE_PARCELAS` | int | Nº de parcelas |
| `CARENCIA` | int | Carência em meses |
| `STATUS_PROPOSTA` | string | `Enviada`(0), `Aprovada`(1), `Recusada`(2), `Cancelada`(3), `Em análise`(4) |
