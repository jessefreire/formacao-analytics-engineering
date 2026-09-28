---
name: reconciliacao-numeros
description: Confere que o mesmo número bate na fonte (SQL), no dbt (teste) e no BI (DAX), e investiga divergências e "vazios" antes de concluir que há bug. Use quando o usuário disser "esse número tá certo?", "não bate", "deu vazio no filtro", "valida o dashboard", "confere com a fonte", ou antes de declarar um dashboard/entrega pronto.
---

# /reconciliacao-numeros

Nenhum número é declarado certo — ou errado — sem ser recalculado em pelo menos duas camadas.
Metade dos "bugs" são comparações com a base errada; a outra metade são bugs de verdade. Só a
conferência separa um do outro.

## Regras

1. **Toda consulta vem comentada**: o que confere e qual o valor esperado (1–2 linhas).
2. **Compare a mesma coisa**: mesmo filtro, mesmo período, mesmo grão. Antes de acusar
   divergência, confirme que o filtro do visual é o que você acha (ex.: "Todos os anos" vs. 2011).
3. **Recalcule na camada de baixo** antes de mexer na de cima.
4. Registre a conclusão, inclusive quando for "falso alarme".

## As três camadas

| Camada | Ferramenta | Exemplo |
|---|---|---|
| Fonte / warehouse | SQL no Databricks | `select sum(orderqty * unitprice) from ... where year(orderdate) = 2011` |
| Transformação | teste singular dbt | `tests/assert_receita_bruta_2011.sql` com tolerância de 1 centavo |
| BI | DAX via MCP (`dax_query_operations` Execute) | `EVALUATE ROW("v", CALCULATE([Receita Bruta], dim_dates[year] = 2011))` |

Com o Power BI Desktop aberto: `connection_operations` ListLocalInstances → Connect →
`dax_query_operations` Execute. Nunca confie num screenshot quando dá para consultar.

## Investigar um visual vazio ("--" ou em branco)

Siga nesta ordem — pare no primeiro que explicar:

1. **O membro existe na dimensão?** `COUNTROWS` na dimensão filtrada.
2. **Ele tem linhas na fato/ponte, em qualquer período?**
   ```dax
   // Quantos pedidos cada motivo tem na base inteira — esperado: alguns com 0
   EVALUATE ADDCOLUMNS(VALUES(dim_sales_reason[reason_name]), "pedidos", CALCULATE(COUNTROWS(bridge_order_sales_reason)))
   ```
   Se 0 em toda a base: **catálogo maior que o usado** — comportamento correto de dimensão.
   Mostrar vazio (não 0) está certo: é ausência de dado, não "vendeu zero".
3. **Órfão?** FK da fato sem par na dimensão → teste `relationships` deveria ter pego.
4. **Relacionamento/direção de filtro no modelo** (M:N, bidirecional) está certo?
5. **A medida** trata BLANK como esperado?

Não confundir "vazio" com "nulo": teste `not_null` não pega catálogo esparso — e não deveria.

## Padrões de bug de DAX já vistos

- `RANKX(ALLSELECTED(dim), ...)` ranqueia quem não tem venda → números gigantes/repetidos.
  Corrigir com `FILTER(ALLSELECTED(dim), CALCULATE([m]) <> BLANK())` + `IF(NOT ISBLANK(...))`
  externo; e ordenar o visual pela medida de valor, não pelo nome.
- Soma atravessando ponte N:N sem `allocation_factor` → total inflado. Conferir: soma por
  motivo sem filtro = total da fato.

## Saída

Uma tabela curta por número conferido: camada, consulta, valor, bate/não bate, conclusão. Se
não bate, a causa e a correção proposta — não corrigir sem mostrar a evidência.
