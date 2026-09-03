# Convenções de Git — Conventional Commits e Branches

> Padrão de mercado para mensagens de commit e nomes de branch. Usado no curso, no desafio BanVic e por praticamente toda empresa que usa CI/CD.

---

## Formato do commit

```
tipo: descrição curta no imperativo
```

Exemplos: `feat: cria stg_clientes` · `fix: corrige join duplicado na fato`

O **tipo** diz que tipo de mudança é — permite gerar changelog automático e entender o histórico de relance.

## Os tipos

| Tipo | Significado | Exemplo |
|---|---|---|
| `feat:` | **Nova funcionalidade** (o que entrega valor) | `feat: cria stg_clientes` |
| `fix:` | **Correção de bug** | `fix: corrige join duplicado na fato` |
| `docs:` | **Documentação** | `docs: atualiza README do projeto` |
| `refactor:` | **Reestruturação sem mudar comportamento** | `refactor: extrai CTE duplicada` |
| `test:` | **Testes** (adicionar/corrigir) | `test: adiciona unique na PK de dim_cliente` |
| `chore:` | **Manutenção/tarefa doméstica** — não muda lógica de negócio | `chore: habilita seeds banvic` |
| `style:` | Formatação (espaço, ponto e vírgula) | `style: indentação SQL` |
| `perf:` | Melhoria de performance | `perf: materializa fato como table` |
| `ci:` | Pipeline de integração contínua | `ci: adiciona job de dbt build` |

> **"Chore" = tarefa doméstica.** Configuração, ajuste de build, renomear arquivo — necessário, mas não é feature nem bug.
>
> **Dica de escolha rápida:** muda comportamento pro usuário? `feat`. Conserta algo quebrado? `fix`. Só arruma a casa? `chore`.

## Como escolher (fluxo de decisão)

```
A mudança conserta algo quebrado?      → fix:
Cria funcionalidade nova?              → feat:
É teste?                               → test:
É documentação?                        → docs:
Reorganiza sem mudar comportamento?    → refactor:
Nenhuma das anteriores (config, etc.)? → chore:
```

## Branches

Padrão do curso: `main` protegida; trabalho em branches com prefixo:

| Prefixo | Uso | Exemplo |
|---|---|---|
| `feature/` | Nova funcionalidade | `feature/staging-models` |
| `fix/` | Correção | `fix/join-fato-duplicado` |
| `chore/` | Manutenção/config | `chore/habilita-seeds` |
| `hotfix/` | Correção urgente direto pra produção | `hotfix/valor-receita` |

Fluxo: `feature/*` → PR/merge na `main` → (produção). O **hotfix pula o fluxo** (merge direto na main) e depois sofre *backport* pra develop.

> Ver também: **Tier 2 vs Tier 3** no `aprofundamento_moduloIV.md` (camadas de branch e ambientes).

## No dbt Cloud (Studio)

- A branch `main` aparece **travada** (🔒) — o Studio impede commit direto nela
- Fluxo: **Create branch** → edita → **Commit** → merge via PR no GitHub
- Mensagens de commit seguem a mesma convenção

## Fluxo padrão: local → GitHub → Studio (validado na prática)

Quando o assistente gera os arquivos no clone local, o caminho inverso funciona assim:

```
1. Local:    cria branch → escreve arquivos → commit → push da branch
2. Studio:   Change branch → carrega a branch nova (ela aparece sozinha)
3. Studio:   cria o PR pelo próprio Studio → merge no GitHub
4. Studio:   volta pra main → Pull from main (traz o merge)
5. Studio:   dbt build + dbt test nos models novos
```

> Esse é o fluxo padrão do projeto — vale para o BanVic e para o desafio final (outro banco, mesmo ritual). Se o PR acusar conflito, conferir primeiro se `base: main` ← `compare: <feature>` não estão invertidos.

## No dia a dia do desafio BanVic

```
chore: habilita seeds banvic
feat: cria models staging (8 stg_*)
test: adiciona testes genericos nas PKs staging
feat: cria int_transacoes_enriquecidas
feat: cria dim_cliente e fact_transacoes (star schema)
docs: documenta models no yml
fix: corrige grao da fact_transacoes
```
