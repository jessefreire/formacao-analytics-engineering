# Resumo — Módulo IV: Engenharia de Dados com dbt e Snowflake

## 1. ETL: O Precursor

**ETL (Extract, Transform, Load)** é o processo tradicional de mover dados entre sistemas. Cada letra representa uma etapa:

| Etapa | Descrição |
|---|---|
| **Extract** | Recuperar dados brutos de uma ou mais fontes e salvá-los em repositório único |
| **Transform** | Estruturar, enriquecer, limpar e converter dados brutos para modelo final |
| **Load** | Carregar dados transformados no Data Warehouse para consumo em BI |

A ordem ETL implica que a transformação ocorre **antes** do carregamento no DW — geralmente em servidor intermediário (staging).

## 2. ELT: A Abordagem Moderna

No **Modern Data Stack (MDS)**, a ordem inverte para **Extract-Load-Transform**:

- Extração + Load simultâneos (ferramentas SaaS movem dados brutos direto para o DW)
- Transformação ocorre **dentro do próprio Data Warehouse** via SQL ou ferramentas visuais
- Vantagem: dados brutos ficam preservados, transformação é mais flexível e aproveita poder computacional do DW

## 3. O Processo de ELT (visão completa)

O processo vai além de apenas extrair e transformar — engloba toda infraestrutura moderna de analytics:

### 3.1 Planejamento

**Entendimento do Problema:**
- Background da empresa, objetivos estratégicos, expectativas
- KPIs principais, "donos" dos indicadores (stakeholders)
- Valores de referência para validação
- Fluxo de decisão: quem usa, quando, para quê

**Mapeamento de Dados:**
- ERD (diagramas), planilhas, documentos
- Mapear disponibilidade e localização dos dados
- Formato físico ≠ formato de acesso (interface vs. armazenamento)

**Modelo Conceitual do DW:**
- Desenhar tabelas Fato e Dimensão
- Atenção à conformidade entre dimensões

### 3.2 Ingestão de Dados

Acessar dados nas fontes transacionais e enviar para camada bruta do DW. Formatos de conexão variam:

| Variável | Opções |
|---|---|
| SGBD | PostgreSQL, MySQL, Oracle, SQL Server |
| Tipo | Relacional, NoSQL |
| Servidor | Desktop, Local, Cloud |
| Conexão | JDBC, ODBC, API REST, Dump |
| Acesso | Somente leitura, Admin, tabelas específicas |

### 3.3 Tipos de Ingestão

| Tipo | Quando usar | Risco |
|---|---|---|
| **Full-load** | Consistência total, volumes menores | Inviável se fonte lenta ou janela curta |
| **Incremental** | Alta frequência, grandes volumes | Dados mutáveis podem gerar inconsistência |

**CDC (Change Data Capture):** técnica que usa logs de transação do banco para capturar INSERT/UPDATE/DELETE — forma mais segura de ingestão incremental.

> **Problema comum:** bancos transacionais são mutáveis. Carga incremental por data pode perder registros cancelados/atualizados retroativamente. Solução: coluna `data_atualização` ou CDC via logs.

### 3.4 Transformação

Etapa central do ELT — onde reside o maior esforço e valor. Principais tarefas:

- Selecionar campos relevantes
- Filtrar dados incorretos/incompletos
- Desduplicar registros
- Separar colunas (parsing)
- Juntar fontes/tabelas (JOINs)
- Renomear colunas
- Criar métricas calculadas
- Ordenar dados
- Modelar fatos e dimensões
- Criar chaves surrogate
- Pivotar/transpor tabelas

### 3.5 Entrega Final (Deploy)

Seguindo boas práticas de engenharia de software: testes, documentação, versionamento antes de disponibilizar em produção.

## 4. Alternativas de Arquitetura ETL/ELT

| Abordagem | Prós | Contras |
|---|---|---|
| **Código personalizado** (Python/Spark) | Máxima flexibilidade | Alta complexidade, dívida técnica, distanciamento do negócio |
| **ETL Visual** (Pentaho, Informática) | Curva de aprendizado baixa | Lock-in, escalabilidade limitada, pouca governança, custo de licença |
| **ELT Moderno** (DW + dbt) | SQL padrão, menor necessidade técnica, foco no negócio | Limitado a dados estruturados; pipelines muito complexos podem ser difíceis |

## 5. Transformação com dbt

**dbt (data build tool)** é a principal ferramenta de transformação no Modern Data Stack.

### 5.1 Estrutura do Projeto

```
├── dbt_project.yml        # Configuração geral do projeto
├── models/                # Modelos SQL (.sql)
├── seeds/                 # Dados estáticos (CSVs)
├── macros/                # Funções Jinja reutilizáveis
├── tests/                 # Testes singulares (.sql)
├── snapshots/             # Capturas temporais
├── analyses/              # Queries avulsas
└── target/                # Arquivos compilados
```

