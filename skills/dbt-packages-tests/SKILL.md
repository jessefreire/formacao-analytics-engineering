# Skill: dbt Packages e Testes — Lições Aprendidas

> Esta skill documenta todo o processo de aprendizado sobre packages no dbt, testes genéricos com `dbt_utils`, erros comuns e como resolvê-los. Criada a partir de erros reais durante a Formação AE (Indicium).

---

## 1. O que são packages no dbt

Packages são **bibliotecas reutilizáveis** que você importa no projeto dbt. É como um "plugin" — você ganha macros, testes e funções prontas sem precisar criar do zero.

**Analogia:** packages no dbt = `pip install` no Python / `npm install` no JavaScript.

---

## 2. Como instalar um package

### 2.1 Criar o `packages.yml`

Na **raiz do projeto** (ao lado do `dbt_project.yml`), crie o arquivo `packages.yml`:

```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.3.1
```

### 2.2 Rodar `dbt deps`

```bash
dbt deps
```

Isso baixa e instala o package na pasta `dbt_packages/`.

### 2.3 Estrutura resultante

```
banvic-dbt/
├── dbt_project.yml
├── packages.yml          ← você cria
├── dbt_packages/         ← dbt deps cria (não commite no git)
│   └── dbt_utils/
│       └── macros/
└── ...
```

> **⚠️ IMPORTANTE:** `dbt_packages/` deve estar no `.gitignore` — não versione packages. Cada pessoa roda `dbt deps` na sua máquina.

---

## 3. O package `dbt_utils` — o mais usado

### 3.1 O que oferece

| Categoria | Macros/Testes | O que faz |
|---|---|---|
| **Date** | `get_series_dates()`, `date_spine()` | Gera séries de datas |
| **Testes** | `unique_combination_of_columns` | Testa unicidade de combinação de colunas |
| **Colunas** | `generate_series()`, `horizon()` | Gera séries numéricas |
| **String** | `concat()`, `split_part()` | Utilitários de texto |
| **OpenGL** | `get_query_results()` | Executa queries dinâmicas |

### 3.2 Versão recomendada

Para o curso (Databricks):
```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.3.1
```

> **Versão 1.4.1 pode causar problemas** com Databricks. Use 1.3.1 se der erro.

---

## 4. Teste `unique_combination_of_columns` — o que aprendemos

### 4.1 O problema

Tabelas de junção N:N (como `colaborador_agencia`) não têm PK própria. A chave é a **combinação** das duas FKs. Precisamos garantir que não existam duplicatas.

### 4.2 O erro inicial (sintaxe errada)

```yaml
# ❌ ERRADO — sintaxe antiga/errada
- name: colaborador_agencia
  columns:
    - name: cod_colaborador
      data_tests:
        - dbt_utils.combination_of_columns:    # ← macro errada
            combination_of_columns:
              - cod_colaborador
              - cod_agencia
```

**Erro retornando:**
```
'dbt.context.macros.MacroNamespace object' has no attribute 'test_combination_of_columns'
```

**Causa:** a macro se chama `unique_combination_of_columns`, não `combination_of_columns`.

### 4.3 O segundo erro (lugar errado)

```yaml
# ❌ ERRADO — teste como tabela separada
- name: colaborador_agencia
  description: ...

- name: cod_colaborador              # ← vira uma "tabela" nova
  data_tests:
    - dbt_utils.combination_of_columns:
        ...
```

**Causa:** o teste foi colocado como uma tabela separada, não como coluna dentro de `colaborador_agencia`.

### 4.4 A sintaxe correta

```yaml
# ✅ CERTO
- name: colaborador_agencia
  description: Tabela de relação entre colaboradores e agências.
  data_tests:                              # ← nível da TABELA, não da coluna
    - dbt_utils.unique_combination_of_columns:   # ← nome correto
        arguments:                                # ← arguments obrigatório
          combination_of_columns:
            - cod_colaborador
            - cod_agencia
```

### 4.5 Resumo das diferenças

| Aspecto | Errado | Certo |
|---|---|---|
| **Nome da macro** | `combination_of_columns` | `unique_combination_of_columns` |
| **Parâmetro** | `combination_of_columns:` direto | `arguments:` → `combination_of_columns:` |
| **Nível no YAML** | `columns:` (nivel coluna) | `data_tests:` (nivel tabela) |

