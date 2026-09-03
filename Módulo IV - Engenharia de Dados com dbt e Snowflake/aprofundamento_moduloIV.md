# Aprofundamento — Módulo IV: Ingestão, Transformação e Camadas de Dados

> Complemento ao `resumo_moduloIV.md`. Detalha os conceitos que a aula cita sem explicar: tipos de processamento (slide "Types of processing"), processos de transformação, campo vs métrica, e a nomenclatura de camadas de dados (bronze/silver/gold).

---

## 1. Tipos de Processamento (Ingestão) — o slide "Types of processing"

### 1.1 Full Load (Full-Refresh)

Carrega **todos os dados da fonte a cada execução**.

- Dia 1: 3 pedidos processados → Dia 2: 5 pedidos (reprocessa tudo)
- ✅ **Mais seguro** — sempre consistente com a fonte
- ❌ **Pesado** (computacionalmente intensivo); rodar de madrugada quando o banco está ocioso
- ❌ Inviável se precisar de atualização frequente (se uma carga leva 1–2h, não dá pra rodar de hora em hora)

### 1.2 Incremental Load

Carrega **somente os registros novos** desde a última execução, usando uma coluna índice (Data ou ID).

- Dia 1: 3 pedidos → Dia 2: só 2 novos (pedidos 4 e 5)
- ✅ Rápido, permite alta frequência
- ❌ **Problema central:** bancos transacionais são **mutáveis** (UPDATE retroativos)
  - Ex.: pedido 2 muda de *Pendente* → *Cancelado* no dia 11. A carga incremental por **data de criação** não pega essa mudança → **superestima vendas** se você não considerar cancelados

### 1.3 Incremental + Overwrite

Evolução do incremental: além dos registros novos, **sobrescreve** os que mudaram (via `data_atualização` ou CDC).

- Dia 2 processa 3 linhas: os novos (4, 5) **+ o pedido 2 atualizado** (sobrescrito)
- Resolve o problema do UPDATE retroativo

### 1.4 CDC (Change Data Capture)

Forma mais segura de processamento incremental. Duas abordagens:

| Abordagem | Como funciona |
|---|---|
| **Coluna `data_atualização`** | Novo índice que captura mudanças, não só criação |
| **Logs de transação** | Usa os logs do banco (INSERT/UPDATE/DELETE) — mais seguro, porém **não é simples de implementar** |

> **PEGADINHA:** bancos transacionais são mutáveis. Carga incremental por data de criação pode **perder** registros cancelados/atualizados retroativamente. Solução: coluna `data_atualizacao` ou CDC via logs.

---

## 2. Slide "Summarizing" — os conceitos citados sem explicação

| Conceito | O que é | Detalhes |
|---|---|---|
| **Tipo de fonte** | Onde o dado está armazenado | SQL, NoSQL, API, texto/arquivos (CSV, JSON, Parquet) |
| **Tipo de acesso** | Como você entra na fonte | Espelho do banco (mirror/replica read-only), API, relatório/exportação |
| **Ambiente** | Onde fonte e destino estão | Cloud, on-premises, híbrido |
| **Frequência** | De quanto em quanto tempo roda | Weekly, daily, hourly, minute-by-minute, near real-time, real-time |
| **Volume por execução** | Quanto dado passa em cada rodada | Define full vs incremental; afeta janela e custo |
| **Tipo de processamento** | De que forma carrega | Full, incremental, incremental + overwrite |

> **Frequência (decoreba):** quanto maior a frequência, maior custo e complexidade. **Não adote** alta frequência se não for estritamente necessário — o curso reforça isso.
>
> **Volume:** se uma carga leva 1–2h, a frequência mínima viável é maior que esse período.

---

## 3. Processos de Transformação — os 12 itens detalhados

> Ideia central: toda limpeza/processamento deve ser **centralizada numa camada só** (dbt) para garantir uma **visão única dos dados** em toda a organização — ninguém faz regra de negócio "do seu jeito" num Excel.

### 3.1 Selecionar os campos relevantes de negócio
Pegar **só as colunas que importam**, descartando o resto. Menos colunas = tabela menor, mais rápida e menos confusa pro BI.

```sql
SELECT cod_cliente, nome, cidade FROM stg_clientes;
```

### 3.2 Filtrar dados incorretos ou incompletos
Eliminar linhas com dados inválidos (nulos críticos, datas futuras, IDs vazios, valores fora do domínio).

```sql
SELECT * FROM stg_pedidos
WHERE valor_total > 0
  AND data_pedido <= CURRENT_DATE;
```

> Cuidado: filtrar demais pode **esconder problemas** — registre o que você remove (auditoria) e valide com testes.

### 3.3 Desduplicar dados
Remover **linhas duplicadas**. Técnicas: `DISTINCT`, `ROW_NUMBER()` por chave + filtrar `rn = 1`, ou `QUALIFY`.

```sql
SELECT * FROM (
  SELECT t.*,
         ROW_NUMBER() OVER (PARTITION BY cod_pedido ORDER BY data_atualizacao DESC) AS rn
  FROM stg_pedidos t
) WHERE rn = 1;
```

### 3.4 Separar colunas em mais colunas (parsing)
Quebrar uma coluna composta em várias. Ex.: `endereco = "Rua X, 123, Centro"` → rua, número, bairro.

```sql
SELECT SPLIT_PART(endereco, ',', 1) AS rua,
       SPLIT_PART(endereco, ',', 2) AS numero
FROM stg_clientes;
```

### 3.5 Juntar dados de fontes/tabelas distintas (JOIN)
Combinar tabelas com `JOIN` para enriquecer. É aqui que nasce o valor analítico.

**Os tipos (o que muda é o que acontece com linhas sem correspondência):**

| JOIN | O que retorna |
|---|---|
| **INNER** | Só linhas com correspondência nos dois lados |
| **LEFT** | Todas da esquerda + correspondências da direita (nulo onde não bate) |
| **RIGHT** | Todas da direita + correspondências da esquerda |
| **FULL OUTER** | Todas dos dois lados, juntando onde bate |

```sql
SELECT p.cod_pedido, c.cidade, a.nome_agencia
FROM stg_pedidos p
JOIN stg_clientes c ON p.cod_cliente = c.cod_cliente
JOIN stg_agencias a ON p.cod_agencia = a.cod_agencia;
```

> **⚠️ O perigo do grão:** juntar `pedidos` com `itens_pedido` (1 pedido → N itens) **explode as linhas**: cada linha da fato vira 1 item. Somar `valor_total` do pedido aí **soma repetido**. É a pegadinha do grão.

### 3.6 Renomear colunas
Padronizar nomes para `snake_case` e nomes legíveis/consistentes.

```sql
SELECT customer_id AS cod_cliente FROM stg_customers;
```

### 3.7 Criar novos campos e métricas calculadas
Derivar colunas novas a partir das existentes.

**Campo calculado (por LINHA):** aritmética/lógica por registro, sem agregação → nova **coluna**, mesma quantidade de linhas.

```sql
SELECT cod_pedido,
       valor_total,
       valor_total * 1.08           AS valor_com_imposto,     -- campo calculado
       DATEDIFF(day, data_pedido, data_entrega) AS dias_entrega, -- campo calculado
       CASE WHEN valor_total > 1000 THEN 'Alto' ELSE 'Baixo' END AS faixa
FROM stg_pedidos;
```

**Métrica calculada (por GRUPO):** agregação (SUM, COUNT, AVG) → **linha resumida por grupo**.

```sql
SELECT cidade,
       COUNT(*)         AS total_pedidos,   -- métrica
       SUM(valor_total) AS receita          -- métrica
FROM stg_pedidos
GROUP BY cidade;
```

### 3.8 Ordenar dados
`ORDER BY` por um ou mais campos — geralmente útil em marts finais.

```sql
SELECT * FROM dim_cliente ORDER BY uf, cidade;
```

### 3.9 Remodelar para modelo de fatos e dimensões
Sair das tabelas transacionais (normalizadas) e montar o **esquema dimensional** — tabelas **fato** (medidas, eventos) + **dimensão** (descrições). Liga ao **Módulo 3** (star schema).

### 3.10 Criar chaves surrogate
Gerar chave **artificial única** (SK) a partir da chave natural, pra juntar fato ↔ dimensão e suportar histórico (SCD).

```sql
SELECT ROW_NUMBER() OVER (ORDER BY cod_cliente) AS cliente_sk, ...
```

> **⚠️ Pegadinha:** `ROW_NUMBER()` pode ser não-determinístico entre execuções. Prefira chaves **determinísticas** (ex.: hash da chave natural).

### 3.11 Transpor ou pivotar tabelas
**Rotacionar** a tabela: linhas em colunas (pivot) ou colunas em linhas (unpivot). Ex.: 12 colunas de mês → 1 coluna `mês` + 1 `valor`.

