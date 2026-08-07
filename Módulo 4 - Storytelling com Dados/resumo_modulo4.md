# Resumo — Módulo 4: Storytelling com Dados

## 1. O que é Data Storytelling?

**Data storytelling** = transformar dados em histórias palpáveis para gerar valor e tomada de decisão. Baseado em *Data Story* (Nancy Duarte) e *Storytelling com Dados* (Cole Knaflic).

- **"V" de Valor** (Big Data): está diretamente ligado à visualização de dados — só se gera valor quando a informação é comunicada de forma convincente.
- **Dado não fala por si**: precisa de um contador de histórias.
- **O cérebro processa histórias**, não números brutos — histórias são mais memoráveis.
- **Não somos bons naturalmente** com storytelling de dados: aprendemos palavras (português) e números (matemática) separadamente, não juntos.
- **O processo é mais criativo que analítico**: a ferramenta facilita o gráfico, mas entender qual gráfico, em qual contexto e para qual público exige esforço criativo.

**Exemplo progressivo (BanVic):**
1. "Novas contas giram em torno de 70" → sem contexto, não diz nada.
2. "2021 teve 70 contas, aumento de 32%" → melhor, mas ainda faltam referências.
3. "2021: 70 contas, +32% vs 2021 anterior (53 contas), na agência 07 (maior volume)" → história completa, cérebro memoriza.

---

## 2. Contexto da Entrega

Três perguntas balizadoras:

### Pergunta 1: Qual é a análise que pretendemos fazer?

| Tipo | Objetivo | Exemplo |
|---|---|---|
| **Exploratória** | Descobrir padrões, buscar "pérolas" entre as ostras | Análise de bastidor, brainstorming |
| **Explanatória** | Comunicar informação já lapidada | Dashboard, relatório |

**Análise explanatória** se divide em:
- **Dashboards**: painéis interativos, atualização periódica (D-1, tempo real), exigem analista para interpretar → suporte à decisão.
- **Relatórios**: arquivos estáticos e estruturados, período específico, detalhado com cruzamentos e conclusões → não exige interpretação (autoexplicativo).

| Aspecto | Dashboard | Relatório |
|---|---|---|
| **Complexidade** | Menor (primeiro momento) | Maior (profundidade) |
| **Flexibilidade** | Maior (interativo, cliques) | Menor (estático) |
| **Replicabilidade** | Menor controle do dev | Difícil de replicar |
| **Melhor para** | Análise exploratória | Análise explanatória |

### Pergunta 2: Para quem se destina a análise?

**Conheça o público** — formato, detalhamento e comunicação mudam completamente.

**Por formato de entrega:**
- **Apresentação ao vivo**: controle alto, feedback em tempo real, menor detalhamento necessário.
- **Email/relatório/dashboard**: sem feedback em tempo real → **análise precisa ser autossuficiente** (tira todas as dúvidas dentro do documento).

**Por nível organizacional:**

| Nível | Foco | Detalhe | Volume |
|---|---|---|---|
| **Operacional** | Análise diária, exploração | Alto — métricas, gráficos, tabelas, múltiplas páginas | Maior |
| **Tático** | Médio prazo, indicadores para decisão | Médio — guiado para exploração, mais condensado | Médio |
| **Gerencial** | Visão resumida, KPIs direcionados | Baixo — poucos gráficos, sucinto, rápido | Menor |

> **Erro comum**: entregar dashboard operacional para gerência (ou vice-versa) → não funciona.

### Pergunta 3: O que esperamos responder?

- Clareza sobre a **pergunta sendo respondida** — toda entrega precisa ter isso explícito.
- **Técnicas analíticas** ajudam: 5 porquês, 5W2H (O quê, Onde, Quanto, Quando, Quem, Como, Por que).
- Quanto mais longe do usuário, mais autossuficiente a análise precisa ser.

---

## 3. Narrativa e Comunicação

**Comunicar eficientemente não é fazer gráficos bonitos** — é passar a quantidade certa de informação, da forma correta, para a pessoa certa (Nancy Duarte).

**Perguntas balizadoras:**
1. Qual a história que queremos contar?
2. Qual a estrutura desta história?

**Estrutura de 3 atos (como ficção):**

| Ato | Função | No dashboard |
|---|---|---|
| **Começo introdutório** | Prender atenção | **KPIs** (cards) — indicadores-chave iniciais |
| **Meio explicativo** | Explicar como chegou aos valores | Gráficos de linha, barra, pizza, detalhamentos |
| **Final conclusivo** | Tirar dúvidas, granularidade | Tabelas detalhadas, menor granularidade |

