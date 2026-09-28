#!/usr/bin/env python3
"""Agrupa a transcrição de um vídeo em blocos com timestamp, para leitura rápida.

Uso:
  python momentos.py <transcricao.json> [--bloco 60]

Entrada: o JSON do youtube-analyzer (scripts/get_transcript.py), com `segments`.
Saída (stdout): uma linha por bloco — `[mm:ss] (t=Ns) texto do bloco`.

Serve para escolher os momentos-chave e montar links com `&t=Ns` sem carregar a
transcrição inteira na conversa. Nada é gravado em disco.

Autoria: Jessé Freire · Indicium AI
"""
import argparse
import json
import sys


def blocos(segmentos, tamanho):
    atual, inicio = [], 0.0
    for seg in segmentos:
        if atual and seg["start"] - inicio >= tamanho:
            yield inicio, " ".join(atual)
            atual, inicio = [], seg["start"]
        atual.append(seg["text"].replace("\n", " ").strip())
    if atual:
        yield inicio, " ".join(atual)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("arquivo")
    p.add_argument("--bloco", type=int, default=60, help="segundos por bloco (padrão 60)")
    args = p.parse_args()

    dados = json.load(open(args.arquivo, encoding="utf-8"))
    if dados.get("status") != "ok":
        print(f"erro: {dados.get('message', 'transcrição indisponível')}")
        return 1
    print(f"# {dados.get('video_url', '')} · idioma {dados.get('language')} · "
          f"{'automática' if dados.get('is_auto_generated') else 'manual'} · {dados.get('word_count')} palavras")
    for ini, texto in blocos(dados["segments"], args.bloco):
        print(f"[{int(ini // 60)}:{int(ini % 60):02d}] (t={int(ini)}s) {texto}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
