# Analytics Engineer Training 2026

> **⚠️ DOCUMENTO VIVO** — Este arquivo, `AGENTS.md` e `INDICE_MODULOS.md` devem ser **atualizados automaticamente** a cada nova conversa com agentes, novo material do curso ou mudança estrutural no projeto. Não deixe para depois.

Documento vivo de acompanhamento da formação em Análise de Dados (Indicium Academy) rumo à transição de UX Designer para Analytics Engineer. Atualizado a cada módulo/subcurso concluído. Inclui resumos, pontos de reforço (erros/dúvidas do quiz de cada módulo) e conexões com o desafio final (modelagem em dbt + dashboard em Power BI).

## Índice

- [Módulo 1 — Introdução à Análise de Dados](#módulo-1--introdução-à-análise-de-dados)
- [Módulo 2 — SQL](#módulo-2--sql-para-análise-de-dados)
- [Conexões com o Desafio Final](#conexões-com-o-desafio-final-dbt--power-bi)
- Módulo 3 e seguintes — *(a preencher assim que estudar/continuar)*

---

## Módulo 1 — Introdução à Análise de Dados

### 1. A área de dados e os papéis

A área de dados é o conjunto de atividades, processos, ferramentas e profissionais dedicados a coletar, armazenar, organizar, analisar, distribuir e utilizar dados. Principais papéis e como se relacionam:

| Papel | Foco principal |
|---|---|
| Arquiteto de Dados | Define políticas, ferramentas e estratégia de modelagem |
| Engenheiro de Dados | Constrói e mantém a infraestrutura de ingestão/armazenamento |
| Engenheiro de Analytics | Transforma dados brutos, constrói o Data Warehouse, garante consistência (aqui entra o **dbt**) |
| Analista de Dados | Transforma e analisa dados para gerar insights/decisão de negócio (dashboards, relatórios) |
| Cientista de Dados | Aplica estatística/ML para modelos preditivos/prescritivos |
| Engenheiro de ML | Leva modelos de ML para produção |

**Reforço pessoal (quiz):** AE é mais focado em modelagem/pipeline (o "encanamento" de dados); dashboard e análise interpretativa são mais território do DA, ainda que o AE eventualmente toque nisso.

### 2. O papel do Analista de Dados

Tripé de habilidades (diagrama de Venn): **conhecimento matemático/estatístico** + **programação** + **conhecimento de negócio** → combinação = Ciência de Dados; cada função é uma especialização parcial desse tripé.

Soft skills mais cobradas: comunicação, escuta ativa, pesquisa ("fazer a pergunta certa"), escrita, resolução de problemas, trabalho em equipe, criatividade, gestão do tempo, ética/governança.

### 3. Processo de trabalho (CRISP-DM adaptado)

1. **Entendimento do problema de negócio** — que decisão precisa ser tomada? que informação embasa isso?
2. **Entendimento dos dados e do usuário** — quais dados existem, onde estão, qualidade; quem é o usuário e como ele decide hoje.
3. **Preparação dos dados / prototipação / documentação (catalogação)**
4. **Exploração** — estatística descritiva + visualização + dashboards para gerar hipóteses.
5. **Conclusões** — refinar a análise, validar com o negócio.
6. **Comunicação** — apresentar de forma que sustente a decisão, sem exagero/distorção.

Processo é cíclico, não linear — normalmente se volta a etapas anteriores.

### 4. Tipos de análise

- **Análise de dados (maior parte do trabalho):** Descritiva, Segmentação, Agregação, Geoespacial.
- **Previsões:** Séries temporais, Classificação, Numérico-contínua (regressão/árvores), Teste A/B.

### 5. Exploratória x Explicativa

- **Exploratória:** trabalho de bastidor, busca padrões/insights, visualização não precisa ser perfeita (ex: dashboard livre para o usuário explorar).
- **Explicativa:** feita depois de já ter o insight, precisa de narrativa guiando a uma conclusão específica.

**Exemplo próprio (validado):** ranking de notas dos alunos = exploratório; gráfico relacionando presença + entrega de tarefas para explicar o desempenho do aluno = explicativo.

Evolução de carreira (livro *Data Story*, Nancy Duarte): **Explorar** (contribuidor individual) → **Explicar** (conselheiro estratégico) → **Inspirar** (liderança, guia ação com dados).

### 6. O que são dados

- **Fontes:** primárias, secundárias, internas, externas.
- **Tipos:** numéricos (contínuos/discretos), categóricos (ordinais/nominais), textuais, data/hora, booleanos, visuais, geográficos.

### 7. Os 5 Vs do Big Data

**Volume, Velocidade, Variedade, Veracidade, Valor.**

- Processamento: **batch** (lotes, intervalos programados) x **streaming** (tempo real/near real-time).
- Estrutura: dados **estruturados** (tabelas), **semiestruturados** (JSON/XML/CSV), **não estruturados** (texto livre, imagem, áudio) — ~80-90% dos dados gerados são não estruturados, mas bancos relacionais (estruturados) ainda dominam em uso por serem "prontos para análise".

**Reforço pessoal (quiz) — Veracidade x Integridade:**
- **Integridade** = o *processo* preservou o dado corretamente? (erro de código/modelagem/ETL quebra integridade)
- **Veracidade** = o *dado em si* é verdadeiro/reflete a realidade? (pipeline perfeito, mas dado de origem é falso/impreciso — ex: cliente que mente na renda, sensor com leitura ruim, conta fake inflando métrica)

### 8. OKRs e KPIs

- **OKR** (Objectives and Key Results): Objetivo = O QUE alcançar; Resultados-Chave = COMO medir se chegou lá (específicos, mensuráveis, sem área cinzenta).
- **KPI**: indicador que mede progresso — tipos: **Produtividade**, **Qualidade**, **Capacidade**, **Estratégico**.
- **Erros comuns:** usar só métricas fáceis; medir o que não importa; **medir tarefa em vez de resultado** (reforço pessoal: "horas trabalhadas" é ruim porque mede esforço/input, não se o objetivo foi atingido, e é fácil de gamear); criar indicador sem adesão da equipe; buscar indicador perfeito (não existe).

### 9. Soft skills e técnicas analíticas (pensamento crítico / resolução de problemas)

| Técnica | Para que serve |
|---|---|
| **PDCA** (Plan-Do-Check-Act) | Ciclo de melhoria contínua de processo |
| **5 Porquês** | Achar a causa raiz de UM problema específico, perguntando "por quê" repetidamente |
| **5W2H** | Checklist (What, Why, Who, Where, When, How, How much) para planejar/detalhar uma ação |
| **Diagrama de Ishikawa** (espinha de peixe, 6 Ms) | Diagnosticar causas de **um problema já escolhido**, categorizando por método, mão de obra, máquina, material, medida, meio ambiente |
| **Matriz GUT** (Gravidade, Urgência, Tendência) | **Priorizar entre vários problemas diferentes** já identificados |
| **Diagrama de Pareto** (80/20) | Identificar quais poucas causas respondem pela maior parte do problema |
| **Brainstorming** | Gerar ideias livremente, sem pré-julgamento, para depois filtrar |
| **Fluxograma** | Mapear visualmente o caminho causa → efeito → solução |

**Reforço pessoal (quiz) — GUT x Ishikawa:** fluxo típico é **GUT primeiro** (decidir qual problema atacar, entre vários) → **Ishikawa depois** (investigar a causa raiz do problema escolhido).

### 10. Ética no mundo de dados

- Cuidado com **viés estrutural** ao clusterizar/prever comportamento de grupos sociais (ex: análise "purista" pode reforçar desigualdade existente nos dados históricos em vez de corrigi-la).
- **Segurança da informação:** identificar dado sensível/estratégico, evitar vazamento e julgamento de valor.

### Material complementar

#### App de Materiais (workflow local) — criado nesta pasta

Para estudar os PDFs/MDs do curso sem depender de pastas, montei um app HTML local sem build:

- **Stack:** `index.html` (design Apple — sidebar translúcida `backdrop-filter: blur`, springs `cubic-bezier(0.25,0.46,0.45,0.94)`, feedback no `pointerdown`, tipografia IBM Plex, dark mode + `prefers-reduced-motion`) lê o array `FILES` + `marked.js` + `motion` (CDN). Sem Node/npm.
- **Servidor:** `python server.py` → `http://localhost:8765` (abre o navegador; precisa ser `http://`, não `file://`, por CORS).
- **Sync automático:** `python .opencode/skill/ae_materials_app/sync.py` varre pastas de módulos (`.md`/`.txt`, **exclui PDFs** pra evitar duplicatas) e regenera `FILES` + `files.json`. A ordem dos itens vem de um `MODULE_TITLES` no script.
- **Cuidados aprendidos:** `python -m ae_materials_app.sync` NÃO funciona (módulo fora do path) → usar o caminho direto `.opencode/skill/ae_materials_app/sync.py`. Atenção a encoding (UTF-8) no terminal Windows/PowerShell.
- **Sidebar colapsável:** botão `⟨/⟩` no header (mesmo tamanho do toggle de tema) ou `Ctrl+B` recolhe pra um **rail de 64px com chips por módulo** (nº do módulo); clicar num chip navega pro 1º material sem expandir. Arrastar a borda direita expande/recolhe (usa `setPointerCapture`). Estado salvo em `localStorage`.
- **Navegação flutuante:** barra fixa no rodapé com **‹ Anterior / Próximo ›** (~50% da largura cada), sempre visível (sem precisar scrollar até o fim); setas `←`/`→` também navegam. Títulos quebram linha em vez de truncar.
- Ao adicionar novo material de curso: colocar na pasta do módulo → rodar o sync → `git commit`.

#### Git local da pasta de estudo (inicializado)

- **`git init`** na raiz `Formação AE/` → primeiro commit `chore: sync + Apple design system`.
- **`.gitignore`** implementado: NÃO versiona `*.pdf`, `*.zip`, `Desafio/Exemplos repo banvic/` (cópias de terceiros), `.agents/` (skills instalados) e artefatos de build (`target/`, `dbt_packages/`, etc.).
- Commits convencionais: `feat:` / `fix:` / `refactor:` / `test:` / `docs:` / `chore:`.

---

#### Linux / Ubuntu — visão geral

- **Significado de "Ubuntu":** palavra zulu/xhosa (sul da África) — "humanidade para os outros" / "eu sou porque nós somos". Nome escolhido pela Canonical para refletir a filosofia do software livre: construído coletivamente, acessível a todos.
- **História do Linux:**
  - 1983 — Richard Stallman inicia o **Projeto GNU** (sistema livre compatível com Unix), faltando o kernel.
  - 1991 — **Linus Torvalds** (estudante em Helsinki) cria, como hobby, um kernel inspirado no MINIX; anuncia no Usenet.
  - Kernel liberado sob **licença GPL** → permite uso, estudo, modificação e redistribuição livre → cresce de forma colaborativa mundial.
  - Kernel Linux + ferramentas GNU = "GNU/Linux" (nome popular encurtou para "Linux").
  - Surgem distribuições (**distros**): Debian (1993), Red Hat, Slackware, etc.
  - 2004 — **Mark Shuttleworth** cria a **Canonical** e lança o **Ubuntu**, baseado no Debian, com foco em acessibilidade para o usuário comum.
- **Instalação:** dual boot, VM (VirtualBox/VMware), live USB, ou **WSL** (Windows Subsystem for Linux — mais provável no meu caso).
- **Comandos principais:**
  - Navegação: `pwd`, `ls`/`ls -la`, `cd`
  - Arquivos: `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`, `nano`/`vim`
  - Permissões: `chmod`, `chown`, `ls -l`
  - Busca: `find`, `grep`
  - Pacotes (APT): `sudo apt update`, `sudo apt install`, `sudo apt upgrade`
  - Processos: `ps aux`, `top`, `kill`
  - Encadeamento: `|` (pipe), `>` (redireciona), `>>` (acrescenta)
- **Rodar programas com o terminal livre:**
  - `comando &` → roda em background, libera o terminal
  - `jobs` / `fg` / `bg` → gerencia processos em background da sessão
  - `Ctrl+Z` → pausa processo em primeiro plano
  - `nohup comando &` → continua rodando mesmo se a sessão/terminal fechar
  - `disown` → desvincula processo já em background da sessão atual
  - `screen` / `tmux` → sessão persistente (útil em servidores via SSH — ex: rodar `dbt run` longo sem perder o processo se a conexão cair)
- **htop:** monitor de processos interativo (melhoria do `top`).
  - Instalar: `sudo apt install htop`
  - Usar: `htop` → setas navegam, `F5` visão em árvore, `F6` ordena por coluna, `F9` mata processo, `F4` filtra, `q` sai.

#### Shell Scripting — Curso Bóson Treinamentos (playlist, 31 vídeos)

**Fundamentos e variáveis**
- Script = arquivo de texto com comandos + shebang `#!/bin/bash` na primeira linha. Rodar: `chmod +x script.sh && ./script.sh` (ou `bash script.sh`).
- Variável de shell (`VAR=valor`, só na sessão) x variável de ambiente (`export VAR=valor`, visível por processos filhos). `env` lista, `unset VAR` remove.
- Arrays: `frutas=(maçã banana uva)`; `${frutas[0]}` (elemento), `${frutas[@]}` (todos), `${#frutas[@]}` (quantidade).
- **Alias** = atalho de texto simples (`alias ll='ls -la'`); **função** = bloco reutilizável com parâmetros/lógica (`minha_func(){ echo $1; }`).
- Arquivos de config: `/etc/profile` (todos os usuários, no login) → `~/.bash_profile`/`~/.profile` (login do usuário) → `~/.bashrc` (toda sessão interativa não-login — onde ficam aliases/variáveis pessoais).

**Scripts básicos e I/O**
- `echo -n` (sem quebra de linha), `echo -e` (interpreta `\t`, `\n`).
- Atribuição sem espaço no `=`: `nome="Carlos"`; uso: `$nome` ou `${nome}`.
- Command substitution: `` `comando` `` (sintaxe antiga) ou `$(comando)` (preferível) — captura saída de um comando numa variável.
- Redirecionamento: `>` (sobrescreve), `>>` (acrescenta), `<` (entrada), `2>` (só erros/stderr), `&>` (saída + erro).

**Cálculos**
- Bash só faz inteiros nativamente: `$((5 + 3))`, `let x=5+3`.
- Para decimais, usa `bc`: `echo "10.5 / 3" | bc -l`.

**Status e condicionais**
- Todo comando retorna código em `$?` (0 = sucesso); `exit N` encerra o script com código customizado.
- `if [ condição ]; then ... elif [ ... ]; then ... else ... fi`.
- `test`/`[ ]`: numéricos `-eq -ne -gt -lt -ge -le`; strings `= != -z -n`; arquivos `-f -d -e -r -w -x -s`.
- Condições compostas: `&&`/`||` (ou `-a`/`-o` dentro do `[ ]` clássico).
- `case "$var" in padrão1) ...;; padrão2) ...;; *) ...;; esac` — alternativa ao if/elif encadeado.

**Loops**
- `for item in lista; do ... done`.
- `while [ condição ]; do ... done` — repete **enquanto verdadeiro**.
- `until [ condição ]; do ... done` — repete **enquanto falso** (oposto do while).
- `for ((i=0; i<5; i++)); do ... done` — estilo linguagem C.

**Entrada de dados**
- Parâmetros posicionais: `$1`, `$2`, `$0` (nome do script), `$#` (qtd de args), `$@` (todos).
- `shift` — desloca os parâmetros posicionais para a esquerda (processa argumentos um a um em loop).
- `getopts` — trata flags de linha de comando no estilo `-a valor -b`.
- `read -p "texto" var` (lê do teclado com prompt), `read -s` (esconde input, ex: senha).

**Interfaces, funções e formatação**
- `whiptail` e `dialog` — criam telas/menus interativos em modo texto (TUI), comuns em instaladores/scripts de configuração de servidor.
- Função com retorno: `return` define apenas o **código de saída** (0-255); para "retornar" valor real, usa-se `echo` na função + captura com `$(minha_funcao)`.
- `break` — encerra um loop (`for`/`while`/`until`) antes da condição normal de parada.
- `printf "Nome: %s, Idade: %d\n" "Carlos" 30` — saída formatada, mais controle que `echo` (`%s` string, `%d` inteiro, `%f` float).

---

## Conexões com o Desafio Final (dbt + Power BI)

Notas soltas para guiar o desafio quando chegar a hora:

- O quadro "Plataforma de dados → Produtos de dados" do Módulo 1 já mapeia onde cada ferramenta entra: **dbt** = Engenheiro de Analytics (Data Marts), **Power BI** = Dashboards (Analista de Dados).
- Antes de modelar no dbt: repetir a etapa "Entender o problema de negócio" e já definir os **KPIs/OKRs** que o dashboard final vai responder — não começar pela tabela.
- O dashboard final do desafio deve ser **análise explicativa** (narrativa guiando a uma conclusão), não só um painel exploratório solto.
- `screen`/`tmux`/`nohup` (Linux) serão relevantes se algum processo de dbt/pipeline rodar em servidor remoto.

---

## Módulo 2 — SQL para Análise de Dados

Resumo técnico completo + guia prático ("como pensar na query") estão em `Resumo_Modulo_2_SQL.md` e `Decoreba_SQL.txt`.

**Núcleo:** ordem de escrita `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT` e de execução `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`.

- **JOINs (horizontal):** INNER (interseção), LEFT/RIGHT/FULL, CROSS (cuidado), SELF (hierarquia).
- **UNION (vertical):** `UNION` remove duplicatas, `UNION ALL` mantém; colunas precisam ser compatíveis.
- **Regra de ouro GROUP BY:** toda coluna do `SELECT` que não é agregação precisa estar no `GROUP BY`.
- **HAVING vs WHERE:** WHERE filtra linhas antes de agregar; HAVING filtra grupos depois (usa agregações).
- **Window functions:** `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG`/`LEAD`, `FIRST_VALUE`/`LAST_VALUE`; sintaxe `FUNÇÃO() OVER (PARTITION BY ... ORDER BY ...)`.
- **CTEs:** `WITH x AS (...), y AS (...) SELECT * FROM y;` — organiza passos e reutiliza.
- **Performance:** evitar `SELECT *`, filtrar cedo, indexar colunas filtradas, usar `EXPLAIN`.

---

## Módulo 3 — *(a preencher)*
