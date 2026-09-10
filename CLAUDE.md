# CLAUDE.md — Formação Analytics Engineer (Indicium)

> Guia de contexto para Claude Code. Para detalhes completos, ler `AGENTS.md`.

> **🔒 GUARDRAIL DE DADOS** — Só usar este toolkit com dados fictícios/de treino ou com autorização explícita do cliente. Confirmar com a gestão antes de usar IA em projeto real.

## Projeto

Repositório de formação em Analytics Engineering: curso Indicium (módulos 0-9), projeto dbt BanVic (Databricks), dashboard Power BI (PBIP) e toolkit de skills.

## Arquivos de Referência (ler quando relevante)

| Arquivo | Quando ler |
|---------|------------|
| `AGENTS.md` | SEMPRE no início — arquitetura, convenções, guardrails, checklist |
| `INSTALACAO.md` | Setup de ambiente (Python, dbt, Databricks, PBI, MCP) |
| `skills/ae-fullflow/SKILL.md` | Fluxo AE ponta a ponta (Databricks → Power BI) |
| `skills/dbt-packages-tests/SKILL.md` | Erros comuns dbt e como resolver |
| `Analytics Engineer Training 2026.md` | Diário de bordo do curso |

## Skills do Projeto (`.claude/skills/`)

- `ae-fullflow` — fluxo completo do Analytics Engineer
- `ae_materials_app` — sync de materiais do curso
- `dbt-packages-tests` — lições dbt

## Skills Power BI (`~/.claude/skills/`, globais)

- `powerbi-report-authoring` — criar/editar PBIR (ler `SKILL.md` + `references/textbox.md` antes de mexer em textbox)
- `powerbi-report-design` — direção visual
- `powerbi-report-planning` — planejamento de relatórios
- `pbi-dax-create`, `pbi-doc`, `pbi-modelo-review` — DAX, docs, auditoria

## MCP

`powerbi-modeling-mcp` — modelagem semântica (tabelas, medidas, relações, DAX). Ver `.mcp.json` e `mcp/README.md`.

## Convenções de SQL

Além do code style da Indicium (`Desafio/indicium-code-style/`, sqlfluff 1.4.5), vale
neste repositório:

1. **Nenhuma query sem comentário.** O comentário declara **o que se confere**, **o que
   se espera ver** e **por que importa**. Em consulta de verificação, declara também
   **o que fazer se divergir**.
2. **Valor esperado dentro do SQL.** Quando existe um número de referência, ele entra
   como coluna `esperado` e o próprio SQL calcula uma coluna `resultado` (`ok`/`DIVERGE`).
   Quem roda não deveria precisar saber de cor qual é o número certo.
3. Vale para arquivo versionado, célula de notebook e SQL colado no chat.

## Guardrails Críticos (Power BI)

1. **NUNCA remover backgrounds/SVGs** sem pedido explícito
2. **Fechar Desktop sem salvar** antes de editar JSON externamente
3. **Salvar após cada lote MCP** (memória é volátil)
4. **Canvas 1280×720**, tema Storm (Fluent2 quebra cards)
5. **Ocultar página**: campo `visibility: HiddenInViewMode` no page.json (`isHidden` não existe)
6. **Textbox**: `paragraphs` como array nativo (ver skill textbox.md)
