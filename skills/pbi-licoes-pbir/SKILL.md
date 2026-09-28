---
name: pbi-licoes-pbir
description: Armadilhas conhecidas de Power BI (PBIR/PBIP, DAX, field parameters, Desktop) e como resolver cada uma — consulta rápida antes de editar ou quando algo "valida mas não funciona". Use quando um visual renderiza errado, o ranking mostra números estranhos, o título dinâmico dá erro, o PBIP não abre, a formatação não aplica, ou ao começar uma edição de PBIR.
---

# /pbi-licoes-pbir

Lições pagas em projeto real. Complementa `powerbi-report-authoring` (mecânica) — aqui é o
que dá errado e como consertar. Sempre `powerbi-report-author validate` depois de editar.

## DAX

| Sintoma | Causa | Correção |
|---|---|---|
| Ranking com números gigantes e repetidos depois de tirar o Top N | `RANKX(ALLSELECTED(dim))` inclui quem não tem venda (BLANK) | `RANKX(FILTER(ALLSELECTED(dim), CALCULATE([m]) <> BLANK()), CALCULATE([m]),, DESC)` dentro de `IF(NOT ISBLANK([m]), ...)`; `sortDefinition` pela medida |
| Título dinâmico: "a coluna faz parte da chave composta..." | `SELECTEDVALUE` na coluna visível do field parameter (tem `groupByColumn`) | `SELECTEDVALUE` na coluna oculta `... Fields` e comparar com `NAMEOF('t'[c])` num `SWITCH` |
| Total inflado por motivo/categoria N:N | soma atravessando a ponte | multiplicar por `allocation_factor` |

## Field parameters

- **No poço de Linhas da matriz não funciona** — renderiza o texto literal ("Categoria") em vez
  dos valores. Use hierarquia nativa (duas colunas no mesmo poço).
- **No papel Y (medida)**, a ligação só nasce arrastando no Desktop uma vez; o JSON resultante
  (bloco `fieldParameters` com `parameterExpr`, `index`, `length`) pode então ser copiado.
- Botão de toggle: `advancedSlicerVisual` ligado à coluna do parâmetro funciona direto no PBIR.
- Remover parâmetro órfão: `table_operations` Delete com `shouldCascadeDelete: true`,
  **depois** de confirmar que nenhum visual o usa.

## PBIR / formatação

- Título de visual dinâmico: `visualContainerObjects.title.text.expr.Measure` no lugar de `Literal`.
- Imagem local em visual `image`: estrutura **plana** `objects.general[].properties.imageUrl.expr.ResourcePackageItem`.
  Fundo de página e `plotArea.image` usam a **aninhada** `image.image.{name,url,scaling}`. Não são intercambiáveis.
- Objetos com seletor `id` às vezes precisam de **duas entradas** (uma sem seletor + uma com
  `{id:"default"}`) — sem isso valida e não aplica. A CLI avisa via `_selectorHint`.
- Card só de texto herda tile branco: além de `background.show:false`, `fillCustom.show:false`.
- **Altura da página é limite físico**: `y + height` além do `page.json.height` é cortado.
  Tirou o Top N de uma tabela? Recalcule a altura da página (e do fundo).
- Colunas de chave/atributo vêm com `summarizeBy: Sum` — trocar para `None`.
- `month_name` precisa de `sortByColumn: month`.
- Validação com erros de `"dropdown"` em slicer é falso-positivo conhecido da CLI.

## Desktop / arquivos

- **Caminho > 260 caracteres**: o Desktop não abre o PBIP ("visual.json has not been found").
  Mantenha a pasta do projeto com caminho curto.
- MCP guarda o modelo na memória do Desktop: **salvar (Ctrl+S) depois de cada lote**.
- Fechar o Desktop sem salvar antes de editar JSON por fora.
- Save do Desktop grava ruído (`"general": [{"properties": {}}]`, `diagramLayout.json`) —
  inofensivo, pode descartar.
- Mover PBIP: mover `.pbip` + `.Report/` + `.SemanticModel/` juntos; `definition.pbir` usa
  caminho relativo (`../X.SemanticModel`) e continua valendo.
- `.pbi/` é estado local — no `.gitignore`.

## Fora do Power BI, mas no mesmo fluxo

- `python-pptx` `.save()` **apaga fontes embutidas** (partes OPC que ele não conhece). Rodar o
  embed de fontes **por último**, depois de qualquer edição.