```sql
SELECT cliente,
       SUM(CASE WHEN status='Finalizado' THEN valor ELSE 0 END) AS finalizado,
       SUM(CASE WHEN status='Cancelado'  THEN valor ELSE 0 END) AS cancelado
FROM stg_pedidos GROUP BY cliente;
```

### 3.12 Agregar ou desagregar tabelas *(está só nos slides EN)*
- **Agregar** = resumir (SUM/COUNT/AVG por grupo) — ex.: vendas por dia/cidade
- **Desagregar** = quebrar uma linha em várias (explodir lista; unpivot) — ex.: 1 pedido com 3 itens vira 3 linhas

> **⚠️ Cuidado com o grão:** agregar muda o grão. Se você agrega por dia e depois tenta calcular por pedido, os números não fecham.

---

## 10. Anatomia de um model dbt — por que SEMPRE termina com SELECT

### 10.1 O contrato do dbt

Um model dbt é um arquivo `.sql` que **só pode conter um `SELECT`**. Nenhum `CREATE TABLE`, nenhum `INSERT`, nenhum `DROP`.

O dbt pega esse SELECT e "embrulha" na materialização correspondente:

```
Você escreve:                          dbt gera e executa no banco:
──────────────                         ────────────────────────────
WITH limpo AS (                        CREATE OR REPLACE VIEW dev.staging.stg_clientes AS (
  SELECT *                              (
  FROM {{ source(...) }}                  WITH limpo AS (
)                                         SELECT * FROM dev.erp_banvic.clientes
SELECT * FROM limpo                     )
                                      )
```

**O banco cria a tabela/view de verdade.** Você nunca vê esse `CREATE` — o dbt faz por você.

### 10.2 Por que isso importa

| Aspecto | Explicação |
|---|---|
| **Separação de responsabilidade** | Você cuida do *o quê* (lógica do SELECT); dbt cuida do *como* (materializar como view/table/incremental) |
| **Reprodutibilidade** | `dbt run` sempre dropa e recria (ou atualiza) — sem estado acumulado, sem surpresa |
| **Testabilidade** | O mesmo SELECT que cria a tabela também pode ser testado (schema tests, data tests) |
| **Versionamento** | O SQL no git = a definição exata da tabela — se alguém perguntar "de onde vem esse dado?", é só abrir o arquivo |

### 10.3 Parts de um model (exemplo real)

```sql
-- models/staging/stg_clientes.sql

{{ config(materialized='view') }}          -- 1. Config (opcional)

with source as (                           -- 2. CTE: lógica intermediária
    select * from {{ source('erp_banvic', 'clientes') }}
),

renamed as (                               -- 3. CTE: transformação
    select
        cod_cliente,
        nome_completo,
        data_nascimento,
        cpf
    from source
)

select * from renamed                      -- 4. SELECT final (OBRIGATÓRIO)
```

| Parte | Função | Obrigatório? |
|---|---|---|
| `{{ config(...) }}` | Configura materialização (`view`, `table`, `incremental`, `ephemeral`) | ❌ (default = `view` em staging/intermediate) |
| CTEs (`with ... as`) | Blocos lógicos intermediários — **não existem no banco**, são organização do código | ❌ (mas padrão de mercado — sempre usar) |
| `{{ source(...) }}` | Referência a uma tabela raw (seed ou fonte externa) | ❌ (usa-se em staging; em marts usa `ref()`) |
| `select * from renamed` | **Resultado final** — dbt materializa a partir desse SELECT | ✅ **Obrigatório** |

### 10.4 Materializações

A config define **como** o banco armazena o resultado:

| Materialização | O que dbt gera | Quando usar |
|---|---|---|
| **`view`** | `CREATE OR REPLACE VIEW` | Staging/intermediate — dados temporários, rápidos de refazer |
| **`table`** | `CREATE OR REPLACE TABLE` | Marts — dados finais pro BI, performance |
| **`incremental`** | `INSERT INTO ... SELECT` (só novos/atualizados) | Tabelas grandes onde reprocessar tudo é caro |
| **`ephemeral`** | CTE embutida no model que referencia | Models auxiliares que não precisam existir como tabela |

### 10.5 `ref()` vs `source()` — a diferença crucial

```sql
-- source: acessa uma tabela RAW (seeds, fontes externas)
{{ source('erp_banvic', 'clientes') }}
  → dev.erp_banvic.clientes

-- ref: acessa outro MODEL dbt (staging, intermediate, marts)
{{ ref('stg_clientes') }}
  → dev.staging.stg_clientes
```

| | `source()` | `ref()` |
|---|---|---|
| **Acessa** | Seeds / fontes externas | Outros models dbt |
| **Schema** | Fixo (o que você definiu em `sources.yml`) | Dinâmico (dbt resolve conforme o target) |
| **DAG** | Não cria dependência no grafo | **Cria dependência** — dbt sabe que precisa rodar `stg_clientes` antes de `fact_transacoes` |
| **Testes** | Pode testar a existência da tabela | Pode testar a existência + schema do model |

### 10.6 Pegadinhas de prova

1. **"Posso usar `CREATE TABLE` num model?"** → Não. O dbt compila seu `.sql` e espera um único SELECT. Se colocar DDL, dá erro de compilação.

2. **"Qual a diferença entre `table` e `incremental`?"** → `table` dropa e recria tudo a cada `dbt run`. `incremental` insere só linhas novas (mais rápido, mas requer lógica de filtro).

3. **"Posso pular as CTEs e fazer SELECT direto?"** → Tecnicamente sim, mas **não faça**. CTEs organizam, documentam e facilitam manutenção. Padrão de mercado é 1 CTE por transformação lógica.

4. **"O que acontece se meu SELECT não retornar linhas?"** → A tabela/view é criada vazia. O dbt não falha — só não tem dados.

5. **"View vs table: qual a diferença de performance?"** → View = query dinâmica (executa a cada consulta); table = dados materializados (mais rápida pra leitura, mas precisa refresh).

---

## 11. Macros no dbt — código reutilizável entre models

### 11.1 O que é uma macro

Uma **macro** é um pedaço de código **Jinja** reutilizável. Pense como uma "função": você define uma vez e chama de qualquer model, teste ou operação.

Tudo que está entre `{{ }}` é Jinja — e Jinja = macro.

### 11.2 Macros built-in (que você já usa sem saber)

```sql
{{ ref('stg_clientes') }}                  -- resolve referência + cria dependência no DAG
{{ source('erp_banvic', 'clientes') }}     -- acessa tabela raw (seed/fonte externa)
{{ config(materialized='view') }}          -- configura materialização
{{ is_incremental() }}                     -- verifica se roda em modo incremental
```

**O que `ref()` faz por baixo dos panos:**

```
Você escreve:               dbt resolve:                    Banco recebe:
─────────────              ──────────────                  ──────────────
{{ ref('stg_clientes') }}  → dev.staging.stg_clientes  →  SELECT * FROM dev.staging.stg_clientes
```

O `ref()` é a macro mais importante do dbt — ela faz **duas coisas**:
1. **Resolve o nome** da tabela (schema + nome do model)
2. **Cria a dependência** no DAG (dbt sabe que precisa rodar `stg_clientes` antes de quem o referencia)

### 11.3 Macros customizadas

Você cria em `macros/` e usa nos models:

**Arquivo:** `macros/utilidades.sql`

```sql
{% macro log_gap(coluna_data, tabela) %}
    -- Retorna linhas onde há buraco de mais de 1 dia na sequência de datas
    SELECT *
    FROM (
        SELECT *,
               LAG({{ coluna_data }}) OVER (ORDER BY {{ coluna_data }}) AS data_anterior,
               DATEDIFF(day, LAG({{ coluna_data }}) OVER (ORDER BY {{ coluna_data }}), {{ coluna_data }}) AS gap_dias
        FROM {{ tabela }}
    )
    WHERE gap_dias > 1
{% endmacro %}
```

**Uso num model:**

```sql
select * from {{ log_gap('data_pedido', ref('stg_pedidos')) }}
```

O dbt **expande a macro** antes de enviar pro banco — o banco nunca vê `{{ log_gap(...) }}`, vê o SQL completo.

### 11.4 Quando criar macros

| Situação | Solução |
|---|---|
| Mesmo pedaço de SQL em 3+ models | Vire uma macro |
| Lógica condicional complexa (`{% if %}`) | Macro encapsula a condição |
| Geração automática de colunas | Macro gera a lista de colunas |
| Padrão de naming que se repete | Macro padroniza |

> **Regra prática:** se você copiou e colou o mesmo SQL em mais de 3 models, isso é candidato a macro.

### 11.5 Macros vs models — a diferença

| | Model | Macro |
|---|---|---|
| **Arquivo** | `models/*.sql` | `macros/*.sql` |
| **Gera tabela/view?** | ✅ Sim — materializa no banco | ❌ Não — só expande Jinja |
| **Tem `ref()`?** | Sim | Sim |
| **DAG?** | Cria nó no grafo | **Não** cria nó (é expand inline) |
| **Uso** | Transformação principal | Função auxiliar reutilizável |

