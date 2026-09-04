# Instalação — Toolkit Analytics Engineer

Guia para configurar o ambiente completo de Analytics Engineering usado neste repositório.

## Pré-requisitos

| Ferramenta | Versão | Download |
|------------|--------|----------|
| **Python** | 3.11+ | https://www.python.org/downloads/ |
| **Node.js** | 18+ | https://nodejs.org/ |
| **Git** | 2.x | https://git-scm.com/ |
| **VS Code Insiders** | latest | https://code.visualstudio.com/insiders/ |
| **Power BI Desktop** | latest | https://powerbi.microsoft.com/desktop/ |
| **OpenCode** | latest | https://opencode.ai/docs/ |

## 1. Python + dbt

```bash
# Criar ambiente virtual (opcional mas recomendado)
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instalar dbt para Databricks
pip install dbt-databricks

# Validar
dbt --version
```

## 2. Databricks Community Edition

1. Criar conta em https://community.cloud.databricks.com/
2. Criar cluster (Single Node, 8GB RAM, Python 3.11)
3. Criar catálogo `dev` com schemas: `erp_banvic`, `staging`, `intermediate`, `marts`
4. Gerar token: Settings → Developer → Access Tokens
5. Configurar `~/.dbt/profiles.yml`:
```yaml
default:
  target: dev
  outputs:
    dev:
      type: databricks
      catalog: dev
      schema: erp_banvic
      host: <seu-host>.cloud.databricks.com
      http_path: <seu-http-path>
      token: <seu-token>
```
6. Validar: `dbt debug`

> **NUNCA commite `profiles.yml`** — contém credenciais.

## 3. Power BI + PBIP

1. Instalar Power BI Desktop
2. Habilitar formato PBIP: Arquivo → Opções → Versão prévia → "Power BI Project (.pbip)"
3. Instalar extensão **Power BI Modeling MCP** no VS Code Insiders
4. Instalar CLIs de authoring:
```bash
npm install -g @microsoft/powerbi-report-author
```

## 4. OpenCode + MCP

1. Instalar OpenCode: https://opencode.ai/docs/
2. Configurar MCP em `~/.config/opencode/opencode.json` (ver `mcp/opencode-mcp-exemplo.json`):
```json
{
  "mcp": {
    "powerbi-modeling-mcp": {
      "command": [
        "C:\\Users\\SEU-USUARIO\\.vscode-insiders\\extensions\\analysis-services.powerbi-modeling-mcp-VERSAO-win32-x64\\server\\powerbi-modeling-mcp.exe",
        "--start"
      ],
      "enabled": true,
      "type": "local"
    }
  }
}
```
3. Ajustar `SEU-USUARIO` e `VERSAO` conforme sua máquina

## 5. Skills

### Skills do projeto (já no repo)
Estão em `skills/` e `.opencode/skill/`:
- `ae-fullflow` — fluxo AE completo
- `ae_materials_app` — sync de materiais
- `dbt-packages-tests` — lições dbt

### Skills Power BI (instalar manualmente)
```bash
# Clonar ou copiar para ~/.claude/skills/
# Disponíveis em: https://github.com/anthropics/skills (ou repositório da equipe)

# Essenciais para este workflow:
# - powerbi-report-authoring
# - powerbi-report-design
# - powerbi-report-planning
# - pbi-dax-create
# - pbi-doc
# - pbi-modelo-review
```

Ver `skills/README.md` para detalhes.

## 6. Verificação

```bash
# dbt
dbt debug

# Power BI CLI
powerbi-report-author --version

# OpenCode
opencode --version

# Git
git status
```

## Estrutura do Projeto

```
Formação AE/
├── skills/              # Skills versionadas (espelho de .opencode/skill/)
├── mcp/                 # Config e docs do MCP
├── INSTALACAO.md        # Este arquivo
├── AGENTS.md            # Guia do projeto + boas práticas
├── .opencode/skill/     # Skills ativas do OpenCode
├── DashboardTreinoBanvic.pbip  # Projeto Power BI
├── dados_treino/        # CSVs para Power BI
├── banvic-dbt/          # Projeto dbt (repo aninhado)
└── Módulo */            # Materiais do curso
```

## Próximos Passos

1. Ler `AGENTS.md` (guia do projeto)
2. Ler `skills/ae-fullflow/SKILL.md` (fluxo completo)
3. Configurar Databricks + dbt (`dbt debug` deve passar)
4. Explorar `DashboardTreinoBanvic.pbip` no Power BI Desktop
