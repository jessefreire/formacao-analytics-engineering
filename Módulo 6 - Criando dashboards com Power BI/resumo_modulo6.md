# Resumo — Módulo 6: Dashboards com Power BI

## 1. Ferramentas de Business Intelligence (BI)

**Business Intelligence** é uma coleção de serviços de software, processos, técnicas e ferramentas que permitem coletar, organizar, analisar e apresentar dados relevantes para a tomada de decisões estratégicas. As ferramentas de BI também são chamadas de **Ferramentas de Suporte à Decisão** — elas não dizem o que fazer, mas oferecem os meios para analisar dados e gerar insights.

| Conceito | Definição |
|---|---|
| **BI** | Envolve integração, armazenamento, modelagem, exploração e compartilhamento de dados |
| **Dashboard** | Forma gráfica e interativa de visualizar dados — é parte da solução de BI, não o todo |

O BI fica responsável pela **visualização, apresentação, análise e compartilhamento** — enquanto a coleta, limpeza e tratamento acontecem no Modern Data Stack (ETL/ELT).

**Principais ferramentas do mercado:** Power BI (Microsoft), Tableau, Qlik, Looker, Metabase. A escolha depende de necessidades de processamento, preço, opções de visualização e personalização.

## 2. Componentes do Power BI

O Power BI tem dois componentes principais:

| Componente | Descrição |
|---|---|
| **Power BI Desktop** | Aplicativo gratuito para Windows. Cria modelos semânticos e relatórios (.pbix). Não precisa de conta. Algumas funcionalidades só existem aqui. |
| **Power BI Service** | Plataforma online (SaaS) em app.powerbi.com. Publica, compartilha e distribui relatórios. Requer conta corporativa/estudantil + licença. |

**Fluxo típico:** Desktop (conectar dados → criar relatório) → Publicar no Service → Distribuir aos consumidores.

### Abas do Power BI Desktop

| Aba | Função |
|---|---|
| **Relatório** | Cria visualizações/dashboards (onde passa mais tempo) |
| **Dados** | Visualiza tabelas, colunas e medidas |
| **Modelo** | Camada semântica — relacionamentos, nomes, descrições |

### Menus laterais (na aba Relatório)

- **Dados** — tabelas, colunas e medidas disponíveis
- **Visualizações** — criar visual (eixos) + formato (personalização)
- **Filtros** — a nível de visual, página ou relatório (cuidado: não são explícitos ao usuário)

### Workspaces no Power BI Service

- **"Meu workspace"** — ambiente pessoal para testes e desenvolvimentos
- **Workspaces compartilhados** — para grupos (requer licença Pró ou Premium)

**RLS (Row Level Security):** segurança a nível de linha. Configura-se as regras no Desktop (Modelagem) e finaliza-se no Service (atribuindo usuários).

**Dashboards vs Relatórios no Service:** Dashboard no Service é um painel de alto nível que agrupa relatórios (diferente do dashboard como conceito geral).

## 3. Fluxo de dados e modelo semântico

### Fluxo de dados (Data Flow)

Funcionalidade do **Power BI Service** (online) que permite criar e gerenciar fluxos de informação. Usa **linguagem M** (Power Query online).

**Benefícios:**
- Reutilização de tabelas em vários relatórios
- Menor contato de desenvolvedores BI com o DW (restrição de acesso)
- Menor taxa de atualização redundante (ex: dimensão de datas)

**Máxima de Matthew Roche (Microsoft):** *"Dados devem ser transformados o mais próximo da fonte possível e o tão próximo da visualização quanto necessário."*

**O que fazer no fluxo de dados:** mudanças de tipo, tradução de nomes técnico → comercial, ajustes simples.
**O que NÃO fazer:** regras de negócio complexas (deixar para o ELT/DW).

### Modelo semântico (antigo "conjunto de dados")

É onde os dados estão armazenados no relatório. Divide-se em duas caixas: **modelo semântico** (dados + regras) e **relatório** (gráficos).

