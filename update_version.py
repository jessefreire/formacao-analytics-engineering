#!/usr/bin/env python3
"""
Regenera version.json a partir do estado real do git (HEAD + remote origin).

Uso:
    python update_version.py          # escreve version.json
    python update_version.py --quiet  # sem output

Chamado automaticamente pelo server.py no startup, para o badge de versao
nunca ficar defasado do checkout local.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "version.json"


def git(*args):
    """Roda um comando git no repo e devolve stdout limpo (ou None se falhar)."""
    try:
        r = subprocess.run(
            ("git", "-C", str(ROOT)) + args,
            capture_output=True, text=True, encoding="utf-8", check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return r.stdout.strip()


def parse_repo(remote_url):
    """Extrai 'owner/repo' de uma URL https ou ssh do GitHub."""
    if not remote_url:
        return None
    m = re.search(r"github\.com[:/](?P<slug>[^/]+/[^/]+?)(?:\.git)?/?$", remote_url)
    return m.group("slug") if m else None


def build_version():
    sha = git("rev-parse", "HEAD")
    if not sha:
        return None
    return {
        "sha": sha,
        "short": sha[:7],
        "date": git("log", "-1", "--format=%cs") or "",
        "message": git("log", "-1", "--format=%s") or "",
        "repo": parse_repo(git("config", "--get", "remote.origin.url")) or "",
    }


def write_version(quiet=False):
    """Escreve version.json e devolve o dict gravado (ou None se git falhar)."""
    data = build_version()
    if data is None:
        if not quiet:
            print("[version] git indisponivel - version.json mantido como esta")
        return None

    previous = None
    if OUT.exists():
        try:
            previous = json.loads(OUT.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            previous = None

    if previous == data:
        if not quiet:
            print(f"[version] ja atualizado (v{data['short']})")
        return data

    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not quiet:
        old = f" (era v{previous['short']})" if previous and previous.get("short") else ""
        print(f"[version] version.json -> v{data['short']}{old}")
    return data


def main():
    return 0 if write_version(quiet="--quiet" in sys.argv) else 1


if __name__ == "__main__":
    sys.exit(main())
