# AGENTS.md — Formação Analytics Engineer (Indicium)

> **⚠️ DOCUMENTO VIVO** — Este arquivo, `INDICE_MODULOS.md` e `Analytics Engineer Training 2026.md` devem ser **atualizados automaticamente** a cada nova conversa com agentes, novo material do curso ou mudança estrutural no projeto. Não deixe para depois.

> Guia persistente para sessões futuras. Atualize quando houver mudanças estruturais.

---

## Arquitetura do Projeto

```
Formação AE/                        # ← Repositório git local (commit "chore: sync")
├── AGENTS.md                    # Este arquivo
├── Analytics Engineer Training 2026.md   # Diário de bordo do curso
├── GUIA_DBT_BANVIC.md           # Guia prático dbt (local vs Cloud)
├── INDICE_MODULOS.md            # Índice consolidado de módulos
├── .gitignore                   # Exclui *.pdf, *.zip, Desafio/referências, .agents/
├── .claude/settings.local.json  # Permissões opencode
├── index.html                   # App de visualização de materiais (design Apple)
├── files.json                   # Manifest gerado pelo sync
├── server.py                    # Servidor local (http://localhost:8765)
├── .opencode/
│   ├── skill/ae_materials_app/  # Skill de auto-sync (templates + sync.py)
│   └── index.html, files.json   # ← duplicatas do sync (candidatas a limpeza)
├── Módulo 1 -  Introdução à Análise de Dados/   # PDF/MD + resumo + decoreba
├── Modulo 2 - SQL para Análise de Dados/        # Oficial + resumo + decoreba
├── Desafio/
│   ├── desafio-banvic-an-lise-de-dados-2024.ipynb
│   └── Exemplos repo banvic/    # Referências de terceiros (NÃO versionar)
└── SEU_PROJETO/                 # ← Criar via fork de techindicium/banvic-dbt
    ├── dbt_project.yml
    ├── models/ (staging/ intermediate/ marts/)
    ├── seeds/banvic/            # 8 CSVs (vêm do template)
    ├── macros/, tests/
    └── profiles.yml             # FORA do repo (~/.dbt/profiles.yml)
```

**Seu projeto real** = fork de `https://github.com/techindicium/banvic-dbt` clonado localmente.
**App de materiais** = local, sem build. Sempre abrir via `http://localhost:8765` (não `file://`, por CORS). Sync: `python .opencode/skill/ae_materials_app/sync.py` (o alias moderno `python -m ae_materials_app.sync` NÃO funciona — module fora do path).

---

## Comandos Corretos

### dbt Core (local)
```bash
# Instalação (uma vez)
pip install dbt-databricks

# Validação de conexão
dbt debug

# Seeds (carregar CSVs no Databricks)
dbt seed --select banvic.agencias          # uma tabela
dbt seed                                   # todas (se habilitadas no dbt_project.yml)

# Models
dbt run --select staging                   # camada inteira
dbt run --select staging.stg_clientes      # model específico
dbt run --select +marts.fact_transacoes    # model + dependências

# Testes
dbt test                                   # todos
dbt test --select staging.stg_clientes     # específicos

# Utilitários
dbt clean                                  # remove target/ dbt_packages/
dbt docs generate && dbt docs serve        # documentação local
```

### Jupyter (análise exploratória)
```bash
jupyter notebook  # abre analise_banvic.ipynb ou seu notebook
```

---

## Convenções de Código

### dbt / SQL
| Item | Convenção |
|------|-----------|
| **Nomes de models** | `stg_<entidade>`, `int_<entidade>`, `fact_<entidade>`, `dim_<entidade>`, `kpi_<nome>` |
| **Colunas** | `snake_case` (ex: `cod_cliente`, `saldo_total`) |
| **Schemas** | `erp_banvic` (seeds/raw), `staging`, `intermediate`, `marts` (via `generate_schema_name`) |
| **Materialização** | `view` em staging/intermediate; `table` em marts |
| **Refs** | Sempre `{{ ref('model_name') }}` — nunca `source()` para seeds internas |
| **Tests** | `unique` + `not_null` em PKs; `accepted_values` em status/categorias; `relationships` em FKs |
| **CTEs** | Uma por transformação lógica; nomes descritivos (`cleaned`, `joined`, `aggregated`) |

### Python (Notebooks)
- Pandas idiomático; evitar loops
- Tipagem explícita em `read_csv` (`dtype=`, `parse_dates=`)
- CEP: normalizar para string 8 dígitos (zeros à esquerda)
- Datas: `utc=True` + `dt.tz_convert('America/Sao_Paulo')` se necessário

