# Curso SQL Completo 2025 — Conteúdo do Curso

**Curso:** Curso SQL Completo 2025 [Iniciantes] + Desafios + Muita Prática
**Autor:** Jhonatan de Souza (Dev Aprender)
**Link:** https://www.youtube.com/watch?v=G7bMwefn8RQ
**Duração:** ~4h
**Bancos usados:** Northwind e AdventureWorks (SQL Server)

Curso gratuito no YouTube que parte do zero absoluto e avança até comandos
intermediários/avançados, com desafios práticos no fim de cada aula (no estilo
do dia a dia do trabalho: o "cliente" pede um problema e você escreve o SQL).

## O que o curso cobre

### 1. Fundamentos
- O que é banco de dados relacional
- Instalação e uso do SQL Server + SSMS
- `SELECT`, `FROM` (consultar colunas e tabelas)
- `AS` (apelidos) e diferença entre coluna/alias

### 2. Filtros
- `WHERE` (filtrar linhas)
- Comparadores: `=`, `>`, `<`, `>=`, `<=`, `<>`
- `AND` / `OR` (combinar condições)
- `IN` (múltiplos valores) e `NOT IN`
- `LIKE` / `NOT LIKE` (padrões com `%` e `_`)
- `BETWEEN` (intervalos) e `IS NULL` / `IS NOT NULL`
- Ordenação com `ORDER BY` (ASC/DESC)

### 3. Funções de agregação
- `COUNT(*)`, `COUNT(coluna)` — contagem
- `COUNT(DISTINCT coluna)` — valores distintos
- `SUM`, `AVG`, `MIN`, `MAX`
- `GROUP BY` — agrupar por coluna
- `HAVING` — filtrar grupos (complemento do WHERE)

### 4. Relacionamentos e JOINs
- Chaves primária (PK) e estrangeira (FK)
- `INNER JOIN` — só o que casa nas duas tabelas
- `LEFT JOIN` — tudo da esquerda + o que casar
- `RIGHT JOIN`, `FULL JOIN`
- Unir múltiplas tabelas num `FROM`

### 5. Combinando consultas
- `UNION` / `UNION ALL` (empilhar resultados)

### 6. Subqueries
- Subconsulta no `WHERE` (comparação com resultado interno)
- Subconsulta no `FROM` (derived table)

### 7. DML — manipulação de dados
- `INSERT INTO ... VALUES / SELECT`
- `UPDATE ... SET ... WHERE`
- `DELETE FROM ... WHERE` (e cuidado com delete sem WHERE!)

### 8. DDL e integridade
- `CREATE TABLE`, tipos de dados
- `ALTER TABLE` (add/drop column, alter type)
- `CONSTRAINT`: `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `DEFAULT`, `UNIQUE`, `NOT NULL`
- `CREATE VIEW` — visões para consultas recorrentes

## Desafios das aulas (referência da transcrição)

> Dica dos desafios: interpretar o pedido em português e traduzir para inglês
> (os nomes das tabelas/colunas dos bancos são em inglês).

1. **Produtos para produção** — nome de todas as peças que pesam **mais de 500** e
   **não mais de 700** kg. → Tabela `Production.Product`, coluna `Weight`.
2. **Empregados casados e assalariados** — lista de todos que são casados e
   assalariados. → `HumanResources.Employee`: `MaritalStatus = 'M'` e
   `SalariedFlag = 1`.
3. **Cobrança de usuário** — achar um usuário ("Ken") que está devendo e obter o
   e-mail dele para cobrança. → Junção de `Person.Person` com
   `Person.EmailAddress` via `BusinessEntityID`.
4. **Clientes com filhos** — filtros e combinações com `AND`/`OR`.

## Como praticar

1. Carregue o banco Northwind (CSVs prontos) e/ou AdventureWorks no
   Databricks/Neon — veja o arquivo `carregar_bancos.md` deste módulo.
2. Para cada bloco acima, escreva 3–5 queries no editor SQL (Databricks/Neon).
3. Repita os desafios das aulas e depois tente resolver com JOINs/agregações
   mais avançadas do que o professor mostrou.

## Referências deste módulo

- `northwind_banco_referencia.md` — schema e dicas da Northwind
- `adventureworks_banco_referencia.md` — schema e dicas da AdventureWorks
- `carregar_bancos.md` — passo a passo para carregar os bancos no Databricks/Neon
