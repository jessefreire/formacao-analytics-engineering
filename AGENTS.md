# AGENTS.md — Formação Analytics Engineer (Indicium)

> **⚠️ DOCUMENTO VIVO** — Este arquivo, `INDICE_MODULOS.md` e `Analytics Engineer Training 2026.md` devem ser **atualizados automaticamente** a cada nova conversa com agentes, novo material do curso ou mudança estrutural no projeto. Não deixe para depois.

> Guia persistente para sessões futuras. Atualize quando houver mudanças estruturais.

> **🔒 GUARDRAIL DE DADOS** — As ferramentas de IA deste toolkit (agentes, MCPs, skills) só devem ser usadas com **dados fictícios/de treino** (como o BanVic) ou quando o **cliente autorizar explicitamente** o uso de IA sobre seus dados. Antes de usar em projeto real, o Engenheiro **deve confirmar com a gestão** se o uso de IA foi aprovado. Nunca envie dados sensíveis, PII ou informações confidenciais para modelos de IA sem autorização formal.

---

## Arquitetura do Projeto

```
Formação AE/                        # ← Repositório git local (commit "chore: sync")
├── AGENTS.md                    # Este arquivo
├── Analytics Engineer Training 2026.md   # Diário de bordo do curso
├── GUIA_DBT_BANVIC.md           # Guia prático dbt (local vs Cloud)
├── INDICE_MODULOS.md            # Índice consolidado de módulos
├── .gitignore                   # Exclui *.pdf, *.zip, Desafio/referências, .agents/
├── .claude/settings.local.json  # Permissões da IDE com IA
├── index.html                   # App de visualização de materiais (design Apple)
├── files.json                   # Manifest gerado pelo sync
├── server.py                    # Servidor local (http://localhost:8765)
├── .opencode/
│   └── skill/
│       ├── ae_materials_app/      # Skill de auto-sync (templates + sync.py)
│       └── dbt-packages-tests/    # Skill de lições: packages, testes dbt_utils, erros comuns
├── Módulo 0 - Banco de Dados BanVic/   # Referência do banco BanVic (visão geral, schema, queries)
├── Módulo 1 -  Introdução à Análise de Dados/   # Oficial + resumo + decoreba + EN
├── Modulo 2 - SQL para Análise de Dados/        # Oficial + resumo + decoreba + EN
├── Módulo 3 - Modelagem de dados/              # Oficial + EN
├── Módulo IV - Engenharia de Dados (dbt/Snowflake)/  # Oficial + EN
├── Módulo 4 - Storytelling com Dados/           # Oficial + EN
├── Módulo 5 - Design de Experiência/            # Apostila + EN
├── Módulo 6 - Dashboards com Power BI/          # Oficial + EN
├── Módulo 7 - Estatística aplicada/             # Oficial + EN
├── Módulo 8 - Python/                           # Oficial + EN
├── Módulo 9 - AI-Powered Productivity/         # Módulo oficial do curso (a preencher)
├── Extra - Curso SQL Completo (YouTube)/       # FORA da grade oficial: Curso SQL (Dev Aprender) + Northwind (CSVs prontos p/ Databricks/Neon) + AdventureWorks (.bak p/ extrair via Docker)
├── Desafio/
│   ├── desafio-banvic-an-lise-de-dados-2024.ipynb
│   └── Exemplos repo banvic/    # Referências de terceiros (NÃO versionar)
├── banvic-dbt/                 # ← Fork de techindicium/banvic-dbt (repo git próprio, aninhado)
│   ├── dbt_project.yml
│   ├── models/ (staging/ intermediate/ marts/)
│   ├── seeds/banvic/            # 8 CSVs (vêm do template)
│   ├── macros/, tests/
│   └── profiles.yml             # FORA do repo (~/.dbt/profiles.yml)
```

**Seu projeto real** = fork de `https://github.com/techindicium/banvic-dbt` clonado localmente em `banvic-dbt/` (repo git próprio, aninhado; ignorado pelo repo do curso via `.gitignore`).
**App de materiais** = local, sem build. Sempre abrir via `http://localhost:8765` (não `file://`, por CORS). Sync: `python .opencode/skill/ae_materials_app/sync.py` (o alias moderno `python -m ae_materials_app.sync` NÃO funciona — module fora do path).

