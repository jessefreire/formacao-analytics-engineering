---
name: estudo-video
description: Transforma um vídeo do YouTube em material de estudo da formação — lê a transcrição, escreve um resumo em palavras próprias (com os momentos-chave e links com tempo) na pasta do módulo certo e sincroniza a plataforma para ele aparecer na navegação e no grafo. Use quando o usuário disser "estuda esse vídeo", "resume essa aula", "transforma esse vídeo em material", "coloca esse vídeo na formação", ou colar um link do YouTube pedindo resumo ou decoreba para estudar.
---

# /estudo-video

Um vídeo vira um `resumo_*.md` (e opcionalmente um `decoreba_*.txt`) no padrão da
plataforma da formação. Autoria: Jessé Freire · Indicium AI.

## Regra que não se negocia

**A transcrição nunca vai para o repositório.** O repo é público e a fala do vídeo é
conteúdo de quem o publicou — o `.gitignore` já barra transcrições pelo mesmo motivo.
Ela fica só no scratchpad. No repo entra apenas o resumo **em palavras próprias**, com no
máximo uma frase curta citada entre aspas. A fonte é o link do vídeo, e só.

## Processo

1. **Transcrição** (para o scratchpad, nunca para o repo):
   ```bash
   python ~/.claude/skills/youtube-analyzer/scripts/get_transcript.py "<url>" > <scratchpad>/video.json
   python ~/.claude/skills/estudo-video/scripts/momentos.py <scratchpad>/video.json
   ```
   `momentos.py` imprime blocos de ~60 s com `(t=Ns)`. Legenda automática erra nome
   próprio e termo técnico — corrigir pelo contexto e avisar o usuário quando for
   relevante. Erro 429: esperar alguns minutos; não há alternativa que baixe o vídeo.

2. **Destino**: escolher o módulo pela lista `MODULES` do
   `.claude/skills/ae_materials_app/sync.py` (ex.: dbt → Módulo IV; Power BI → Módulo 6;
   IA → Módulo 9). Conteúdo fora da grade do curso → Módulo 10 (material extra). Na
   dúvida, perguntar uma vez.

3. **Resumo** `resumo_<tema>.md` na pasta do módulo (nome em ASCII, minúsculo, com `_`):
   ```markdown
   # Resumo — <título em português>

   > Vídeo: <título original>, <canal> (~<duração>). Fonte: <url>.
   > Legenda automática em <idioma> — nomes e termos podem ter erro de transcrição.

   ## 1. <primeira ideia central>
   <explicação em palavras próprias; tabela quando houver lista de conceitos>

   ## Momentos do vídeo
   | Tempo | O que acontece |
   |---|---|
   | [3:05](<url>&t=185s) | <descrição curta> |

   ## O que levar para o projeto
   - <ação prática, ligada à formação ou ao trabalho de AE>
   ```
   Seguir o tom dos resumos existentes (ex.: `Módulo 9 - AI-Powered Productivity/
   resumo_modulo9_claude_for_ae.md`): explicativo, com tabelas, sem transcrever falas.

4. **Decoreba** (opcional, se o usuário pedir): `decoreba_<tema>.txt`, lista curta de
   conceitos e comandos, no formato dos `decoreba_*.txt` do mesmo módulo.

5. **Sincronizar**: `python .claude/skills/ae_materials_app/sync.py`. Os padrões
   `resumo_*`/`decoreba_*` já são reconhecidos — o material aparece na navegação e, no
   grafo, ligado ao módulo.

6. **Conferir**: `python scripts/confere_portugues.py` sem acusação nova; `git status` sem
   nenhum arquivo de transcrição; o material abre na plataforma.

## Vários vídeos sobre o mesmo tema

Um resumo por vídeo. Para uma visão cruzada, um `resumo_<tema>_panorama.md` que cita os
resumos individuais — nunca uma transcrição consolidada.
