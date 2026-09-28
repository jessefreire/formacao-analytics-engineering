---
name: pbi-apresentacao
description: Abre um .pbip/.pbix no Power BI Desktop em modo apresentação — tela cheia, sem ribbon, painéis, abas, barra de status, ícones de hover ou bordas de seleção — para gravar vídeo ou apresentar sem Power BI Service. Use quando o usuário quiser "mostrar o dashboard sem a interface", "gravar o dashboard", "apresentar sem publicar", "modo leitura no Desktop", ou não tiver conta no Service.
---

# /pbi-apresentacao

App local em `D:\Documentos\pbi-apresentacao\` (Python, só biblioteca padrão). O próprio
Desktop renderiza — fidelidade total — e nenhum arquivo do relatório é alterado.

## Como funciona

O Desktop desenha a interface num WebView2. O app o inicia com
`WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS=--remote-debugging-port=9229`, conecta via Chrome
DevTools Protocol e injeta CSS que esconde a moldura; depois deixa a janela em tela cheia sem
bordas (Win32).

## Uso

1. **Feche todas as janelas do Power BI Desktop** (a porta só liga quando ele inicia do zero).
2. Arraste o arquivo sobre `apresentar.bat`, ou:
   ```bash
   cd /d D:\Documentos\pbi-apresentacao && python -m pbi_apresentacao abrir "C:\caminho\Relatorio.pbip"
   ```
3. Atalhos: **F9** liga/desliga · **Ctrl+F9** sai e restaura · **Ctrl+clique** nos botões.
4. Outros: `conectar` (retoma um Desktop aberto pelo app), `restaurar` (emergência).

## Dicas de gravação

- Zoom "Ajustar à largura" se as páginas forem mais altas que 16:9.
- Tooltips, slicers, toggles e scroll funcionam normalmente.

## Se algo aparecer de volta

Seletores em `pbi_apresentacao/estilo.py` (levantados no Desktop 2.157). Para achar um novo:
com o Desktop aberto pelo app, `Runtime.evaluate` com `document.elementFromPoint(x, y)` e subir
pelos pais. **Nunca** esconder `.visualHeaderAbove/.visualHeaderBelow` — são classes do
contêiner inteiro do visual.

## Limitações

- Botões exigem Ctrl+clique (modo edição por baixo).
- PBIP com caminho > ~130 caracteres na pasta não abre no Desktop (limite de 260 do Windows).