**Dois cenários de uso:**
1. **Com fluxo de dados:** modelo semântico usa o fluxo como fonte (Desktop → conecta ao Data Flow)
2. **Sem fluxo de dados:** modelo semântico consolida tudo no Power Query (caso de empresas menores)

**No modelo semântico criamos:**
- Colunas calculadas e medidas em DAX
- Relacionamentos entre tabelas
- Tabelas calculadas

Quando há apenas um relatório vinculado, modelo semântico + relatório = mesmo arquivo .pbix.

## 4. Modo de armazenamento dos dados

| Modo | Descrição | Quando usar |
|---|---|---|
| **Importação** | Cópia dos dados comprimidos no modelo (VertiPaq compacta ~10x). Dados armazenados em cache. | Padrão. Suporta todas as fontes, DAX e M. Até 48 atualizações/dia. |
| **DirectQuery** | Sem cópia — consultas em tempo real no DW. Metadados apenas. | Dados > 1GB (capacidade compartilhada), necessidade de tempo real, restrição de segurança. |
| **Duplo (Dual)** | Combinação dos dois — algumas tabelas importadas, outras DirectQuery. | Cenários com tabelas volumosas + tabelas que precisam de velocidade. |

### Limitações da Importação que levam ao DirectQuery

1. **Tamanho:** modelo compactado não pode passar de 1GB (capacidade compartilhada)
2. **Atualização:** limite de 8x (compartilhada) ou 48x (dedicada) por dia
3. **Segurança:** quando não é permitido ter cópia local dos dados

### Árvore de decisão

1. Preciso de fontes específicas? **Sim → Importação**
2. Preciso de todas as funções DAX, M e tabelas calculadas? **Sim → Importação**
3. Preciso de atualização em tempo real? **Sim → DirectQuery**
4. Preciso de espaço para grandes volumes? **Sim → Duplo** / **Não → Importação**

## 5. Estrutura das tabelas — Esquema Estrela (Star Schema)

O Power BI tem por definição que a melhor estrutura é o **Esquema Estrela**:
- **Tabelas fato:** contêm valores de eventos (transações, propostas) — granularidade fina
- **Tabelas dimensão:** contêm detalhes descritivos (clientes, agências, datas) — granularidade grossa
- **Ligação:** chaves (PK na dimensão → FK na fato)

### Tipos de relacionamento

| Tipo | Cardinalidade | Recomendação |
|---|---|---|
| **Um para muitos (1:*)** | 1 linha da dimensão → N linhas na fato | **Recomendado** — padrão do Star Schema |
| **Um para um (1:1)** | 1 linha → 1 linha (ambos exclusivos) | **Não recomendado** — preferir consolidar tabelas |
| **Muitos para muitos (*:*)** | Sem valores exclusivos em nenhum dos lados | **Não recomendado** — gera ambiguidade. Usar Bridge Table |

### Direção do filtro cruzado

| Direção | Descrição |
|---|---|
| **Única** (padrão) | Dimensão filtra a fato, mas fato não filtra dimensão. Seta aponta da dimensão para a fato. |
| **Ambas** (bidirecional) | Dimensão filtra fato e fato filtra dimensão. Permite análises mais complexas, mas pode gerar ambiguidade e perda de desempenho. |

**Dica:** acompanhe a seta do relacionamento para entender a direção do filtro.

### Dimensão com função múltipla

Quando uma dimensão tem várias colunas se relacionando com a mesma fato (ex: data de criação e data de atualização). O Power BI permite apenas **um relacionamento ativo** entre duas tabelas (linha contínua). Os demais ficam inativos (linha pontilhada). Para usar relacionamentos inativos: função DAX **USERELATIONSHIP**.

**Funções DAX relacionadas:**
- **CROSSFILTER** — muda a direção do filtro cruzado entre duas tabelas
- **USERELATIONSHIP** — ativa um relacionamento inativo dentro de uma medida

## 6. Power Query e Linguagem M

