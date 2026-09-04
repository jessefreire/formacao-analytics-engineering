# Skills do Projeto

Skills versionadas neste repositório para uso com OpenCode e Claude Code.

## Skills Incluídas

| Skill | Descrição | Uso |
|-------|-----------|-----|
| **ae-fullflow** | Fluxo ponta a ponta do Analytics Engineer | Databricks → SQL → dbt → GitHub → Power BI → SVG → Tema JSON |
| **ae_materials_app** | Auto-sync dos materiais do curso | Sincroniza `index.html` com novos arquivos |
| **dbt-packages-tests** | Lições de packages e testes dbt | `dbt_utils`, testes genéricos, erros comuns |

## Como Usar

### OpenCode
As skills em `.opencode/skill/` são carregadas automaticamente. Esta pasta `skills/` é um espelho para compartilhamento — copie para `.opencode/skill/` ou referencie diretamente.

### Claude Code
Copie a pasta da skill para `~/.claude/skills/`:
```bash
cp -r skills/ae-fullflow ~/.claude/skills/
```

## Skills Externas (não versionadas)

Estas skills são referenciadas mas moram fora do repo:

### Power BI (`~/.claude/skills/`)
- `powerbi-report-authoring` — criar/editar PBIR via CLI
- `powerbi-report-design` — direção visual
- `powerbi-report-planning` — planejamento de relatórios
- `pbi-dax-create` — criar medidas DAX
- `pbi-doc` — documentar PBIP
- `pbi-modelo-review` — auditar modelo

### Outras
- `candidatar`, `lighthouse-correcao`, `mobile-first`, etc.

Ver `INSTALACAO.md` na raiz para guia completo de setup.
