# Design system da plataforma

Referência do visual e da navegação de `templates/index.html.j2`. Os tokens seguem a identidade
Indicium AI (azul `#3a58ee`, Inter + Roboto Mono, faixas `#1c1d2f`), usados apenas como cor e
tipografia: a plataforma não carrega logo nem arquivo de marca.

## Tokens

| Papel | Claro | Escuro |
|---|---|---|
| Fundo | `#ffffff` | `#0f1120` |
| Cartão / código | `#f5f6fb` | `#1c1d2f` |
| Texto | `#0d0e1c` | `#f2f3fa` |
| Texto de rótulo (`--muted`) | `#5a5d7a` | `#9a9db8` |
| Acento | `#3a58ee` | `#8ca0ff` |
| Faixa escura (`--brand-dark`) | `#1c1d2f` | `#1c1d2f` |
| Raios | 6 / 12 / 20 / 999 | igual |
| Espaçamento | 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 | igual |

O tema vive em `data-theme` no `<html>`. As telas com canvas (grafo, dependências do Raio-X)
leem cores pela função `token('--nome')` e se redesenham ao trocar o tema.

## Regra de contraste

Medido sobre branco: `--dim #7b7e9e` dá 3,95:1, então só serve para texto de 14px ou mais e para
elementos decorativos. Rótulos, legendas e eyebrows de 13px ou menos usam `--muted` (6,4:1).
Verde como texto usa `#15803d`; o verde do token (`#16a34a`) fica para traço de gráfico
(`--ok-anel`, `--warn-anel`, `--bad-anel`). Estado nunca é só cor: sempre chip com texto.

## Responsividade (mobile-first)

- Base em 320px; pontos de quebra em 640, 901 (sidebar fixa) e 1200.
- Alvo de toque de 44px (36px com `pointer: fine`); campos com 16px para não dar zoom no iOS.
- Casca em `100dvh` com `env(safe-area-inset-*)`; `.main` é o contêiner de rolagem.
- Menu vira gaveta abaixo de 901px: `visibility: hidden` quando fechada, `inert` no conteúdo
  quando aberta, Esc fecha e devolve o foco a `#mobileToggle`.
- Chips de filtro em `.trilho` (rolagem horizontal própria); tabelas em `.tabela-rolagem`
  (`role="region"`, `tabindex="0"`); as do Raio-X viram cartões abaixo de 640px.
- Cuidado com especificidade: `.content table` define `min-width: 34rem`; regras de modo
  cartão precisam de `.content .rx-tabela` ou `.rx-rolagem .rx-tabela` para vencer.

## Navegação

- Grupos recolhíveis (estado em `localStorage.navAbertos`), com ícone por grupo no trilho recolhido.
- Busca global (Ctrl+K ou `/`), com `combobox`/`listbox`; migalha no topo; hash `#id` com
  `pushState`/`popstate`; últimos abertos na tela Início.
- Início é uma entrada sintética do `sync.py` (`id: inicio`, `view: inicio`, `oculto: true`);
  fica fora da lista e do grafo.

## Conferência antes de entregar

Auditoria em 320×568 e 1280×800, nos dois temas: `#main` e documento com `scrollWidth` igual a
`clientWidth`, nenhum alvo de toque abaixo de 44px, nenhuma fonte abaixo de 12px. Depois de
redimensionar a janela de teste, recarregue a página: a medição logo após o redimensionamento
pode vir com o layout anterior.

## Antes × depois (320×568)

| Item | Antes | Depois |
|---|---|---|
| Telas com overflow horizontal | 7 de 7 | 0 de 8 |
| Alvos de toque abaixo de 44px | em todas as telas | 0 |
| Fontes abaixo de 12px | em todas as telas | 0 |
