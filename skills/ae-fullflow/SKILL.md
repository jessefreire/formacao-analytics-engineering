# Skill: Analytics Engineer Completo

> Fluxo ponta a ponta de um Analytics Engineer: Databricks → SQL → dbt → GitHub → Power BI → Figma/SVG → Tema JSON.

> **🔒 GUARDRAIL DE DADOS** — Só usar com dados fictícios/de treino ou com autorização explícita do cliente. Confirmar com a gestão antes de usar IA em projeto real.

## Quando usar

- Criar um dashboard completo do zero (dados → visual)
- Configurar ambiente dbt + Databricks
- Criar models dbt (staging/intermediate/marts)
- Construir relatório Power BI em formato PBIP
- Criar mockups SVG para backgrounds de relatório
- Gerar temas JSON personalizados para clientes
- Versionar e deployar projetos de dados

---

## Fluxo Completo do AE

### Fase 1: Infraestrutura & Dados

#### 1.1 Databricks Community Edition
```
1. Criar conta em community.cloud.databricks.com
2. Criar cluster (Python 3.11, Single Node, 8GB RAM mínimo)
3. Criar catálogo `dev` e schemas: erp_banvic, staging, intermediate, marts
4. Anotar: host, http_path, token (gerado via Settings → Developer → Access Tokens)
```

#### 1.2 dbt Core (local)
```bash
pip install dbt-databricks
dbt init banvic-dbt  # ou fork do template
dbt debug           # valida conexão
```

#### 1.3 profiles.yml (~/.dbt/profiles.yml)
```yaml
default:
  target: dev
  outputs:
    dev:
      type: databricks
      catalog: dev
      schema: "{{ env_var('DBT_SCHEMA') }}"
      host: <your-host>
      http_path: <your-http-path>
      token: <your-token>
```

### Fase 2: Modelagem dbt

#### 2.1 Convenções de Nomenclatura
| Camada | Prefixo | Materialização | Exemplo |
|--------|---------|----------------|---------|
| **Seeds** | Nome da tabela | table (via dbt seed) | `agencias.csv` → `erp_banvic.agencias` |
| **Staging** | `stg_` | view | `stg_erp__agencias` |
| **Intermediate** | `int_` | view | `int_dimensao_clientes` |
| **Marts** | `fact_` / `dim_` / `kpi_` | table | `fact_transacoes`, `dim_clientes` |

#### 2.2 Estrutura de um Model Staging
```sql
-- models/staging/erp_banvic/stg_erp__agencias.sql
with
    source as (
        select * from {{ source('erp_banvic', 'agencias') }}
    ),
    renamed as (
        select
            cod_agencia as pk_agencia,
            nome_agencia,
            tipo_agencia,
            cidade as cidade_agencia,
            uf as uf_agencia
        from source
    )
select * from renamed
```

#### 2.3 YAML de Testes (_schema.yml)
```yaml
version: 2
models:
  - name: stg_erp__agencias
    columns:
      - name: pk_agencia
        tests:
          - unique
          - not_null
      - name: tipo_agencia
        tests:
          - accepted_values:
              values: ['Física', 'Digital']
```

#### 2.4 Comandos Essenciais
```bash
dbt run --select staging           # roda toda camada staging
dbt test --select stg_erp__agencias  # testa model específico
dbt test                           # todos os testes
dbt docs generate && dbt docs serve  # documentação local
```

### Fase 3: Versionamento Git

#### 3.1 Convenções de Commit
```
feat: adicionar model dim_clientes
fix: corrigir join em int_fato_transacoes
refactor: extrair CTEs em stg_erp__contas
test: adicionar testes de accepted_values
docs: atualizar descrições no schema.yml
chore: sincronizar seeds
```

#### 3.2 .gitignore Essencial
```gitignore
target/
dbt_packages/
logs/
*.duckdb*
.venv/
```

### Fase 4: Power BI (PBIP)

#### 4.1 Formato PBIP
```
Projeto.pbip              # Arquivo de projeto
Projeto.Report/           # Relatório
  definition/
    report.json           # Tema e config
    pages/
      <page-id>/
        page.json         # Canvas e background
        visuals/
          <visual-id>/
            visual.json   # Config do visual
  StaticResources/
    RegisteredResources/  # SVGs de fundo
    SharedResources/      # Temas
Projeto.SemanticModel/    # Modelo semântico
  definition/
    tables/               # Tabelas TMDL
    relationships.tmdl    # Relacionamentos
    model.tmdl            # Config do modelo
```