**Power Query** é o editor de transformação de dados do Power BI (surgiu como suplemento do Excel). Interface: menus de edição + etapas aplicadas (histórico) + consultas (lateral esquerda).

**Linguagem M** (Power Query Formula Language): linguagem que manipula/modela dados. Toda alteração no Power Query gera código M, mas a interface abstrai a necessidade de escrever código manualmente.

**Quando usar Power Query:**
- Verificar/alterar tipo de dado (texto → número, moeda)
- Renomear colunas (linguagem técnica → linguagem de negócio)
- Excluir colunas desnecessárias

**Quando NÃO usar:**
- Regras de negócio complexas (deixar para o ELT/DW)
- Criação de colunas com lógica complexa (preferir dbt)

**Editor Avançado:** único local onde você precisa escrever M manualmente.

## 7. Linguagem DAX

**DAX** = Data Analysis Expressions. Linguagem para criar medidas, colunas calculadas, tabelas calculadas e RLS. Mais de 200 funções disponíveis.

### Medidas vs Colunas calculadas

| Aspecto | Medida | Coluna calculada |
|---|---|---|
| **Contexto** | Dinâmico — depende do filtro do visual | Estático — calculada a nível de linha |
| **Armazenamento** | Não ocupa espaço (só processada no visual) | Ocupa espaço (armazenada no modelo) |
| **Quando usar** | Agregações, cruzamentos entre tabelas | Classificações, categorizações simples |

**Medidas implícitas:** aplicadas diretamente nas colunas em visuais (soma, contagem, média).
**Medidas explícitas:** cálculos escritos em DAX (recomendados para análises completas).

**Boa prática:** criar uma **tabela virtual** (ex: "Medidas") para centralizar todas as medidas do modelo.

### Funções DAX principais

| Função | Descrição |
|---|---|
| **CALCULATE** | Avalia uma expressão em um contexto modificado por filtros. Uma das mais importantes. |
| **FILTER** | Cria uma tabela filtrada a partir de condições. Usada dentro do CALCULATE para filtros complexos. |
| **DIVIDE** | Divide valores de forma segura (trata divisão por zero automaticamente). |
| **SUM, AVERAGE, COUNT, DISTINCTCOUNT** | Funções de agregação básicas. |
| **USERELATIONSHIP** | Ativa relacionamento inativo dentro de uma medida. |
| **CROSSFILTER** | Muda a direção do filtro cruzado entre tabelas. |

### Variáveis em DAX

Declaradas com **VAR**, finalizadas com **RETURN**. Benefícios:
- Melhora de desempenho (não recalcula a mesma medida)
- Melhora a legibilidade
- Simplifica a depuração

### Classificações de funções DAX

| Categoria | Exemplos |
|---|---|
| **Agregação** | SUM, AVERAGE, COUNT, MIN, MAX |
| **Data e hora** | DATE, YEAR, MONTH, DATEDIFF |
| **Inteligência temporal** | FIRSTDATE, PREVIOUSYEAR, SAMEPERIODLASTYEAR |
| **Lógicas** | IF, SWITCH (equivale ao CASE-WHEN do SQL) |
| **Relação** | USERELATIONSHIP, CROSSFILTER |
| **Iteradoras ("X")** | SUMX, MINX, MAXX, AVERAGEX, COUNTX, RANKX — operam a nível de linha e coluna |

## 8. Criação de relatórios

### Estrutura de um dashboard

1. **Cabeçalho:** logo, título, última data de atualização
2. **Filtros (segmentações):** data, agência, cliente, tipo de transação + botão "limpar filtros"
3. **Indicadores (cards):** total transacionado, quantidade de transações, média, percentuais
4. **Séries temporais:** gráfico de linhas (valor por ano/mês)
5. **Detalhamento:** matriz com agência, UF, valores agregados

### Boas práticas de visualização

- **Gráfico de linhas:** para séries temporais (ideia de continuidade)
- **Gráficos de barras horizontais:** para ranking
- **Matriz:** para detalhamento tabular com múltiplas medidas
- **Segmentação de dados:** para filtros explícitos ao usuário (preferir aos filtros do menu lateral)
- **Botões de navegação:** para transição entre páginas
- **Botão "limpar segmentações":** ponto de partida para o usuário

