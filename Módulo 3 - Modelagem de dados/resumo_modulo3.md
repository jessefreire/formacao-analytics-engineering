# Resumo — Módulo 3: Modelagem de dados

## 1. Introdução aos bancos de dados analíticos

Bancos de dados analíticos são sistemas especializados projetados para suportar análise de dados em larga escala, otimizados para consultas complexas e geração de insights. Diferem dos bancos transacionais em propósito, estrutura, conteúdo e usuários.

### OLTP vs OLAP

| Critério | OLTP (Transacional) | OLAP (Analítico) |
|---|---|---|
| **Objetivo** | Operações diárias (vendas, ERP) | Análise e tomada de decisão |
| **Processamento** | Transações rápidas, leitura/escrita de poucos dados | Consultas complexas, grandes volumes |
| **Armazenamento** | Orientado a linha (row-oriented) | Orientado a coluna (column-oriented) |
| **Estrutura** | Altamente normalizada | Desnormalizada (fato + dimensão) |
| **Consultas** | Simples e frequentes | Complexas e intensivas (leitura) |
| **Conteúdo** | Dados operacionais atuais | Dados históricos consolidados (várias fontes) |
| **Usuários** | Colaboradores operacionais | Analistas, gerentes, executivos |

### Particionamento de tabelas

Técnica de "quebrar" o armazenamento de colunas em partes menores para otimizar consultas. O particionamento mais comum é por **data** (dia, mês, ano).

**Cardinalidade** = número de elementos distintos em um conjunto de dados. Relações podem ser 1:1, 1:N ou N:N.

> **Por que não particionar por coluna de alta cardinalidade?** (1) O banco precisaria consultar muitas partições para retornar agregações; (2) colunas como ID raramente são usadas em filtros/agrupamentos explícitos.

---

## 2. Conceitos de ETL

**ETL** = Extração → Transformação → Carga (nessa ordem tradicional).

| Etapa | O que faz |
|---|---|
| **Extração** | Coleta dados de diversas fontes (bancos, CSVs, APIs) |
| **Transformação** | Limpeza, estruturação, enriquecimento dos dados |
| **Carga (Load)** | Carrega dados transformados no DW/BI |

### ETL vs ELT

Na abordagem moderna (**ELT**), a ordem muda: extrai → carrega dados brutos no DW → transforma dentro do próprio DW usando SQL (dbt, dataform).

**Vantagens do ELT moderno:**
- **Modularidade**: ferramentas 3rd-party para integração (Fivetran, Airbyte)
- **Simplicidade**: transformação centralizada em SQL (não Java/Python/Scala)
- **Governança**: ambiente único para documentação e permissionamento
- **Versionamento**: dbt separa modelos SQL do banco → controle de versão
- **Separação de ambientes**: schemas distintos (sources → staging → marts)
- **Testes**: analista escreve testes em SQL diretamente nos modelos

---

## 3. Data Warehouse vs Data Lake vs Data Lakehouse

| Aspecto | Data Warehouse | Data Lake | Data Lakehouse |
|---|---|---|---|
| **Dados** | Estruturados | Estruturados, semi, não estruturados | Todos os tipos (unificado) |
| **Qualidade** | Alta (fonte de verdade) | Baixa (risco de "data swamp") | Alta (governança + ACID) |
| **Esquema** | Star/Snowflake (fato + dimensão) | Schema-on-read | Unificado (melhor dos dois) |
| **Uso principal** | BI e análise relatórios | Big Data, ML, streaming | BI + ML + streaming |
| **Custo** | Mais alto | Baixo (armazenamento bruto) | Unificado (reduz infra) |

**Componentes do DW:** fontes de dados, camada ELT, camada de armazenamento, camada de metadados, camada de apresentação.

**Data Lakehouse:** une flexibilidade do DL com robustez do DW. Usa transações **ACID** (Atomicidade, Consistência, Isolamento, Durabilidade), indexação, caching e otimização de consultas.

---