**Etapa 0 — A capa:**
- Título, logo, navegação, data de atualização.
- Ambientação do usuário ("onde estou?").

**Importância da coerência:**
- Informações desconexas = números sem contexto → não geram insights.
- A narrativa é o **fio condutor** que une os pontos da análise.
- Pode haver variações (vertical/horizontal, múltiplas páginas) — depende do projeto.

---

## 4. Escolha do Elemento Gráfico

**Princípio fundamental:** "Menos é mais" — objetivo é facilitar a tomada de decisão. Use gráficos que todos entendam.

### Gráfico de Linhas
- **Uso:** dados ao longo do tempo (séries temporais) — dias, meses, anos.
- **Indicações:** tendências, previsões, anomalias temporais.
- **Eixo x** = tempo, **eixo y** = valores.
- **Pegadinha — Gráfico Espaguete**: muitas categorias → linhas sobrepostas → ilegível. **Solução:** filtrar principais ou destacar uma linha (cor viva/mais grossa) e cinza para as demais.
- **NÃO usar** para enfatizar quantidades/categorias (use barras).

### Gráfico de Barras
- **Uso:** dados categóricos, comparações entre categorias.
- **Por que funciona:** cérebro calcula facilmente diferenças de comprimento.
- **Tipos:**
  - **Vertical**: ênfase no quantitativo, categorias curtas.
  - **Horizontal**: melhor para ranking (leitura em Z), nomes longos.
  - **Empilhada**: comparação de totais + subcomponentes (limitada — sem base zero após a primeira).
  - **Empilhada 100%**: dois subcomponentes, base zero dupla.
  - **Agrupada**: base zero para todas, mas cuidado com excesso de séries.
- **Pegadinha**: eixo y SEMPRE começa em zero — senão distorce proporções.

### Tabelas e Textos (Indicadores)
- **Tabelas**: interagem com sistema verbal, versáteis.
  - Usos: público misto, grandezas não comparáveis, complemento ao final do dashboard.
  - **Design:** maximizar **relação sinal-ruído** (Tufte) — bordas finas/cinza, foco nos dados.
  - **Heatmap**: gradiente de cor em coluna → realça padrões, destaca maior/menor.
  - **Ícones/cores**: destaque de valores especiais (metas, campeões).
- **Textos/Indicadores**: no início do dashboard (região superior), mostram ponto de partida.
  - Completam gráficos (ex: variação percentual ao lado de um gráfico de linhas).

### Gráfico de Pizza / Rosca
- **Uso:** comparar partes com o todo (100%).
- **Funciona bem com**: categorias dicotômicas (Sim/Não, Digital/Física) ou 2-3 fatias.
- **EVITAR:**
  - Muitas categorias (fatias pequenas → ilegível).
  - Categorias de tamanho semelhante (use barras).
  - Comparação entre múltiplos gráficos de pizza.
  - Somatório ≠ 100%.
- **Por que evitar**: cérebro calcula área de círculo com mais dificuldade que comprimento de barra.

### Mapa de Árvore (Treemap)
- **Uso:** partes com o todo, hierarquia (3-4 segmentos).
- Estrutura: retângulos (ramificações) contendo retângulos menores (folhas).
- **Cuidado**: público pode não conhecer; dados muito semelhantes dificultam comparação.

### Gráficos de Mapas
- **Quando usar**: dados geográficos (cidade, estado, país, lat/long).
- **Tipos:**
  - **Coroplético**: cores por região (distribuição de variáveis, renda, população).
  - **Marcadores**: pontos específicos (endereços, concentrações).
- **Limitação**: comparações imprecisas — para análise profunda, use gráficos/tabelas junto.
- **Posição no dashboard**: entre KPIs e gráficos de linha (começo/meio).

### Gráfico de Dispersão e Bolhas
- **Dispersão (scatterplot)**: relação entre **dois valores numéricos** (x e y).
  - Usos: correlação, agrupamentos, padrões em grandes datasets.
  - **Pegadinha**: **correlação ≠ causalidade** — uma coisa não necessariamente causa a outro.
  - Nicho: público pode não conhecer → usar para exploração, depois traduzir em visual mais simples.
- **Bolhas**: como dispersão + **terceira dimensão** (tamanho da bolha = ex: quantidade de clientes).

---

## 5. Transformando seus Gráficos (Data-Ink)

