# Skills do Projeto

Skills versionadas neste repositório para uso com qualquer IDE com IA (Claude Code, OpenCode).

## Skills Incluídas

| Skill | Descrição | Uso |
|-------|-----------|-----|
| **ae-fullflow** | Fluxo ponta a ponta do Analytics Engineer | Databricks → SQL → dbt → GitHub → Power BI → SVG → Tema JSON |
| **ae_materials_app** | Auto-sync dos materiais do curso | Sincroniza `index.html` com novos arquivos |
| **dbt-packages-tests** | Lições de packages e testes dbt | `dbt_utils`, testes genéricos, erros comuns |

## Como Usar

As skills já estão ativas em `.claude/skills/` (Claude Code) e `.opencode/skill/` (OpenCode). Esta pasta `skills/` é o espelho canônico para compartilhamento.

Para uso global (fora deste projeto), copie para `~/.claude/skills/`:
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