### Páginas do relatório (exemplo BanVic)

| Página | Conteúdo |
|---|---|
| **Visão Geral** | Cards de KPI, gráfico de linhas temporal, matriz por agência |
| **Tipos de transação** | Gráficos de barra horizontal (contagem e valor por tipo) |

## 9. Otimização de modelos

### Premissas fundamentais

1. **Star Schema** — cardinalidade 1:muitos performa melhor
2. **Analisar medidas e visuais** — usar o **Performance Analyzer** (Desktop)
3. **Desabilitar data/hora automática** — evita tabelas calculadas ocultas desnecessárias
4. **Minimizar tabelas e colunas calculadas** — ocupam espaço na memória

### Estratégias de redução de dados

| Estratégia | Descrição |
|---|---|
| **Filtragem vertical** | Remover colunas desnecessárias (preferir na origem/Power Query) |
| **Filtragem horizontal** | Remover linhas desnecessárias (limitar histórico em tabelas fato) |
| **Agrupamento e resumo** | Reduzir granularidade das tabelas (agregar antes de importar) |
| **Trocar para DirectQuery** | Quando o tamanho do modelo é o problema (custo: menor desempenho) |

### Performance de visuais e DAX

- **Visuais:** menos é mais. Remover visuais que não agregam valor. Preferir design externo (Figma) com camadas consolidadas.
- **DAX:** uma consulta não deve levar mais que **0,12 segundos**. Otimizar se estiver acima.

---

## Pontos de reforço pessoal

- **BI x Dashboard:** BI é o guarda-chuva (integração, armazenamento, modelagem, exploração, compartilhamento). Dashboard é só a parte visual.
- **Importação x DirectQuery:** Importação = cópia em cache (rápido, limitado por tamanho). DirectQuery = consulta em tempo real (ilimitado, mais lento).
- **Medida x Coluna calculada:** Medida = dinâmica, não ocupa espaço, depende do filtro. Coluna calculada = estática, ocupa espaço, calculada por linha.
- **Direção única x Ambas:** Única = dimensão filtra fato (padrão, seguro). Ambas = bidirecional (mais poder, risco de ambiguidade e perda de desempenho).
- **Fluxo de dados x Modelo semântico:** Fluxo = camada de consolidação no Service (reutilização). Modelo semântico = camada de dados no Desktop (relacionamentos + DAX).
- **Star Schema:** Sempre preferir 1:muitos. Evitar 1:1 (consolidar) e *:* (usar Bridge Table).

---

## Conexões com o Desafio Final (dbt + Power BI)

- **dbt → Power BI:** Os models do dbt (staging → intermediate → marts) são a fonte de dados do Power BI. O dashboard se conecta nas tabelas fato e dimensão do esquema estrela construído no dbt.
- **Star Schema no dbt = Star Schema no Power BI:** A modelagem dimensional que você construir no dbt (facts + dims) é exatamente o que o Power BI espera receber. Se a modelagem estiver certa no dbt, os relacionamentos no Power BI são automáticos.
- **Transformação no dbt, não no Power BI:** Toda regra de negócio, limpeza e enriquecimento deve estar no dbt. O Power BI recebe dados prontos e foca em visualização e medidas DAX.
- **Medidas DAX vs métricas dbt:** Métricas agregadas (totais, médias, percentuais) são feitas em DAX no Power BI. Transformações de linha e regras de negócio ficam no dbt.
- **Otimização:** Se o modelo dbt estiver bem construído (Star Schema, granularidade correta), o Power BI terá melhor performance — menos necessidade de DirectQuery ou tabelas calculadas.
- **Desafio final:** O dashboard Power BI é a entrega final do desafio. Ele deve ser **análise explicativa** (narrativa guiando a conclusão), com KPIs claros, filtros interativos e visualizações que gerem insights sobre os dados do BanVic.