#### 4.2 Canvas Padrão
- **Tamanho**: 1280×720 (padrão Power BI)
- **SVGs**: `viewBox="0 0 1280 720"`
- **Background**: Scaling=`Fill`, Transparency=0

#### 4.3 Temas
- **Recomendado**: Storm (para build 2.155+ — renderiza cardVisual)
- **Evitar**: Fluent2-CY26SU08 (quebra cards)
- **Custom theme**: `SharedResources/BuiltInThemes/TemaCliente.json`

#### 4.4 Visuais — Boas Práticas
| Elemento | Configuração |
|----------|-------------|
| **Slicers** | `syncGroups` para sincronização cross-page |
| **Cards** | `cardVisual` para KPIs, sem label (título no SVG) |
| **Botões** | `actionButton` tipo `PageNavigation`, 100% transparentes |
| **Gráficos** | Cores do tema do cliente, sem gridlines desnecessários |
| **Medidas** | Tabela calculada `Medidas` para agrupamento |

#### 4.5 Guardrails Críticos
1. **NUNCA remover backgrounds** sem pedido explícito
2. **Fechar Desktop** antes de editar JSON externamente
3. **Salvar após cada lote MCP** (memória é volátil)
4. **Refresh de dados** = sempre no Desktop (MCP não executa)
5. **SVG hardcoded** =.Static timestamp no SVG; usar card dinâmico

### Fase 5: Mockups SVG

#### 5.1 Estrutura de um SVG de Fundo
```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
  <defs>
    <filter id="sh">...</filter>  <!-- Sombra -->
  </defs>
  <rect width="1280" height="720" fill="#EDF1F5"/>  <!-- Canvas -->
  <rect width="1280" height="64" fill="#0F7E8C"/>   <!-- Header -->
  <!-- Logo, título, chips, filtros, painéis -->
</svg>
```

