# CLAUDE.md — Formação Analytics Engineer (Indicium AI)

> Guia de contexto para Claude Code. Para detalhes completos, ler `AGENTS.md`.

> **🔒 GUARDRAIL DE DADOS** — Só usar este toolkit com dados fictícios/de treino ou com autorização explícita do cliente. Confirmar com a gestão antes de usar IA em projeto real.

## Projeto

Repositório de formação em Analytics Engineering: curso Indicium AI (módulos 0-9), projeto dbt BanVic (Databricks), dashboard Power BI (PBIP) e toolkit de skills.

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

Além do code style da Indicium AI (`Desafio/indicium-code-style/`, sqlfluff 1.4.5), vale
neste repositório:

1. **Nenhuma query sem comentário**, incluindo as colocadas no chat. Uma ou duas linhas
   acima da consulta dizendo **o que se confere** e **qual o valor esperado**.
2. **Comentário curto.** O objetivo é entender a consulta de relance. Explicação longa
   vira parágrafo antes de rodar e atrapalha mais do que ajuda — se o contexto for
   grande, ele vai para o `.md` ou para a célula de markdown, não para dentro do SQL.
3. Não inflar a consulta para acomodar a conferência. Colunas `esperado`/`resultado`
   calculadas no SQL cabem em script de verificação dedicado (ver
   `03-verificacao-da-carga.sql`), não em consulta de conferência rápida.

## Convenções de Português

1. **Prosa em português leva acento** — comentário, docstring, markdown de célula,
   título de célula (`DBTITLE`), README e documento de entrega inclusive. Não há
   restrição técnica: os arquivos são UTF-8 e o Databricks executa acento sem
   problema.
2. **Identificador fica em ASCII** — nome de variável, função, alias de SQL, nome de
   tabela e de coluna, e nome de arquivo. Alias acentuado quebra o lexer do sqlfluff
   (`LXR | Unable to lex characters`), e nome de arquivo acentuado quebra os links do
   README, do docx e dos decks.
3. **Conteúdo acentuado se escreve com as ferramentas de arquivo, nunca por heredoc de
   shell.** A raiz do problema foi essa: escapamento de heredoc falhou tantas vezes
   que o reflexo virou evitar acento em vez de trocar de ferramenta.
4. **Script que imprime acento começa com**
   `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` — o console do Windows
   é cp1252 e morre com `UnicodeEncodeError` no meio do relatório.
5. **Conferir com `python scripts/confere_portugues.py`**, na mesma rotina do
   `linta_notebook.py`. Ele acusa palavra sem acento, mojibake (`Ã§`, `Â`, `â€`) e o
   erro inverso — acento dentro de identificador de SQL.

## Guardrail Crítico — rubrica de avaliação nunca vai para o repositório do desafio

O usuário é candidato da Certificação em AE (desafio Adventure Works) **e**, em outra
sessão, tem acesso à rubrica confidencial de correção (via `certificacao-ae-correcao`,
pasta `Avaliador AE`). Essa rubrica pode orientar **meu** raciocínio silencioso sobre onde
vale investir esforço, mas ela **nunca** pode aparecer, direta ou indiretamente, em nada
que faça parte da entrega: `Desafio/desafio-adventureworks/`, o repositório
`certificacao-ae-adventureworks`, PRs, mensagens de commit, slides, vídeo.

**Nunca escrever, nesses lugares:** número de item do formulário (`item 2.5`, `1.3`),
nome de bloco (`Bloco 2`), peso ou nota (`peso 5,00`, `vale metade da nota`), palavras
como `formulário`, `checklist`, `pontuação` referidas à correção, ou frases como "isto
atende ao item X" / "fecha o item Y".

**Sempre pode:** citar o **briefing público** do desafio, suas etapas numeradas (Etapa 1
a 11) e suas exigências textuais — isso é material do próprio candidato, não da correção.

Se uma justificativa técnica só faz sentido citando a rubrica, reescreva-a citando o
briefing ou a boa prática de engenharia em si (ex.: "o briefing pede testes de source" em
vez de "item 2.5 do formulário exige testes de source"). Encontrado um vazamento
retroativo — buscar com `grep -rn` por esses termos no repositório do desafio antes de
declarar a correção concluída.

## Guardrails Críticos (Power BI)

1. **NUNCA remover backgrounds/SVGs** sem pedido explícito
2. **Fechar Desktop sem salvar** antes de editar JSON externamente
3. **Salvar após cada lote MCP** (memória é volátil)
4. **Canvas 1280×720**, tema Storm (Fluent2 quebra cards)
5. **Ocultar página**: campo `visibility: HiddenInViewMode` no page.json (`isHidden` não existe)
6. **Textbox**: `paragraphs` como array nativo (ver skill textbox.md)