### Git
- Repo local inicializado em `Formação AE/` (root). `main` branch protegida; trabalho em branches `feature/`, `fix/`
- Commits convencionais: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`
- `.gitignore`: `target/`, `dbt_packages/`, `logs/`, `.venv/`, `*.pyc`, `.DS_Store`, `*.pdf`, `*.zip`, `Desafio/Exemplos repo banvic/`, `.agents/`

### App de Materiais (HTML + Server)
- **Sem build**: `index.html` lê `FILES` (array injetado pelo sync) + `marked.js` + `motion` (CDN)
- **Design Apple**: sidebar translúcida (`backdrop-filter: blur`), springs `cubic-bezier(0.25,0.46,0.45,0.94)`, feedback no `pointerdown`, tipografia IBM Plex, respeita `prefers-reduced-motion` e dark mode
- **Servidor**: `python server.py` (porta 8765, abre navegador, header CORS)
- **Sync**: `python .opencode/skill/ae_materials_app/sync.py` regenera `FILES` + `files.json`

---

## Regras de Negócio Descobertas (BanVic)

| Domínio | Regra |
|---------|-------|
| **Clientes** | `tipo_cliente` ∈ {`PF`, `PJ`}; PK = `cod_cliente` |
| **Agências** | `tipo_agencia` ∈ {`Física`, `Digital`}; PK = `cod_agencia`; FK `cod_localidade` → `localidades` |
| **Contas** | `tipo_conta` ∈ {`PF`, `PJ`}; PK = `num_conta`; FKs → `clientes`, `agencias`, `colaboradores` |
| **Transações** | `nome_transacao` ∈ {`Saque`, `Depósito`, `Transferência`, `Pagamento`, `Tarifa`, `Rendimento`}; valor negativo = saída |
| **Propostas Crédito** | `status_proposta` ∈ {`Enviada`(0), `Aprovada`(1), `Recusada`(2), `Cancelada`(3), `Em análise`(4)}; `carencia` em meses |
| **Colaboradores** | Hierarquia via `cod_gerente` (auto-referência); alocação em agência via `colaborador_agencia` (N:N) |
| **Localidades** | `cod_localidade` PK; campos: `cidade`, `uf`, `regiao` |

---

## Integrações

| Serviço | Uso | Configuração |
|---------|-----|--------------|
| **Databricks** | Data Warehouse (target dbt) | `profiles.yml` → `type: databricks`; host, http_path, token, catalog, schema |
| **GitHub** | Versionamento + fork do template | Fork de `techindicium/banvic-dbt` |
| **Power BI** | Dashboard final (requisito do curso) | Conectar nos models `marts.*` (via SQL endpoint Databricks) |
| **Banco Central (SGS)** | Dados macro (ex: dólar) | Lib `python-bcb-sgs` no notebook; opcional |
| **Overleaf/LaTeX** | Relatório executivo final | Fora do repo; exportar PDF |

---

## Cuidados ao Editar

1. **Nunca commite `profiles.yml`** — fica em `~/.dbt/profiles.yml`
2. **Seeds desabilitadas por padrão** — `dbt_project.yml:41` tem `+enabled: false` para `banvic.*`; use `dbt seed -s <tabela>` ou habilite no YAML
3. **`generate_schema_name` macro** — prefixa schema com target em dev (`seu_usuario_dev_staging`); não edite sem entender
4. **Models triviais existentes** — `my_first_dbt_model` e `my_second_dbt_model` são exemplos; **substitua/remova** ao criar models reais
5. **`_seed_schema.yml`** — define tipos de colunas nas seeds; mantenha sincronizado com CSVs reais
6. **Databricks Community Edition** — tem limites (horas, cluster size); planeje `dbt run` em horários de baixo uso

---

## Como Validar Alterações

| Etapa | Comando/Verificação |
|-------|---------------------|
| **Syntax SQL** | `dbt parse` (falha se SQL inválido) |
| **Compilação** | `dbt compile --select <model>` → verifica `target/compiled/` |
| **Execução** | `dbt run --select <model>` → checa logs + `target/run/` |
| **Testes** | `dbt test --select <model>` → 0 falhas = OK |
| **Qualidade** | `dbt test` completo + `dbt docs generate` → revisa lineage |
| **Dados** | `dbt run-operation dbt_audit_helper.get_table_row_counts` (se tiver audit helper) |
| **Notebook** | Rodar células sequenciais; outputs consistentes; exportar CSV final para BI |

---

## Checklist de Entrega do Desafio Final

- [ ] Fork `techindicium/banvic-dbt` → clone local
- [ ] `profiles.yml` configurado + `dbt debug` OK
- [ ] `dbt seed` todas as 8 tabelas
- [ ] Models `staging/` (8) com testes
- [ ] Models `intermediate/` (joins/enriquecimento)
- [ ] Models `marts/` (facts + dims + KPIs) materializados como `table`
- [ ] `dbt test` passa 100%
- [ ] Dataset consolidado exportado para Power BI
- [ ] Dashboard Power BI publicado
- [ ] Relatório PDF (LaTeX/Overleaf) com insights + recomendações

---

## Referências Rápidas

- **Template oficial**: https://github.com/techindicium/banvic-dbt
- **dbt-databricks docs**: https://github.com/databricks/dbt-databricks
- **Databricks Community**: https://community.cloud.databricks.com/
- **Curso Indicium**: Materials no `Analytics Engineer Training 2026.md`

---

## Materiais do Curso (Oficiais + Resumos)

### Módulo 1 — Introdução à Análise de Dados
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `[FADA] Conteúdo - Módulo 01 - Introdução à Análise de Dados.docx.pdf` |
| **Oficial (MD)** | `[FADA] Conteúdo - Módulo 01 - Introdução à Análise de Dados.docx.md` |
| **Slides EN (PDF)** | `[FADA _ English] Slides - Introduction to data analysis.pptx.pdf` |
| **Slides EN (MD)** | `[FADA _ English] Slides - Introduction to data analysis.pptx.md` |
| **Resumo (seu)** | `resumo_modulo1.md` |
| **Decoreba (seu)** | `decoreba_modulo1.txt` |

### Módulo 2 — SQL
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `Conteúdo - Módulo 2 - SQL (1).pdf` |
| **Oficial (MD)** | `Conteúdo - Módulo 2 - SQL (1).md` |
| **Slides (PDF)** | `[Academy] Querying data with SQL - Slides.pptx.pdf` |
| **Slides (MD)** | `[Academy] Querying data with SQL - Slides.pptx.md` |
| **Resumo (seu)** | `Resumo_Modulo_2_SQL.md` |
| **Decoreba (seu)** | `Decoreba_SQL.txt` |

### Módulos Futuros (a preencher)
- Módulo 3 — *(a preencher)*
- Módulo 4 — *(a preencher)*
- ...

> **Índice consolidado** será mantido em `INDICE_MODULOS.md` (atualizado conforme novos módulos).