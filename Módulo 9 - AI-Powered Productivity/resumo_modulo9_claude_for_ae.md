# Resumo — Módulo 9: Claude for AE

> Subcurso FEA, 2 aulas (~40 min), com **Kauê Oliveira** (Analytics Engineer, ex-Lighthouse).
> A segunda aula se chama *Refatoração, documentação e otimização*. Primeira vez que a Indicium dá
> essa aula. A primeira metade é sobre **como não se enfraquecer usando IA**; a segunda é um
> hands-on de exploração e refatoração num projeto dbt real.
>
> Referências como `(A01)` e `(A02)` apontam a aula de origem.

## 1. O ganho é real — e onde ele aparece

A aula não vende hype: parte do que já se observou dentro da empresa nas três frentes de projeto
(plataforma, migrações e produtos de dados) `(A01)`.

| Ganho | Como aparece na prática |
|---|---|
| **Velocidade de execução** | Reduz semanas de trabalho, mantendo qualidade |
| **Onboarding em projeto novo** | O assistente com acesso ao repo funciona como um sênior sempre disponível |
| **Trabalho mecânico** | Slide, documentação, boilerplate — libera tempo para o conteúdo |
| **Curva de aprendizado** | Menos tempo decorando sintaxe, mais tempo entendendo o problema |

O ponto de onboarding merece destaque porque resolve um problema estrutural: **nem sempre existe
documentação organizada no projeto, e nem sempre há outro dev disponível** para te desbloquear. O
assistente com acesso ao repositório cobre justamente esse vão.

> **A barreira que caiu:** a distância entre *entender um problema* e *conseguir expressar isso em
> código* encurtou. Ter fluência de sintaxe em Python ou SQL custava anos de estudo; hoje essa
> barreira é bem menor. O trabalho técnico ficou mais acessível `(A01)`.

E é justamente por isso que a aula chega numa conclusão contra-intuitiva: com a sintaxe ficando
barata, **soft skills e boas práticas ganharam destaque** — trabalhar bem com colegas, comunicar,
ser organizado. O que parecia detalhe passou a ser diferencial.

## 2. Os quatro modos de falha (e eles são reais)

Esta é a parte mais valiosa do subcurso. Vem de conversas com lideranças, devs experientes e
coordenação — são padrões que **já apareceram**, principalmente em início de carreira `(A01)`.

| Modo de falha | O que acontece | O custo |
|---|---|---|
| **Entrega rápido e errado** | Pulou o processo correto na pressa de entregar | Perde confiança, e confiança custa caro para recuperar |
| **Não sei justificar** | A Team Lead pergunta "por que essa decisão?" e não há resposta | É lido como falta de domínio técnico; perde relevância |
| **Executor de briefing** | Recebe a task, joga na IA, repassa a saída | Vira intermediário entre a ferramenta e a task; perde o lugar de consultor |
| **Ciclo da adoção irrefletida** | Delega sem entender → entrega → ganha falsa confiança → não conhece o projeto | Bola de neve: quem percebe é a liderança ou, pior, o cliente |

**Pegadinha:** o modo mais perigoso é o que *parece* sucesso. Você entrega, passa, e conclui que
está indo bem — enquanto não entende o projeto em que está inserido. O erro só aparece depois, e
não é você que encontra.

A aula é explícita quanto à intenção: **não é para assustar, é para incentivar o uso consciente**.
A meta é a ferramenta te fortalecer, não virar muleta.

> **O caso do "vou pedir pro Claude":** numa conversa descontraída, o cliente pediu uma demanda e a
> pessoa respondeu que ia pedir para o Claude. Mesmo que seja verdade, não se diz — você está
> comunicando que não vai fazer o seu trabalho. Queima o seu filme e o da empresa `(A01)`.

## 3. O que o cliente compra

O argumento que sustenta tudo acima: **o cliente não compra o código, ele compra confiança e
expertise** `(A01)`.

O posicionamento da consultoria tem três pernas, e a IA se encaixa em duas delas:

| Perna | Relação com IA |
|---|---|
| Clientes Enterprise — grandes, estruturados, exigentes | Contexto: o erro custa caro |
| **Velocidade sem comprometer qualidade** | A IA é necessária aqui — não há como prescindir |
| **The best people** — vendidos como especialistas | A IA **não** substitui: é você que explica ao cliente por que fez e por que não fez |

É nessa terceira perna que os modos de falha da seção anterior machucam de verdade.

Some-se a isso o movimento de cargo para **FDE** (*forward deployed engineer*) — o engenheiro mais
próximo do cliente. Num mercado com muita aplicação irrefletida de IA sem retorno, cresce a demanda
por quem sabe conduzir a conversa de "isso é hype, isso não é hype".

## 4. Os três princípios

```
1. Processos ANTES de ferramentas
2. Conhecimento ANTES da execução
3. Revisão ANTES da geração
```

**Processos antes de ferramentas.** Dar muito menos importância a qual modelo é o da vez e muito
mais ao processo que se quer otimizar e à dor do cliente. A ferramenta não é a estrela do show — é
*consequência* da compreensão do processo, não o contrário. Não adotar só para adotar `(A01)`.

**Conhecimento antes da execução.** Somos vendidos como especialistas; não faz sentido delegar a
compreensão. Delegar compreensão é se alienar do processo — e **a entrega vai com o seu nome, não
com o nome da IA**.

**Revisão antes da geração.** A habilidade que importa migrou de *escrever com a sintaxe certa*
para *ler e entender o que está acontecendo*.

Daí o workflow que a aula propõe:

```
entender o processo
   → construir conhecimento (inclusive documentação própria)
      → executar com a IA
         → revisar com leitura crítica
```

## 5. Explorar um projeto antes de mexer nele

A premissa do hands-on: **fazer pergunta é hábito que se desenvolve**, o Claude Code é muito bom em
ler, e a pergunta certa direciona a ferramenta para te fortalecer `(A02)`.

### `/init` e o `CLAUDE.md`

Vale ver o que ele faz **antes** de escrever, porque isso explica por que o arquivo sai bom:

```
/init
 → analisa o codebase para criar o CLAUDE.md; explora a estrutura primeiro
 → busca por padrões, lê arquivo, lista diretório
 → reconhece que é um projeto dbt
 → lê os arquivos de config principais e o README
 → só então escreve  (~14s, ~637 tokens no exemplo)
```

Ou seja: o `/init` não é um template. Ele **investiga** e escreve sobre o que encontrou — é a
razão de o resultado ser específico do projeto em vez de genérico.

> **O repo de referência mostra o que um projeto dbt maduro carrega.** Além de `models/`,
> `macros/`, `seeds/`, `snapshots/` e `tests/`, aparecem `.sqlfluff` (lint de SQL),
> `.dbt-checkpoint.yaml` (hooks de pre-commit para dbt), `.pre-commit-config.yaml`,
> `bitbucket-pipelines.yml` (CI), `hooks/`, `bus_matrix/` e `target-defer-databricks` /
> `target-defer-snowflake` (defer do dbt). Vale como checklist do que falta no seu projeto.

O `/init` gera o `CLAUDE.md`, e a analogia da aula é boa: **é um readme para a máquina**. O readme
comum é markdown para outro desenvolvedor ler; o `CLAUDE.md` é o readme para o próprio Claude. Ele
já traz resumo do que o projeto faz, configurações de plataforma e comandos básicos (instalar
dependências, rodar o dbt).

### Prompt direcionado ganha de leitura crua

Ler o `CLAUDE.md` inteiro é muita informação. O que funciona melhor é direcionar:

```
Estrutura do projeto: explique de maneira simplificada o que ele faz,
como as camadas se relacionam, e quais convenções e cuidados um
AE Júnior precisa conhecer antes de começar.
```

**Dizer "AE Júnior" no prompt não é detalhe** — reduz o escopo do que ele apresenta e muda o nível
de linguagem da resposta.

### As duas alavancas de contexto

| Alavanca | Uso |
|---|---|
| Pergunta genérica | "O que é Bus Matrix?" — conhecimento geral |
| `@arquivo` | Aponta um arquivo específico como referência |

