# Skill: ae-materials-app

> Automatiza descoberta e sincronização dos materiais do curso (resumos, decorebas, configs) no `index.html` do visualizador local.

---

## O que faz

| Ação | Descrição |
|------|-----------|
| **Descobre arquivos** | Varre a raiz do projeto por padrões conhecidos (`resumo_modulo*.md`, `decoreba_modulo*.txt`, etc.) |
| **Extrai metadados** | Título do `# ` no markdown, número do módulo via regex, categoria automática |
| **Atualiza `index.html`** | Reescreve o array `FILES` mantendo o resto do app intacto |
| **Gera `files.json`** | Exporta metadados para outros usos (ex: scripts de build, CI) |
| **Comando único** | `python -m ae_materials_app.sync` |

---

## Instalação

```bash
# Na raiz do projeto (Formação AE/)
git init  # se ainda não tiver
# A skill já está em .opencode/skill/ae_materials_app/
```

---

## Uso

```bash
# 1. Adiciona novo material (ex: resumo_modulo3.md)
# 2. Sincroniza
python -m ae_materials_app.sync

# 3. Commit
git add index.html files.json
git commit -m "chore: sync module 3 materials"

# 4. Visualiza
python server.py
```

---

## Padrões reconhecidos

| Glob | Categoria | Prefixo ID | Done default |
|------|-----------|------------|--------------|
| `AGENTS.md` | Config | `agents` | ✅ |
| `INDICE_MODULOS.md` | Config | `indice` | ✅ |
| `Analytics Engineer Training 2026.md` | Config | `diario` | ✅ |
| `GUIA_DBT_BANVIC.md` | Config | `guia` | ✅ |
| `resumo_modulo*.md` | Módulo N | `resumo` | ✅ |
| `decoreba_modulo*.txt` | Módulo N | `decoreba` | ✅ |
| `Resumo_Modulo_*_SQL.md` | Módulo N | `resumo` | ✅ |
| `Decoreba_*.txt` | Módulo N | `decoreba` | ✅ |

> Adicione novos padrões em `sync.py` → `PATTERNS`.

---

## Estrutura

```
.opencode/skill/ae_materials_app/
├── SKILL.md              # Este arquivo
├── sync.py               # Script principal (entry point: python -m ae_materials_app.sync)
├── templates/
│   └── index.html.j2     # Template do index.html com marcadores
└── __init__.py           # Torna pacote Python
```

---

## Template (`index.html.j2`)

O template deve conter **marcadores** onde o array `FILES` será injetado:

```html
<script>
// ========== FILES AUTO-GENERATED ==========
const FILES = [
  // INJETADO AQUI
];
// ========== END FILES ==========

// ========== RESTO DO APP (inalterado) ==========
...
</script>
```

Se os marcadores não existirem, o script tenta substituir `const FILES = [...];` por regex.

---

## Adicionando novo padrão de arquivo

Edite `sync.py`, lista `PATTERNS`:

```python
PATTERNS = [
    # (glob, categoria, prefixo_id, done_default)
    ("meu_padrao_*.md", "Minha Categoria", "meu", True),
]
```

---

## Dependências

- Python 3.8+ (stdlib only: `pathlib`, `re`, `json`)
- `marked.js` via CDN no `index.html` (já incluso)

---

## Integração com Git Hooks (opcional)

```bash
# .git/hooks/pre-commit
#!/bin/sh
python -m ae_materials_app.sync
git add index.html files.json
```

---

## Troubleshooting

| Problema | Solução |
|----------|---------|
| "Template não encontrado" | Verifique se `templates/index.html.j2` existe e tem os marcadores |
| Arquivo não aparece | Confira se o glob em `PATTERNS` casa com o nome |
| Ordem errada | Ajuste a chave `sort` em `discover_files()` |
| Módulo não detectado | Regex `MODULE_RE` espera `modulo3`, `Modulo_4`, `modulo5` no nome |