> ⚠️ **Fora do git (copiar à mão ao trocar de máquina):** `Extra - Curso SQL Completo (YouTube)/AdventureWorks2017.bak` e `AdventureWorks2025.bak` (~48 MB cada) estão no `.gitignore` (`*.bak`) de propósito. `bancoNorthwind.txt` (1 MB) e tudo mais ESTÁ versionado. Se o usuário estiver configurando uma máquina nova, só esse `.bak` precisa ser copiado manualmente (pendrive/Drive); todo o resto vem do clone. Ao converter o `.bak` para CSV/Databricks (guia em `carregar_bancos.md`), pode descartar o `.bak` se quiser liberar espaço.

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
- **Sidebar**: colapsa/recolhe via botão `⟨/⟩` no header (mesmo tamanho do toggle de tema, 32×32) ou `Ctrl+B`. Estado persistido em `localStorage`.
  - **Recolhida** (`data-sidebar-collapsed="true"`): vira um rail estreito (64px) com **chips** por módulo (nº do módulo ou `●` p/ Config). Clicar num chip **navega pro 1º material do módulo sem expandir**.
  - Arrastar o handle da borda direita (zona de 12px) **expande** (arrastando pra direita) ou **recolhe** (pra esquerda) — usa `pointermove`/`pointerup` + `setPointerCapture`.
  - Scroll fica no `.nav`, não na `.sidebar` (pra scrollbar não tampar o handle).
- **Navegação de materiais**: barra **flutuante fixa** no rodapé (`.file-nav`) com **‹ Anterior** e **Próximo**, cada um ocupando ~50% da largura. O botão sem vizinho some (`:disabled { display:none }`). Atalhos `←`/`→` no teclado. No mobile fica compacto (só setas).
- **Servidor**: `python server.py` (porta 8765, abre navegador, header CORS)
- **Sync**: `python .opencode/skill/ae_materials_app/sync.py` regenera `FILES` + `files.json`

---

## Dois Ambientes dbt (importante não confundir)

O projeto roda em **dois lugares diferentes**, e só um deles está conectado nesta máquina:

| Ambiente | Onde | Status local | Para que serve |
|---|---|---|---|
| **dbt Cloud + Databricks** | `cloud.getdbt.com` + workspace Databricks | ❌ **não conectado localmente** | Foi o ambiente das aulas; onde saiu o 61/61 de testes |
| **dbt Core + DuckDB** | `banvic-dbt/dev.duckdb` (target `local`) | ✅ ativo | É o que gera os CSVs que alimentam o dashboard |

**Fluxo real do dashboard hoje** (não passa por Databricks):

```
banvic-dbt/  ──dbt build --target local──>  dev.duckdb
                                                │
                        python export_marts_local.py
                                                │
                                                v
                              dados_treino/*.csv (4 marts)
                                                │
                                                v
                        DashboardTreinoBanvic.pbip (param PastaDados)
```

- `dev.duckdb` está no `.gitignore` (`*.duckdb*`) — é artefato local, reconstruível com `dbt build --target local`.
- Adapters instalados: `dbt-databricks` **e** `dbt-duckdb`. O target default é `local` (DuckDB).
- Os CSVs em `dados_treino/` foram gerados por `export_marts_local.py` — ver o script para a lista de tabelas exportadas.
- **Consequência prática:** mudança de model só chega no dashboard depois de `dbt build --target local` + `python export_marts_local.py` + refresh no Desktop.

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

### Power BI (PBIP + MCP/skills) — guardrails duramente aprendidos
- **NUNCA remover `objects.background` (tela de fundo) nem arquivos de `StaticResources/RegisteredResources` sem pedido explícito.** O Desktop faz garbage-collection de recursos "não usados" no save — remover o fundo temporariamente (ex: para debug) **apaga o SVG e o registro de forma irreversível**. Debug visual sem mexer no fundo.
- **Edição externa × Desktop aberto:** o Desktop guarda cópia própria das consultas Power Query. Editar partições M via XMLA com sessão aberta causa conflito (erro de referência cíclica no refresh). Regra: **M via arquivos TMDL com o Desktop fechado** (ou edite na UI); refresh sempre no Desktop; MCP só para o resto (tipos, colunas, relações, medidas, auditoria).
- **Refresh via MCP não executa no Desktop** (silent no-op). Refresh de dados = sempre no Desktop.
- **Deleção de arquivos `.Report` com Desktop aberto ressuscita no save.** Deletar visual = com Desktop fechado + reload antes de qualquer save (ou apague pela UI).
- **Salvar após cada lote MCP** (medidas, colunas): objetos criados via XMLA vivem só na memória — kill/fechamento sem save perde tudo (caso real: tabela `Medidas` inteira perdida).
- **Tema Storm nos relatórios de treino** (padrão da aula): o tema base Fluent2 (build 2.155) não renderiza `cardVisual` (cards em branco); Storm renderiza. Suspeita também para outros arquivos com big numbers apagados.

