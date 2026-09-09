# Desafio Final — Adventure Works

> **Tradução do `Briefing Desafio.txt`.** Traduzido integralmente, sem cortes nem resumo.
> Os trechos que o original já trazia em português foram mantidos como estavam. As
> observações do tradutor estão no fim, separadas, para não se misturarem ao texto oficial —
> **em caso de divergência, vale o original em inglês.**

---

## A certificação

Este desafio busca avaliar seu raciocínio analítico, sua capacidade de criar visualizações e
de argumentar com base em dados. Ao aplicar as técnicas e ferramentas apresentadas ao longo
do curso, obter esta certificação indica que você:

- compreende o processo de construção de uma plataforma de analytics moderna;
- compreende os objetivos da modelagem dimensional em data warehouses modernos;
- sabe aplicar SQL e usar ferramentas de transformação para modelar dados em data warehouses
  modernos;
- está familiarizado com as boas práticas de visualização de dados e com sua aplicação numa
  ferramenta de BI.

---

## 1. Contexto geral

Você foi contratado pela **Adventure Works (AW)**, uma fabricante de bicicletas em rápido
crescimento, que conta com mais de 500 produtos distintos, 20.000 clientes e 31.000 pedidos.
Para sustentar seu crescimento e se diferenciar da concorrência, a Adventure Works pretende
usar seus dados de forma estratégica, orientando suas decisões para se tornar uma empresa
data-driven.

A liderança da empresa já listou uma série de perguntas que deseja responder por meio de
análise de dados — perguntas que vão guiar o desenvolvimento das tabelas fato e dimensão do
data warehouse. Para dar a partida no projeto e obter resultados rápidos, decidiu-se começar
pela área de vendas, ainda que tabelas de outras áreas possam ser necessárias para obter as
informações desejadas.

Na sua avaliação inicial, você identificou diversos sistemas usados pela Adventure Works que
geram dados relevantes para o negócio e que devem, eventualmente, ser integrados à
infraestrutura de dados:

| Função | Sistema |
|---|---|
| ERP | SAP |
| CRM | Salesforce |
| Web Analytics | Google Analytics |
| Website | Wordpress |

Nas conversas iniciais, você também identificou que o projeto **não tem apoio unânime**
dentro da empresa; há dúvidas quanto ao prazo, aos custos envolvidos e a se haverá retorno
sobre o investimento.

O projeto foi concebido e patrocinado pelo **Diretor de Inovação da AW, João Muller**, e
conta também com o respaldo do **CEO da empresa, Carlos Silveira**, que vê o uso de dados
como um diferencial estratégico de longo prazo. A **Diretora Comercial, Silvana Teixeira**,
por outro lado, acredita que os recursos investidos no projeto poderiam ter sido alocados em
ações promocionais que — na visão dela — geram resultado imediato de vendas. Além disso, ela
não vê como a criação de uma infraestrutura de dados moderna vai beneficiar seu departamento
comercial, dado que promessas anteriores de tornar a área "data-driven" — feitas por
fornecedores de outros sistemas, como CRM e Web Analytics — não entregaram os resultados
prometidos.

Um pedido específico do **CEO Carlos Silveira** é que a construção desta plataforma de dados
garanta a qualidade e a acurácia dos dados de saída; ou seja, o time de Analytics Engineering
precisa ser capaz de confirmar que as informações estão alinhadas com os números verificados
pela equipe de auditoria contábil. Carlos citou o exemplo das vendas brutas de 2011, que
totalizaram **US$ 12.646.112,16**. Ele gostaria que fossem feitos testes para verificar a
acurácia desse número nos modelos que estão sendo construídos, seguindo a abordagem de um
workshop de "Modern Data Stack" que ele assistiu recentemente.

Além dessas pessoas, o **Diretor de TI, Nilson Ramos**, é o responsável por garantir o acesso
aos dados e designou um analista, **Gabriel Santos**, para ajudar nisso. Gabriel é hoje
responsável por administrar bancos de dados e responder perguntas ad-hoc das áreas de negócio
que exigem SQL. A agenda dele é bastante apertada, então comunicação coordenada e interações
eficientes são essenciais para garantir que todos os dados necessários estejam disponíveis
para o projeto.