Combinadas, você faz pesquisa **com o contexto do seu projeto** ao mesmo tempo.

### Investigar um modelo, não só ler

Pedir as dependências de um modelo (ex: `fct_sales.sql`) devolve a DAG, o tipo de materialização,
dependências de macro e as chaves usadas. O aprendizado conceitual é mais importante que a saída:

> **Modelo não é unidade fechada.** Tem coisa antes e coisa depois. Se você mexe aqui, o que vem
> **downstream** pode quebrar. Ter essa visualização antes de alterar é o que separa refatoração de
> estrago `(A02)`.

E um passo além da modelagem: perguntar **qual processo de negócio está modelado ali** e quem
consome. Em vendas — é o vendedor vendo se bateu meta? O gerente acompanhando o time? Essa visão de
negócio não é bobagem.

### Documentação própria, sem sujar o repo

Você pode usar a IA para fazer um fichamento seu dentro do próprio repositório e **simplesmente não
commitar**. A alteração fica local, não vai para produção, e você ganha material de referência
`(A02)`.

## 6. Caso de uso 1 — Refatoração

O modelo legado do exemplo é o que a aula chama de **ninho de rato**: a versão digital do emaranhado
de fios num servidor. Dois problemas concretos `(A02)`:

| Problema | Por que é ruim |
|---|---|
| `SELECT` dentro do `FROM` | É **subquery** — em vez de ver `from dim_clientes`, você vê outra tabela sendo construída inline |
| Aliases como `T3` | Ninguém sabe o que cada join é. Use nomes descritivos |

A refatoração foi feita em dois passos deliberados, e a ordem importa:

```
1. "reorganize o modelo sales_orders_legacy para facilitar a leitura"
   -> ficou legível, mas as deficiências continuaram

2. "reescreva com CTEs descritivas"
   -> WITH purchasing_orders AS (...), products AS (...), shipping AS (...)
```

**CTE** (*common table expression*) é bloco de código nomeado e reaproveitável: em vez de query
dentro de query, cada parte no seu lugar, com nome que diz o que é.

A justificativa que aparece escrita na tela é a formulação mais precisa do benefício: refatorar
para CTE dá **um nome significativo a cada etapa** e permite **ler a query de cima para baixo,
em vez de de dentro para fora**. É isso que a subquery aninhada impede.

Dois detalhes práticos do exemplo:

- A chave surrogada é gerada com **`dbt_utils.generate_surrogate_key`** — a mesma macro do
  package que já está no `banvic-dbt`.
- O resultado foi salvo como um **arquivo novo** (`..._refactored.sql`), sem sobrescrever o
  legado. Refatoração como proposta, não como fato consumado.

> **A IA levantou o risco de governança sozinha.** Depois de refatorar, ela avisou que o
> resultado era idêntico em execução **mas** que o arquivo estava em `legacy/` marcado como
> *DO NOT TOUCH*, e que era melhor confirmar com o time antes de commitar — mesmo sendo só
> formatação. É o princípio "revisão antes da geração" acontecendo do lado da ferramenta, e um
> bom argumento para marcar convenção desse tipo no `CLAUDE.md`: o que está escrito, ela lê.

**Pegadinha:** o modelo ficar bonito não significa que está correto. A segmentação em CTEs pode não
refletir o processo de negócio real. A aula insiste: **testar, validar com liderança ou cliente, e
comparar o output** do modelo antigo com o novo. Ganho de produtividade sem validação é risco, não
ganho.

### A regra de camada que o exemplo viola

> **Staging não carrega regra de negócio.** Staging é transformação mínima: renomear e fazer cast de
> formato. A regra de negócio vai para intermediate ou marts. O modelo do exemplo estava errado
> exatamente por isso `(A02)`.

Esse é um ótimo uso da IA: pedir para **separar** um modelo que mistura tudo em staging +
intermediate/marts. Especialmente em migração do tipo **lift and reshape** (pega o legado, reformula
e refatora), que é diferente do **lift and shift** (traz como está).