> **PEGADINHA:** macros **não criam tabelas** — elas são "copiadas e coladas" no model que as chama. É como um `#include` em C: o código é inline, não existe separadamente no banco.

### 11.6 Macros mais usadas no dbt

| Macro | O que faz |
|---|---|
| `{{ ref('model') }}` | Referencia outro model |
| `{{ source('schema', 'table') }}` | Referencia tabela raw |
| `{{ config(...) }}` | Configura materialização |
| `{{ is_incremental() }}` | Retorna `true` se rodando em modo incremental |
| `{{ run_query('SQL') }}` | Executa SQL arbitrário durante o compile time |
| `{{ exceptions.warn('msg') }}` | Emite warning durante o compile |
| `{{ adapter.dispatch(...) }}` | Lógica específica por adapter (Snowflake vs Databricks) |

**Resumo de prova:**
- **Macro** = código Jinja reutilizável (`{% macro nome(...) %} ... {% endmacro %}`)
- **`ref()` e `source()` são macros** built-in do dbt
- Macros **não criam tabelas** — são expand inline no model
- Criar macro customizada quando mesma lógica aparece em 3+ models

---

## 12. Comandos essenciais do dbt

### 12.1 Comandos de ciclo de vida (os mais usados)

| Comando | O que faz | Quando usar |
|---|---|---|
| **`dbt run`** | Roda todos (ou selecionados) models → cria/atualiza tabelas e views no banco | Sempre que alterar um model |
| **`dbt test`** | Roda todos (ou selecionados) testes → verifica integridade dos dados | Depois de `dbt run`, antes de commitar |
| **`dbt seed`** | Carrega CSVs do diretório `seeds/` como tabelas no banco | Na primeira vez ou quando os CSVs mudarem |
| **`dbt build`** | Executa **tudo junto** (seeds + models + testes) na ordem do DAG | Comando único pra rodar o pipeline inteiro |
| **`dbt clean`** | Remove pastas `target/` e `dbt_packages/` | Quando algo está "sujo" e precisa refazer do zero |
| **`dbt debug`** | Verifica se a conexão com o banco está funcionando | Antes de qualquer coisa; se der erro de conexão |

### 12.2 Comandos de seleção (filtrar o que roda)

```bash
dbt run --select staging           # só models da pasta staging/
dbt run --select stg_clientes     # só 1 model específico
dbt run --select +marts.fact_*    # esse model + todos os que ele depende
dbt run --exclude staging         # tudo EXCETO staging
dbt test --select stg_clientes    # testa só esse model
```

| Sintaxe | Significado |
|---|---|
| `--select <pattern>` | Roda só o que bate com o padrão |
| `--exclude <pattern>` | Roda tudo EXCETO o que bate |
| `-s` | Atalho pra `--select` |
| `+model` | Model + dependências **anteriores** (upstream) — todos os níveis |
| `model+` | Model + dependências **posteriores** (downstream) |
| `+model+` | Tudo que está antes E depois |
| `N+model` | Model + **N níveis** pra cima (ex: `1+dim_clientes` = intermediate + marts) |
| `N+` | Tudo com pelo menos N níveis de distância (ex: `2+` = staging pra baixo) |
| `tag:financeiro` | Seleciona por tag (definida no YAML) |
| `path:models/staging` | Seleciona por caminho |

**Exemplos práticos:**

```bash
dbt run -s 1+dim_clientes    # roda dim_clientes + intermediate (1 nível acima)
dbt run -s 2+dim_clientes    # roda staging + intermediate + marts (2 níveis acima)
dbt run -s dim_clientes+     # roda dim_clientes + tudo que depende dele (downstream)
dbt run -s 1+                # roda TUDO (todos os models com pelo menos 1 nível)
dbt run -s 0+dim_clientes    # só dim_clientes (0 níveis = só ele)
```

> **Dica prática:** `dbt run -s 1+dim_clientes` é o mais útil no dia a dia — você já rodou o staging e quer rerodar intermediate + marts sem refazer tudo.

### 12.3 Comandos de documentação

```bash
dbt docs generate    # gera documentação (site HTML) — requer models rodados
dbt docs serve       # abre o site da doc no navegador (porta 8000)
```

O `dbt docs` mostra:
- **Linha DAG** (grafinho de dependências entre models)
- **Colunas** de cada tabela (definidas no YAML)
- **Testes** aplicados a cada coluna
- **Descrições** dos models

### 12.4 Comandos utilitários

| Comando | O que faz |
|---|---|
| **`dbt parse`** | Valida sintaxe SQL e Jinja (sem rodar no banco) |
| **`dbt compile`** | Compila e mostra o SQL final que seria enviado ao banco (sem executar) |
| **`dbt run-operation <macro>`** | Roda uma macro customizada como comando |
| **`dbt snapshot`** | Roda snapshots (SCD Type 2) — muda linhas com `strategy: check` ou `timestamp` |
| **`dbt deps`** | Instala dependências (packages) definidas em `packages.yml` |

### 12.5 Ordem típica de execução

```
1. dbt debug          ← primeiro sempre: validar conexão
2. dbt seed           ← carregar CSVs brutos (uma vez, ou quando mudar)
3. dbt run            ← rodar models (staging → intermediate → marts)
4. dbt test           ← validar integridade
5. dbt docs generate  ← gerar documentação
6. dbt docs serve     ← visualizar no navegador
```

**Atalho:** `dbt build` faz tudo de uma vez (seeds + models + testes).

### 12.6 Flags úteis

| Flag | Efeito |
|---|---|
| `--full-refresh` | Dropa e recria tables/views (ignora incremental) |
| `--vars '{"chave": "valor"}'` | Passa variáveis pro Jinja |
| `--profiles-dir <caminho>` | Aponta pra outro diretório de profiles |
| `--target <ambiente>` | Roda num target diferente (dev/prod) |
| `--dry-run` | Mostra o que faria sem executar |
| `--threads <N>` | Número de threads paralelas (default: 4) |

### 12.7 Pegadinhas de prova

1. **"Qual a diferença entre `dbt run` e `dbt build`?"** → `dbt run` só roda models. `dbt build` roda seeds + models + testes, respeitando o DAG.

2. **"Posso rodar `dbt test` antes de `dbt run`?"** → Sim, mas os testes vão falhar se as tabelas não existirem ainda. Ordem correta: `run` → `test`.

3. **"O que `--full-refresh` faz em incremental?"** → Ignora a lógica incremental e recria a tabela do zero (como se fosse `table`). Útil quando a lógica do model mudou.

4. **"O que `dbt compile` faz?"** → Compila o SQL e mostra em `target/compiled/` sem executar no banco. Útil pra debugar o que o Jinja gerou.

5. **"Onde ficam os logs?"** → Em `logs/dbt.log`. Tudo que o dbt faz é logado lá.

---

## 13. Prático: criando o primeiro model de staging (Aula 20)

### 13.1 Passo 1 — Criar o `sources.yml`

**Arquivo:** `models/staging/_erp_banvic.yml` (o `_` impede que dbt tente compilar como model)

```yaml
version: 2

sources:
  - name: erp
    description: Esse é o sistema ERP da banvic com dados de clientes, colaboradores, contas e transações.
    schema: erp_banvic
    tables:
      - name: localidades
        description: Tabela fonte de localidades com informação de cidade e estado.

      - name: clientes
        description: Tabela fonte de clientes com informações pessoais de cada cliente da Banvic.

      - name: contas
        description: Tabela fonte de contas com informações de contas dos clientes.

      - name: agencias
        description: Tabela fonte de agências com informações de localização e tipo.

      - name: colaboradores
        description: Tabela fonte de colaboradores com informações pessoais e hierarquia.

      - name: colaborador_agencia
        description: Tabela de relação entre colaboradores e agências.

      - name: propostas_credito
        description: Tabela fonte de propostas de crédito com status e valores.

      - name: transacoes
        description: Tabela fonte de transações realizadas nas contas dos clientes.
```

**O que esse YAML faz:**
- Define a fonte `erp` com schema `erp_banvic` (= onde as seeds estão)
- Cada `source('erp', 'tabela')` nos models resolve pra `dev.erp_banvic.tabela`
- Lista as 8 tabelas disponíveis

### 13.2 Passo 2 — Criar o model `stg_localidades.sql`

**Arquivo:** `models/staging/stg_erp__localidades.sql`

```sql
with
fonte_localidades as (
    select *
    from {{ source('erp', 'localidades') }}
),

renomeado as (
    select
        cod_localidade as pk_localidade
        , cast(cidade as string) as cidade
        , cast(uf as string) as uf
    from fonte_localidades
)

select *
from renomeado
```

**O que esse model faz:**
- Puxa tudo da tabela `localidades` via `source('erp', 'localidades')`
- Renomeia `cod_localidade` → `pk_localidade` (chave primária)
- Converte `cidade` e `uf` pra string (garante tipo consistente)
- Materializa como **view** (default em staging)