## 4. Modelagem de dados

Processo de representar e organizar informações por meio de modelos conceituais, lógicos e físicos.

| Nível | O que faz | Detalhes |
|---|---|---|
| **Conceitual** | Identifica entidades e relacionamentos | DER, sem detalhe de colunas |
| **Lógico** | Traduz para esquema relacional | Define PK, FK, colunas, relacionamentos |
| **Física** | Implementação técnica | Tipos de dados, índices, restrições (DDL) |

**Benefícios:** clareza/consistência, eficiência de armazenamento, flexibilidade, qualidade dos dados.

### Esquemas dimensionais (Kimball)

- **Star Schema**: tabela fato central + tabelas dimensão ao redor (desnormalizado, poucos joins)
- **Snowflake Schema**: dimensões normalizadas em subdimensões (menos redundância, mais joins)
- **Constelação**: múltiplos esquemas estrela conectados

> O **Star Schema** é o formato recomendado para Power BI.

### Kimball vs Inmon (estratégias de DW)

| | Kimball (bottom-up) | Inmon (top-down) |
|---|---|---|
| **Abordagem** | Constrói data marts por processo de negócio, um de cada vez | Constrói o DW corporativo normalizado (3NF) primeiro; marts derivam depois |
| **Modelo** | Dimensional (star/snowflake) já no mart | Relacional normalizado como "fonte única da verdade" |
| **Velocidade** | Entrega valor cedo, em ciclos rápidos | Mais demorado (custo inicial alto) |
| **Foco** | Pragmático, voltado ao negócio/analistas | Enterprise, centralizado, padrão corporativo |

> A proposta de Kimball é a mais conhecida e é a que o banvic-dbt segue: staging (normalizado) → intermediate → marts (star schema por processo).

---

## 5. Tabelas Fato

Armazenam **métricas/medidas numéricas** de negócio (vendas, transações, valores). Cada linha = um evento.

**Características:**
- Medidas numéricas agregáveis (soma, média, contagem)
- **Chaves estrangeiras** → conectam às dimensões
- **Granularidade**: nível de detalhe (transação individual, diária, mensal)

> **Dados atômicos** = dados no **menor nível de detalhe possível** (cada transação individual). Não é "dado pequeno" — é **granularidade mínima**. Regra Kimball: *"go as granular as possible"* — os resumos derivam do fato atômico; se nascer agregado, o detalhe se perde para sempre. ⚠️ "Atômico" tem **dois sentidos** no módulo: (1) aqui, granularidade da fato; (2) na 1ª Forma Normal, atributo indivisível.

**Tipos:**

| Tipo | Descrição |
|---|---|
| **Transacional** | Cada linha = uma transação individual (alta granularidade) |
| **Agregada** | Dados pré-calculados em nível superior (ex: vendas/mês) para performance |

---

## 6. Tabelas Dimensão

Fornecem **contexto descritivo** dos fatos (quem, quando, onde, por quê, como). Usadas para filtrar, agrupar, classificar.

**Características:**
- **Chave única** (PK) — cada linha da fato liga a UMA dimensão
- **Atributos** descritivos (nome, categoria, status, região)
- **Hierarquias** (ano → trimestre → mês → dia)

### Surrogate Key

Chave artificial (não é o ID da origem) que garante unicidade mesmo quando há múltiplas fontes ou histórico de mudanças. Essencial para SCD.

### Slowly Changing Dimension (SCD)

Técnica para gerenciar mudanças em dimensões ao longo do tempo:

| Tipo | O que faz | Histórico? |
|---|---|---|
| **SCD1** | Substitui registro anterior pelo novo | Não mantém |
| **SCD2** | Cria nova linha a cada mudança, com período de validade | Mantém completo |

### Dimensão degenerada

Dimensão muito simples (poucos atributos, ex: status de transação) que é integrada diretamente na **tabela fato** para simplificar o modelo.

---

## 7. Tabelas Ponte (Bridge Table)

