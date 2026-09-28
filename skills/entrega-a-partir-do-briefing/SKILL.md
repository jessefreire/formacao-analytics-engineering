---
name: entrega-a-partir-do-briefing
description: Monta o pacote final de um projeto a partir do próprio briefing — mapa "o briefing pede × onde está", PDFs gerados dos .md, arquivo de links públicos, pasta de entregáveis limpa e o ZIP no nome e limite exigidos. Use quando o usuário disser "vamos submeter", "monta a entrega", "o que falta entregar", "gera o zip", "confere se está tudo", ou colar a seção de submissão de um briefing.
---

# /entrega-a-partir-do-briefing

A entrega é julgada também pela aderência ao que foi pedido. O briefing é a única régua: tudo
sai dele, citado com as palavras dele.

## Processo

1. **Ler a seção de entrega/submissão** do briefing e a página da plataforma (costuma ter
   detalhes a mais: nome de arquivo sugerido, ordem, limite de tamanho).
2. **Tabela "pede × onde está"**, uma linha por item, com a forma exigida
   (arquivo no ZIP / link no txt) e o arquivo real. Marque lacunas.
3. **Conferir cada item contra o conteúdo pedido**, não só a existência. Ex.: "apresentação
   cobrindo X, Y, Z" — o deck cobre X, Y, Z? Avise o usuário da lacuna; a decisão é dele.
4. **Gerar o que falta**:
   - `.md` → PDF: `python-markdown` + Edge headless
     (`msedge --headless --no-pdf-header-footer --print-to-pdf=<pdf> <html>`); diagramas
     mermaid exigem renderizar no navegador antes (`--virtual-time-budget`).
   - Conferir o PDF gerado (páginas, texto, sem código cru).
5. **Arquivo de links** (`.txt`): na ordem da página de submissão, cada link com título.
   **Testar cada link sem login** (navegador isolado) e pelas permissões ("anyone: reader").
   Preferir link direto de arquivo (vídeo) além do link de pasta.
6. **Pasta de entregáveis limpa**: só o que é entregue. Rascunhos, insumos intermediários,
   arquivos temporários → `rascunhos/` (mover, não apagar).
7. **ZIP**: nome sugerido pela plataforma; pasta raiz com o mesmo nome; o que vai por link
   (vídeo, repositório) fica fora. Conferir tamanho vs. limite e `testzip()`.
8. **Repositório**: README e docs refletindo o estado final (nada "pendente" que já fechou),
   `git status` limpo, push.

## Cuidados

- Limite de tamanho: a exceção "suba no Drive e mande o link" vale só se a pasta passar do
  limite — com o vídeo indo por link, normalmente não passa.
- Vídeo: conferir a duração contra o limite. Para caber, acelerar esperas sem fala (ex.:
  comandos rodando) em vez de cortar execução que precisa aparecer; nunca sobrescrever o original.
- Nome de arquivo sem acento e sem espaço quando for referenciado em link.
- Nunca incluir material de avaliação/correção em nada que seja entregue — só o briefing público.