### 13.3 Passo 3 — Rodar o model

```bash
dbt run --select stg_erp__localidades
```

| Comando | O que faz |
|---|---|
| `dbt run` | Roda o model → cria a view no Databricks |
| `--select stg_erp__localidades` | Roda SÓ esse model (não todos) |

**Resultado esperado:** `1 of 1 OK created view dev.staging.stg_erp__localidades`

### 13.4 Convenção de naming do curso

| Elemento | Padrão | Exemplo |
|---|---|---|
| **Arquivo do model** | `stg_<fonte>__<tabela>.sql` | `stg_erp__localidades.sql` |
| **Nome do model** (= nome da view/tabela) | `stg_<fonte>__<tabela>` | `stg_erp__localidades` |
| **Schema no banco** | `staging` | `dev.staging.stg_erp__localidades` |
| **Arquivo YAML** | `_erp_banvic.yml` (com `_` no início) | Ignorado como model |

> **Regra:** duplo `__` entre fonte e tabela. Isso separa visualmente: `stg_erp__clientes` = staging + fonte erp + tabela clientes.

### 13.5 Estrutura de pastas resultante

```
models/
└── staging/
    └── erp_banvic/
        ├── schema/
        │   ├── _erp_banvic.yml        ← sources (definição das fontes)
        │   ├── stg_erp__localidades.yml ← testes do model
        │   └── ...
        ├── stg_erp__localidades.sql    ← primeiro model de staging
        └── ...
```

### 13.6 Próximos models (mesmo padrão)

Repetir o padrão pras 7 tabelas restantes:

| Arquivo | Source | O que faz |
|---|---|---|
| `stg_erp__clientes.sql` | `source('erp', 'clientes')` | Limpa e tipa clientes |
| `stg_erp__contas.sql` | `source('erp', 'contas')` | Limpa e tipa contas |
| `stg_erp__agencias.sql` | `source('erp', 'agencias')` | Limpa e tipa agências |
| `stg_erp__colaboradores.sql` | `source('erp', 'colaboradores')` | Limpa e tipa colaboradores |
| `stg_erp__colaborador_agencia.sql` | `source('erp', 'colaborador_agencia')` | Limpa e tipa relação collab-agência |
| `stg_erp__propostas_credito.sql` | `source('erp', 'propostas_credito')` | Limpa e tipa propostas |
| `stg_erp__transacoes.sql` | `source('erp', 'transacoes')` | Limpa e tipa transações |

**Atalho:** `dbt run --select staging` roda todos os models de staging de uma vez.

### 13.7 Model `stg_erp__clientes.sql` (Aula 20)

**Arquivo:** `models/staging/stg_erp__clientes.sql`

```sql
with
fonte_clientes as (
    select *
    from {{ source('erp', 'clientes') }}
),

renomeado as (
    select
        cast(cod_cliente as int) as pk_cliente
        , cast(cod_localidade as int) as fk_localidade
        , primeiro_nome || ' ' || ultimo_nome as nome_cliente
        , email as email_cliente
        , tipo_cliente
        , cast(data_inclusao as timestamp) as ts_inclusao
        , regexp_replace(cpfcnpj, '[^a-zA-Z0-9]', '') as cpfcnpj_cliente
        , cast(data_nascimento as date) as data_nascimento_cliente
        , endereco as endereco_cliente
        , regexp_replace(cep, '[^a-zA-Z0-9]', '') as cep_cliente
    from fonte_clientes
)

select *
from renomeado
```

**Transformações aplicadas:**

| Linha | Transformação | Por quê |
|---|---|---|
| `cast(cod_cliente as int)` | Converte PK pra inteiro | Garante tipo numérico pra joins |
| `cast(cod_localidade as int)` | Converte FK pra inteiro | Mesmo motivo |
| `primeiro_nome \|\| ' ' \|\| ultimo_nome` | Concatena nome completo | `\|\|` = concatenação SQL padrão |
| `email as email_cliente` | Renomeia com sufixo `_cliente` | Padroniza nomes |
| `cast(data_inclusao as timestamp)` | Converte pra timestamp | Precisa de hora pra auditoria |
| `regexp_replace(cpfcnpj, '[^a-zA-Z0-9]', '')` | Remove pontuação do CPF/CNPJ | Mantém só letras e números |
| `cast(data_nascimento as date)` | Converte pra data | Tipo correto pra cálculos |
| `regexp_replace(cep, '[^a-zA-Z0-9]', '')` | Remove formatação do CEP | "01234-567" vira "01234567" |

**Comando pra rodar:**

```bash
dbt run --select stg_erp__clientes
```

**Nota:** o `regexp_replace` é específico do **Databricks/Spark SQL**. Em outros bancos:
- PostgreSQL: `regexp_replace(col, '[^a-zA-Z0-9]', '', 'g')`
- SQL Server: `REPLACE(REPLACE(REPLACE(...))` (não tem regex nativo fácil)

### 13.8 Dicas práticas do Studio (erros reais)

| Erro | Causa | Solução |
|---|---|---|
| **`UNRESOLVED_COLUMN`** | Nome da coluna no código ≠ nome real no banco | Conferir no Databricks Catalog; o erro lista as colunas disponíveis |
| **Mesmo erro depois de corrigir** | Esqueceu de **salvar** o arquivo antes de rodar | **Ctrl+S** (ou Cmd+S) antes de `dbt run` — o Studio não roda a versão mais recente se não salvar |
| **`Table not found`** | `source()` apontando pra schema/tabela errado | Conferir o `_erp_banvic.yml`: schema deve ser `erp_banvic` (onde as seeds estão) |
| **`Reference error`** | Model referenciado não existe ou名字 errado | Conferir o `ref('nome_exato')` — maiúsculas/minúsculas importam |

> **Regra de ouro no Studio:** sempre **salvar (Ctrl+S)** antes de rodar. O dbt Cloud não assume que você quer a versão mais recente — ele roda o que está salvo.

> **Erro que repete:** cuidado com **vírgula extra** entre CTEs. Vírgula vai **depois do `)`**, nunca **antes do nome** da próxima CTE:
>
> ```sql
> -- ❌ ERRADO
> ),
> 
> , proxima_CTE as (
> 
> -- ✅ CERTO
> ),
> 
> proxima_CTE as (
> ```

### 13.9 Model intermediate: `int_dimensao_clientes.sql`

**Arquivo:** `models/intermediate/int_dimensao_clientes.sql`

```sql
with
clientes as (
    select *
    from {{ ref('stg_erp__clientes') }}
),

, localidades as (
    select *
    from {{ ref('stg_erp__localidades') }}
),

, clientes_enriquecido as (
    select
        clientes.pk_cliente
        , clientes.nome_cliente
        , clientes.email_cliente
        , clientes.tipo_cliente
        , clientes.cpfcnpj_cliente
        , clientes.ts_inclusao
        , clientes.data_nascimento_cliente
        , clientes.endereco_cliente
        , clientes.cep_cliente
        , localidades.cidade as cidade_cliente
        , localidades.uf as uf_cliente
    from clientes
    left join localidades on clientes.fk_localidade = localidades.pk_localidade
)

select *
from clientes_enriquecido
```

**Comando:**

```bash
dbt run --select int_dimensao_clientes
```

**O que esse model faz:**

| Parte | Função |
|---|---|
| CTE `clientes` | Puxa staging de clientes via `ref()` |
| CTE `localidades` | Puxa staging de localidades via `ref()` |
| CTE `clientes_enriquecido` | **Junta** as duas com `LEFT JOIN` |
| `left join ... on fk_localidade = pk_localidade` | Ligação: cliente → localidade |
| Sufixo `_cliente` nas colunas de localidade | Evita conflito de nomes |

**Diferença intermediate vs staging:**

| | Staging | Intermediate |
|---|---|---|
| **Referência** | `source()` (dados brutos) | `ref()` (outros models) |
| **Operação** | Limpeza, rename, cast | **Joins**, enriquecimento |
| **Grão** | 1 tabela = 1 fonte | 1 tabela = várias fontes juntas |
| **Materialização** | `view` (default) | `view` (default) |

### 13.10 Model marts: `dim_clientes.sql`

**Arquivo:** `models/marts/dim_clientes.sql`

```sql
with
clientes as (
    select *
    from {{ ref('int_dimensao_clientes') }}
)

select *
from clientes
```

**Comando:**

```bash
dbt run --select dim_clientes
```

**O que esse model faz:** puxa tudo do intermediate e materializa como **table** (marts = tables pro BI).

**Por que existe se é só `select *`?**

| Motivo | Explicação |
|---|---|
| **Separação de responsabilidade** | Intermediate = lógica de negócio; Marts = "pronto pra BI" |
| **Ponto de adição** | Aqui você adiciona colunas calculadas, KPIs, formatação final |
| **Performance** | Marts são `table` (materializadas), não `view` — mais rápidas pro BI |
| **Contrato com o BI** | O Power BI conecta aqui; mudanças intermediárias não quebram o dashboard |