#### 5.2 Convenções de Design
| Elemento | Cor | Posição |
|----------|-----|---------|
| **Canvas** | `#EDF1F5` (cinza claro) | Fundo todo |
| **Header** | `#0F7E8C` (teal) | y=0, h=64 |
| **Painéis** | `#FFFFFF` com sombra | rx=8, filter=url(#sh) |
| **Filtros** | `#FFFFFF` com sombra | Abaixo do header |
| **Chips** | Branco (ativo) / Translucido (inativo) | No header, à direita |
| **Relógio** | Ícone + timestamp | No header, antes dos chips |

#### 5.3 Fluxo de Criação
1. Desenhar mockup no Figma (ou caneta no SVG direto)
2. Exportar como SVG otimizado
3. Colocar em `StaticResources/RegisteredResources/`
4. Referenciar no `page.json` → `objects.background`
5. Posicionar visuais Power BI sobre as áreas do SVG

### Fase 6: Tema JSON para Clientes

#### 6.1 Estrutura Básica
```json
{
  "name": "TemaCliente",
  "dataColors": [
    "#0F7E8C",
    "#1A3A44",
    "#4E6E77",
    "#A8C5D0",
    "#EDF1F5"
  ],
  "textClasses": {
    "title": { "fontSize": 14, "fontFace": "Segoe UI", "color": "#1A3A44" },
    "label": { "fontSize": 11, "fontFace": "Segoe UI", "color": "#4E6E77" }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background": [{ "color": { "solid": { "color": "#FFFFFF" } } }],
        "border": [{ "show": true, "color": "#E0E0E0" }],
        "title": [{ "show": true, "fontSize": 13, "fontColor": "#1A3A44" }]
      }
    }
  }
}
```

#### 6.2 Paleta de Cores
- **Primária**: Cor principal do cliente (ex: teal BanVic)
- **Secundária**: Tons complementares para gráficos
- **Neutra**: Cinzas para fundo, bordas, texto
- **Status**: Verde (positivo), Vermelho (negativo), Amarelo (atenção)

#### 6.3 Aplicação
1. Salvar como `TemaCliente.json` em `StaticResources/SharedResources/BuiltInThemes/`
2. Referenciar no `report.json` → `theme.name`
3. Ou importar via Power BI Desktop → Visualizar → Temas → Navegar

### Fase 7: Style Guide & Páginas Ocultas

> **PADRÃO OBRIGATÓRIO:** todo relatório Power BI deve ter N páginas visíveis + 2 ocultas: **Style Guide** (cores + tipografia) e **Theme JSON** (tema copiável). Isso garante consistência visual e reuso entre relatórios do mesmo cliente.

#### 7.1 Auditoria de Estilos
Antes de criar o Style Guide, auditar todos os visuais:
```python
# Coletar de cada visual.json:
# - fontSize (em objects.value.properties.fontSize)
# - fontColor (em objects.value.properties.fontColor)
# - fontFace (em objects.value.properties.fontFamily)
# - Cores de dataPoint (em objects.dataPoint.properties.fill)
```

#### 7.2 Página Style Guide (ocultar via UI após criar)
> O campo correto é `"visibility": "HiddenInViewMode"` no `page.json` — `isHidden` NÃO existe no schema. Ocultar via Desktop (botão direito → Ocultar página) grava esse campo; escrevê-lo direto no JSON também funciona.

- **SVG de fundo**: header teal + 2 painéis brancos (Cores | Tipografia), mesmo estilo do dashboard
- **Cores**: `shape` (retângulo) com `fill` da cor + `textbox` ao lado com hex + descrição. NÃO usar `cardVisual` vazio (não renderiza).
- **Tipografia**: `textbox` com amostra de cada tamanho + uso
- **Nomes de visuais**: nunca vazios (usar ID da pasta), 1-50 caracteres

#### 7.3 Página Theme JSON (ocultar via UI após criar)
- **SVG de fundo**: header + 1 painel branco grande
- **Conteúdo**: `textbox` com instruções + JSON do tema (fonte Consolas) + resumo de cores/fontes
- **Textbox correto**: `paragraphs` como **array nativo** (não embrulhar em `expr`). Ver `powerbi-report-authoring/references/textbox.md`:
```json
"objects": {
  "general": [{
    "properties": {
      "paragraphs": [{
        "textRuns": [{
          "value": "texto aqui",
          "textStyle": {"fontFamily": "Segoe UI", "fontSize": "12px", "color": "#1F4858"}
        }],
        "horizontalTextAlignment": "left"
      }]
    }
  }]
}
```
- **Border**: só `show` e `color`. Propriedade `weight` é inválida.

#### 7.4 Padrões BanVic (referência)
| Elemento | Valor |
|----------|-------|
| **Canvas** | 1280×720 |
| **Cor primária** | `#0F7E8C` |
| **Cor secundária** | `#235362` |
| **Cor terciária** | `#1F4858` |
| **Texto** | `#4E6E77` |
| **Fundo** | `#EDF1F5` |
| **Painéis** | `#FFFFFF` |
| **Fonte KPI** | 24px, Segoe UI, #235362 |
| **Fonte eixo** | 9px, Segoe UI, #4E6E77 |
| **Fonte data** | 10px, Segoe UI |

---

## Checklist de Projeto AE

- [ ] Databricks configurado (cluster, catálogo, schemas)
- [ ] dbt profiles.yml configurado (nunca committar)
- [ ] Seeds carregadas (dbt seed)
- [ ] Models staging criados com testes
- [ ] Models intermediate criados (joins/enriquecimento)
- [ ] Models marts criados (facts + dims)
- [ ] dbt test 100% passando
- [ ] Dados exportados para CSV/Power BI
- [ ] PBIP criado (Report + SemanticModel)
- [ ] SVGs de fundo criados (1280×720)
- [ ] Tema do cliente configurado
- [ ] Visuais posicionados sobre SVGs
- [ ] Slicers sincronizados cross-page
- [ ] Navegação por chips configurada
- [ ] Medidas DAX criadas
- [ ] Página Style Guide criada (cores + tipografia)
- [ ] Página Theme JSON criada (copiável)
- [ ] Páginas ocultas via UI do Desktop
- [ ] Commit git realizado
- [ ] Dashboard validado no Desktop

---

## Referências

- **dbt docs**: https://docs.getdbt.com/
- **Databricks Community**: https://community.cloud.databricks.com/
- **Power BI PBIP**: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview
- **SVG spec**: https://www.w3.org/TR/SVG/
- **Tema Power BI**: https://learn.microsoft.com/en-us/power-bi/desktop-report-themes