## 7. Caso de uso 2 — Documentação

Uso mais mecânico e de retorno imediato: uma pasta de staging sem nenhuma documentação vira YAML
descrito automaticamente `(A02)`.

Duas ressalvas que a aula faz, e que evitam retrabalho:

- **Confirmar a necessidade** antes: "isso é mesmo necessário?" Dar um passo atrás.
- **Cuidado com teste gerado no automático:** a IA pode encher o modelo de testes. Você decide
  quais fazem sentido — e precisa conferir o **grão** da tabela para saber se o teste está certo.

## 8. Caso de uso 3 — Otimização

Um detalhe de interface que passa batido e muda o risco do que você faz: a barra de status do
Claude Code mostra o **modo de permissão ativo** — `manual mode on` (pede autorização a cada
passo) ou `accept edits on` (aplica edição sem perguntar), alternável com `shift+tab`. Em
refatoração de modelo legado, saber em qual modo você está é a diferença entre revisar um diff e
descobrir a alteração depois.

O exemplo é um modelo deliberadamente lento: cálculo ineficiente puxando um modelo dentro de outro
`SELECT`, com casts no lugar errado. O que ele deveria fazer é trazer o `sales_order` **uma vez**
numa CTE e reutilizar essa CTE ao longo do código `(A02)`.

O ciclo de otimização fecha com medição, não com impressão:

```
1. medir o tempo de run atual (dbt ou data warehouse)
2. pedir a refatoração pensando em performance
3. medir de novo e comparar
```

## 9. As cinco perguntas de fechamento

O subcurso termina com um checklist mental para aplicar em qualquer entrega feita com IA `(A02)`:

| Pergunta | O que ela protege |
|---|---|
| **Justificativa** — por que essa escolha e não outra? | Você conseguir explicar para a liderança e o cliente |
| **Necessidade** — isso é realmente necessário aqui? | Não construir o que ninguém pediu |
| **Tradeoff** — o que essa abordagem ganha e o que cobra? | Decisão consciente em vez de default |
| **Risco** — o que pode quebrar em produção? | O ambiente real, não o local |
| **Validação** — qual o impacto downstream? | Os modelos que vêm depois do que você mexeu |

Se você não sabe responder essas cinco, ainda não terminou — independente de o código estar rodando.

## Conexão com o Desafio Final (dbt + Power BI)

Este é o subcurso que mais fala diretamente do trabalho do desafio:

- **Staging sem regra de negócio** é a regra que o `banvic-dbt` já segue: os `stg_erp__*` só
  renomeiam e fazem cast (`cast(num_conta as int) as pk_conta`), e o enriquecimento fica nos
  `int_*`. A aula explica *por que* essa fronteira existe, não só que ela existe.
- **CTEs descritivas** é o padrão dos models daqui — `with transacoes as (...), contas as (...),
  fato_transacoes as (...)`. Vale como régua de revisão: se um model seu tem `SELECT` dentro do
  `FROM`, ele é candidato a refatoração.
- **Impacto downstream** é literalmente o risco do `fact_transacoes`: mexer no grão dele quebra o
  dashboard do Power BI, que consome os CSVs dos marts. Antes de alterar model, olhar quem consome.
- **Comparar output antes e depois** é o que falta no fluxo atual deste repo. Hoje o caminho é
  `dbt build --target local` → `export_marts_local.py` → refresh no Desktop, sem comparação de
  contagem entre versões. Uma checagem de linhas e somas antes/depois pegaria regressão silenciosa.
- **Documentação com ressalva de grão**: os `.yml` daqui testam `unique` + `not_null` na PK. O aviso
  da aula sobre conferir o grão é exatamente o tipo de erro que o teste de unicidade pega — e é por
  isso que `stg_erp__contas` e `dim_contas` estavam sem `.yml` até agora.
- **As cinco perguntas** valem para as decisões já tomadas aqui: por que `bothDirections` no
  relacionamento de agência, por que DuckDB local em vez de Databricks, o que quebra se o caminho
  dos CSVs mudar de máquina.
