# Índice Consolidado — Formação Analytics Engineer (Indicium Academy)

> **⚠️ DOCUMENTO VIVO** — Este arquivo, `AGENTS.md` e `Analytics Engineer Training 2026.md` devem ser **atualizados automaticamente** a cada nova conversa com agentes, novo material do curso ou mudança estrutural no projeto. Não deixe para depois.

> Documento vivo. Atualize a cada módulo concluído. Mantenha a estrutura para facilitar navegação.

---

## Módulo 1 — Introdução à Análise de Dados

**Status:** ✅ Concluído  
**Temas principais:** Papéis da área de dados, perfil do Analista de Dados, processo CRISP-DM, tipos de análise, 5 Vs do Big Data, OKRs/KPIs, soft skills, ética.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo completo) | `[FADA] Conteúdo - Módulo 01 - Introdução à Análise de Dados.docx.pdf` |
| MD (Conteúdo completo) | `[FADA] Conteúdo - Módulo 01 - Introdução à Análise de Dados.docx.md` |
| PDF (Slides EN) | `[FADA _ English] Slides - Introduction to data analysis.pptx.pdf` |
| MD (Slides EN) | `[FADA _ English] Slides - Introduction to data analysis.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo1.md` | Resumo estruturado com tabelas, conexões com desafio final |
| `decoreba_modulo1.txt` | Pontos-chave para memorização (formato "pegadinhas" do quiz) |

### Conceitos-Chave (Referência Rápida)
| Conceito | Detalhe |
|----------|---------|
| **6 Papéis** | Arquiteto, Eng. Dados, Eng. Analytics, Analista Dados, Cientista Dados, Eng. ML |
| **Tripé DA** | Matemática/Estatística + Programação + Negócio |
| **CRISP-DM (6 etapas)** | Entender problema → Entender dados/usuário → Preparar → Explorar → Concluir → Comunicar (cíclico) |
| **Tipos de análise** | Descritiva, Segmentação, Agregação, Geoespacial, Séries temporais, Classificação, Regressão, Teste A/B |
| **Exploratória vs Explicativa** | Bastidor (busca padrões) vs Narrativa guiando conclusão |
| **5 Vs** | Volume, Velocidade, Variedade, **Veracidade ≠ Integridade** |
| **OKR vs KPI** | OKR = Objetivo + Key Results; KPI mede progresso (tipos: Produtividade, Qualidade, Capacidade, Estratégico) |
| **Ferramentas gestão** | PDCA, 5 Porquês, 5W2H, Ishikawa, GUT (priorizar), Pareto, Brainstorming, Fluxograma |
| **Ordem GUT → Ishikawa** | GUT escolhe qual problema atacar; Ishikawa investiga causa raiz |
| **Ética** | Viés estrutural em clusters; segurança de dados sensíveis |

### Conexões com Desafio Final
- **dbt** = Eng. Analytics (Data Marts) — "encanamento"
- **Power BI** = Dashboards (Analista de Dados) — análise **explicativa**
- Antes de modelar: definir KPIs/OKRs que o dashboard responderá

---

## Módulo 2 — SQL para Análise de Dados

