# Code style da Indicium — resumo de trabalho

> **O que é isto.** Resumo em minhas palavras do
> [`indiciumtech/indicium-code-style`](https://bitbucket.org/indiciumtech/indicium-code-style),
> o padrão de código que a Indicium aplica em todos os desenvolvimentos. O repositório é de
> leitura pública (confirmado por `git ls-remote` anônimo), e este arquivo é **derivado**, não
> cópia — mesma prática que uso para o material do curso.
>
> Fonte: `sql_style_guide.md`, `sql_best_practices.md` e `dbt_coding_conventions.md`.
> Serve como checklist da análise exploratória (Etapa 2) e do projeto dbt (Etapa 5) do
> desafio final.

---

## 1. A regra que mais me pegou

**Não usar alias de tabela desnecessário, e muito menos iniciais.** A orientação é: se o nome
da tabela tem três palavras ou menos, **não dê alias**. Escreva a coluna prefixada pelo nome
da tabela inteiro.

```sql
/* certo */
select
    customers.email
    , orders.invoice_number
from customers
inner join orders on customers.id = orders.customer_id

/* errado */
select c.email, o.invoice_number
from customers as c
inner join orders as o on c.id = o.customer_id
```

Isso derruba o hábito de escrever `soh`, `sod`, `p`, `c`. No AdventureWorks,
`salesorderheader` é uma palavra: **sem alias.**

Quando o nome é longo demais, use um **subconjunto das palavras** em vez de iniciais —
`partner_shipments_order_line_items` pode virar `line_items` se for a única tabela de itens
na consulta.

## 2. A outra que muda como se lê um join

**Na condição do join, a tabela citada primeiro vem imediatamente depois do `on`.** O motivo
é bonito: assim a leitura revela se o join multiplica linhas.

```sql
/* chave primária = chave estrangeira -> um-para-muitos -> FANOUT */
from customers
left join orders on customers.id = orders.customer_id

/* chave estrangeira = chave primária -> muitos-para-um -> sem fanout */
from orders
left join customers on orders.customer_id = customers.id
```

Escrever na ordem errada não muda o resultado, mas esconde o risco de duplicação — que é
exatamente o problema do motivo de venda no nosso desafio.

## 3. Formatação

| Regra | |
|---|---|
| Linter | **sqlfluff 1.4.5** — a versão está fixada no guia, e as regras derivam dela |
| Largura | máximo **100** caracteres por linha |
| Indentação | **4 espaços**. Nunca tab |
| Palavras-chave e funções | **minúsculas** |
| Vírgula | **à frente** da coluna, não no fim da linha anterior |
| Fim de linha | nunca terminar com operador (`and`, `or`, `+`, `||`) |
| Aspas | simples, para strings |
| Comentário | sempre `/* */` |
| CTE | indentada; e **preferir CTE a subquery** |
| `join` | `inner join` explícito, nunca `join` solto |
| `on` | sempre em linha própria e indentado a partir do `join` |
| Parênteses | sem espaço extra encostado neles |

**Cláusula `select`:** uma única coluna fica na mesma linha do `select`; duas ou mais, cada
uma em sua linha — **inclusive a primeira** —, um nível a mais de indentação.

```sql
select id

select
    id
    , email
```

## 4. Sintaxe: o que a casa prefere

| Use | Em vez de |
|---|---|
| `!=` | `<>` |
| `\|\|` | `concat` |
| `is null` / `is not null` | `isnull` / `notnull` |
| `case` | `iff`, `if` |
| `where` | `having`, quando os dois resolvem |
| `union all` | `union`, salvo se realmente precisar remover duplicata |
| `select distinct` | agrupar por todas as colunas |
| `coalesce` | `ifnull`, `nvl` |
| `count(*)` | `count(1)`, `count(0)` |
| data como **string** | palavra-chave, em funções de date part |

Mais: **sempre `as`** ao apelidar coluna, expressão ou tabela; **sempre apelidar agregação**;
**nunca palavra reservada como identificador**; **não usar `using`** em join; e evitar
`order by` a menos que o resultado dependa dele.

Identificadores — alias e nome de CTE — em **`snake_case` minúsculo**.

## 5. Nomes de coluna

**Data e hora**, pela natureza do campo:

- data em UTC → `<evento>_date`
- data com fuso → `<evento>_date_<fuso>`, ex. `order_date_et`
- data+hora em UTC → `<evento>_at`
- data+hora com fuso → `<evento>_at_<fuso>`, ex. `created_at_pt`
- indicadores de fuso: `et`, `ct`, `mt`, `pt`

**Booleano** leva prefixo de verbo em terceira pessoa: `is_`, `was_`, `has_`, `had_`,
`does_`, `did_`.

## 6. dbt

**Nome de modelo no plural** — tabela é coleção de coisas. Prefixos:

| Prefixo | Camada |
|---|---|
| `stg_` | staging |
| `dim_` | dimensão |
| `fact_` | fato |
| `agg_` | agregado |
| `bridge_` | bridge |

Modelo de source: `<nome do source>__<nome da tabela>`, com **dois** underscores, porque os
nomes podem conter underscore.

> ⚠️ **Divergência interna a conhecer:** o `dbt_coding_conventions.md` usa `bridge_`, e o doc
> `5.4) Boas práticas envolvendo tabelas bridges` do referencial de processos usa **`bdg_`**.
> Duas fontes da casa discordam. Eu sigo o code style, que é o documento normativo de código.

Outras regras:

- **Só source e staging leem de `source()`.** Todo o resto lê de `ref()`.
- **Um modelo, uma chave primária.** Chave composta? Crie surrogate. **Agregado e bridge são
  exceção** e podem não ter PK.
- Configuração específica do modelo vai **dentro do modelo**, não no `dbt_project.yml`.
- Jinja com espaço por dentro dos delimitadores: `{{ ref('customers') }}`, nunca
  `{{ref('customers')}}`. Mas argumento nomeado de macro **sem** espaço no `=`:
  `{{ foo('bar', baz=123) }}`.
- Source e staging materializados vão para schema `<schema de produção>_staging`; dado
  sensível para `<schema>_sensitive`.
- Documentação e testes em um `schema.yml` **por modelo**, nomeado `<nome do modelo>.yml`.
- Modelo de source deve **renomear** coluna quando o nome da origem conflita com palavra
  reservada.

## 7. Como isto se aplica ao desafio

- **Etapa 2 (exploratória):** todo SQL do notebook segue as seções 1 a 5. Em particular, sem
  alias de iniciais — `from adventure_works.salesorderheader`, não `as soh`.
- **Etapa 5 (dbt):** as seções 6 valem inteiras. A bridge do motivo de venda vira
  `bridge_orders_sales_reasons`, e a camada bruta pode manter `group` e `type` entre
  backticks porque o rename acontece no staging.
- **A camada bruta é a exceção consciente:** ela espelha a origem, então preserva nomes
  reservados. O guia manda renomear **no modelo de source**, e é lá que renomeio.