**Fluxo completo até agora:**

```
Seeds (CSVs)                Staging               Intermediate         Marts
─────────────              ─────────             ─────────────        ─────────
clientes.csv    →  stg_erp__clientes     ─┐
localidades.csv →  stg_erp__localidades   ─┼→ int_dimensao_clientes → dim_clientes
                                          ┘
```

### 13.11 Prática: models de Agências e Colaboradores

Siga o mesmo padrão de clientes. Cria esses 4 arquivos no Studio:

**`models/staging/stg_erp__agencias.sql`**

```sql
with
fonte_agencias as (
    select *
    from {{ source('erp', 'agencias') }}
),

renomeado as (
    select
        cast(cod_agencia as int) as pk_agencia
        , nome as nome_agencia
        , tipo_agencia as tipo_agencia
        , cast(cod_localidade as int) as fk_localidade
    from fonte_agencias
)

select *
from renomeado
```

**`models/staging/stg_erp__colaboradores.sql`**

```sql
with
fonte_colaboradores as (
    select *
    from {{ source('erp', 'colaboradores') }}
),

renomeado as (
    select
        cast(cod_colaborador as int) as pk_colaborador
        , cast(cod_localidade as int) as fk_localidade
        , primeiro_nome || ' ' || ultimo_nome as nome_colaborador
        , email as email_colaborador
        , cast(cod_gerente as int) as fk_gerente
    from fonte_colaboradores
)

select *
from renomeado
```

**`models/intermediate/int_dimensao_agencias.sql`**

```sql
with
agencias as (
    select *
    from {{ ref('stg_erp__agencias') }}
),

localidades as (
    select *
    from {{ ref('stg_erp__localidades') }}
),

agencias_enriquecido as (
    select
        agencias.pk_agencia
        , agencias.nome_agencia
        , agencias.tipo_agencia
        , localidades.cidade as cidade_agencia
        , localidades.uf as uf_agencia
    from agencias
    left join localidades on agencias.fk_localidade = localidades.pk_localidade
)

select *
from agencias_enriquecido
```

**`models/marts/dim_agencias.sql`**

```sql
with
agencias as (
    select *
    from {{ ref('int_dimensao_agencias') }}
)

select *
from agencias
```

**Rodar tudo:**

```bash
dbt run --select stg_erp__agencias stg_erp__colaboradores int_dimensao_agencias dim_agencias
```

**Ou por camada:**

```bash
dbt run --select staging      # todos os staging
dbt run --select intermediate # todos os intermediate
dbt run --select marts        # todas as dimensões
```

**Padrão que você já domina:**

| Camada | Arquivo | `source()` ou `ref()` |
|---|---|---|
| Staging | `stg_erp__*.sql` | `source('erp', 'tabela')` |
| Intermediate | `int_dimensao_*.sql` | `ref('stg_erp__*')` |
| Marts | `dim_*.sql` | `ref('int_dimensao_*')` |

**Fluxo completo com agências:**

```
Seeds (CSVs)                Staging               Intermediate              Marts
─────────────              ─────────             ─────────────             ─────────
agencias.csv     →  stg_erp__agencias      ─┐
localidades.csv  →  stg_erp__localidades    ─┼→ int_dimensao_agencias → dim_agencias
                                            ┘
```

### 13.12 Intermediate e Mart de Colaboradores

**`models/intermediate/int_dimensao_colaboradores.sql`**

```sql
with
colaboradores as (
    select *
    from {{ ref('stg_erp__colaboradores') }}
),

localidades as (
    select *
    from {{ ref('stg_erp__localidades') }}
),

colaboradores_enriquecido as (
    select
        colaboradores.pk_colaborador
        , colaboradores.nome_colaborador
        , colaboradores.email_colaborador
        , colaboradores.fk_gerente
        , localidades.cidade as cidade_colaborador
        , localidades.uf as uf_colaborador
    from colaboradores
    left join localidades on colaboradores.fk_localidade = localidades.pk_localidade
)

select *
from colaboradores_enriquecido
```

**`models/marts/dim_colaboradores.sql`**

```sql
with
colaboradores as (
    select *
    from {{ ref('int_dimensao_colaboradores') }}
)

select *
from colaboradores
```

**Rodar:**

```bash
dbt run --select int_dimensao_colaboradores dim_colaboradores
```

**Fluxo:**

```
colaboradores.csv → stg_erp__colaboradores  ─┐
                                             ├→ int_dimensao_colaboradores → dim_colaboradores
localidades.csv  → stg_erp__localidades    ─┘
```

### 13.13 ERD do BanVic — mapa de relações

**Fonte:** diagrama visual fornecido em aula.

```
localidades (1) ──── (N) clientes
localidades (1) ──── (N) colaboradores
localidades (1) ──── (N) agencias

clientes (1) ──── (N) contas
agencias (1) ──── (N) contas
colaboradores (1) ── (N) contas

clientes (1) ──── (N) propostas_credito
colaboradores (1) ── (N) propostas_credito

contas (1) ──── (N) transacoes

colaboradores (N) ── (N) agencias (via colaborador_agencia)
```

**Tabelas e colunas (do ERD):**

| Tabela | PK | FKs | Colunas |
|---|---|---|---|
| **localidades** | `cod_localidade` | — | cidade, uf |
| **clientes** | `cod_cliente` | `cod_localidade` → localidades | primeiro_nome, ultimo_nome, email, tipo_cliente, data_inclusao, cpf_cnpj, data_nascimento, endereco, cep |
| **colaboradores** | `cod_colaborador` | `cod_localidade` → localidades | primeiro_nome, ultimo_nome, email, cpf, data_nascimento, endereco, cep |
| **agencias** | `cod_agencia` | `cod_localidade` → localidades | nome, endereco, tipo_agencia, data_abertura |
| **contas** | `num_conta` | `cod_cliente` → clientes, `cod_agencia` → agencias, `cod_colaborador` → colaboradores | data_abertura, tipo_conta, saldo, data_ultimo_lancamento |
| **colaborador_agencia** | — | `cod_colaborador` → colaboradores, `cod_agencia` → agencias | — (tabela de junção N:N) |
| **propostas_credito** | `cod_proposta` | `cod_cliente` → clientes, `cod_colaborador` → colaboradores | data_entrada_proposta, taxa_juros_mensal, valor_proposta, valor_financiamento, valor_entrada, valor_prestacao, quantidade_parcelas, carencia, status_proposta |
| **transacoes** | `cod_transacao` | `num_conta` → contas | data_transacao, nome_transacao, valor_transacao |

> **PEGADINHA:** `colaborador_agencia` é tabela de junção N:N (um colaborador pode estar em várias agências, uma agência tem vários colaboradores). Não tem PK própria — a combinação `(cod_colaborador, cod_agencia)` é a chave.

---

## 14. Testes genéricos no dbt

### 14.1 O que são testes genéricos

Testes genéricos são **validações automáticas** que você define no YAML. O dbt gera um SQL que, se **retornar linhas**, significa que o teste **falhou**.

### 14.2 Os 4 testes genéricos

| Teste | O que valida | Quando usar |
|---|---|---|
| **`unique`** | Todos os valores da coluna são únicos | PKs, chaves naturais |
| **`not_null`** | Nenhum valor é nulo | Colunas obrigatórias |
| **`accepted_values`** | Valores estão numa lista permitida | Status, categorias, tipos |
| **`relationships`** | Valores existem em outra tabela (FK) | Chaves estrangeiras |

### 14.3 Como funciona por baixo dos panos

Quando você escreve no YAML:

```yaml
columns:
  - name: pk_cliente
    tests:
      - unique
      - not_null
```

O dbt gera automaticamente:

```sql
-- Teste unique: retorna linhas se tiver duplicata
select pk_cliente, count(*) as duplicatas
from dev.staging.stg_erp__clientes
group by pk_cliente
having count(*) > 1

-- Teste not_null: retorna linhas se tiver nulo
select *
from dev.staging.stg_erp__clientes
where pk_cliente is null
```

**Se retornar 0 linhas = PASS ✅**
**Se retornar linhas = FAIL ❌**

### 14.4 Exemplo completo no YAML

```yaml
version: 2

sources:
  - name: erp
    description: Esse é o sistema ERP da Banvic com dados de clientes, colaboradores, contas e transações.
    schema: erp_banvic
    tables:
      - name: localidades
        description: Tabela que registra as informações de cidade e estado.
        columns:
          - name: cod_localidade
            description: Chave primária da tabela localidades.
            data_tests:
              - unique
              - not_null

      - name: clientes
        description: Tabela que armazena dados dos clientes, incluindo nome, e-mail, tipo de cliente, CPF/CNPJ, data de nascimento e endereço.

      - name: agencias
        description: Tabela que contém informações sobre as agências, como nome, endereço, cidade, estado, tipo de agência e data de abertura.

      - name: colaboradores
        description: Tabela que contém dados dos colaboradores, como nome, e-mail, CPF, data de nascimento e endereço.

      - name: contas
        description: Tabela fonte de contas com informações de contas dos clientes.

      - name: colaborador_agencia
        description: Tabela de relação entre colaboradores e agências.

      - name: propostas_credito
        description: Tabela fonte de propostas de crédito com status e valores.

      - name: transacoes
        description: Tabela fonte de transações realizadas nas contas dos clientes.
```