**Status:** ✅ Concluído  
**Temas principais:** Bancos de dados (relacional vs NoSQL), SQL (DQL/DML/DDL/DCL/TCL), consultas básicas, WHERE, GROUP BY, HAVING, JOINs, UNION, funções (agregação, escalares, analíticas), CTEs, performance.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo completo) | `Conteúdo - Módulo 2 - SQL (1).pdf` |
| MD (Conteúdo completo) | `Conteúdo - Módulo 2 - SQL (1).md` |
| PDF (Slides) | `[Academy] Querying data with SQL - Slides.pptx.pdf` |
| MD (Slides) | `[Academy] Querying data with SQL - Slides.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `Resumo_Modulo_2_SQL.md` | Resumo técnico completo com exemplos SQL, checklist autoavaliação, material complementar |
| `Decoreba_SQL.txt` | Guia prático "como pensar na query" + referência rápida de sintaxe |

### Conceitos-Chave (Referência Rápida)

#### Estrutura Básica
| Item | Detalhe |
|------|---------|
| **Ordem cláusulas** | `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT` |
| **Ordem execução** | `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` |

#### Tipos de Banco
| Tipo | Uso | Exemplos |
|------|-----|----------|
| Relacional | Estrutura fixa, integridade, transações | PostgreSQL, MySQL, Oracle, SQL Server |
| NoSQL | Flexibilidade, escalabilidade | MongoDB, Cassandra, Redis |
| Cloud (DBaaS) | Gerenciado, escalável | AWS RDS, BigQuery, Azure SQL |
| Distribuído | Alta escala, tolerância a falhas | Cassandra, DynamoDB, Bigtable |

#### Chaves
| Chave | Função |
|-------|--------|
| **PK** | Identificador único (não nulo, não repetido) |
| **FK** | PK de outra tabela — cria relacionamento |
| **Integridade Referencial** | Impede órfãos (ex: excluir cliente com pedidos) |

#### WHERE — Filtros
| Operador | Exemplo |
|----------|---------|
| Igualdade | `WHERE cidade = 'SP'` |
| Comparação | `>=, >, <, <=, <> / !=` |
| Lógicos | `AND` (todas), `OR` (uma), `NOT` (nega) |
| Nulos | `IS NULL` / `IS NOT NULL` |
| Lista | `IN ('SP','RJ','MG')` / `NOT IN` |
| Intervalo | `BETWEEN 10 AND 100` |
| Padrão texto | `LIKE 'Jo%'` (`%`=qualquer seq, `_`=1 char) |

#### Agregação
| Função | Retorna |
|--------|---------|
| `COUNT(*)` / `COUNT(col)` | Total linhas / não-nulas |
| `SUM(col)` | Soma |
| `AVG(col)` | Média |
| `MIN(col)` / `MAX(col)` | Menor / Maior |

**Regra de Ouro GROUP BY:** toda coluna no `SELECT` fora de agregação deve estar no `GROUP BY`.

#### HAVING vs WHERE
| Filtro | Momento | Uso |
|--------|---------|-----|
| `WHERE` | Antes do GROUP BY | Linhas individuais |
| `HAVING` | Após GROUP BY | Grupos (usa agregações) |

#### JOINs (Horizontal)
| Tipo | Retorna |
|------|---------|
| `INNER JOIN` | Apenas matches em ambas (interseção) |
| `LEFT JOIN` | Tudo da esquerda + matches direita (NULL se não) |
| `RIGHT JOIN` | Tudo da direita + matches esquerda |
| `FULL JOIN` | Tudo de ambas, NULL onde não match |
| `CROSS JOIN` | Produto cartesiano (sem ON — **cuidado**) |
| `SELF JOIN` | Tabela com ela mesma (hierarquia) |

#### UNION (Vertical)
| Variante | Comportamento |
|----------|---------------|
| `UNION` | Remove duplicatas |
| `UNION ALL` | Mantém duplicatas (mais rápido) |
| **Requisito** | Mesmas colunas (nome, tipo, ordem) |

#### Funções Escalares (por categoria)
| Categoria | Funções |
|-----------|---------|
| Texto | `UPPER`, `LOWER`, `TRIM`, `CONCAT`, `SUBSTR`, `REPLACE`, `SPLIT_PART`, `LEFT`, `RIGHT` |
| Numéricas | `ROUND`, `ABS`, `CEIL`, `FLOOR` |
| Data/Hora | `NOW`, `YEAR`, `MONTH`, `DAY`, `DATEADD` |
| Conversão | `CAST`, `COALESCE` (NULL → valor), `NULLIF` (igual → NULL) |

#### Window Functions (Analíticas)
| Função | Uso |
|--------|-----|
| `ROW_NUMBER()` | Numeração sequencial |
| `RANK()` | Ranking com saltos em empates |
| `DENSE_RANK()` | Ranking sem saltos |
| `LAG(col)` | Valor linha anterior |
| `LEAD(col)` | Valor próxima linha |
| `FIRST_VALUE` / `LAST_VALUE` | Extremos da janela |
| `SUM/AVG/COUNT OVER` | Agregação por linha |

**Sintaxe:** `FUNCAO() OVER (PARTITION BY grupo ORDER BY ordem)`

#### CTEs
```sql
WITH cte1 AS (SELECT ...), cte2 AS (SELECT ... FROM cte1)
SELECT * FROM cte2;
```
- Organiza passos, reutiliza resultados, melhora legibilidade

#### Performance
| Prática | Por que |
|---------|---------|
| Evite `SELECT *` | Menos dados trafegados |
| Filtre cedo (`WHERE`) | Reduz linhas processadas |
| Crie índices em colunas filtradas | Busca O(log n) vs O(n) |
| `EXPLAIN` | Mostra plano de execução |

---

## Módulo 3 — Modelagem de dados

**Status:** ⏳ Pendente  
**Temas previstos:** Modelagem relacional, normalização, star/snowflake schema, fato vs dimensão, lineage, dbt.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo) | `[FADA] Conteúdo - Módulo 3 - Modelagem de dados.docx.pdf` |
| MD (Conteúdo) | `[FADA] Conteúdo - Módulo 3 - Modelagem de dados.docx.md` |
| PDF (Slides EN) | `[English _ FADA] Módulo 3 - Modelagem de dados.pptx.pdf` |
| MD (Slides EN) | `[English _ FADA] Módulo 3 - Modelagem de dados.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo3.md` | Resumo estruturado da modelagem de dados |
| `decoreba_modulo3.txt` | Pontos-chave para memorização |

---

## Módulo IV — Engenharia de Dados com dbt e Snowflake

**Status:** ⏳ Pendente  
**Temas previstos:** dbt Core vs Cloud, transformação SQL, lineage, testes, documentação, Snowflake como DW.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo) | `[FEA] Conteúdo - Módulo IV - Engenharia de Dados com dbt e Snowflake.pdf` |
| MD (Conteúdo) | `[FEA] Conteúdo - Módulo IV - Engenharia de Dados com dbt e Snowflake.md` |
| PDF (Slides EN) | `[Academy] EN-US - Asynchronous FEA - Analytics Engineering Class with dbt and Snowflake.pptx.pdf` |
| MD (Slides EN) | `[Academy] EN-US - Asynchronous FEA - Analytics Engineering Class with dbt and Snowflake.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_moduloIV.md` | Resumo estruturado de dbt/Snowflake (local vs Cloud) |
| `decoreba_moduloIV.txt` | Pontos-chave para memorização |

---

## Módulo 4 — Storytelling com Dados

**Status:** ⏳ Pendente  
**Temas previstos:** Narrativa com dados, data-ink ratio, gráficos escolhas, audiência, apresentação executiva.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo) | `Conteúdo - Módulo 4 - Storytelling com Dados.docx.pdf` |
| MD (Conteúdo) | `Conteúdo - Módulo 4 - Storytelling com Dados.docx.md` |
| PDF (Slides EN) | `[English _ FADA] Módulo 4 - Storytelling com Dados.pptx.pdf` |
| MD (Slides EN) | `[English _ FADA] Módulo 4 - Storytelling com Dados.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo4.md` | Resumo estruturado de storytelling com dados |
| `decoreba_modulo4.txt` | Pontos-chave para memorização |

---

## Módulo 5 — Design de Experiência

**Status:** ⏳ Pendente  
**Temas previstos:** UX para dados, usabilidade em dashboards, percepção visual, acessibilidade.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Apostila) | `[FADA] - APOSTILA - Módulo 5 - Design de Experiência.docx.pdf` |
| MD (Apostila) | `[FADA] - APOSTILA - Módulo 5 - Design de Experiência.docx.md` |
| PDF (Slides EN) | `Copy of [FADA] Módulo 5 - Design de Experiência.pptx.pdf` |
| MD (Slides EN) | `Copy of [FADA] Módulo 5 - Design de Experiência.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo5.md` | Resumo estruturado de design de experiência/UX |
| `decoreba_modulo5.txt` | Pontos-chave para memorização |

---

## Módulo 6 — Dashboards com Power BI

**Status:** ⏳ Pendente  
**Temas previstos:** Power BI Desktop, modelagem DAX, visuais, filtros, publicação, gateway.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo) | `Conteúdo - Módulo 6 - Criando dashboards com Power BI.docx.pdf` |
| MD (Conteúdo) | `Conteúdo - Módulo 6 - Criando dashboards com Power BI.docx.md` |
| PDF (Slides EN) | `[English _ FADA] - Módulo 6 - Criando dashboards com Power BI.docx.pptx.pdf` |
| MD (Slides EN) | `[English _ FADA] - Módulo 6 - Criando dashboards com Power BI.docx.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo6.md` | Resumo estruturado de dashboards no Power BI |
| `decoreba_modulo6.txt` | Pontos-chave para memorização |

---

## Módulo 7 — Estatística aplicada à análise de dados

**Status:** ⏳ Pendente  
**Temas previstos:** Estatística descritiva, distribuições, testes de hipótese, correlação, regressão, p-valor.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo) | `[FADA] Conteúdo - Módulo 7 - Estatística aplicada à análise de dados.docx.pdf` |
| MD (Conteúdo) | `[FADA] Conteúdo - Módulo 7 - Estatística aplicada à análise de dados.docx.md` |
| PDF (Slides EN) | `Copy of [FADA] Módulo 7 - Estatística aplicada à análise de dados.pptx.pdf` |
| MD (Slides EN) | `Copy of [FADA] Módulo 7 - Estatística aplicada à análise de dados.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo7.md` | Resumo estruturado de estatística aplicada |
| `decoreba_modulo7.txt` | Pontos-chave para memorização |

---

## Módulo 8 — Python

**Status:** ⏳ Pendente  
**Temas previstos:** Python para análise de dados, pandas, matplotlib/seaborn, Jupyter, ETL básico.

### Arquivos Oficiais
| Tipo | Arquivo |
|------|---------|
| PDF (Conteúdo) | `[FADA] Conteúdo - Módulo 8 - Python.pdf` |
| MD (Conteúdo) | `[FADA] Conteúdo - Módulo 8 - Python.md` |
| PDF (Slides EN) | `[English _ FADA] Módulo de Python.pptx.pdf` |
| MD (Slides EN) | `[English _ FADA] Módulo de Python.pptx.md` |

### Resumos Pessoais
| Arquivo | Descrição |
|---------|-----------|
| `resumo_modulo8.md` | Resumo estruturado de Python para dados |
| `decoreba_modulo8.txt` | Pontos-chave para memorização |

---

## Como Atualizar Este Índice

1. **Ao concluir um módulo:**
   - Mude `Status` para `✅ Concluído`
   - Preencha "Temas principais"
   - Adicione linhas nas tabelas "Arquivos Oficiais" e "Resumos Pessoais"
   - Complete a seção "Conceitos-Chave" com tabelas de referência rápida

2. **Quando novos módulos forem liberados:**
   - Copie o bloco do "Módulo 3" e adapte o número
   - Mantenha a estrutura idêntica para consistência

3. **Nomenclatura de arquivos sugerida:**
   ```
   [Módulo X] Arquivo Oficial.pdf
   [Módulo X] Arquivo Oficial.md
   resumo_moduloX.md
   decoreba_moduloX.txt
   ```

---

## Referências Cruzadas

| Documento | Localização |
|-----------|-------------|
| Diário de bordo completo | `Analytics Engineer Training 2026.md` |
| Guia dbt prático | `GUIA_DBT_BANVIC.md` |
| Configuração projeto | `AGENTS.md` |
| Desafio BanVic (exemplos) | `Exemplos repo banvic/` |