Tabela auxiliar para resolver relacionamentos **muitos-para-muitos** entre fato e dimensão.

**Quando usar:**
- Relacionamento N:N entre tabelas
- Conectar tabelas com granularidades diferentes
- Muitas combinações possíveis entre dados

**Pré-requisito:** cada tabela ligada pela bridge deve ter chave primária (ou surrogate key).

**Função:** tabela de "de-para" com apenas chaves primárias — não possui valor de negócio próprio.

**Benefícios:** simplicidade nos joins, escalabilidade, flexibilidade.
**Atenção:** aumenta número de joins (performance), exige manutenção cuidadosa.

---

## 8. Boas práticas no Databricks (Lakehouse)

O Databricks usa **Delta Lake** (armazenamento aberto com transações ACID) e **Unity Catalog** (governança centralizada).

| Prática | Descrição |
|---|---|
| **RBAC** | Role-Based Access Control via Unity Catalog (permissões granulares) |
| **Criptografia** | Em trânsito e em repouso + políticas de linhagem/auditoria |
| **Optimize** | Compacta arquivos Parquet (16MB–1GB) |
| **Z-Ordering** | Organiza dados por colunas frequentes em filtros |
| **Auto-optimize** | Compactação automática (128MB por padrão) |
| **Particionamento** | Por baixa cardinalidade ou colunas de filtro frequente |
| **Delta Cache** | Cópia local dos dados para leitura rápida |
| **CBO** | Cost-based optimizer usa estatísticas para planejar joins |
| **Serverless** | SQL Warehouse com autoescalonamento (paga só o que usa) |
| **Auto-termination** | Suspende clusters ociosos para economizar |
| **Query Profile / Spark UI** | Monitora gargalos (shuffle, memória, paralelismo) |

---

## Pontos de reforço pessoal (onde houve mais dúvida no quiz)

- **Armazenamento linha vs coluna:** OLTP = linha (transação completa junta); OLAP = coluna (cada coluna independente, ideal para agregações)
- **ETL vs ELT:** a diferença é a ORDEM — ETL transforma ANTES de carregar; ELT carrega bruto e transforma DENTRO do DW com SQL
- **Star vs Snowflake:** Star = desnormalizado (menos joins, recomendado para BI); Snowflake = dimensões normalizadas (menos redundância, mais complexo)
- **Fato vs Dimensão:** Fato = o QUE aconteceu (métrica numérica); Dimensão = COMO/QUANDO/ONDE aconteceu (contexto descritivo)
- **SCD1 vs SCD2:** SCD1 sobrescreve (sem histórico); SCD2 cria nova linha (mantém histórico com datas de validade)
- **Surrogate Key vs PK da origem:** surrogate key é artificial e resolve problemas de rastreamento quando há mudanças (SCD) ou múltiplas fontes
- **Dimensão degenerada:** dimensão tão simples que vale mais a pena colocar na tabela fato do que criar tabela separada
- **Particionamento:** NÃO usar coluna de alta cardinalidade (como ID); preferir datas ou colunas de baixa cardinalidade usadas em filtros

---

## Conexões com o Desafio Final (dbt + Power BI)

- O template banvic-dbt já segue a arquitetura Kimball: **staging** (normalizada) → **intermediate** → **marts** (star schema)
- As seeds (CSVs brutos) equivalem às **fontes de dados** do DW — você modela elas em `stg_*` models
- No dbt, cada model SQL transforma dados (camada **ELT**: bruto → staging → marts) — a transformação acontece DENTRO do Databricks
- Os **marts** devem ser `table` (não `view`) e seguir star schema para consumo no Power BI
- No Power BI, o star schema com fato central + dimensões ao redor é o formato recomendado pela própria Microsoft
- As tabelas dimensão do desafio (clientes, agências, colaboradores, datas) precisam de **surrogate keys** para garantir análise histórica correta
- Boas práticas do Databricks (Optimize, Z-Ordering, particionamento) impactam a performance do dashboard final