### 14.5 `relationships` (o mais poderoso)

Valida integridade referencial (FK):

```yaml
columns:
  - name: fk_localidade
    description: "FK pra tabela de localidades"
    tests:
      - relationships:
          to: ref('stg_erp__localidades')
          field: pk_localidade
```

Isso verifica: **todo `fk_localidade` que existe em `stg_erp__clientes` também existe em `stg_erp__localidades`**. Se tiver um cliente com `fk_localidade = 999` e não existir localidade 999, o teste falha.

### 14.6 Resumo de prova

| Genérico | O que testa | Exemplo de falha |
|---|---|---|
| `unique` | Duplicatas | Dois clientes com mesmo `pk_cliente` |
| `not_null` | Nulos | Cliente sem `email_cliente` |
| `accepted_values` | Valores inválidos | `tipo_cliente = 'X'` (não é PF nem PJ) |
| `relationships` | FK quebrada | Cliente com `fk_localidade` que não existe |

### 14.7 Rodar testes

```bash
dbt test                           # todos os testes
dbt test --select stg_erp__clientes  # só os desse model
dbt test --select staging          # todos os testes de staging
```

### 14.8 Onde ficam os testes

| Tipo | Onde define | Arquivo |
|---|---|---|
| **Genéricos** | No YAML do model | `schema.yml` ou `_erp_banvic.yml` |
| **Singulares** | Arquivo `.sql` separado | `tests/sem_duplicatas.sql` |

> **Próxima aula:** testes singulares — SQL customizado que você escreve do zero.

### 14.9 Packages no dbt — como expandir funcionalidades

#### O que são packages

Packages são **bibliotecas reutilizáveis** que você importa no projeto. É como um "plugin" — ganha macros, testes e funções prontas.

**Analogia:** packages no dbt = `pip install` no Python.

#### Como instalar

**1. Criar `packages.yml` na raiz do projeto:**

```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.3.1
```

**2. Rodar:**

```bash
dbt deps
```

**3. Estrutura resultante:**

```
banvic-dbt/
├── dbt_project.yml
├── packages.yml          ← você cria
├── dbt_packages/         ← dbt deps cria (NÃO versionar)
│   └── dbt_utils/
└── ...
```

> **⚠️** `dbt_packages/` deve estar no `.gitignore`. Cada pessoa roda `dbt deps` na sua máquina.

#### O package `dbt_utils` (o mais usado)

| Macro | O que faz |
|---|---|
| `get_series_dates()` | Gera uma série de datas |
| `date_spine()` | Cria tabela de datas com intervalo |
| `unique_combination_of_columns` | Testa unicidade de combinação de colunas |

**Versão recomendada:** 1.3.1 (compatível com Databricks Community Edition).

### 14.10 Teste `unique_combination_of_columns` — erros e correção

#### O problema

Tabelas de junção N:N (como `colaborador_agencia`) não têm PK própria. A chave é a **combinação** das duas FKs — precisa garantir que não existam duplicatas.

#### Sintaxe correta

```yaml
- name: colaborador_agencia
  description: Tabela de relação entre colaboradores e agências.
  data_tests:
    - dbt_utils.unique_combination_of_columns:
        arguments:
          combination_of_columns:
            - cod_colaborador
            - cod_agencia
```

#### Erros comuns

| Erro | Causa | Solução |
|---|---|---|
| `has no attribute 'test_combination_of_columns'` | Macro errada | Usar `unique_combination_of_columns` |
| `has no attribute 'test_combination_of_columns'` | Versão errada do package | Usar `version: 1.3.1` |
| YAML mal indentado | Indentação incorreta | 2 espaços, nunca tabs |
| Teste como tabela separada | Nível errado no YAML | Colocar `data_tests:` no nível da tabela |

#### O que o teste faz (SQL gerado)

```sql
with validation_errors as (
    select
        cod_colaborador, cod_agencia
    from `dev`.`erp_banvic`.`colaborador_agencia`
    group by cod_colaborador, cod_agencia
    having count(*) > 1
)
select * from validation_errors
```

- Retornou linhas = **FAIL** (tem duplicatas)
- Retornou nada = **PASS** (combinação é única)

#### Lições aprendidas

1. **Nome correto:** `unique_combination_of_columns` (não `combination_of_columns`)
2. **`arguments:` é obrigatório** na sintaxe do dbt_utils
3. **Nível correto:** `data_tests:` no nível da **tabela**, não da coluna
4. **Versão importa:** 1.3.1 funciona com Databricks; 1.4.1 pode não funcionar
5. **`dbt clean` + `dbt deps`** resolve problemas de cache

### 14.11 Model `int_dimensao_datas` — usando `dbt_utils.date_spine()`

#### O problema

Precisamos de uma tabela de datas pra análises (filtrar por dia, mês, trimestre, ano, fim de semana). Em vez de criar manualmente, usamos o `dbt_utils.date_spine()` pra gerar automaticamente.

#### Código completo

```sql
with
date_spine as (
    {{
        dbt_utils.date_spine(
            datepart="day",
            start_date="cast('2000-01-01' as date)",
            end_date="cast('2030-01-01' as date)"
        )
    }}
),

criar_datas as (
    select
        row_number() over(order by date_day) as pk_data
        , cast(date_day as date) as dt_data
        , extract(day from date_day) as dia
        , extract(month from date_day) as mes
        , extract(year from date_day) as ano
        , extract(quarter from date_day) as trimestre
        , extract(dow from date_day) as dia_da_semana
        , case
            when extract(dow from date_day) in (0, 6) then true
            else false
        end as is_final_de_semana
    from date_spine
)

select *
from criar_datas
```

#### O que cada parte faz

| Parte | Função |
|---|---|
| `dbt_utils.date_spine()` | Gera série de datas (2000-2030, 1 dia) |
| `row_number()` | Cria PK auto-incrementada |
| `extract(day/month/year/quarter)` | Extrai componentes da data |
| `extract(dow)` | Dia da semana (0=Dom, 6=Sáb) |
| `case when in (0, 6)` | Marca fim de semana |

#### Comandos

```bash
dbt run --select int_dimensao_datas
dbt build --select int_dimensao_datas
```

#### Por que `datepart="day"`?

| Datepart | Intervalo | Uso |
|---|---|---|
| `day` | 1 dia | Análise diária (mais comum) |
| `week` | 1 semana | Análise semanal |
| `month` | 1 mês | Análise mensal |

> **Dica:** `day` é o mais granular — depois você agrega no BI por semana/mês/trimestre conforme precisa.

### 14.12 Models de Contas — estratégia dimensão × fato

#### A estratégia

A tabela `contas` alimenta **duas coisas** no marts: uma dimensão e um fato. Por isso existem **2 intermediários**:

```
stg_erp__contas ──→ int_dimensao_contas ──→ dim_contas
              └──→ int_fato_contas    ──→ fact_contas
```

| Model | Camada | O que seleciona |
|---|---|---|
| `stg_erp__contas` | Staging | Limpa e renomeia TUDO |
| `int_dimensao_contas` | Intermediate | Colunas da dimensão (atributos) |
| `int_fato_contas` | Intermediate | Colunas do fato (medidas + FKs) |
| `dim_contas` | Marts | Dimensão final |
| `fact_contas` | Marts | Fato final |

#### `stg_erp__contas.sql`

```sql
with
fonte_contas as (
    select *
    from {{ source('erp', 'contas') }}
),

renomeado as (
    select
        cast(num_conta as int) as pk_conta
        , cod_cliente as fk_cliente
        , cod_agencia as fk_agencia
        , cod_colaborador as fk_colaborador
        , cast(num_conta as int) as numero_conta
        , tipo_conta
        , cast(data_abertura as timestamp) as ts_abertura_conta
        , cast(saldo_total as numeric(32,2)) as saldo_total
        , cast(saldo_disponivel as numeric(32,2)) as saldo_disponivel
        , cast(data_ultimo_lancamento as timestamp) as ts_ultimo_lancamento
    from fonte_contas
)

select *
from renomeado
```

#### `int_dimensao_contas.sql`

```sql
with
contas as (
    select *
    from {{ ref('stg_erp__contas') }}
),

selecionar_colunas as (
    select
        pk_conta
        , numero_conta
        , tipo_conta
        , ts_abertura_conta
    from contas
)

select *
from contas
```

#### `int_fato_contas.sql`

```sql
with
contas as (
    select *
    from {{ ref('stg_erp__contas') }}
),

selecionar_colunas as (
    select
        pk_conta
        , fk_cliente
        , fk_agencia
        , saldo_total
        , saldo_disponivel
        , ts_ultimo_lancamento
    from contas
)

select *
from contas
```