### Power BI Dashboard — boas práticas (construção BanVic)
- **Canvas padrão**: 1280×720 (não 1920×1080). SVGs de fundo devem ter `viewBox="0 0 1280 720"`.
- **SVG backgrounds**: criam a identidade visual (header, filtros, painéis). Power BI visuals ficam por cima com preenchimento/borda transparentes.
- **Navegação por chips**: botões `actionButton` tipo `PageNavigation` com `fill.show=false`, `text.show=false`, `outline.show=false`, `border.show=false`. Posicionados exatamente sobre os chips SVG (só captam clique).
- **Sincronização de slicers cross-page**: configurar `syncGroups` em `filtersState` para manter filtros sincronizados entre páginas.
- **Cards de data dinâmica**: card `cardVisual` posicionado sobre área do timestamp no SVG (mostra hora real, nunca hardcoded no SVG).
- **Medidas**: criar tabela calculada `Medidas` para agrupar todas as DAX measures. Formato `0.00` ou `0.00%` conforme tipo.
- **Colunas renomeadas**: renomear no model (TMDL) para nomes amigáveis (`nome_agencia` → `Nome da Agência`). CSVs mantêm nomes originais.
- **Relacionamentos**: `BothDirections` seguro quando há apenas1 fact table (filtra dim ↔ fact bidirecionalmente).
- **Edição externa × Desktop**: ao editar JSON externamente, **fechar Desktop sem salvar** e reabrir para carregar mudanças.
- **Caminho dos CSVs = parâmetro M `PastaDados`** (`SemanticModel/definition/expressions.tmdl`). As 4 partições fazem `File.Contents(PastaDados & "arquivo.csv")` — ao trocar de máquina, editar **um** valor (Desktop → Transformar dados → Gerenciar parâmetros) em vez de 4 partições.
- **Parâmetro M em TMDL: NÃO precisa de `ref expression` no `model.tmdl`.** Basta criar `definition/expressions.tmdl`; o Desktop descobre sozinho e, no save, **remove** o `ref expression` que você tiver escrito e registra o nome no `annotation PBI_QueryOrder`. Confirmado no save de 04/09/2026 — o parâmetro e as 4 partições sobreviveram intactos.
- **`activePageName` inválido o Desktop autocorrige.** Apontava para "Theme JSON" (página oculta) e no save virou o ID da Visão Geral. A doc classifica como erro *não-bloqueante* de autofix — não vale gastar esforço corrigindo à mão.
- **`pageOrder` usa o `name` da página, não o nome da pasta.** O schema `pagesMetadata` diz "(page names)". Pasta ≠ `name` é suportado e o Desktop preserva. Ferramentas externas (ex: `powerbi-report-author validate`) sinalizam isso como erro — é **falso positivo**, não "conserte".
- **Tema embutido (Storm) declarado como `SharedResources` é correto.** O validador exige `RegisteredResources` para tema customizado; tema embutido que o Desktop copia para `BuiltInThemes/` fica em `SharedResources` mesmo. Outro falso positivo — não mexer.
- **Páginas ocultas**: o campo é `"visibility": "HiddenInViewMode"` no `page.json` (`isHidden` NÃO existe no schema). Ocultar via UI do Desktop (botão direito → Ocultar página) grava esse campo; escrevê-lo à mão também funciona. Ver as páginas Style Guide e Theme JSON como referência.
- **Textbox estático**: usar tipo `textbox` com `paragraphs` como **array nativo** (não embrulhar em `expr`). Ver `powerbi-report-authoring/references/textbox.md`.
- **Swatches de cor**: usar tipo `shape` (retângulo) com `fill` da cor. `cardVisual` vazio não renderiza.
- **Nomes de visuais**: nunca vazios, 1-50 caracteres. Usar ID da pasta.
- **Border**: propriedade `weight` é inválida. Só `show`, `color`.

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

- [x] Fork `techindicium/banvic-dbt` → clone local (`jessefreireufc/banvic-dbt`)
- [x] Ambiente dbt Cloud configurado (Databricks free + catálogo `dev` + ambiente Development) — `dbt debug` OK no Studio; ver `SETUP_AMBIENTE_AULAS.md`
- [x] `dbt seed` todas as 8 tabelas (em `dev.erp_banvic`, via dbt Cloud, 24/08/2026)
- [x] Models `staging/` (8) com testes
- [x] Models `intermediate/` (joins/enriquecimento)
- [x] Models `marts/` (facts + dims + KPIs) materializados como `table`
- [x] `dbt test` passa 100% — **38/38 no local (DuckDB, medido em 04/09/2026)**; o 61/61 registrado antes veio do dbt Cloud/Databricks e o local não reproduz esse número (contagens de teste diferentes entre os dois ambientes; a divergência não foi investigada)
- [x] Dataset consolidado exportado para Power BI (4 CSVs em `dados_treino/`)
- [x] Dashboard Power BI publicado (2 páginas, 22 visuais, PBIP format)
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
| **Slides EN (PDF)** | `[Academy] Querying data with SQL - Slides.pptx.pdf` |
| **Slides EN (MD)** | `[Academy] Querying data with SQL - Slides.pptx.md` |
| **Resumo (seu)** | `Resumo_Modulo_2_SQL.md` |
| **Decoreba (seu)** | `Decoreba_SQL.txt` |

