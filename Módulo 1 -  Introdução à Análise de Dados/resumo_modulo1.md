# Resumo — Módulo 1: Introdução à Análise de Dados

## 1. O que é a área de dados

Conjunto de atividades, processos, ferramentas e profissionais dedicados a coletar, armazenar, organizar, analisar, distribuir e utilizar os dados de uma empresa. Importa porque permite decisões baseadas em evidência (não em achismo), reduzindo riscos, otimizando recursos e ajudando a cumprir normas de segurança/privacidade.

Usamos dados para três coisas: entender o passado, avaliar o presente e projetar o futuro.

## 2. Os papéis da área de dados

| Papel | Foco |
|---|---|
| **Arquiteto de Dados** | Define políticas, ferramentas e estratégia de modelagem — traduz negócio em requisitos técnicos |
| **Engenheiro de Dados** | Constrói e mantém infraestrutura de ingestão/armazenamento |
| **Engenheiro de Analytics** | Transforma dados brutos, constrói o Data Warehouse, garante consistência (aqui entra o dbt) |
| **Analista de Dados** | Transforma e analisa dados para gerar insights e decisões |
| **Cientista de Dados** | Aplica estatística/ML para modelos preditivos |
| **Engenheiro de ML** | Leva modelos de ML para produção |

Esses papéis não são isolados — se comunicam formando equipes multidisciplinares. Uma forma de organizar isso é separar **plataforma de dados** (infraestrutura: ingestão, armazenamento, entrega) de **produtos de dados** (o que sai daí: elementos no DW, relatórios/dashboards, modelos de previsão).

## 3. O perfil do Analista de Dados

Tripé de habilidades (visualizado como diagrama de Venn):
- **Conhecimento matemático/estatístico**
- **Programação**
- **Conhecimento de negócio**

A combinação plena dos três = Ciência de Dados. Cada função da área é uma especialização parcial desse tripé (ex: Eng. Analytics pesa mais para programação + negócio; Analista de Dados pesa mais para negócio + estatística).

**Soft skills mais cobradas:** comunicação, escuta ativa, pesquisa (fazer a pergunta certa), escrita, resolução de problemas, trabalho em equipe, criatividade, gestão do tempo, ética/governança, inteligência emocional, pensamento estratégico.

## 4. Processo de trabalho (CRISP-DM adaptado)

1. **Entendimento do problema de negócio** — que decisão precisa ser tomada? que produto/solução a pessoa precisa?
2. **Entendimento dos dados e do usuário** — quem é o usuário, como decide hoje, quais dados existem e sua qualidade
3. **Preparação/prototipação/documentação (catalogação)**
4. **Exploração** — estatística descritiva + visualização para gerar hipóteses
5. **Conclusões** — refinar e validar com o negócio
6. **Comunicação** — apresentar de forma que sustente a decisão, sem distorção

É **cíclico**, não linear — sempre se volta a etapas anteriores.

## 5. Tipos de análise

- **Análise de dados** (maior parte do trabalho): Descritiva, Segmentação, Agregação, Geoespacial
- **Previsões:** Séries temporais, Classificação, Numérico-contínua (regressão), Teste A/B

**Exploratória x Explicativa:**
- *Exploratória* = trabalho de bastidor, busca padrões, visualização não precisa ser perfeita
- *Explicativa* = já tem o insight, precisa de narrativa guiando a uma conclusão

Evolução de carreira em comunicação (livro *Data Story*, Nancy Duarte): **Explorar** (contribuidor individual) → **Explicar** (conselheiro estratégico) → **Inspirar** (liderança via dados).

## 6. O que são dados

- **Fontes:** primárias, secundárias, internas, externas
- **Tipos:** numéricos (contínuos/discretos), categóricos (ordinais/nominais), textuais, data/hora, booleanos, visuais, geográficos

## 7. Os 5 Vs do Big Data

**Volume, Velocidade, Variedade, Veracidade, Valor**

- **Processamento:** batch (lotes programados) x streaming (tempo real)
- **Estrutura:** estruturados (tabelas), semiestruturados (JSON/XML/CSV), não estruturados (texto, imagem, áudio) — ~80-90% dos dados gerados são não estruturados, mas bancos relacionais ainda dominam em uso
- **Classificação de volume:** Small Data (<500GB, uma máquina), Medium Data (500GB-100TB), Big Data (>100TB, processamento distribuído)
- **Armazenamento:** de planilhas → Data Warehouse → Data Lake (a depender do volume/variedade)

## 8. OKRs e KPIs

- **OKR:** Objetivo (O QUE alcançar) + Resultados-Chave (COMO medir, específicos e mensuráveis)
- **KPI:** tipos — Produtividade, Qualidade, Capacidade, Estratégico
- **Erros comuns:** usar só métricas fáceis, medir tarefa em vez de resultado (ex: "horas trabalhadas" mede esforço, não resultado, e é fácil de gamear), criar indicador sem adesão da equipe

## 9. Soft skills e técnicas analíticas (pensamento crítico / resolução de problemas)

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

## 10. Ética no mundo de dados

- Cuidado com **viés estrutural** ao clusterizar/prever comportamento de grupos sociais (ex: análise "purista" pode reforçar desigualdade existente nos dados históricos em vez de corrigi-la)
- **Segurança da informação:** identificar dado sensível/estratégico, evitar vazamento e julgamento de valor

---

## Pontos de reforço pessoal (onde houve mais dúvida no quiz)

- **Analytics Engineer x Analista de Dados:** Analytics Engineer é o "encanamento" (modelagem/pipeline); dashboard e interpretação são mais território do Analista de Dados
- **Veracidade x Integridade:** Integridade = o *processo* preservou o dado corretamente (erro de ETL quebra isso); Veracidade = o *dado em si* reflete a realidade (pipeline perfeito, mas dado de origem impreciso)
- **GUT x Ishikawa:** GUT decide qual problema atacar entre vários; Ishikawa investiga a causa raiz do problema já escolhido

---

## Conexões com o Desafio Final (dbt + Power BI)

- O quadro "Plataforma de dados → Produtos de dados" já mapeia onde cada ferramenta entra: **dbt** = Engenheiro de Analytics (Data Marts), **Power BI** = Dashboards (Analista de Dados)
- Antes de modelar no dbt: repetir a etapa "Entender o problema de negócio" e já definir os **KPIs/OKRs** que o dashboard final vai responder — não começar pela tabela
- O dashboard final do desafio deve ser **análise explicativa** (narrativa guiando a uma conclusão), não só um painel exploratório solto
