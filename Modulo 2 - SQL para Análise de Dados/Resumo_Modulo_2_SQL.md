# Resumo de Estudo — Módulo 2: Consultando Dados com SQL

*Curso: SQL para Análise de Dados | Indicium Academy*
*Cenário prático usado no módulo: banco fictício BanVic*

---

## 1. Bancos de Dados

Um banco de dados é uma coleção organizada e estruturada de informações, geralmente armazenada em formato eletrônico. Um **SGBD (Sistema de Gerenciamento de Banco de Dados)** é a interface que traduz consultas, localiza a informação e devolve a resposta — exemplos: Oracle, PostgreSQL, MySQL, SQL Server.

A operação de um banco pode ser pensada em três camadas: camada de consulta (onde o usuário pergunta), camada de processamento (onde o SGBD traduz a pergunta) e camada de armazenamento (onde os dados brutos ficam guardados).

### Principais tipos de banco de dados

| Tipo | Características | Vantagens | Desvantagens | Exemplos |
|---|---|---|---|---|
| Relacional | Dados em tabelas (linhas/colunas), com relacionamentos via chaves; usa SQL | Estrutura bem definida, integridade dos dados, consultas eficientes, suporte a transações | Escalabilidade e flexibilidade limitadas, custo elevado | Oracle, SQL Server, MySQL, PostgreSQL |
| Não relacional (NoSQL) | Estrutura flexível: documentos, grafos, chave-valor | Escalabilidade, flexibilidade, custo | Dificuldade em consultas complexas, menor integridade | MongoDB, Cassandra, Redis, Couchbase |
| Em nuvem | Modelo de implementação (pode ser relacional ou não) hospedado por um provedor (DBaaS) | Escalabilidade, disponibilidade, acesso remoto | Dependência do fornecedor, latência, custo | AWS, GCP, Azure |
| Orientado a objetos | Dados armazenados como "objetos" (dados + métodos) | Modelagem mais natural, reutilização de código | Curva de aprendizado íngreme, incompatibilidade com sistemas legados | ObjectDB, db4o |
| Distribuído | Múltiplos bancos interligados em rede, funcionando como um único sistema | Alta escalabilidade, tolerância a falhas | Complexidade de coordenação | Cassandra, DynamoDB, Bigtable |

O modelo **relacional**, proposto por Edgar Codd em 1970, é o mais difundido no mundo (responde pela maior parte dos dados armazenados hoje).

### Estrutura do modelo relacional

- **Tabela**: armazena uma categoria de informação (ex.: "Clientes").
- **Coluna (campo/atributo)**: todos os valores do mesmo tipo (texto, número, data...).
- **Linha (registro)**: uma entrada única na tabela.
- **Campo**: interseção de linha e coluna — a menor unidade de dado.
- **Chave Primária (PK)**: identifica cada registro de forma única (ex.: CPF). Não pode se repetir.
- **Chave Estrangeira (FK)**: a PK de uma tabela inserida em outra, criando o relacionamento entre elas (ex.: `cod_cliente` na tabela de pedidos).
- **Integridade referencial**: garante consistência — por exemplo, impede excluir um cliente que ainda tem pedidos vinculados.

---

## 2. O que é SQL

**SQL (Structured Query Language)** é a linguagem padrão para consultar e manipular dados em bancos relacionais. A interação acontece por meio de *queries* (consultas).

### Sublinguagens do SQL

| Sigla | Nome | Função | Comandos principais |
|---|---|---|---|
| DQL | Data Query Language | Consultar (ler) dados, sem modificar nada | `SELECT` |
| DML | Data Manipulation Language | Inserir, atualizar, excluir dados | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DDL | Data Definition Language | Define a estrutura (esqueleto) do banco | `CREATE`, `ALTER`, `DROP`, `RENAME`, `TRUNCATE` |
| DCL | Data Control Language | Gerencia permissões de acesso | `GRANT`, `REVOKE` |
| TCL/DTL | Transaction Control Language | Confirma ou desfaz transações | `COMMIT`, `ROLLBACK` |

No dia a dia de um analista de dados, o **DQL (SELECT)** é, disparado, o mais usado, seguido pelo DML.

### Ordem obrigatória das cláusulas