---

## 5. O que o teste faz por baixo dos panos

O dbt gera esse SQL automaticamente:

```sql
with validation_errors as (
    select
        cod_colaborador, cod_agencia
    from `dev`.`erp_banvic`.`colaborador_agencia`
    group by cod_colaborador, cod_agencia
    having count(*) > 1
)

select *
from validation_errors
```

- **Retornou linhas** = tem duplicatas = **FAIL**
- **Retornou nada** = combinação é única = **PASS**

---

## 6. Checklist de packages

| Etapa | Comando | O que verifica |
|---|---|---|
| 1. Criar `packages.yml` | — | Versão correta do package |
| 2. Instalar | `dbt deps` | Packages baixados em `dbt_packages/` |
| 3. Limpar cache | `dbt clean` | Remove `target/` e `dbt_packages/` |
| 4. Reinstalar | `dbt deps` | Instala do zero |
| 5. Rodar testes | `dbt test` | Macros existem e funcionam |

---

## 7. Erros comuns e soluções

| Erro | Causa | Solução |
|---|---|---|
| `has no attribute 'test_...'` | Macro não existe no package | Verificar nome da macro + versão do package |
| `Compilation Error` | YAML mal indentado | Conferir indentação (2 espaços) |
| `TABLE_OR_VIEW_NOT_FOUND` | Tabela não existe ainda | Rodar `dbt build` antes de `dbt test` |
| `UNRESOLVED_COLUMN` | Nome da coluna errado | Conferir no Databricks Catalog |
| `dbt deps` não instala | `packages.yml` na pasta errada | Deve estar na raiz do projeto |
| `Syntax error at or near ','` | Vírgula extra entre CTEs | Remover a vírgula antes do nome do próximo CTE |

---

## 9. CTEs e vírgulas — erro que repete

### O problema

Quando você tem múltiplas CTEs, é fácil colocar uma vírgula **extra** antes do nome da próxima CTE:

```sql
-- ❌ ERRADO (vírgula duplicada)
),

, selecionar_colunas as (

-- ✅ CERTO (sem vírgula)
),

selecionar_colunas as (
```

### Por que acontece

O padrão do dbt é colocar vírgula **depois** do `)` de fechamento da CTE anterior:

```sql
CTE anterior as (
    ...
),              ← vírgula aqui (certa)
proxima_CTE as (
    ...
)
```

Mas quando copia e cola ou edita rápido, a vírgula pode ficar **também antes** do nome da próxima CTE.

### Regra

| Contexto | Vírgula? |
|---|---|
| Depois do `)` da CTE anterior | ✅ Sim |
| Antes do nome da próxima CTE | ❌ Não |

```sql
-- ✅ Padrão correto
with
cte_um as (
    ...
),

cte_dois as (
    ...
),

cte_tres as (
    ...
)

select * from cte_tres
```

> **Mnemônica:** vírgula **depois do parêntese**, nunca **antes do nome**.

---

## 8. Fluxo correto (de trás pra frente)

```
1. Criar packages.yml
2. Rodar dbt deps
3. Criar models (SQL)
4. Rodar dbt build          ← cria as tabelas
5. Rodar dbt test           ← testa as tabelas
6. Rodar dbt docs generate  ← gera documentação
```

> **Nunca rodar `dbt test` antes de `dbt build`** — as tabelas ainda não existem.

---

## 9. Lições aprendidas (erros reais)

1. **Sempre conferir o nome exato da macro** — `combination_of_columns` vs `unique_combination_of_columns`
2. **`arguments:` é obrigatório** na sintaxe do `dbt_utils`
3. **Teste de combinação fica no nível da tabela**, não da coluna
4. **Versão do package importa** — 1.3.1 funciona, 1.4.1 pode não funcionar com Databricks
5. **`dbt clean` + `dbt deps`** resolve muitos problemas de cache
6. **Indentação YAML** é sensível — use 2 espaços, nunca tabs
7. **`dbt build` antes de `dbt test`** — tabelas precisam existir
8. **ERD é o mapa** — sempre consultar antes de escrever colunas nos models