> **Nota:** o `select * from contas` no final puxa todas as colunas. Se fosse pra selecionar só as do CTE, seria `select * from selecionar_colunas`.

#### Dimensão vs Fato — o que vai em cada uma

| Tipo | O que é | Exemplo de colunas |
|---|---|---|
| **Dimensão** | Atributos (quem/onde/quando) | `pk_conta`, `numero_conta`, `tipo_conta`, `ts_abertura_conta` |
| **Fato** | Medidas + FKs (quanto/quando) | `pk_conta`, `fk_cliente`, `fk_agencia`, `saldo_total`, `saldo_disponivel`, `ts_ultimo_lancamento` |

> **Regra de ouro:** se é **texto/data descrição** → dimensão. Se é **número que soma/conta** → fato. Se é **FK** → fato.

---

## 4. Campo calculado vs Métrica calculada

| | Campo calculado | Métrica calculada |
|---|---|---|
| **Escopo** | 1 linha | Grupo de linhas |
| **Função** | Aritmética/lógica por registro | Agregação (SUM, COUNT, AVG, MIN, MAX) |
| **Resultado** | Nova **coluna**, mesma qtd de linhas | Nova **linha resumida** |
| **Não muda o grão** | ✅ Mantém | ❌ Muda (resume) |
| **SQL** | na lista do `SELECT` | com `GROUP BY` ou janela (`OVER`) |
| **No BI** | vira uma **coluna** | vira uma **medida DAX/M** |

> **Mnemônica:** *campo = linha a linha; métrica = grupo a grupo.* O campo `valor_com_imposto` (por linha) alimenta a métrica `SUM(valor_com_imposto) GROUP BY uf`.

---

## 5. Self-Service e Semantic Layer

- **Objetivo:** o usuário de negócio monta o próprio relatório **sem depender do time de dados** — mas **sem errar** (sem métrica errada, sem grão errado)
- **Só funciona se o pesado já foi feito na transformação (item 3.7):**
  - Campo calculado → aparece como **coluna pronta** no BI
  - Métrica calculada → aparece como **medida pronta**
  - Testes garantem integridade → usuário confia no número
- **A pegadinha conceitual:** self-service **não** é "deixar o usuário calcular tudo". É *deixar o usuário explorar dados prontos e confiáveis*. O cálculo fica centralizado na transformação; a exploração fica self-service
- Os models `marts/` (fatos + dimensões + KPIs já calculados) = **semantic layer** que o BI consome. Quanto mais negócio você empurra pra essa camada, mais self-service o usuário tem

---

## 6. Camadas de Dados: curso vs mercado

### 6.1 Nomenclatura do curso (dbt)

| Camada | Prefixo | O que acontece |
|---|---|---|
| **Raw / Bruta** | `erp_banvic` | Dados brutos como vieram da fonte (seeds/sources) |
| **Staging** | `stg_*` | Limpeza simples: renomear, tipar, filtrar, desduplicar |
| **Intermediate** | `int_*` | Joins, enriquecimento, lógica de negócio intermediária |
| **Marts** | `dim_*`, `fact_*`, `kpi_*` | Star schema final pronto pro BI (tables) |

### 6.2 Nomenclatura do mercado

**Arquitetura Medallion (Databricks/Delta Lake) — a mais comum em vagas:**

| Medallion | Equivale ao curso | Nível de qualidade |
|---|---|---|
| **Bronze** | Raw / dados brutos | Dado cru, imutável |
| **Silver** | Staging + Intermediate | Limpo, validado, enriquecido |
| **Gold** | Marts | Pronto para negócio/BI, star schema |

**Outras nomenclaturas:**

| Nomenclatura | Camadas |
|---|---|
| **Genérica (Snowflake)** | `raw` → `landing`/`staging` → `consumption` |
| **Trusted/Refined** | `raw` → `trusted` → `refined` |
| **Integration/Presentation** | `integration` → `presentation` |
| **DW clássico** | `ODS` → `EDW` (normalizado) → `Data Marts` |
| **Kimball (Mód. 3)** | `staging` (normalizada) → `intermediate` → `marts` |

> **Pegadinha:** o curso usa **4 pastas** (raw, staging, intermediate, marts), mas a medallion usa **3 camadas** (bronze, silver, gold) — porque **silver junta staging + intermediate**. Não existe correspondência 1:1 exata; o que conta é o **nível de transformação** de cada uma.
>
> **No desafio:** Power BI conecta em **marts = gold**. "Onde ficam seus dados silver?" → `staging` + `intermediate`.

### 6.3 Mapa BanVic (bronze → silver → gold)

```
Bronze (erp_banvic)          Silver (staging+int)        Gold (marts)
  clientes.csv        →    stg_clientes          →    dim_cliente
  transacoes.csv      →    stg_transacoes  ┐           │
  contas.csv          →    stg_contas       ┼→ int_…  → fact_transacoes
  agencias.csv        →    stg_agencias     ┘           │
  localidades.csv     →    stg_localidades        →    dim_agencia / dim_localidade
```

---

## 7. Versionamento: Tier 2 vs Tier 3 e Hotfix (Code Versioning)

A quantidade de **camadas de branch** entre desenvolvimento e produção define o *tier* do pipeline de versionamento.

### Tier 2 (2 camadas — simples)

```
Branch main ──────────────────────── Schema de produção
    │
    ├── dbt_carla_almeida ──────── dbt_carla_almeida (schema)
    │
    └── dbt_joao_silva ──────────── dbt_joao_silva (schema)
```

- Devs brancham **direto da `main`**
- Cada dev tem seu próprio schema no DW
- Sem camada intermediária de validação

### Tier 3 (3 camadas — mais seguro)

```
Branch Main ──────────────────────── Banco produção → Schema de produção
    │
    └── Branch Develop ──────────── Banco desenvolvimento → Schema de desenvolvimento
            │
            ├── dbt_carla_almeida ── dbt_carla_almeida (schema)
            │
            └── dbt_joao_silva ──── dbt_joao_silva (schema)
```

- Existe uma `branch develop` **entre** `main` e as branches dos devs
- A `develop` tem **seu próprio banco/schema** no DW
- Valida na `develop` → só depois merge na `main` → produção

### Resumo

| | Tier 2 | Tier 3 |
|---|---|---|
| **Camadas** | main → devs | main → develop → devs |
| **Banco de dev** | ❌ (só schemas) | ✅ (banco separado) |
| **Validação intermediária** | ❌ | ✅ (develop serve de staging) |
| **Complexidade** | Baixa | Maior, mas mais seguro |
| **Uso típico** | Projeto pequeno/time único | Time grande, múltiplos devs |

### Hotfix

Correção **urgente** aplicada **direto na branch main** (ou develop), **pulando o fluxo normal**:

```
Fluxo normal: feature branch → develop → main (com testes, review)
Hotfix:       hotfix branch ──────────→ main (pula develop/testes)
```

- Existe pra resolver bugs críticos que **não podem esperar** o ciclo normal
- **Risco:** pula testes e review → pode introduzir novos bugs
- **Boa prática:** depois do hotfix na main, fazer **backport** (merge reverso) pra develop, pra não divergir

> **No Módulo IV:** o slide de "Separation of Environments" mostra exatamente isso — cada branch no git cria um schema separado no DW. O hotfix é a exceção: merge direto sem passar pelo schema de desenvolvimento.

---

## 8. Incremental × SCD (conexão com o Módulo 3)

O incremental e o SCD veem **o mesmo problema de dois ângulos**:

| | Incremental load (Mód. IV) | SCD (Mód. 3) |
|---|---|---|
| **Problema** | Bancos transacionais são **mutáveis** — UPDATEs retroativos quebram a carga incremental | Dimensões mudam ao longo do tempo — o que fazer com o histórico? |
| **Pergunta** | *Como extraio as mudanças da fonte?* (ingestão) | *Como armazeno as mudanças no DW?* (modelagem) |
| **Solução** | Coluna `data_atualização` ou logs (CDC) | SCD1 (sobrescreve) ou SCD2 (nova linha + validade) |

> **Incremental é o mecanismo de captura; SCD é a política de armazenamento.**

**Como se cruzam:**
- **Full load + SCD1** → recarrega tudo, sobrescreve (sem histórico) — consistente, pesado
- **Incremental (data de criação) + SCD2** → captura só novos, mas **perde** UPDATEs retroativos → histórico incompleto (pedido cancelado do slide). *Erro clássico de prova.*
- **Incremental + overwrite (CDC) + SCD2** → captura o alterado, dimensão **cria nova linha** com período de validade — histórico completo
- **Incremental + overwrite + SCD1** → captura o alterado e **sobrescreve** a linha — sempre a versão atual

**Pegadinha de prova:**
> **SCD1 ≈ "incremental + overwrite"** (substitui o registro anterior).
> **SCD2 ≈ requer CDC** (precisa detectar a mudança para criar a nova linha de validade).

