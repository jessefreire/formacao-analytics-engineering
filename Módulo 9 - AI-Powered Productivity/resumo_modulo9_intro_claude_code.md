# Resumo — Módulo 9: Intro ao Claude Code

> Subcurso FEA, 3 aulas (~25 min), com Felipe Campos (AI Engineer). Cobre o que é o Claude Code,
> as quatro formas de estender ele (agentes, skills, commands, hooks) e como empacotar e
> distribuir isso via plugins e marketplace.
>
> Referências como `(A01)`, `(A02)`, `(A03)` apontam a aula de origem.

## 1. O que é o Claude Code

Interface de **linha de comando** para trabalhar com o Claude dentro do seu projeto. Integra em
qualquer IDE — VS Code, Databricks, Neovim — e **não exige plugin extra**; também roda direto no
terminal `(A01)`.

O ponto central é o **contexto por diretório**: ele enxerga a árvore de arquivos a partir de onde
foi aberto. Abriu na área de trabalho, tem acesso à pasta e a todas as subpastas — lê e altera
arquivos ali dentro.

Além de ler e escrever, executa shell: roda testes, instala dependências, executa scripts e faz
commit, sem sair do fluxo do terminal.

> **O ambiente é o seu, não dele:** o Claude usa as ferramentas instaladas na sua máquina. Se uma
> skill ou MCP precisa de Docker, Python ou Node.js e você não tem, ele falha e devolve o erro —
> não resolve sozinho `(A02)`.

## 2. Por que Linux importa (e o caminho no Windows)

As ferramentas nativas de leitura de arquivo funcionam bem melhor em Linux, porque executam
comandos que são nativos de lá `(A01)`.

| Situação | Recomendação da aula |
|---|---|
| Máquina Linux (Ubuntu, Arch) | Cenário ideal, tudo funciona |
| Máquina Windows corporativa | Usar **WSL** — mantém tudo num SO só |
| Quer o Linux "de verdade" | Dual boot funciona |
| Vai usar OpenCode | **Só Linux** — não instala no Windows |

O contraponto honesto que a aula faz: o WSL facilita porque unifica o ambiente, mas te obriga a
mexer no Linux só por linha de comando. E isso é apresentado como vantagem no médio prazo —
quem sabe linha de comando entende o que está acontecendo quando algo quebra.

## 3. Os três modelos e quando usar cada um

| Modelo | Perfil | Quando usar |
|---|---|---|
| **Opus** | Topo de linha, faz tudo com excelência, **caro** | Planejar algo que você não conhece |
| **Sonnet** | Intermediário, funciona bem para tudo | Dia a dia |
| **Haiku** | Focado em **velocidade** | Tarefa simples ou que precisa ser rápida |

**Pegadinha:** o Opus não é "o melhor dos mundos" para uso diário justamente por ser caro — ele
consome a sessão rápido. A aula menciona que o plano trabalha em **sessões de 5 horas** de tokens,
então gastar Opus em tarefa trivial encurta seu dia de trabalho `(A01)`.

## 4. Ferramentas nativas

O Claude já vem com um conjunto de tools, e você pode criar outras `(A01)`:

| Tool | Função |
|---|---|
| `read` / `write` / `edit` | Ler arquivo, criar arquivo, editar arquivo já existente |
| `bash` | Executar comando de shell (`ls`, `tree`, `cd`, `mkdir`…) |
| `glob` | Localizar arquivos por padrão na árvore |
| `grep` | Filtrar conteúdo dentro dos arquivos |
| `web search` / `web fetch` | Pesquisar e coletar dados da internet |

Quando não consegue resolver com as tools existentes, ele escreve scripts próprios para dar conta.

## 5. As quatro formas de estender

Esta é a espinha dorsal do subcurso. Os quatro mecanismos parecem próximos, e a diferença entre
eles está em **como são acionados**:

