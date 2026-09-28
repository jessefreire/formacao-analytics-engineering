---
name: pbi-mockup-design
description: Cria o mockup de um dashboard Power BI no canvas /design a partir das perguntas de negócio e KPIs — ou direto de uma entrevista/reunião com o cliente (texto, arquivo ou vídeo), passando por um levantamento validado — baixa fidelidade, depois alta fidelidade, já com as medidas do Power BI (1280px), fundos exportáveis como SVG e cada interação mapeada para o objeto real do PBI. Use quando o usuário pedir "faz o mockup do dashboard", "wireframe", "protótipo do relatório", "desenha as telas antes do Power BI", "monta o mockup a partir dessa entrevista", "transforma essa reunião em dashboard", ou precisar do JPEG do mockup.
---

> Autoria: Jessé Freire · Indicium AI.

# /pbi-mockup-design

Encaixa entre `powerbi-report-planning` (o que construir) e `powerbi-report-authoring`
(construir). O mockup é a fonte canônica da estrutura: o PBI segue o mockup, não o contrário.

## Processo

0. **Levantamento (quando a entrada é uma entrevista ou reunião)**. Aceita três formas:
   texto colado; arquivo `.txt`/`.md` de transcrição ou ata; ou link de vídeo, lido com
   `python ~/.claude/skills/youtube-analyzer/scripts/get_transcript.py "<url>"` (saída
   no scratchpad, nunca no repositório). Preencher `templates/levantamento.md` seguindo
   `references/levantamento.md`: público e decisão, perguntas numeradas, KPIs com os seis
   atributos, filtros, restrições, **evidência curta** da fala para cada pergunta, e
   lacunas. **Mostrar o levantamento ao usuário e só seguir depois da validação** — é o
   ponto em que um mal-entendido custa minutos em vez de um dashboard refeito.
   Sem entrevista (perguntas já definidas), pular para o passo 1.
1. **Régua de cobertura primeiro** (a partir do levantamento, quando houver): listar perguntas e indicadores. Cada um precisa de um
   visual; cada aprofundamento, de um **filtro ou toggle** — não de tela nova.
2. **Baixa fidelidade (P&B)**: decide o que mostrar e a ordem de leitura (KPIs → gráficos →
   tabela). Sem cor. Uma página por grupo de pergunta; capa se houver 3+ páginas de conteúdo.
3. **Alta fidelidade**: cor, tipografia, tema — o mesmo tema que o relatório vai usar
   (ex.: Storm; Fluent2 quebra cards). Fonte nativa do PBI (Arial/Segoe) para não haver substituição.
4. **Artboards "-fundo"** por página: header, menu e cards vazios na posição exata — viram o
   SVG de fundo da página no Power BI.
5. **Mapa de interação → objeto PBI** (tabela no doc da etapa).
6. **Exportar** JPEG (entregável) e SVG dos fundos.
7. **Revisar** contra a régua de cobertura antes de aprovar.

## Medidas do canvas

- **Largura fixa 1280px** (padrão de página do PBI). A altura cresce com o conteúdo.
- **Medir a altura no navegador** (`getBoundingClientRect()` / `document.body.scrollHeight`),
  nunca estimar — ela vira o `page.json.height`, e o que passar dela é cortado no PBI.
- Tabela sem Top N cresce: reserve altura ou use scroll interno do visual.

## Interação → objeto real do Power BI

| No mockup | No Power BI |
|---|---|
| Botões de métrica (Receita/Pedidos/...) | field parameter + `advancedSlicerVisual` |
| Toggle de dimensão (País/Estado/Cidade) | field parameter; título dinâmico via medida |
| Hierarquia Categoria → Produto | colunas no mesmo poço de Linhas da matriz (**field parameter não funciona ali**) |
| Barra de filtros global | slicers com Sincronizar Slicers (`syncGroup` por campo) |
| "Limpar filtros" | bookmark de reset em `actionButton` |
| Menu de abas | botões de navegação de página |
| Ranking "todos, ordenado" | tabela sem Top N; "Top N" vira callout de concentração |
| Callout "destaque" | par de medidas "(Texto)" + "(Legenda)" em cards |

Filtro global restringe dados; toggle só muda o agrupamento — documentar a diferença perto da barra.

## Exportação

- JPEG: html2canvas no próprio canvas → dataURL → salvar (servidor local descartável ou
  equivalente). Uma imagem por página.
- SVG dos fundos: extrair o `<svg>` do artboard "-fundo", com declaração XML; conferir que a
  altura bate com a da página.

## Armadilhas

- Filtro com valores demais (ex.: 558 cidades) como dropdown sem busca é ruim — decidir antes.
- Coluna constante (ex.: status único) não vira filtro nem gráfico.
- Quando o briefing pede uma ferramenta específica (ex.: Figma) e outra for usada, registrar a nota.