```
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

---

## 3. Consultas Básicas

**SELECT / FROM** — define quais colunas mostrar e de qual tabela:
```sql
SELECT coluna_1, coluna_2 FROM tabela;
SELECT * FROM tabela;          -- * = todas as colunas
```

**LIMIT** — restringe o número de linhas retornadas:
```sql
SELECT * FROM tabela LIMIT 10;
```

**ORDER BY** — ordena o resultado (padrão é `ASC`; use `DESC` para decrescente). Pode ordenar por múltiplas colunas, usando a segunda como critério de desempate:
```sql
SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 5; -- 5 mais caros
SELECT nome, estado, cidade FROM clientes ORDER BY estado ASC, cidade ASC;
```

**WHERE** — filtra linhas segundo uma condição:
```sql
WHERE cidade = 'São Paulo'                 -- igualdade (texto entre aspas simples)
WHERE preco >= 100.00                      -- comparação: <> != > < >= <=
WHERE categoria = 'Eletrônicos' AND preco > 500.00   -- lógico: AND / OR / NOT
WHERE estado IN ('SP', 'RJ', 'MG')         -- lista de valores
WHERE data_de_envio IS NULL                -- valores nulos (IS NOT NULL para o oposto)
```

**LIKE** — busca por padrão de texto usando curingas:
- `%` representa qualquer sequência de caracteres (inclusive nenhuma).
- `_` representa exatamente um caractere.
```sql
WHERE nome LIKE 'Jo%'      -- começa com "Jo"
WHERE nome LIKE '%ar%'     -- contém "ar" em qualquer posição
```

**IN / NOT IN** — alternativa mais limpa a vários `OR`:
```sql
WHERE estado IN ('SP', 'RJ', 'MG')
-- equivalente a: WHERE estado = 'SP' OR estado = 'RJ' OR estado = 'MG'
```

**BETWEEN / NOT BETWEEN** — filtra por intervalo (inclusive):
```sql
WHERE preco BETWEEN 10 AND 100
```

### Operadores aritméticos
`+`  `-`  `*`  `/`  `%` (módulo)  `ABS()`  `ROUND()`

### Operadores lógicos
`AND` (todas as condições verdadeiras) · `OR` (ao menos uma verdadeira) · `NOT` (nega a condição)

---

## 4. Agregação e Classificação Condicional

**GROUP BY** — agrupa linhas com valores em comum, geralmente combinado com uma função de agregação:
```sql
SELECT colunaA, colunaB, SUM(colunaC) AS soma
FROM tabela
GROUP BY colunaA, colunaB;
```
Regra de ouro: toda coluna do `SELECT` que **não** está dentro de uma função de agregação precisa aparecer no `GROUP BY`.

**HAVING** — filtra os *grupos* já formados (o `WHERE` filtra linhas *antes* do agrupamento; o `HAVING` filtra *depois*):
```sql
SELECT colunaA, SUM(colunaC) AS soma
FROM tabela
GROUP BY colunaA
HAVING soma > 100;
```

**CASE WHEN** — cria uma nova coluna com lógica condicional (equivalente ao SE/IF do Excel):
```sql
SELECT
  colunaA,
  CASE
    WHEN condicao1 THEN 'resultado1'
    WHEN condicao2 THEN 'resultado2'
    ELSE 'resultado3'
  END AS nova_coluna
FROM tabela;
```

---

## 5. Combinando Tabelas: JOIN e UNION

**JOIN** — combina colunas de duas ou mais tabelas com base em uma chave comum (definida na cláusula `ON`):

| Tipo | O que retorna |
|---|---|
| INNER JOIN (ou só JOIN) | Apenas os registros com correspondência em ambas as tabelas (interseção) |
| LEFT JOIN | Todos os registros da tabela da esquerda + correspondências da direita (nulo se não houver) |
| RIGHT JOIN | Todos os registros da tabela da direita + correspondências da esquerda |
| FULL (OUTER) JOIN | Todos os registros de ambas as tabelas, com nulo onde não houver correspondência |
| CROSS JOIN | Produto cartesiano — cada linha de uma tabela combinada com cada linha da outra (sem `ON`; cuidado com volume gerado) |
| SELF JOIN | Uma tabela unida com ela mesma (ex.: hierarquia funcionário/gestor) |

```sql
SELECT t1.colunas, t2.colunas
FROM tabela1 t1
JOIN tabela2 t2 ON t1.colunaX = t2.colunaX;
```

**UNION** — empilha (verticalmente) os resultados de duas ou mais consultas `SELECT` em um único conjunto. Exige que as tabelas tenham as mesmas colunas. Pode ser custoso em tabelas grandes:
```sql
SELECT colunas FROM tabela1
UNION
SELECT colunas FROM tabela2;
```

---

## 6. Funções em SQL

Funções são procedimentos que recebem um ou mais argumentos e retornam um resultado. Existem três tipos principais:

### Funções de agregação
Reduzem um conjunto de valores a um único resultado: `SUM`, `AVG`, `COUNT`, `MIN`, `MAX`.

### Funções escalares
Manipulam valores individualmente, divididas em quatro grupos:
- **Texto**: `UPPER`, `LOWER`, `TRIM`, `CONCAT`, `SUBSTR`, `REPLACE`, `SPLIT_PART`, `LEFT`, `RIGHT`
- **Numéricas**: `ROUND`, `ABS`, `CEIL`/`CEILING`, `FLOOR`
- **Data/hora**: `NOW`, `YEAR`, `MONTH`, `DAY`, `DATEADD`
- **Conversão**: `CAST`, `CONVERT`, `COALESCE`, `NULLIF`

Exemplos úteis de manipulação textual:
```sql
SELECT UPPER(SUBSTR(nome, 1, 1)) || LOWER(SUBSTR(nome, 2)) FROM tabela;  -- primeira letra maiúscula
SELECT REPLACE(email, '@empresa.com', '') FROM tabela;                   -- extrai usuário do email
SELECT SPLIT_PART(email, '@', 1) FROM tabela;                            -- separa por delimitador
```

### Funções analíticas (window functions)
Calculam um valor agregado **para cada linha**, com base em uma "janela" definida pela cláusula `OVER` (opcionalmente dividida em partições com `PARTITION BY` e ordenada com `ORDER BY`):
```sql
SELECT colunaA, colunaB,
       AVG(colunaC) OVER (PARTITION BY colunaB ORDER BY colunaA) AS media