### Descrição dos dados

A Adventure Works tem um banco de dados transacional (**PostgreSQL**) que armazena dados de
suas diversas áreas. Esses dados estão distribuídos em **68 tabelas divididas em 5 schemas**:
HR (recursos humanos), sales (vendas), production (produção) e purchasing (compras).

`Desafio/imagemDesafio.png`

---

## 2. Objetivo do desafio

O objetivo é construir um modelo de dados que permita análises claras e confiáveis, usando um
conjunto de dados derivado dos dados brutos da Adventure Works, de modo a responder as
seguintes perguntas de negócio:

**a** — Qual o número de pedidos, a quantidade comprada e o valor total da transação por
produto, tipo de cartão, motivo da venda, data da venda, cliente, status, cidade, estado e
país?

**b** — Quais produtos têm o maior valor médio por pedido, por mês, ano, cidade, estado e
país? (valor médio por pedido = receita bruta − descontos de produto / número de pedidos no
período analisado)

**c** — Quem são os 10 principais clientes por valor total de transação, filtrando por
produto, tipo de cartão, motivo da venda, data da venda, status, cidade, estado e país?

**d** — Quais são as 5 principais cidades por valor total de transação, filtrando por
produto, tipo de cartão, motivo da venda, data da venda, cliente, status, cidade, estado e
país?

**e** — Qual o número de pedidos, a quantidade comprada e o valor total da transação por mês
e ano? (dica: gráfico de série temporal)

**f** — Qual produto tem o maior número de unidades compradas pelo motivo de venda
"Promotion"?

---

## 3. Preparação para o desafio

**Instruções de ingestão de dados (EL):**

Antes de começar o desafio, você vai precisar ingerir os dados da Adventure Works. Siga as
instruções de pré-requisito e o tutorial de configuração inicial na página principal do
repositório. No fim da página de instruções principais, você encontra links direcionando para
as instruções específicas de cada trilha.

**USE SOMENTE O SCHEMA `adventure_works` PARA O DESAFIO.**

---

## 4. Etapas do desafio

Para desenvolver as entregas, é essencial completar as seguintes etapas:

1. **Pesquisa e definição de KPIs e perguntas de negócio** relevantes para o contexto de
   negócio da Adventure Works. Você deve propor quais indicadores devem ser acompanhados no
   dashboard e apresentar uma justificativa.

2. **Criação de uma análise exploratória de dados** para obter insights, e uma apresentação
   explicando como esses insights contribuíram para o entendimento do conjunto de dados.

3. **Diagrama conceitual do data warehouse em formato PDF:** crie um modelo conceitual com as
   tabelas fato e dimensão necessárias para responder as perguntas de negócio listadas no
   objetivo. Indique brevemente as tabelas de origem usadas para criar cada tabela dimensão e
   a tabela fato. (Ferramenta sugerida: draw.io)

4. **Configuração do data warehouse na nuvem e do dbt.** Sugestão: Databricks Free Edition e
   dbt Cloud.

5. **Transformação de dados:** transforme os dados brutos usando dbt (sugestão: dbt Cloud).
   Essa transformação deve incluir os seguintes elementos:
   - documentação de tabelas e colunas nos data marts;
   - testes de source;
   - testes nas chaves primárias das tabelas dimensão e fato;
   - testes de qualidade de dados.

   O código deve estar hospedado em um repositório (sugestão: GitHub). Você deve fornecer o
   link do repositório do GitHub.

6. **Criação de um mockup de dashboard**, baseado na sua pesquisa de KPIs e nos insights da
   análise exploratória. Atenção às boas práticas de visualização de dados e de data
   storytelling.

7. **Desenvolvimento do dashboard**, seguindo a lógica estabelecida no mockup e utilizando os
   insumos derivados da definição de KPIs e da análise exploratória, respondendo também as
   perguntas mínimas listadas no objetivo do desafio. Essas são as perguntas mínimas que
   devem ser respondidas por meio das análises feitas no dashboard criado; no entanto, um
   dashboard completo e bem estruturado também vai pesar na avaliação final do componente de
   BI.