| Mecanismo | O que é | Como é acionado |
|---|---|---|
| **Agente** | Persona especializada num domínio | Você chama, ou o Claude delega |
| **Skill** | Procedimento reutilizável | **Automático** (pelo texto) ou manual via `/` |
| **Command** | Igual à skill na estrutura | **Só manual** — nunca automático |
| **Hook** | Ação que sempre acontece | Disparado por evento do ciclo de vida |

### Agentes

Redirecionam o comportamento do Claude para um domínio **sem trocar o modelo** `(A02)`. Estrutura:
um *front matter* obrigatório e, abaixo dele, a definição em markdown.

```yaml
---
name: analytics-engineer
description: Especialista em transformações dbt, modelagem de dados e camada semântica
model: sonnet
---

Aqui para baixo é markdown puro: linguagem natural explicando
o que o agente faz, o que ele usa, quais skills ele deve chamar.
```

> **O pulo do gato é o encadeamento:** dentro do markdown do agente você aponta quais skills ele
> usa; a skill aponta o script que executa; o script conversa com a API do Databricks e traz dado
> de verdade. Agente → skill → script é a cadeia que transforma prompt em automação real `(A02)`.

A aula é honesta sobre o limite: não há garantia de que um agente "especialista em Airflow" fique
restrito a Airflow — mas na prática observada ele **melhora** naquele domínio.

### Skills

Mesma estrutura do agente, com diferenças no front matter. O que as distingue é a **invocação
automática**: o Claude lê a `description` e ativa a skill sozinho quando o que você pediu se
encaixa `(A02)`.

Por isso a `description` é o campo que mais importa. A boa prática que a aula ensina é escrever
**quando usar e quando NÃO usar** — sem o negativo, a skill dispara fora de hora.

Três formas de acionar:

```
1. Automática  — o Claude decide pela description
2. Direta      — /nome-da-skill + seu prompt
3. Só manual   — disableModelInvocation: true no front matter
```

### Commands

Praticamente iguais às skills, com **uma** diferença que é toda a diferença: **não têm invocação
automática**. Você digita `/`, o nome e executa. Servem para o que você quer disparar
deliberadamente `(A02)`.

**Pegadinha:** skill e command se parecem tanto no arquivo que é fácil escrever um esperando o
comportamento do outro. A régua: se você quer que o Claude decida sozinho, é skill; se você quer
manter o controle do gatilho, é command.

### Hooks

Para o que deve acontecer **sempre**, sem depender da decisão do modelo. O exemplo da aula é
segurança: bloquear a leitura de `.env` por um script bash que intercepta a tentativa `(A02)`.

Os hooks se penduram no ciclo de vida do agente:

```
sessionStart
   └─ prompt do usuário
        └─ loop do agente
             ├─ pre-use          (antes de usar uma tool)
             ├─ permission request (o Claude pede autorização)
             ├─ execução da tool
             ├─ post-use         (depois de usar a tool)
             ├─ taskCreated / taskCompleted
             └─ falha de tool
sessionEnd
```

Dois exemplos concretos:

| Evento | Matcher | Ação |
|---|---|---|
| `pre-use` | tool é `bash` | roda `validate_bash.sh` antes de deixar executar |
| `post-use` | tool é `write` ou `edit` | roda `ruff format` no arquivo alterado |

**Pegadinha:** o hook de `post-use` com `ruff format` só funciona se o `ruff` estiver instalado no
ambiente — senão o hook falha. Hook que depende de ferramenta externa herda a dependência dela.

Sobre o pedido de permissão: por padrão o Claude **pede autorização** antes de executar. Existe um
modo automático que libera, mas ele é opcional — não é o comportamento padrão `(A02)`.

## 6. MCP e LSP

**MCP (Model Context Protocol)** é ao mesmo tempo um conjunto de ferramentas e um **servidor de
tools**. Existem MCPs para praticamente tudo — Notion, Slack, Jira, GitHub — e você pode construir
os seus `(A03)`.

O argumento de economia é direto: o MCP do GitHub foi feito pelo GitHub. Não faz sentido você
escrever chamada de API para gerenciar pull request e criar repositório quando o MCP oficial já
abstrai isso. **Reutilize em vez de reimplementar.**