FROM tabela;
```
Subtipos: funções de janela (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`), agregação analítica (`SUM`, `COUNT` com `OVER`), deslocamento (`FIRST_VALUE`, `LAST_VALUE`), proporção (`PERCENT_RANK`, `CUME_DIST`) e estatística (`STDDEV`, `VAR`).

---

## 7. Organizando Consultas Complexas: CTEs

**CTE (Common Table Expression)** — organiza o código e guarda o resultado de uma consulta para ser reutilizado em outra, tornando consultas complexas mais legíveis e fáceis de manter:
```sql
WITH cte1 AS (
  SELECT colunas FROM tabelaX
),
cte2 AS (
  SELECT colunas FROM tabelaY
)
SELECT cte1.colunas, cte2.colunas
FROM cte1
JOIN cte2 ON cte1.colunaA = cte2.colunaA;
```
Boas práticas: comentar o que cada CTE faz, especialmente as com regras de negócio ou cálculos específicos — facilita a manutenção por outras pessoas (ou por você mesmo, no futuro).

---

## 8. Gestão de Usuários

Controla quem pode acessar e o que pode fazer no banco de dados:

- **CREATE USER / ALTER USER / DROP USER** — criar, modificar e excluir contas.
- **CREATE ROLE / ALTER ROLE / DROP ROLE** — papéis (roles) agrupam privilégios e simplificam a administração.
- **GRANT / REVOKE** — concede ou revoga privilégios de usuários/roles sobre objetos do banco.

```sql
GRANT SELECT, INSERT ON clientes TO usuario_x;
REVOKE INSERT ON clientes FROM usuario_x;
```

---

## 9. Melhoria de Desempenho

Práticas para evitar consultas lentas conforme o volume de dados cresce:

1. **Criar índices** nas colunas mais consultadas — acelera a busca de registros.
2. **Ajustar o esquema do banco** — tabelas normalizadas evitam consultas excessivamente complexas.
3. **Usar WHERE e JOIN com eficiência** — reduz o volume de dados processado.
4. **Evitar operações em larga escala** sem necessidade (`SELECT *`, `ORDER BY` em grandes volumes) — traga só as colunas necessárias.
5. **Monitorar o desempenho** com `EXPLAIN`, que mostra o plano de execução da consulta (estratégia de acesso, uso de índices, custo estimado).
6. **Usar cache de consultas**, quando disponível, para consultas repetidas.

```sql
EXPLAIN SELECT colunas FROM tabela WHERE condicoes;
```

---

## Checklist de Autoavaliação

Antes de seguir para o próximo módulo, veja se você consegue responder:

- Qual a diferença entre banco relacional e não relacional, e quando usar cada um?
- O que são chave primária e chave estrangeira, e por que elas garantem integridade referencial?
- Qual a ordem correta das cláusulas em uma query SQL?
- Qual a diferença entre `WHERE` e `HAVING`?
- Quando usar `INNER JOIN` vs. `LEFT JOIN` vs. `FULL JOIN`?
- Qual a diferença entre `JOIN` (horizontal) e `UNION` (vertical)?
- Quais são os três tipos de função em SQL e um exemplo de cada?
- Para que serve uma CTE, e por que ela ajuda na manutenção do código?
- Cite três boas práticas para melhorar o desempenho de uma consulta.

---

## Material Complementar (indicado no curso)

- **Livro**: *Learning SQL*, Alan Beaulieu
- **Repositório**: [github.com/cathytanimura/sql_book](https://github.com/cathytanimura/sql_book)
- **Artigo**: [SQL Cheat Sheet — GeeksforGeeks](https://www.geeksforgeeks.org/sql-cheat-sheet/)
- **Artigo**: [Window Functions — Medium/Comunidade DS](https://medium.com/comunidadeds/windows-functions-desvendando-o-poder-das-fun%C3%A7%C3%B5es-de-janela-no-sql-805cf12bfff2)
- **Livro**: *SQL para Análise de Dados*, Cathy Tanimura