**Data-Ink (Edward Tufte):** maximizar relação dados/tinta.
> Fórmula: `Data Ink = Tinta dos dados / Total de tinta utilizada no gráfico`

- **Sinal** = informação que queremos comunicar.
- **Ruído** = elementos que dificultam a mensagem.

**Dicas práticas:**
- Remova bordas grossas, sombras, elementos decorativos desnecessários.
- Combine tipos de gráficos (barras + linhas) para simplificar.
- Use título + subtítulo explicativos (não genéricos) → situam o usuário.
- **Eixos vs rótulos:**
  - Eixos → mostrar tendências/padrões.
  - Rótulos → valores numéricos específicos.
- Legendas são essenciais → usuário não está na mesma sala que você.
- **Seja o primeiro avaliador**: coloque o chapéu do usuário, pergunte se está claro.
- Não tenha ciúmes de suas criações — simplifique sempre que possível.

---

## 6. Ética na Visualização de Dados

Baseado em *Algoritmos de Destruição em Massa* (Cathy O'Neil).

**Dois motivos principais:**
1. Responsabilidade do analista sobre informações distribuídas.
2. Evitar visuações ruins que gerem insights incorretos/falaciosos.

**Princípios:**
- **Imparcialidade**: evitar vieses em visuais e insights.
- **Transparência**: não manipular dados para favorecer narrativa.
- **LGPD**: conhecer e seguir regras de coleta/tratamento/armazenamento de dados pessoais.
- **Impacto social**: análises podem afetar milhões — modelos mal concebidos reforçam desigualdades.
- **Ciclo vicioso de feedback**: rankings podem ser inflados, gerando desconfiança (ex: ranking de universidades nos EUA).

**Nunca:**
- Inflar informações para distorcer realidade.
- Usar gráficos exacerbados que não refletem os dados.
- Esconder metodologia ou limitações dos dados.

---

## 7. Qual análise devo fazer? (Fluxo completo)

**Três etapas (como degraus de uma escada):**

| Etapa | Tipo | Característica |
|---|---|---|
| 1. **Reuniões/Brainstorming** | Exploração de ideias | Não entregável, criativa, sem julgamento |
| 2. **Dashboard Exploratório** | Detectar tendências | Gráficos complexos, SQL/Python, pode não chegar ao usuário final |
| 3. **Dashboard Declarativo** | Visão consolidada | Simples, direto, narrativa clara — apresenta as "pérolas" |

- **Exploratório**: abre as ostras, encontra pérolas, pode ser complexo, volume alto de gráficos.
- **Declarativo**: traduz complexidade em visualizações acessíveis, estático (filtros de página), afirma contextos.
- **Ciclo**: respostas dos declarativos geram novas perguntas → novos exploratórios.

---

## Pontos de reforço pessoal

- **Correlação ≠ Causalidade**: gráfico de dispersão mostra relação, não que uma variável causa a outra.
- **Eixo de barras sempre inicia em zero**: distorcer a base é manipulação visual.
- **Pizza só funciona com 2-3 categorias**: muitas fatias → use barras.
- **Dashboard ≠ Relatório**: dashboard = interativo/periódico; relatório = estático/período fixo.
- **Análise Explanatória x Exploratória**: explanatória é o produto final (o público vê); exploratória é bastidor.
- **Gráfico espaguete**: muitas linhas → destaque apenas o principal.
- **"Menos é mais"**: Data-Ink — maximize dados, minimize ruído.
- **Coroplético é bonito, mas impreciso**: para comparação exata, complemente com tabelas/gráficos.

---

## Conexões com o Desafio Final (dbt + Power BI)

- **dbt** = camada de transformação dos dados (staging → marts) → garante que os dados cheguem **lapidados** ao Power BI.
- **Power BI** = camada de visualização → aqui entra o storytelling: escolher gráficos certos, estrutura de 3 atos, Data-Ink.
- O dashboard do desafio deve ser **análise declarativa** (explanatória): narrativa guiando à conclusão, autoexplicativo.
- Lembrar dos **3 públicos** (operacional/tático/gerencial) → desafio é provavelmente **gerencial** (KPIs sucintos).
- Aplicar **Data-Ink** no Power BI: remover bordas, poluição visual; usar cores com propósito.
- Garantir **ética**: não distorcer eixos, não manipular dados do BanVic para favorecer narrativa.
- A **estrutura de 3 atos** se aplica diretamente ao layout do Power BI:
  - KPIs no topo (começo introdutório).
  - Gráficos no meio (meio explicativo).
  - Tabela detalhada ao final (final conclusivo).