8. **Documentação das regras de negócio.**

9. **Criação de uma apresentação final e gravação de vídeo.** Vídeo: você deve gravar um vídeo
   apresentando todas as etapas do projeto (DW, EL, transformação com dbt e BI). Grave usando
   uma ferramenta de gravação, como Nimbus ou OBS Studio. O vídeo não deve passar de 10
   minutos de duração. Você pode usar o YouTube ou outra plataforma, se preferir.

   Abaixo, uma estrutura narrativa básica para guiar seu vídeo. Você pode incluir informações
   adicionais — como decisões de modelagem, métricas customizadas e insights diversos
   derivados do seu dashboard — mas é essencial que seu vídeo inclua as seguintes
   demonstrações:
   - uma breve explicação do objetivo do projeto e dos resultados esperados;
   - uma explicação das tabelas dimensão criadas e da relação delas com a tabela fato;
   - uma demonstração de `dbt run` mostrando que todos os modelos executam com sucesso;
   - uma demonstração mostrando que todos os testes aplicados ao source passam. Use
     `dbt test --select source:*`;
   - uma demonstração mostrando que todos os testes aplicados aos modelos passam. Use
     `dbt test`;
   - uma demonstração da tabela fato e dos joins feitos entre a tabela fato e as tabelas
     dimensão; uma explicação de quais métricas foram criadas na tabela fato e por quê;
   - apresentação dos testes de dados;
   - apresentação do dashboard, incluindo como os filtros funcionam, as visualizações e as
     possibilidades de análise.

**[OPCIONAL]**

10. **Planejamento do projeto de dados (formato PDF):** considere as informações levantadas
    nas avaliações iniciais, resumidas na seção de contexto. Preste atenção especial aos
    objetivos esperados do projeto, aos stakeholders e aos riscos/contingências. Além disso,
    que outro valor pode ser extraído de projetos de infraestrutura de dados? Existem outros
    riscos e contingências que você considera relevantes incluir no plano do projeto? (Use o
    template disponível no anexo no canto superior direito da página.)

---

## 5. Apresentação e submissão do desafio

Você deve entregar:

- **Notebook** contendo a análise exploratória e explicativa dos dados, em Python ou SQL. O
  notebook deve incluir código, gráficos e comentários sobre cada insight da fase de análise
  exploratória.
- **Arquivo PDF do modelo conceitual.**
- **Link para o repositório do dbt** contendo os modelos transformados.
- **Arquivo JPEG do mockup do dashboard** criado no Figma.
- **Um dashboard em Power BI ou Databricks AI/BI** focado na área comercial. Para Power BI,
  envie o arquivo PBIX com todas as medidas DAX documentadas dentro do arquivo. Se usar
  Databricks AI/BI, forneça o link do dashboard e o arquivo JSON.
- **Arquivo contendo a documentação das regras de negócio.**
- **Apresentação (slides)** cobrindo as etapas do projeto, incluindo argumentos a respeito de
  cultura data-driven, insights derivados da análise exploratória, justificativa para a
  escolha dos indicadores e dos visuais do dashboard, um passeio pelo dashboard e suas
  principais funcionalidades e, por fim, recomendações de iniciativas acionáveis para o
  cliente com base no objetivo estabelecido.
- **Um vídeo de 3 a 5 minutos** apresentando o projeto. É essencial incluir uma demonstração
  do dashboard em ação e mostrar a modelagem usada dentro da ferramenta de BI (seja Power BI
  ou Databricks AI/BI).

Todas as etapas do projeto devem ser arquivadas em um arquivo WinRAR ou pasta Zip e
submetidas pela plataforma, da seguinte forma:

> **GitHub:** você deve entregar todo o projeto de transformação no GitHub através de um link
> em um arquivo de texto na pasta.
>
> **BI:** se o BI desenvolvido for no AI/BI, disponibilizar o link em um arquivo de texto na
> pasta.
>
> **Youtube/Drive/Dropbox:** você deve inserir o vídeo em alguma dessas plataformas através de
> um link em um arquivo de texto na pasta.
>
> **Modelo Conceitual:** você deve exportar e inserir o Modelo Conceitual do Projeto Final na
> pasta de WinRAR ou Zip.
>
> **Apresentação, Mockup e outros arquivos:** você deve exportar em JPEG/PDF e inserir na
> pasta de WinRAR ou ZIP, não esqueça de adicionar o arquivo de texto com os links.

**Observação:** se essa pasta passar do limite de 40 MB do Moodle, você pode compactar o
projeto inteiro em um arquivo WinRAR ou Zip, subir para uma pasta do Google Drive e nos enviar
o link em um arquivo de texto. Lembre-se de que o acesso a qualquer link fornecido precisa
estar configurado como público, para agilizar a correção.

---

## 6. O que será avaliado

Nossa avaliação é baseada em um total de 10 pontos e considera critérios como:

- adesão aos requisitos de entrega;
- profissionalismo na entrega e na apresentação;
- clareza e compreensão do conteúdo.

A **nota mínima para aprovação é 7**. Você tem **30 dias** após a inscrição para submeter o
desafio. Se não atingir o requisito, terá uma segunda chance para corrigir os pontos
considerados insuficientes.

Os critérios de aprovação do aluno serão os seguintes:

- entendimento do negócio e foco em atender as necessidades do cliente;
- capacidade analítica para definir métricas e visualizações que sejam significativas e que
  gerem insights acionáveis para o cliente;
- análise exploratória de dados (EDA) e diagramas conceituais bem estruturados e organizados,
  acompanhados de documentação dos insights;
- entendimento e capacidade de organização para projetos de transformação e modelagem de
  dados, junto a conhecimento básico de Git;
- criação de dashboard que responda as principais perguntas de negócio e que respeite as boas
  práticas de visualização de dados, experiência do usuário (UX) e data storytelling,
  incluindo documentação e validação de dados;
- capacidade de gerar recomendações acionáveis a partir das análises e de articular a
  importância de uma cultura data-driven — tendo em mente que a Diretora Comercial desconhece
  o potencial dos dados para melhorar a performance;
- apresentação da solução cobrindo todas as etapas do desafio.

Bom trabalho!

---

## Observações do tradutor

Coisas que a tradução preservou porque estão no original, e que valem atenção na hora de
entregar:

1. **A duração do vídeo aparece com dois valores diferentes.** Na etapa 9 o original diz
   *"should not exceed 10 minutes"*; na seção de submissão, *"a 3-to-5-minute video"*. Não é
   erro de tradução — a contradição está no texto oficial. Confirmar com o instrutor; na
   dúvida, 5 minutos atende as duas leituras.

2. **A contagem de schemas está certa, mas falta um nome.** O original diz "5 schemas" e
   lista quatro (HR, sales, production, purchasing). O quinto é **`Person`** — verificado no
   `install.sql` da base oficial, que cria Person (13 tabelas), HumanResources (6),
   Production (25), Purchasing (5) e Sales (19), totalizando as 68. `Person` não é
   dispensável: é dele que saem `Address`, `StateProvince` e `CountryRegion`, sem os quais
   não existem os cortes por cidade, estado e país que as perguntas (a), (b), (c) e (d)
   exigem.

3. **O mockup é pedido "criado no Figma".** Se a intenção for aceitar qualquer ferramenta,
   vale confirmar antes de investir tempo em outra.

4. **A fórmula da pergunta (b) precisa de cuidado com a precedência.** *"Gross revenue −
   product discounts / number of orders"*, lida literalmente, dividiria apenas os descontos.
   A leitura pretendida é `(receita bruta − descontos) / número de pedidos`.

5. **`adventure_works` não é um schema do banco de origem.** A instrução "USE SOMENTE O
   SCHEMA `adventure_works`" não corresponde a nada no repositório oficial — a string não
   aparece lá uma única vez, e no PostgreSQL a base nasce com os cinco schemas do item 2.
   Provavelmente é o schema de destino da ingestão. Confirmar no tutorial da trilha.