### Módulo 3 — Modelagem de dados
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `[FADA] Conteúdo - Módulo 3 - Modelagem de dados.docx.pdf` |
| **Oficial (MD)** | `[FADA] Conteúdo - Módulo 3 - Modelagem de dados.docx.md` |
| **Slides EN (PDF)** | `[English _ FADA] Módulo 3 - Modelagem de dados.pptx.pdf` |
| **Slides EN (MD)** | `[English _ FADA] Módulo 3 - Modelagem de dados.pptx.md` |

### Módulo IV — Engenharia de Dados com dbt e Snowflake
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `[FEA] Conteúdo - Módulo IV - Engenharia de Dados com dbt e Snowflake.pdf` |
| **Oficial (MD)** | `[FEA] Conteúdo - Módulo IV - Engenharia de Dados com dbt e Snowflake.md` |
| **Slides EN (PDF)** | `[Academy] EN-US - Asynchronous FEA - Analytics Engineering Class with dbt and Snowflake.pptx.pdf` |
| **Slides EN (MD)** | `[Academy] EN-US - Asynchronous FEA - Analytics Engineering Class with dbt and Snowflake.pptx.md` |

### Módulo 4 — Storytelling com Dados
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `Conteúdo - Módulo 4 - Storytelling com Dados.docx.pdf` |
| **Oficial (MD)** | `Conteúdo - Módulo 4 - Storytelling com Dados.docx.md` |
| **Slides EN (PDF)** | `[English _ FADA] Módulo 4 - Storytelling com Dados.pptx.pdf` |
| **Slides EN (MD)** | `[English _ FADA] Módulo 4 - Storytelling com Dados.pptx.md` |

### Módulo 5 — Design de Experiência
| Tipo | Arquivo |
|------|---------|
| **Apostila (PDF)** | `[FADA] - APOSTILA - Módulo 5 - Design de Experiência.docx.pdf` |
| **Apostila (MD)** | `[FADA] - APOSTILA - Módulo 5 - Design de Experiência.docx.md` |
| **Slides EN (PDF)** | `Copy of [FADA] Módulo 5 - Design de Experiência.pptx.pdf` |
| **Slides EN (MD)** | `Copy of [FADA] Módulo 5 - Design de Experiência.pptx.md` |

### Módulo 6 — Dashboards com Power BI
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `Conteúdo - Módulo 6 - Criando dashboards com Power BI.docx.pdf` |
| **Oficial (MD)** | `Conteúdo - Módulo 6 - Criando dashboards com Power BI.docx.md` |
| **Slides EN (PDF)** | `[English _ FADA] - Módulo 6 - Criando dashboards com Power BI.docx.pptx.pdf` |
| **Slides EN (MD)** | `[English _ FADA] - Módulo 6 - Criando dashboards com Power BI.docx.pptx.md` |

### Módulo 7 — Estatística aplicada à análise de dados
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `[FADA] Conteúdo - Módulo 7 - Estatística aplicada à análise de dados.docx.pdf` |
| **Oficial (MD)** | `[FADA] Conteúdo - Módulo 7 - Estatística aplicada à análise de dados.docx.md` |
| **Slides EN (PDF)** | `Copy of [FADA] Módulo 7 - Estatística aplicada à análise de dados.pptx.pdf` |
| **Slides EN (MD)** | `Copy of [FADA] Módulo 7 - Estatística aplicada à análise de dados.pptx.md` |

### Módulo 8 — Python
| Tipo | Arquivo |
|------|---------|
| **Oficial (PDF)** | `[FADA] Conteúdo - Módulo 8 - Python.pdf` |
| **Oficial (MD)** | `[FADA] Conteúdo - Módulo 8 - Python.md` |
| **Slides EN (PDF)** | `[English _ FADA] Módulo de Python.pptx.pdf` |
| **Slides EN (MD)** | `[English _ FADA] Módulo de Python.pptx.md` |