### 5.2 Conexão com o DW

- Arquivo `profiles.yml` em `~/.dbt/profiles.yml` (fora do repo por segurança)
- Targets: `dev` (desenvolvimento) e `prod` (produção)
- Verificação: `dbt debug`

### 5.3 Fontes de Dados (Sources)

Definidas em `sources.yml` no diretório staging. Sintaxe:
```sql
SELECT * FROM {{ source('nome_fonte', 'nome_tabela') }}
```

Cada source deve ser referenciada por apenas um modelo (consistência).

### 5.4 Modelos dbt

Cada modelo é um arquivo `.sql` que se torna objeto no DW. Duas interfaces principais:

| Função | Uso |
|---|---|
| `{{ source('fonte', 'tabela') }}` | Referência a dado bruto do DW (não depende de outros modelos) |
| {{ ref('modelo') }}` | Referência a outro modelo dbt (dependência automática) |

**Sequência de construção:**
1. Mapear tabelas no `sources.yml`
2. Criar modelos `stg_*` (staging: limpeza simples — renomear, tipar, criar colunas)
3. Criar dimensões com chaves surrogate (`dim_*`)
4. Criar tabelas fato (`fct_*`)

### 5.5 Chaves Surrogate

Geradas via `ROW_NUMBER()` a partir da chave natural. **Cuidado:** em DW modernos, auto-incremento pode ser perigoso se diferentes execuções gerarem ordens diferentes — prefira chaves determinísticas.

### 5.6 Materialização

| Tipo | Descrição |
|---|---|
| **view** | Query executada a cada consulta (mais lento para BI, rápido no dev) |
| **table** | Resultado persistido (melhor performance para BI) |
| **ephemeral** | CTE temporária — existe só durante a execução do pipeline |

Configuração: no `dbt_project.yml` (preferencialmente) ou por modelo com `{{ config(materialized='table') }}`. Configuração no modelo sobrescreve a do projeto.

### 5.7 Testes no dbt

**Testes genéricos (schema tests):** definidos em `.yaml`, executam validações padrão:
- `unique` — sem valores duplicados
- `not_null` — sem nulos
- `accepted_values` — valores dentro de lista pré-definida
- `relationships` — integridade referencial entre modelos

**Testes singulares (data tests):** queries SQL que devem retornar **0 linhas** para passar. Úteis para validar métricas com o cliente.

> **Boa prática:** escrever testes **antes** dos modelos (TDD). Incluir pelo menos `unique` + `not_null` na PK de cada modelo.

### 5.8 Documentação e Linhagem

- Descrições em arquivos `.yml` (tabelas + colunas)
- `dbt docs generate` — gera documentação HTML navegável
- `dbt docs serve` — visualização local com árvore de dependências (linhagem)

### 5.9 Orquestração

- **dbt Core (open-source):** sem orquestrador nativo — usar Airflow, Prefect, ou cron
- **dbt Cloud:** possui orquestrador incorporado

---

## Pontos de reforço pessoal (onde há mais dúvida)

- **ETL vs ELT:** ETL transforma ANTES de carregar; ELT carrega bruto e transforma DENTRO do DW
- **Source vs Ref:** `source()` = dado bruto do DW (sem dependência); `ref()` = outro modelo dbt (cria dependência/linhagem)
- **Full vs Incremental:** incremental com dados mutáveis pode gerar inconsistência — precisa de CDC ou coluna de atualização
- **Chave surrogate:** cuidado com `ROW_NUMBER()` não determinístico — ordem pode mudar entre execuções
- **Materialização:** configuração no modelo sobrescreve a do projeto; prefira configurar no `dbt_project.yml`
- **Testes singulares:** sucesso = 0 linhas retornadas (escreva a query para "dar errado")
- **Grão da tabela fato:** juntar orders + order_details muda o grão para nível de item (pedido deixa de ser único)
- **profiles.yml:** fica FORA do repo (`~/.dbt/`) — nunca commitar credenciais

---

## Conexões com o Desafio Final (dbt + Power BI)

- O **dbt** é a ferramenta de transformação do desafio: você vai construir o DW da BanVic usando a mesma estrutura (staging → intermediate → marts)
- **Airbyte** (ingestão) + **dbt** (transformação) + **Power BI** (visualização) = pipeline completo do MDS aplicado ao desafio
- Os modelos `stg_*`, `dim_*`, `fct_*` seguem exatamente o padrão ensinado no módulo
- Testes genéricos (`unique`, `not_null`, `relationships`) garantem integridade dos dados antes do Power BI consumir
- `dbt docs generate` serve como documentação técnica do projeto entregue
- O grão da tabela fato determina como você agrega métricas no Power BI — planeje com cuidado