**LSP (Language Server Protocol)** aparece de passagem: servidores de linguagem dando inteligência
de código em tempo real, sem parsing manual. A aula é transparente ao dizer que o instrutor tem
pouca experiência com isso. A distinção útil que fica: MCP é ferramenta que você invoca; LSP é
contexto contínuo, em tempo real.

## 7. Plugins e marketplace — empacotar e distribuir

Construir é uma coisa; **distribuir para o time** é outra. É o problema que plugins e marketplaces
resolvem `(A01, A03)`.

A motivação é separação por papel: skill de montar slide, skill de dbt para analytics engineer e
skill de Airflow para engenheiro de dados **não devem morar no mesmo lugar**. Cada papel ganha seu
plugin; os plugins ficam no marketplace; cada pessoa instala o que usa.

### Estrutura de um plugin

```
meu-plugin/
├── plugin.json        # name, version, description, author
├── agents/
├── skills/
├── commands/
└── hooks.json         # hooks precisam ser declarados em JSON, na raiz
```

A organização em pastas é boa prática, não obrigação — **exceto os hooks**, que precisam mesmo do
`hooks.json`. O `plugin.json` usa **versionamento semântico**: cada feature nova sobe a versão, e é
isso que permite distribuir atualização de forma controlada.

### O marketplace na prática

O exemplo mostrado tinha **14 plugins, 54 skills e 15 agentes** — plugins de Airflow, AWS, dbt,
Databricks, Terraform, design e um de "commons" com ferramentas genéricas `(A03)`.

> **O plugin de economia de contexto:** um dos mais simples e mais úteis. Um hook **bloqueia** a
> leitura direta de arquivo grande; um script indexa esse arquivo num banco local que simula banco
> vetorial; a busca passa a ser por palavra, e o resultado volta sem o Claude ter lido o arquivo
> inteiro. Troca leitura caras em tokens por consulta baratas `(A03)`.

## 8. Boas práticas de tamanho e composição

Duas regras práticas que a aula extrai da documentação `(A03)`:

| Item | Limite | Por quê |
|---|---|---|
| `CLAUDE.md` | **máx. 500 linhas** | É carregado como contexto do projeto |
| Skill individual | não deixar virar 2500 linhas | Divida e referencie |

A solução para skill grande é **composição**: uma skill referencia outra, que referencia outra,
formando uma árvore de dependências. Isso mantém cada arquivo pequeno e permite reaproveitar peça
em contextos diferentes.

## Conexão com o Desafio Final (dbt + Power BI)

Este subcurso é o mais "meta" dos três — é sobre a ferramenta com que você trabalha, não sobre o
BanVic. Mesmo assim, quatro ligações diretas:

- **`CLAUDE.md` com máximo de 500 linhas** é regra que se aplica a este repositório agora. O
  `AGENTS.md` daqui é o documento longo; o `CLAUDE.md` é o enxuto que aponta para ele — exatamente
  o padrão que a aula recomenda.
- **Agente de analytics engineer** é literalmente o exemplo usado na aula (`transformações dbt,
  modelagem, camada semântica`). O encadeamento agente → skill → script é o que as skills
  `ae-fullflow` e `dbt-packages-tests` deste repo fazem.
- **MCP em vez de chamada de API própria**: o `powerbi-modeling-mcp` configurado no `.mcp.json`
  deste projeto é a aplicação direta do argumento — não escrever integração XMLA à mão.
- **Hook como guardrail**: o bloqueio de `.env` do exemplo é o mesmo mecanismo que resolveria, de
  forma automática, os guardrails de Power BI que hoje vivem como texto no `AGENTS.md` (nunca
  remover background, fechar o Desktop antes de editar TMDL). Texto depende de o agente ler; hook
  não depende.

Uma ressalva de escopo: o guardrail de dados deste projeto continua valendo. Skill, agente e MCP
só com dado de treino ou com autorização explícita do cliente.