**Exemplo concreto (cliente muda de cidade):**

Fonte (mutável) — cliente 123 mudou de SP → Curitiba em 15/06:

| cod_cliente | nome | cidade | uf | data_atualizacao |
|---|---|---|---|---|
| 123 | Maria Souza | São Paulo | SP | 01/01/2026 |
| 124 | João Lima | Rio | RJ | 01/01/2026 |
| 123 | Maria Souza | Curitiba | PR | 15/06/2026 |

Extração incremental por `data_atualizacao`:
- Dia 02/01 → linhas 123 (SP), 124 (RJ)
- Dia 16/06 → linha **123 (Curitiba)** ← pegou o UPDATE (se o índice fosse `data_criacao`, extrairia 0 linhas e perderia a mudança)

Dimensão `dim_cliente` com SCD2:

| cliente_sk | cod_cliente | nome | cidade | validade_inicio | validade_fim | atual |
|---|---|---|---|---|---|---|
| 1 | 123 | Maria Souza | São Paulo | 02/01/2026 | 16/06/2026 | ✗ |
| 2 | 124 | João Lima | Rio | 02/01/2026 | NULL | ✓ |
| 3 | 123 | Maria Souza | Curitiba | 16/06/2026 | NULL | ✓ |

Join da fato com a dimensão por validade:

```sql
SELECT f.cod_pedido, f.data_pedido, c.cidade
FROM fact_pedidos f
JOIN dim_cliente c ON f.cliente_sk = c.cliente_sk
                   AND f.data_pedido BETWEEN c.validade_inicio
                                 AND COALESCE(c.validade_fim, '9999-12-31')
```

> **E as surrogate keys ligam tudo:** com SCD2, uma mesma chave natural tem **várias linhas** na dimensão — cada uma precisa de uma surrogate key distinta. Por isso o alerta do Mód. IV: `ROW_NUMBER()` auto-incrementado é perigoso — se a ordem muda entre execuções, a chave muda e o histórico quebra.

---

## 9. Orquestração de Pipelines, DAGs e Airflow

### 9.1 O problema: por que orquestrar?

Um pipeline não é um comando só — são **várias tarefas encadeadas** com dependências. Exemplo do slide:

```
ERP extraction ──→ Loading ──→ Source test: ERP ──────────┐
Planilha extraction → Loading → Source test: planilhas ──┼──→ dbt build commercial
CRM extraction ──→ Loading ──→ Source test: CRM ─────────┼──→ dbt build marketing
```

Perguntas sem orquestrador: **quando** rodar? **em que ordem**? **e se falhar no meio**? (slide mostra: CRM falhou → email "impacto nos dados de marketing"). Rodar na mão não escala e não avisa de nada.

### 9.2 O que é um DAG

**DAG = Directed Acyclic Graph** (Grafo Dirigido Acíclico) — a representação do pipeline:

| Palavra | Significado no pipeline |
|---|---|
| **Graph** | Nós (tarefas) ligados por arestas (dependências) |
| **Directed** | As setas têm direção: A **antes de** B |
| **Acyclic** | **Sem ciclos** — A → B → C, nunca A → B → A |

Tarefas sem dependência entre si (extrair ERP e extrair CRM) rodam **em paralelo**.

> **PEGADINHA:** DAG **não** é ferramenta — é a *estrutura*. O Airflow é a ferramenta que **executa** DAGs. E o `ref()` do dbt já gera um DAG internamente (por isso `dbt docs` mostra a linhagem) — o orquestrador **agenda e monitora** a execução desse grafo.

### 9.3 O que é um orquestrador

É o **maestro** do pipeline. As 5 responsabilidades do slide:

1. **Agendar** tarefas (schedule — "todo dia às 02:00")
2. **Monitorar** a execução (o que rodou, quanto demorou, status)
3. **Notificar** em caso de falha (email/Slack com o impacto)
4. **Visualizar** e gerenciar as etapas (UI com o grafo)
5. **Garantir a ordem** definida (executa respeitando dependências)

### 9.4 Airflow em detalhe

**Apache Airflow** = orquestrador open-source mais usado do mercado, escrito em Python.

**Arquitetura:**

```
┌─────────────┐   lê DAGs   ┌──────────────┐
│  Scheduler   │────────────→│ Metadata DB  │←───── Webserver (UI)
│ (decide quando)│           │ (estado tudo) │
└──────┬──────┘             └──────────────┘
       │ enfileira tarefas
┌──────▼──────┐
│  Executor    │─── distribui ───→  Workers (executam as tasks)
└─────────────┘
```

- **Scheduler:** decide "hora de rodar o DAG X" respeitando dependências
- **Executor:** distribui tarefas pros workers (Local, Celery, Kubernetes)
- **Workers:** executam cada task de verdade
- **Metadata DB:** guarda o estado (runs, logs, status)
- **Webserver:** a UI dos screenshots do slide (Tree, Graph, Gantt, Code)

**Conceitos fundamentais:**

| Conceito | O que é |
|---|---|
| **DAG** | Arquivo Python que define o pipeline inteiro |
| **Task** | Unidade de trabalho dentro do DAG |
| **Operator** | Molde da task: `BashOperator` (shell — ex.: `dbt build`), `PythonOperator` (função Python), `Sensor` (espera algo) |
| **Run** | Uma execução do DAG (ex.: a run de 02:00 de hoje) |
| **schedule** | Frequência — sintaxe cron (`0 2 * * *` = todo dia 02:00) |
| **retries** | Quantas tentativas antes de falhar de vez |
| **backfill** | Rodar retroativamente datas passadas |

**DAG mínimo de exemplo:**

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="banvic_pipeline",
    schedule="0 2 * * *",              # todo dia às 02:00
    start_date=datetime(2026, 1, 1),
    catchup=False,                     # não roda datas passadas
    default_args={"retries": 2},       # tenta 2x antes de falhar
) as dag:

    seed = BashOperator(task_id="dbt_seed", bash_command="dbt seed --select banvic.*")
    staging = BashOperator(task_id="dbt_staging", bash_command="dbt run --select staging")
    marts = BashOperator(task_id="dbt_marts", bash_command="dbt run --select marts")
    testes = BashOperator(task_id="dbt_test", bash_command="dbt test")

    seed >> staging >> marts >> testes   # o ">>" define as dependências
```

O `>>` desenha o DAG em código. Se `staging` falhar, `marts` e `testes` **não rodam** — e o Airflow avisa.

**A UI (screenshots do slide):**

- **Tree/Grid view:** linha = task; coluna = run (verde ok, vermelho falhou)
- **Graph view:** o DAG desenhado
- **Gantt view:** duração de cada task (acha gargalos)
- **Code view:** o Python do DAG
- **Clear:** reprocessa task falha (reprocessamento seletivo)

### 9.5 dbt + orquestração

> dbt Core **não possui orquestrador nativo** — usar ferramenta externa (Airflow, Prefect). Alternativa: **dbt Cloud**, com orquestrador incorporado.

| Cenário | Como orquestra |
|---|---|
| **dbt Core** | Airflow, Prefect, Dagster, ou cron (simples demais p/ produção séria) |
| **dbt Cloud** | Orquestrador embutido (schedules, alertas, CI/CD) |
| **Airflow + dbt** | `BashOperator` chamando `dbt build`, ou lib **Cosmos** (cada model vira uma task do Airflow) |

> **PEGADINHA:** `dbt build` já executa seeds + models + testes **na ordem certa** (DAG interno do dbt). O orquestrador externo orquestra **acima** disso: ingestão → dbt build → export → alertas.

### 9.6 Alternativas ao Airflow

| Ferramenta | Característica |
|---|---|
| **Airflow** | Padrão de mercado, maduro, UI completa; mais pesado de operar |
| **Prefect** | Mais "Pythonico", leve, fácil de startar |
| **Dagster** | Focado em data assets (testes e linhagem nativos — filosofia próxima do dbt) |
| **cron** | Só agenda; sem monitoramento/visualização |
| **dbt Cloud** | Orquestra só o dbt, mas faz bem |

### 9.7 No desafio BanVic

```
02:00 → dbt seed (8 CSVs → erp_banvic)
      → dbt build (staging → intermediate → marts, com testes no meio)
      → export/validação → Power BI refresh
      → falha? → email/Slack avisando onde quebrou
```

No Databricks Community Edition (limite de horas), orquestrar é ainda mais importante: agenda na janela disponível e `retries` cobre falhas transitórias de cluster.

**Resumo de prova:**
- **DAG** = grafo dirigido **acíclico** (estrutura, não ferramenta)
- **Orquestrador** = agenda + ordem + monitoramento + alertas + visualização
- **dbt Core** não orquestra; **dbt Cloud** sim
- **Airflow**: DAG em Python, Operators, `>>` define dependências, UI Graph/Gantt
- Falha no meio do DAG → dependentes **não executam** + notificação