# Skills do Projeto

> Mapa completo (skills do projeto, de Power BI, as criadas no desafio e o MCP):
> [`../SKILLS_E_MCP.md`](../SKILLS_E_MCP.md)

Skills versionadas neste repositório para uso com qualquer IDE com IA (Claude Code, OpenCode).

## Skills Incluídas

| Skill | Descrição | Uso |
|-------|-----------|-----|
| **ae-fullflow** | Fluxo ponta a ponta do Analytics Engineer | Databricks → SQL → dbt → GitHub → Power BI → SVG → Tema JSON |
| **ae_materials_app** | Auto-sync dos materiais do curso | Sincroniza `index.html` com novos arquivos |
| **dbt-packages-tests** | Lições de packages e testes dbt | `dbt_utils`, testes genéricos, erros comuns |

### Criadas a partir do desafio Adventure Works

Ativas como globais em `~/.claude/skills/`; aqui fica a cópia versionada.

| Skill | Descrição | Uso |
|-------|-----------|-----|
| **databricks-ingestao** | Carga da camada bruta a partir do DDL | `read_files` idempotente, tipos certos, 5 conferências |
| **dbt-modelagem-dimensional** | Decisões de modelo dimensional | grão da fato, ponte N:N com `allocation_factor`, membros `-1` |
| **pbi-mockup-design** | Mockup do dashboard antes do Power BI | canvas `/design`, 1280px, fundos SVG, interação → objeto do PBI |
| **pbi-licoes-pbir** | Armadilhas de Power BI e a correção | RANKX, field parameters, PBIR, caminho longo |
| **reconciliacao-numeros** | Bater o número em SQL, dbt e DAX | investigar divergência e filtro vazio |
| **pbi-apresentacao** | Dashboard em tela cheia sem a interface do Desktop | gravar ou apresentar sem Power BI Service |
| **entrega-a-partir-do-briefing** | Montar e conferir o pacote de entrega | "pede × onde está", PDFs, links públicos, ZIP |
| **pbi-raio-x** | Raio-X do modelo Power BI | nota, achados, dependências e impacto das medidas — tela Raio-X |
| **estudo-video** | Vídeo do YouTube vira resumo da formação | resumo em palavras próprias, com momentos e links com tempo |

A `pbi-mockup-design` ganhou o modo **entrevista → levantamento → mockup**
(`references/levantamento.md` e `templates/levantamento.md`).

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
