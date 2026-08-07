

## Material Teórico 

Formação em Engenharia de Analytics 

#### Autoria (obrigatório) 

Exemplo: Prof. Dr. João Silva. Incluir todos os autores, se aplicável. 

Prof. Rulyan Fernandes 

Módulo (obrigatório) 

Detalhe o nome do módulo 

Módulo IV - Engenharia de Dados com dbt e Stitch. 

#### Temas abordados (obrigatório) 

Liste os temas abordados no módulo conforme o Plano de Ensino do curso. 

- Introdução ao ETL 

- ETL na prática 

- DW da Northwind 

#### Objetivos de Aprendizagem (obrigatório) 

Descreva os objetivos de aprendizagem que o aluno conseguirá obter neste módulo. 

- Aprender os principais conceitos sobre engenharia de dados 

- Diferenças entre ETL e ELT 

- Tipos de processamento etc. 

- Aprender a mover dados para um data warehouse usando Kondado a partir de diferentes exemplos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

1 

- Mover dados da Northwind para o Big Query 

- Aplicar os conhecimentos de DW e ETL do início ao fim construindo o DW da Northwind usando o dbt. 

- Construir o DW da Northwind no dbt. 

#### Apresentação do Módulo (obrigatório) 

Escreva  uma breve apresentação do módulo para estimular o interesse dos alunos. 

Caro aluno(a), 

Neste módulo você vai aprender como mover dados entre diferentes fontes de dados e um data warehouse através da engenharia de dados. 

###### Imagens/figuras/tabelas/gráficos 

Atentando-se aos aspectos de direitos autorais, caso queira acrescentar uma imagem, utilize o banco Unsplash. Você também pode utilizar imagens do **Wikipedia, Wikimedia Commons, WikiArt, FreeImages e Pixabay** , que são bancos de imagens gratuitos. No mais, pode ser utilizada qualquer imagem com licença Creative Commons, mas lembre-se de observar a qualidade da imagem e cite a fonte no material, indicando o link e marcando no texto para solicitar o elemento visual. 

Ao construir imagens própria, lembre-se de compartilhar os arquivos originais (editáveis) na pasta da disciplina. 

###### Trechos de código 

Para incluir trechos de código, adicione em formato textual dentro de uma tabela como no exemplo: 

SELECT * FROM ABC 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

2 

#### Introdução (opcional) 

Escreva uma introdução para o conteúdo do módulo em linguagem dialógica. Não é necessário em cursos onde o material é 100% prático ou multimídia. 

Aprendemos o que são bancos de dados e sua linguagem, o SQL. Também aprendemos que existem bancos de dados especializados para consultas analíticas chamados de Data Warehouses e que eles são criados a partir de uma arquitetura de fatos e dimensões. Mas como fazemos para mover e transformar os dados brutos armazenados nas fontes de dados das empresas para os data warehouses? 

Neste capítulo, aprenderemos como sair da teoria para a prática através do processo de transformação de dados entre fontes distintas chamado de ELT. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

3 

#### Desenvolvimento (opcional) 

Desenvolva o conteúdo do módulo utilizando tópicos  e subtópicos.  Não é necessário em cursos onde o material é 100% prático ou multimídia. 

# O Precursor: ETL 

Durante muito tempo (e ainda utilizado em muitas empresas atuais), o processo padrão de construção de _pipelines_ de dados era o ETL. ETL (do inglês, _extract-transform-load_ ) é o processo sistemático de extrair, transformar, limpar e carregar os dados brutos em um banco de dados ou outro local para visualização ou consumo por outra aplicação. Cada letra da sigla significa uma de suas etapas: 

- _Extract_ : recuperar dados brutos de uma ou mais fontes e salvá-los em um repositório de dados único 

- _Transform_ : estruturar, enriquecer, limpar e converter dados brutos para um modelo de dados final. 

- _Load_ : carregar os dados transformados para um data warehouse ou repositório de dados para utilização em uma ferramenta de BI. 



<!-- Start of picture text -->
Sistemas Data Platform Data Products<br>Transacionais<br>|' smessaedads itLy Extragéio Transformacao Carregamento |_| !i FailIB HH<br>' it Data {} } '<br>H io Marts 1 | BI i<br>i a ii nner<br><!-- End of picture text -->

_Fig. 45_ Exemplo de processo de ETL 

A sigla ETL não apenas lista suas as etapas, mas também representa a ordem em que tradicionalmente essas etapas são realizadas em um projeto. No _Modern Data Stack_ , no entanto, uma outra abordagem é 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

4 

proposta chamada de ELT, em que primeiro os dados brutos são carregados para um Data Warehouse e depois transformados dentro do próprio DW. Para evitar confusões e manter o padrão do MDS, usaremos a sigla ELT para denotar o processo como um todo. 

# O ELT 

Embora existam algumas diferenças de arquitetura e ferramentas utilizadas nos processos de ELT modernos, o quadro geral é o mesmo: na etapa de Extração, ferramentas especializadas permitem “mover” dados de centenas de fontes como ERPs, CRMs, bancos de dados, REST APIs etc. diretamente para um Data Warehouse na nuvem ou on-premises com um baixo custo técnico. Desta forma, a etapa de _Load_ é feita simultaneamente à extração. Dentro do DW, a transformação de dados é feita através de scripts SQL ou ferramentas visuais. 

No diagrama abaixo vemos como a etapa de ELT se destaca na arquitetura geral do MDS: 



<!-- Start of picture text -->
Sistemas Data Platform Data Products<br>Transacionais<br>as | a iae<br>' Ko Ingestao (E-L) > rel '<br>H Bancos de sf Data tt —— H<br>H dados H H Warehouse a '<br>' | | | Area staging (ex. 5 a ‘<br>i semaores | {| Data Lake) ransformagao de Dados (T) i<br>Lame | i :<br><!-- End of picture text -->

_Fig. 46_ Exemplo do fluxo de ELT 

Na prática, o processo de ELT é onde a maior parte do trabalho é realizado em um projeto de Analytics. Em projetos de menor complexidade, um Engenheiro de Analytics pode ser responsável pelo fluxo completo: desde a coleta de dados até a entrega final. Em projetos mais críticos, é comum que essa responsabilidade seja dividida entre os Engenheiros de Analytics 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

5 

e Engenheiros de Dados. 

Nas próximas seções vamos apresentar o processo de ELT passo a passo, contextualizando com as etapas apresentadas em outras seções do livro. Esses processos serão detalhados nos próximos capítulos, incluindo exemplos práticos de aplicação. Vamos lá? 

# O Processo de ELT 

O processo de ELT se inicia com o problema de negócio: precisamos ter dados confiáveis para utilização na tomada de decisão. Esse problema é o norte de todo o projeto de Analytics ainda que apareça em diferentes “sabores” a depender do cliente ou metodologia utilizada. Vendo dessa forma, percebemos que a maior parte dos conceitos e ferramentas apresentadas neste livro como parte da “caixa de ferramentas” de um Engenheiro de Analytics são necessárias mas não suficientes para um projeto de analytics de sucesso. O real valor será calculado a partir da qualidade e disponibilidade da informação disponível para o usuário final dos dados: o tomador de decisão. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

6 



<!-- Start of picture text -->
Ingestao (E-L)<br>Transformacao<br>(T)<br>Entrega<br>(deploy)<br><!-- End of picture text -->

_Fig. 47_ Etapas do Processo de ELT 

Assim, o processo de ELT é na verdade muito mais amplo que apenas extrair os dados das fontes transacionais e disponibilizá-los em um _data_ 

> Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

7 

_warehouse_ . De fato, ele engloba todas as etapas de desenvolvimento de uma infraestrutura moderna de analytics: desde o planejamento dos requisitos de negócio, até a entrega final dos dados através de tabelas ou _dashboards_ . 

### Planejamento 

O planejamento é essencial para alinhar os objetivos de negócio com a implementação técnica. As etapas de planejamento, no entanto, não são feitas pensando em entregar um planejamento completo do projeto, mas sim de forma incremental e incluindo o necessário para a implementação de cada pequena etapa. 

##### Entendimento do Problema 

Na etapa de Entendimento do Problema, nosso objetivo é obter o máximo de informações sobre os problemas de negócio que devem ser resolvidos com o projeto. Para isso, precisamos solitar aos times de negócio e _stakeholders_ informações relevantes para o entendimento dos dados, tais como planilhas, consultas, relatórios e dashboards. Entre as informações que queremos obter estão: 

- Background da empresa; 

- Objetivos estratégicos; 

- Expectativas com o projeto; 

- Principais KPIs (indicadores) relacionados ao projeto; 

- “Donos” dos indicadores ou stakeholders que devem ser consultados; 

- Valores de referência para validação posterior; 

- Fluxo de decisão: quem usa os indicadores, quando e para quê. 

##### Mapeamento de Dados 

A partir das necessidades de negócio identificadas, precisamos avaliar a disponibilidade de dados. Nem sempre os dados identificados pelos usuários de negócio são de fácil acesso, ou mesmo acessáveis em primeiro lugar. Além disso, é comum que a forma com que os dados brutos estão armazenados fisicamente seja bem diferente do formato com que os dados são acessados pela interface dos sistemas 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

8 

empresariais ou relatórios. 

Para realizar o mapeamento de dados utilizamos técnicas como diagramas ERD, planilhas e outros documentos. O importante é conseguir mapear quais dados estão disponíveis e onde estão de uma forma mais conceitual, sem entrar em muitos detalhes ainda. 

##### Elaboração do Modelo Conceitual do DW 

O próximo passo é desenharmos (ou atualizarmos) o modelo conceitual do _data warehouse_ que estamos desenvolvendo. Como já falamos no Capítulo 11 - Modelando um Data Warehouse, precisamos desenhar as tabelas Fato e Dimensão apropriadas e o relacionamento entre elas, tomando especial atenção na conformidade entre dimensões. 

### Ingestão de Dados 

Definido quais dados precisamos e onde buscá-los, precisamos realizar a Ingestão de dados para nosso _Data Warehouse_ . Isto é, extrair esses dados das fontes transacionais e disponibizá-los na camada bruta do _data warehouse_ . Falaremos de forma detalhada sobre essa etapa no Capítulo 14 - Ingestão de dados. 

### Transformação 

Na etapa de transformação é que os dados brutos, extraído diretamente dos diferentes sistemas da empresa, são lapidados e transformados em dados prontos para serem utilizados na tomada de decisão. É nesta etapa que reside o maior esforço e valor gerado da Engenharia de Analytics. Veremos quais as principais tarefas, boas práticas e ferramentas práticas no Capítulo 15 - Transformação de dados. 

##### Entrega Final 

Seguindo as boas práticas de programação), somente disponibilizaremos os novos dados pro usuário final depois de realizar testes, documentação e outras tarefas comuns no processo de _deploy_ de softwares. Ao final do processo, os novos dados ficam disponibilizados no ambiente “produção” do data warehouse para serem transformados em informação e geração 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

9 

de valor de negócio. 

No próximoa capítulo vamos detalhar o processo de ingestão de dados, a etapa inicial do ELT. Vamos lá? 

# Ingestão de dados 

A etapa de Ingestão de Dados compreende os processos de acessar os dados onde estão armazenados e enviá-los para um outro local para processamento. Também pode incluir ferramentas que coletam dados diretamente de eventos. Nosso objetivo nesta etapa é obter os dados na sua forma mais bruta para realizar a transformação dentro do DW. 

Na próxima seção falaremos brevemente sobre o processo de acessar os dados das fontes transacionais. Em seguida, passamos de forma introdutória sobre os tipos de ingestão ou processamento de dados ( _full_ ou incremental). Por fim, mostramos um exemplo prático de ingestão utilizando uma ferramenta do _Modern Data Stack_ , o Airbyte. 

# Acessando dados 

De nada adianta construir um _Modern Data Stack_ se não conseguimos acessar os dados armazenados nas fontes transacionais, APIs, planilhas etc. Cada fonte de dados terá um ou mais formatos de conexão, que podem variar em: 

- Vencedor do Banco de Dados: SQL Server, MySQL, PostgreSQL, Oracle, etc. 

- Tipo de Banco de Dados: Relacional, NoSQL, etc 

- Servidor: Desktop Simples, Servidor Local, Cloud, etc. 

- Tipos de Conexão: JDBC, ODBC, API, Dump do Banco etc. 

- Nível de acesso: Somente Leitura, Administrador, Tabelas Específicas, etc 

A forma mais comum de conexão a um banco de dados é através de uma conexão direta via protocolo _JDBC_ ou _ODBC_ . Neste tipo de conexão nós podemos enviar consultas SQL diretamente para o banco de dados como vimos no Capítulo 5. Em outros casos, pode ser necessário utilizar uma API 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

10 

REST desenvolvida pela aplicação que estamos consultando. Nestes casos, a disponibilidade dos dados será limitada pelo que está disponível na API. 

# Tipos de Ingestão 

É importante verificar os requisitos de negócio para mapear o tipo e periodicidade de processamento de dados necessário. É comum que em projetos de DW o processamento seja feito em lotes (batch), geralmente no período noturno onde há menor sobrecarga nos sistemas. No entanto, em alguns projetos pode ser necessário um processamento com maior frequência, por exemplo, horário ou mesmo em tempo-real. 

É importante reforçar que o processamento de grandes volumes de dados com alta frequência possuem desafios técnicos adicionais e um custo de implementação e manutenção mais elevado e se não for estritamente necessário para o projeto, é melhor evitá-lo. Sobretudo em etapas iniciais de implementação. 

### Ingestão _full_ 

Para garantir a consistência dos dados, a forma mais segura de processamento é através de _full-loads_ , ou seja, carregando todos os dados da fonte original em cada execução. Como esse processo é geralmente intensivo em termos computacionais, é comum que seja realizado em momentos onde o banco de dados fonte é menos utilizado (por exemplo, de madrugada). O problema dessa abordagem é que ela se torna menos viável se for necessário que os dados sejam atualizados com maior frequência, tanto pelo risco de tornar o sistema fonte lento, como pelo fato de que se uma carga completa demorar 1-2 horas para ser feita, é tecnicamente inviável que a frequência de atualização seja menor que esse período. 

### Ingestão incremental 

Na prática, a forma mais tradicional de aumentar a frequência de atualização dos dados é utilizar uma carga ( _load_ ) incremental, ou seja, de forma que somente são adicionados os novos registros entre cada 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

11 

execução. Para isso é necessário utilizar uma coluna que indexe a recência dos registros como Data ou ID, de modo que a cada execução somente os registros após esse índice são extraídos. No exemplo da tabela abaixo, suponha que diariamente às 23:59 seja feita uma carga incremental da tabela de Pedidos da empresa ACME S/A usando a coluna de data como índice. No dia 10/01/2015, ao rodar a extração teríamos uma tabela com três registros (1,2,3). No dia seguinte, a extração incremental só traria 2 registros (4,5). 

|**ID do Pedido**|**Data**|**Cliente**|**Produto**|**Valor Total**|
|---|---|---|---|---|
|1|10/01/2015|João da Silva|Bicicleta<br>Voadora|R$ 150,00|
|2|10/01/2015|Joana D’arc|Bicicleta<br>Aquática|R$ 200,00|
|3|10/01/2015|Tony Stark|Bicicleta<br>Rodas|4<br>R$ 180,00|
|4|11/01/2015|Carlos|Bicicleta|R$ 150,00|
|||Santos|Voadora||
|5|11/01/2015|Edson<br>Arantes|Bicicleta<br>Rodas|4<br>R$ 180,00|



O problema da carga incremental é que bancos de dados transacionais em geral não são _imutáveis_ , ou seja, nem sempre é possível atualizar uma extração apenas com novos dados. Por exemplo, vamos adicionar mais uma coluna de status na tabela de Pedidos que pode ter três valores (Pendente, Finalizado e Cancelado). Neste caso, não basta extrair os novos registros, mas também precisamos nos preocupar com atualizações em registros anteriores (UPDATEs). Se nosso objetivo for criar uma métrica de total de vendas por dia, por exemplo, ao não considerar pedidos cancelados estaríamos superestimando as vendas e gerando uma métrica equivocada ao utilizar um processamento incremental. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

12 

||**ID do**<br>**Pedido**|**Data do**<br>**Pedido**|**Clien**|**te**|**Produto**||**Status**|**Valor**<br>**Total**|
|---|---|---|---|---|---|---|---|---|
|1||10/01/2015|João<br>Silva|da|Bicicleta<br>Voadora||Finaliza<br>do|R$ 150,00|
|2||10/01/2015|Joana||Bicicleta||Pendent|R$|
||||D’arc||Aquática||e|200,00|
|3||10/01/2015|Tony||Bicicleta|4|Pendent|R$ 180,00|
||||Stark||Rodas||e||
||**ID do**<br>**Pedido**|**Data do**<br>**Pedido**|**Clien**|**te**|**Produto**||**Status**|**Valor**<br>**Total**|
|1||10/01/2015|João<br>Silva|da|Bicicleta<br>Voadora||Finaliza<br>do|R$ 150,00|
|2||10/01/2015|Joana<br>D’arc||Bicicleta<br>Aquática||Cancela<br>do|R$ 200,00|
|3||10/01/2015|Tony St|ark|Bicicleta<br>Rodas|4|Pendent<br>e|R$ 180,00|
|4||11/01/2015|Carlos<br>Santos||Bicicleta<br>Voadora||Finaliza<br>do|R$ 150,00|
|5||11/01/2015|Edson<br>Arante|s|Bicicleta<br>Rodas|4|Pendent<br>e|R$ 180,00|



Como podemos abordar esse problema? Em outras palavras, como não precisar fazer uma carga total em ambientes onde há dados que podem se atualizar retroativamente (mutáveis)? Veremos que uma das formas é através de um novo índice que identifique a atualização do registro, e não apenas sua data de criação. Por exemplo, vamos adicionar uma nova coluna Data de Atualização na tabela acima para capturar mudanças nos registros e indexar essa mudança na extração de modo que a extração do dia 11/01/2015 vai também considerar o Pedido 2. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

13 

|**ID do**<br>**Pedido**|**Data do**<br>**Pedido**|**Cliente**|**Produto**|**Status**|**Valor**<br>**Total**|**Data de**<br>**Atualizaçã**<br>**o**|
|---|---|---|---|---|---|---|
|1|10/01/2015|João<br>da Silva|Bicicleta<br>Voadora|Finaliza<br>do|R$ 150,00|10/01/2015|
|3|10/01/2015|Tony<br>Stark|Bicicleta<br>4 Rodas|Penden<br>te|R$ 180,00|10/01/2015|
|2|10/01/2015|Joana<br>D’arc|Bicicleta<br>Aquática|Cancel<br>ado|R$ 200,00|11/01/2015|
|4|11/01/2015|Carlos<br>Santos|Bicicleta<br>Voadora|Finaliza<br>do|R$ 150,00|11/01/2015|
|5|11/01/2015|Edson<br>Arantes|Bicicleta<br>4 Rodas|Penden<br>te|R$ 180,00|11/01/2015|



Nem sempre é o caso de existir um índice que nos permita identificar alterações nos dados como na tabela anterior. Por este motivo, a forma mais segura de processamento incremental é através do uso de técnicas baseadas em logs de transações do banco de dados que registram todas as operações de INSERT, DELETE, UPDATE, etc. realizadas. 

Tanto a abordagem baseada em uma data de modificação ou log são técnicas chamadas de CDC (do inglês, change data capture). 

# Ingestão de dados na prática 

A ingestão de dados no ELT é realizada de forma a reduzir ao mínimo a transformação dos dados brutos que serão carregados no data warehouse. Na prática, há diferentes formas de realizar essa ingestão desde que esse princípio de mínima transformação seja mantido. 

Entre as principais ferramentas do _Modern Data Stack_ utilizadas para a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

14 

ingestão de dados destacamos alternativas SaaS como Fivetran, Stitch e Hevo, além de alternaticas open-source como o Airbyte e Meltano. 

A escolha entre contratar uma ferramenta SaaS ou implementar uma solução _open-source_ vai depender da sua capacidade de investimento e competências do time de dados. Também deve ser levado em conta se a solução escolhida possui todas as integrações necessárias para o projeto. Em alguns casos, pode ainda ser necessário desenvolver uma nova integração, o que geralmente é facilitado ao implementarmos uma solução _open-source_ . 

Para o exemplo prático deste capítulo utilizaremos a ferramenta _Airbyte_ que pode ser configurada diretamente em seu computador seguindo as instruções nesta página. 

### Instalando o Airbyte 

Se você configurou seguiu as instruções de instalação do Airbyte ele deverá estar disponível em http://localhost:8000. 

### Configurando uma fonte de dados 

A fonte de dados do nosso exemplo será o banco de dados da Northwind que você deverá ter configurado em seu computador ou em algum outro ambiente que tenha acesso. 

Se você ainda não possui um banco de dados configurado, pode criá-lo através do seguinte comando (se requisitada, inserir a senha _password_ ): 

docker run --rm --name northwind -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres 

createdb psql -h localhost -U postgres -p 5432 northwind 

cat assets/data/northwind.sql | psql -h localhost -U postgres -p 5432 -d northwind 

O banco de dados da _northwind_ estará disponível no seguinte endereço: 

Host: localhost 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

15 

Port: 5432 User: postgres Password: password 

Database: northwind 

Que poderá ser acessado na tela de configuração de uma fonte ( _source_ ) no _Airbyte_ como abaixo: 



<!-- Start of picture text -->
New Source<br>Set up the source<br>Source type<br>@® Postares<br>Source name<br>Postgres<br>Host<br>Port<br>5432<br>DB Name<br>Schemas<br>User<br>Password<br>JDBC URL Parameters (Advanced)<br><!-- End of picture text -->

_Fig. 48_ Configurando uma fonte no Airbyte 

### Configurando um destino 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

16 

Agora vamos escrever em um Data Warehouse ( _BigQuery_ ). Para isso vamos criar um destino para o BigQuery e uma conta de serviço que permite escrever no BigQuery. Essa conta deverá ter as permissões de Usuário do BigQuery e Editor de dados do BigQuery. Você deverá criar uma chave JSON e adicioná-la no campo _credentials_ do Airbyte: 



<!-- Start of picture text -->
Destinations / BigQuery Overview Settings<br>Destination Settings<br>Destination type<br>Destination name<br>BigQuery<br>Project ID<br>tutorial-dbt-284217<br>Dataset Location<br>us<br>Default Dataset ID<br>northwind_aula_th<br>Loading Method Standard Inserts<br>Service Account Key JSON (Required for cloud, optional for open-source)<br>Transformation Query Run Type<br>interactive<br>Google BigQuery Client Chunk Size<br>15<br><!-- End of picture text -->

_Fig. 49_ Configurando um destino no Airbyte 

### Ativando um _sync_ 

Para executar a ingestão de dados em si, precisamos realizar um _sync_ da conexão entre fonte e destindo de dados no Airbyte. Cada _sync_ pode ser configurado para executar em intervalos pré-definidos (ex. a cada 24 horas), por período (ex. todo dia às 02:00) ou através de configurações 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

17 

avançadas de CRON. VocÊ pode verificar o status de cada _sync_ na página _Connections_ 



<!-- Start of picture text -->
Northwind <> BigQuery<br>@ Postgres > @ BigQuery «<br>Status Replication Transformation _Settings<br>Sync History<br>® sync Running ‘1:02PM 10/25<br>Sync Succeeded s:049M 10/13<br>syne Succeeded 4:59PM 10/13<br><!-- End of picture text -->

_Fig. 50_ Verificando o status dos _syncs_ no Airbyte 

### Pronto! 

É tão simples quanto parece. O processo de ingestão se resume a configurar conexões entre a fonte de dados e o _data warehouse_ , deixando o trabalho duro para a etapa de transformação. O processo é muito semelhante se utilizássemos outras ferramentas de ingestão do ELT, mudando apenas algumas nomenclaturas. 

# Transformação de dados 

A etapa de transformação de dados é o núcleo do processo de ELT. É neste momento que as regras de negócio são aplicadas nos modelos para gerar as tabelas finais que serão consumidas por um BI, em um relatório ou mesmo por outro sistema. O tipo de processo e tecnologia usada na transformação vai depender do tipo de dados que queremos transformar, volume de dados, arquitetura de sistemas possível (por exemplo, nuvem vs _on-premises_ ), capacidade técnica da equipe, entre outros. 

Na primeira seção deste capítulo listamos os tipos de transformações comuns em projetos de Analytics e que são parte fundamental do 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

18 

trabalho da Engenharia de Analytics. Em seguinda, comparamos diferentes arquiteturas de transformação de dados. Por fim, apresentamos um exemplo prático completo do _dbt_ , principal ferramenta de transformação de dados no Modern Data Stack. 

# Os Processos de Transformação 

O ideal é que as diversas transformações necessárias para limpar e processar os dados para o uso nas diversas ferramentas posteriores no pipeline (como relatórios, BI, modelos de IA etc.) sejam centralizadas nesta etapa para garantir uma visão única dos dados em toda a organização: 

- Selecionar os campos relevantes de negócio; 

- Filtrar dados incorretos ou incompletos; 

- Desduplicar dados; 

- Separar colunas em mais colunas (ex. separar uma coluna com dados separados por “,”); 

- Juntar dados de fontes de dados e/ou tabelas distintas; 

- Renomear colunas; 

- Criar novos campos e métricas calculadas; 

- Ordenar dados por um ou mais campos; 

- Remodelar os dados para um modelo de fatos e dimensões; 

- Criar novas chaves surrogate; 

- Transpor ou pivotar tabelas. 

# Alternativas de Arquitetura de ETL/ELT 

Os processos de transformação de dados são semelhantes não importa a arquitetura do _pipeline_ de dados utilizado, seja ela uma arquitetura de ETL tradicional ou de um ELT moderno. No entanto, cada arquitetura vai impactar profundamente na estrutura de times, profissionais responsáveis e produtividade do processo de transformação como um todo. Em geral, há 3 grandes alternativas de arquitetura: 

- Códigos personalizados: essa é a forma mais flexível de transformação de dados, onde a transformação é feita através de scripts escritos em Python, Java, Scala, etc. A principal ferramenta 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

19 

utilizada é o Spark, uma biblioteca escrita em Scala com APIs em diferentes linguagens. Embora flexível, ETLs em código puro demandam uma capacidade técnica alta da equipe que irá criar e manter os pipelines, configuração de orquestração de tarefas (“o que vem antes do quê”), log de erros entre outros; 

- Ferramentas de ETL Visuais: são ferramentas de ETL que permitem criar blocos de transformação de dados de forma visual ou até “drag-and-drop”. A curva de aprendizado é geralmente menor em relação aos métodos baseado em código, porém no médio prazo as ferramentas visuais geralmente deixam a desejar em termos de boas práticas como versionamento, _debugging_ , etc. A depender da ferramenta o custo de licenciamento também pode ser elevado; 

- Data Warehouse/Data Lakehouse: a transformação dentro do próprio _data warehouse_ é a chave do chamado modelo ELT. As vantagens dessa abordagem são a facilidade de utilizar uma linguagem padrão (SQL) e utilizar ferramentas específicas como dbt para cuidar das atividades auxiliares. Isso permite uma redução do tempo de entrega dos pipelines e uma necessidade técnica menor. Por outro lado, é limitado em dados estruturados (que podem ser armazenados em um banco de dados) e não é adequado para pipelines muito complexos. 

No MDS, vamos utilizar o próprio _Data Warehouse_ como ambiente de transformação e utilizar ferramentas como o dbt para modelar os dados seguindo as melhores práticas de desenvolvimento. Essa decisão evita a necessidade dos Engenheiros de Analytics dominarem muitas linguagens de programação e frameworks de desenvolvimento distintos e foquem apenas na construção do data warehouse utilizando apenas o necessário para o framework do ELT. No equilíbrio entre desenvolvimento e conhecimento de negócio, nosso foco é o negócio. 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

20 

### ETL baseado em ferramentas visuais 

O diagrama abaixo apresenta uma arquitetura comum em projetos de dados liderados pela área de BI. Nestes projetos as três etapas do ETL são geralmente realizadas dentro de uma ferramenta monolítica como Pentaho ou Informática. 



<!-- Start of picture text -->
FERRAMENTA nil<br>Bancos BI<br>datiosd ' Responsavel pela extracdo/ingestdo, limpeza, regras de<br>rr] H neg6cio etc. de forma centralizada Relatorios<br>Servidores ><br>Eg ®pentaho e Informatica Slserver<br>Saas Sistemas<br>Engenheiro de Dadwsalista de Dados Analista de Dados<br><!-- End of picture text -->

_Fig. 51_ ETL baseado em ferramentas. 

As principais desvantagens dessa abordagem são: 

- **Lock-in:** toda a lógica do pipeline de dados fica presa dentro da ferramenta. Qualquer mudança de ferramenta envolve um grande retrabalho; 

- **Escalabilidade:** essas ferramentas em geral possuem dificuldade de escalar para grandes volumes de dados ou necessitam grandes investimentos para isso; 

- **Flexibilidade:** por serem ferramentas visuais, suas capacidades são limitadas pelas funcionalidades disponíveis e reduzem a flexibilidade dos projetos; 

- **Governança:** em geral é complicado garantir governança nessas ferramentas, de modo que acabam sendo limitadas a um único desenvolvedor, tornando o processo dependente de uma pessoa e 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

21 

não algo estruturado da empresa. 

### ETL baseado em código 

O diagrama abaixo apresenta uma arquitetura comum em projetos de dados complexos liderados pela área de TI. As três etapas do ETL são atribuídas às equipes de Data Engineering ou outras áreas técnicas da empresa, enquanto os analistas de negócios e cientistas de dados ficam limitados ao consumo desses dados na ponta. 



<!-- Start of picture text -->
foe Pee<br>\\<br>NALON ZV<br><!-- End of picture text -->

_Fig. 52_ ETL baseado em código. 

As principais desvantagens dessa abordagem são: 

- **Dívida técnica:** necessidade de equipes que entendem dos códigos e transformações especializadas e customizados para cada projeto; 

- **Distância dos analistas:** como são projetos complexos e liderados por times técnicos, há uma grande distância do time de negócio que é “dono” dos dados. Isso gera conflito entre os times, atraso nos projetos e dificuldade de geração de valor. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

22 

### Abordagem Moderna 

Na abordagem moderna as etapas de processamento de dados ficam dentro do Data Warehouse, de modo que o processo é invertido para Extract-Load-Transform (ELT). A principal é diferença em relação à abordagem tradicional é a criação de uma nova função, do Engenheiro de Analytics, responsável por transformar os dados dentro do Data Warehouse. Essa função resolve o distanciamento entre dados e negócio comum nos processos de ETL tradicionais. 



<!-- Start of picture text -->
x7<br><!-- End of picture text -->

_Fig. 53_ ELT moderno. 

# Transformação de dados com dbt 

Nesta seção vamos apresentar como fazer a modelagem de um DW na prática usando o dbt. Para tanto, nós precisamos primeiro realizar a carga dos dados brutos em nosso DW (que fizemos na seção anterior). Com os dados já inseridos no DW, vamos criar uma séries de modelos para materializar o modelo conceitual do DW que criamos anteriormente. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

23 

Antes de começar a parte técnica, é bom lembrar que o objetivo de um DW é gerar resultado para a empresa e não criar um sistema que, embora possa ser tecnicamente bem feito, não tenha uma visão de negócio. Deste modo, a forma como criamos os marts e suas tabelas fato e dimensões deve ser sempre pensado nos problemas prioritários na tomada de decisão e na utilização pelo usuário final. Um erro comum de projetos de DW é pensar mais nos modelos de dados das aplicações-fonte e menos no modelo de negócios do usuário final. Se for difícil saber _a priori_ como será essa utilização, podemos recorrer a instrumentos já usados na tomada de decisão como relatórios, planilhas, etc. para ter uma ideia de que tipo de relações e atributos são mais relevantes para o cliente. 

Atualmente o dbt possui uma versão SaaS chamada dbt cloud além da versão open-source. A versão SaaS possui um custo de aprendizagem menor para quem tem menos contato com programação, mas neste curso vamos utilizar a versão open-source. No geral, ambos são muito similares e você utilizar a versão cloud de forma equivalente se desejar. 

###### **Dica!** 

Para lembrar os comandos do dbt facilmente utilize essa cheatsheet 

### Começando um projeto 

Nesta subseção vamos aprender como iniciar um projeto dbt. Vamos lá? 

##### Instruções de exemplo 

A forma mais fácil de acompanhar esta seção é clonar o projeto de exemplo disponível neste repositório. Siga as instruções no README do repositório para instalar e configurar o dbt corretamente no seu computador. 

##### Criando um projeto dbt 

O primeiro passo de um projeto dbt é a criação da pasta onde estão estruturados os arquivos do projeto. A forma mais fácil de criar essa pasta é através do comando dbt init. Você também vai precisar criar um repositório git na pasta para controlar o versionamento do projeto. Todo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

24 

projeto é iniciado com um arquivo dbt_project.yml padrão, neste arquivo são configurados diversas opções do projeto incluindo a conexão com o data warehouse, tipo de materialização das tabelas, entre outros. 

###### **Atenção!** 

Se você clonou o repositório de exemplo, as etapas dessa subseção já terão sido feitas para você. 

**name** : 'northwind' **version** : '1.0.0' **config-version** : 2 

**profile** : 'northwind' 

**model-paths** : ["models"] **analysis-paths** : ["analyses"] **test-paths** : ["tests"] **seed-paths** : ["seeds"] **macro-paths** : ["macros"] **snapshot-paths** : ["snapshots"] 

**target-path** : "target" _# directory which will store compiled SQL files_ **clean-targets** : _# directories to be removed by `dbt clean`_ - "target" 

- "dbt_packages" 

**models** : **northwind** : **staging** : **+materialized** : table 

Exemplo de dbt_project.yml 

O dbt init também cria uma estrutura de pastas e arquivos padrão para todo projeto dbt: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

25 

├── analyses ├── dbt_packages ├── dbt_project.yml ├── logs ├── macros ├── models ├── README.md ├── seeds ├── snapshots ├── target └── tests 9 directories, 2 files 

##### Configurando a conexão com o Data Warehouse 

A conexão com o data warehouse é configurada por padrão no arquivo profiles.yml que fica armazenado no caminho ~/.dbt/profiles.yml (LINUX). As permissões do arquivo devem ser restritas ao usuário pois possuem credenciais de acesso aos dados que não devem ser compartilhadas. 

A opção target permite alterar entre um ambiente de desenvolvimento e produção de forma simples. O target de produção deve se chamar “prod” pois é usado em outros APIs do dbt. Durante o desenvolvimento, esse target não deve ser usado mas sim um target “dev” ou equivalente. 

Atualmente o dbt possui drivers para os principais data warehouses na nuvem e alguns bancos de dados tradicionais, cada driver possui configurações específicas que podem ser consultadas aqui. 

**northwind** : 

**outputs** : **dev** : **dataset** : northwind **job_execution_timeout_seconds** : 300 **job_retries** : 1 **keyfile** : path/to/keyfile.json **location** : US **method** : service-account 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

26 

**priority** : interactive **project** : <project_id> **threads** : 1 **type** : bigquery 

Exemplo de dbt Profile 

Para verificar se tudo está bem configurado, podemos usar o comando dbt debug no terminal. Em caso de sucesso, devemos ter um output como esse: 

dbt debug (...) Connection test: [OK connection ok] 

All checks passed! 

### Salvando nossas alterações 

É importante salvar frequentemente nossas alterações no projeto. Por ser um projeto de código (lembrem-se do princípio de _data as code_ ), as alterações são salvas como _commits_ em um sistema de controle de versão git. 

###### **Importante!** 

Se você não tem contato com git, recomendamos revisar o capítulo sobre Git ou buscar outros conteúdos _online_ . 

git init git branch -M main git add . git commit -m "Criei um projeto dbt" git remote add origin https://github.com/USERNAME/dbt-northwind.git 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

27 

git push -u origin main 

### Criando nossos primeiros modelos 

Agora que temos o ambiente configurado podemos trabalhar na construção dos modelos dbt. Cada modelo se tornará um objeto no _data warehouse_ seguindo nosso planejamento do ELT. 

##### Começando uma nova _branch_ 

Antes de iniciar nossa construção dos modelos, é recomendável criar uma nova _branch_ de trabalho para salvarmos nossas alterações. Para isso podemos executar no terminal: 

git checkout -b novos_modelos_dbt 

##### Criando nossas primeiras fontes de dados 

Agora que configuramos nossa conexão com o data warehouse, precisamos criar nossas primeiras fontes de dados. Essas fontes são definidas no arquivo sources.yml, onde é possível descrever quais os bancos de dados, schemas e tabelas que queremos deixar disponíveis no dbt. 

###### **Atenção!** 

Nesta seção é esperado que os dados brutos da Northwind já estejam disponíveis no Data Warehouse através de um processo de ingestão como visto aqui ou através de um dbt seed como sugerido aqui. 

Depois de definidas as fontes, elas podem ser chamadas nos modelos através da sintaxe: 

select * 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

28 

from {{source('nome_fonte', 'nome_tabela')}} 

Não é necessário mapear todas as tabelas do data warehouse de uma vez, mas podemos adicionar de forma incremental o que for necessário para os modelos. O uso do arquivo de sources permite criar a linhagem dos dados através da função { source('nome_da_fonte',’nome_da_tabela’)}} e também permite documentar e escrever testes sobre as fontes de dados. 

**version** : 2 

**sources** : 

- **name** : northwind _# aqui você deve substituir pelo nome do dataset criado pela ferramenta de ingestão no bigquery_ **schema** : **description** : Essa é a fonte de dados do nosso ERP **tables** : 

- **name** : products **description** : Essa é a tabela de produtos do ERP. 

- **name** : employees **description** : Essa é a tabela de funcionários do ERP. 

- **name** : customers 

**description** : Essa é a tabela de clientes do ERP. O dono desse dado é a equipe comercial. 

Uma boa prática é incluir o arquivo sources.yml no diretório _staging_ onde fazemos as primeiras transformações sobre os dados originais. Em geral, cada source deve ser referenciada apenas em um modelo, facilitando a consistência na modelagem como iremos discutir na próxima seção. 

##### Criando nossos primeiros modelos 

Um modelo em dbt é um arquivo .sql que tem como input uma tabela fonte do banco de dados ou um outro modelo do dbt. Por padrão, o dbt irá 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

29 

criar um objeto no banco de dados com o mesmo nome do arquivo e com o tipo de materialização escolhida (tabela, visualização, etc). Ao utilizar corretamente a interface do dbt, conseguimos garantir a linhagem dos dados, isto é, a ordem correta com que cada script sql deve ser executada no banco de dados. Embora seja possível escrever um modelo .sql que referencia diretamente uma tabela do banco de dados, essa prática deve ser evitada. As duas interfaces principais de um modelo são as funções {{ source('nome_da_fonte',’nome_da_tabela’)}} e {{ ref(‘nome_do_modelo’) }} A primeira indica ao dbt que aquele modelo utiliza dados da tabela fonte do banco de dados que não depende de outros modelos, e a segunda indica que a fonte dos dados é um outro modelo que pode ou não existir no banco de dados inicialmente e deve ser processado na sequência correta. 



<!-- Start of picture text -->
| source.table {{ source(source’, table TH stg_orders [_ftrettstg_orders ii} _| fet_orders |<br><!-- End of picture text -->

_Fig. 54_ Exemplo de dependências no dbt 

Nos modelos _staging_ (abreviados com o prefixo stg) importamos as _sources_ e aplicamos transformações simples para “limpar” os dados da origem e adequar a nosso modelo de dados: 

- Renomear colunas 

- Alterar tipos de dados 

- Criar novas colunas dependentes (concatenar, separar, etc) 

Em nosso primeiro modelo vamos ler a tabela _customers_ da fonte northwind e criar uma versão _staging_ em nosso DW. Neste momento é interessante verificar as colunas e tipos que foram criados durante a ingestão através de uma ferramenta de consulta SQL. A partir do _data model_ , podemos copiar e colar as colunas em uma CTE em nosso modelo e realizar as transformações necessárias. 

###### **Atenção.** 

Você pode notar que os modelos dim_products e stg_products já estão disponíveis no repositório de exemplo. Use-os como referência para construir os demais modelos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

30 

###### with 

source_data as ( select country , city , fax , postal_code , address , region , customer_id 

, contact_name , phone 

, company_name , contact_title from {{source('northwind','customers')}} ) 

select * 

from source_data 

Ao explorar melhor as chaves e o modelo conceitual do DW, identificamos as seguintes relações no nosso mart de orders: 



<!-- Start of picture text -->
T7.<br><!-- End of picture text -->

_Fig. 55_ Modelo conceitual da Northwind 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

31 

Para facilitar nosso entendimento, também criamos um modelo conceitual com o mapeamento das relações. Na prática, podemos fazer isso diretamente no código e depois deixar o próprio dbt gerar esse diagrama para nós: 



<!-- Start of picture text -->
Ts)<br>)]<br>I ))<br>|<br>fot_order_detail<br>)<br>|<br>a)<br><!-- End of picture text -->

_Fig. 56_ Modelo dimensional da Northwind 

A partir deste diagrama podemos definir uma sequência de tarefas que precisamos para modelar nosso data mart antes de rodar o pipeline: 

1. Incluir todas as tabelas necessárias no arquivo sources.yml 

2. Criar os modelos staging necessários 

3. Criar as tabelas dimensão e chaves surrogates 

4. Criar a tabela fato 

A estrutura final do nosso projeto ficaria mais ou menos assim: 

├── marts 

- │ ├── dim_customers.sql 

- │ ├── dim_customers.yml 

- │ ├── dim_employees.sql 

- │ ├── dim_products.sql 

- │ ├── dim_products.yml 

- │ ├── dim_shippers.sql 

- │ ├── dim_suppliers.sql 

- │ ├── fct_order_detail.sql 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

32 

│ └── fct_order_detail.yml └── staging ├── sources.yml ├── stg_customers.sql ├── stg_employees.sql ├── stg_order_detail.sql ├── stg_orders.sql ├── stg_products.sql ├── stg_shippers.sql └── stg_suppliers.sql 

Vamos omitir as etapas 1 e 2 e partir diretamente para a etapa 3: Criar as tabelas dimensão e chaves surrogates. Vamos iniciar pela tabela de clientes ( _customers_ ) e criar uma chave surrogate auto-incremental a partir da chave de negócio customer_id: 

###### **Importante!** 

As chaves auto-incrementais são muito utilizadas em bancos de dados e de fácil entendimento pelos consumidores dos dados. No entanto, em _data warehouses_ modernos elas podem ser perigosas. Por quê? 

with staging as ( select * from {{ref('stg_customers')}} ) , transformed as ( select row_number() over (order by customer_id) as customer_sk -- auto-incremental surrogate key , customer_id , country , city , fax , postal_code 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

33 

, address , region , contact_name , phone , company_name , contact_title from staging ) 

select *  from transformed 

Depois de criadas as tabelas dimensão, mudamos nossa atenção para a tabela fato. Iniciamos pela tabela de capa do pedido ( _orders_ ) e suas dimensões dim_shippers, dim_customers e dim_employees. A ideia é criar uma tabela fato apenas com as chaves estrangeiras porém logo vemos que algumas colunas da tabela de pedidos não são medidas mas crescem proporcionalmente à tabela fato (informações de entrega, Código do Pedido, etc). Deste modo, resolvemos deixar essas informações na tabela fato como dimensões degeneradas. 

with customers as ( select customer_sk , customer_id FROM {{ref('dim_customers')}} ), employees as ( select employee_sk , employee_id FROM {{ref('dim_employees')}} ), suppliers as ( select supplier_sk , supplier_id FROM {{ref('dim_suppliers')}} 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

34 

), shippers as ( select shipper_sk , shipper_id FROM {{ref('dim_shippers')}} ), products as ( select product_sk , product_id FROM {{ref('dim_products')}} ), orders_with_sk as ( select orders.order_id , employees.employee_sk as employee_fk , customers.customer_sk as customer_fk , shippers.shipper_sk as shipper_fk , orders.order_date , orders.ship_region , orders.shipped_date , orders.ship_country , orders.ship_name , orders.ship_postal_code , orders.ship_city , orders.freight , orders.ship_address , orders.required_date from {{ref('stg_orders')}} orders LEFT JOIN employees employees ON orders.employee_id = employees.employee_id LEFT JOIN customers customers ON orders.customer_id = customers.customer_id LEFT JOIN shippers shippers ON orders.shipper_id = shippers.shipper_sk ) 

select * from orders_with_sk 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

35 

Ocorre que não queremos apenas a capa dos pedidos mas também o detalhamento desses pedidos na tabela fato, ou seja, queremos que o grão da tabela seja cada item do pedido de modo que possamos somar um total ou média de pedidos por produto/cliente sem recorrer a outras operações de JOIN. Como já vimos no capítulo anterior, a melhor opção é juntar a capa do pedido (orders) e o detalhe do pedido (order_details) na mesma tabela fato, ainda que essa arquitetura não seja tão eficiente em termos de armazenamento: 

(...) , **final as** ( **select** order_dtl.order_id , orders.employee_fk , orders.customer_fk , orders.shipper_fk , orders.order_date , orders.ship_region , orders.shipped_date , orders.ship_country , orders.ship_name , orders.ship_postal_code , orders.ship_city , orders.freight , orders.ship_address , orders.required_date , order_dtl.product_fk , order_dtl.discount , order_dtl.unit_price , order_dtl.quantity **from** orders_with_sk orders **left join** orders_detail_with_sk order_dtl **on** orders.order_id = order_dtl.order_id ) 

###### **select** * **from final** 

### Rodando o pipeline 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

36 

Falamos sobre como criar os modelos .sql do dbt mas não como eles são materializados de fato, ou seja, se tornam tabelas, visualizações etc. Este processo é realizado através do comando dbt run ou dbt build, que processa as dependências entre os modelos geradas a partir das macros {{ ref() }} e {{ source()}} e executa cada script na sua sequência correta: 

###### **Para saber mais.** 

Leia a documentação oficial do dbt e entenda a diferença entre o _dbt run_ e _dbt build_ . 

$ dbt run 

00:01:47  Running with dbt=1.3.0 00:01:47  Found 2 models, 5 tests, 0 snapshots, 0 analyses, 319 macros, 0 operations, 14 seed files, 7 sources, 0 exposures, 0 metrics 00:01:47 00:01:48  Concurrency: 1 threads (target='dev') 00:01:48 00:01:48  1 of 2 START sql table model northwind.stg_products ............................ [RUN] 00:01:51  1 of 2 OK created sql table model northwind.stg_products ....................... [CREATE TABLE (77.0 rows, 7.5 KB processed) **in** 3.34s] 00:01:51  2 of 2 START sql view model northwind.dim_products ............................. [RUN] 00:01:53  2 of 2 OK created sql view model northwind.dim_products ........................ [CREATE VIEW (0 processed) **in** 1.20s] 00:01:53 00:01:53  Finished running 1 table model, 1 view model **in** 0 hours 0 minutes and 5.38 seconds (5.38s). 00:01:53 00:01:53  Completed successfully 00:01:53 00:01:53  Done. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2 

Podemos notar no output do dbt run que o dbt nos informa o tipo de materialização de cada modelo. Mas como configuramos isso? Há duas formas: através de uma configuração em cada modelo ou de forma mais geral no dbt_project. No primeiro exemplo abaixo, podemos dizer para o 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

37 

dbt materializar o modelo fct_order_detail como tabela no banco de dados, aumentando a performance em relação à visualização ( _view_ ). No segundo caso, resolvemos que as tabelas staging não são necessárias em nosso DW mas apenas no processo de transformação e por isso definimos que todos os modelos na pasta models/staging não serão materializados ( _ephemeral_ ). Quando os dois casos estiverem presentes para o mesmo modelo, a configuração dada no modelo leva prioridade sobre a presente no projeto. Em geral, devemos evitar configurar materializações nos modelos e utilizar as opções do dbt_project. 

{{config (materialized='table')}} 

with customers ( (...) ) (...) 

Exemplo de configuração de materialização no modelo do dbt 

**models** : **northwind** : **staging** : **materialized** : ephemeral **marts** : **materialized** : table 

Exemplo de configuração de materialização no dbt_project.yaml 

Em geral, tabelas são preferíveis para otimizar as consultas no BI pois possuem um desempenho melhor de leitura que uma visualização (view). Durante a etapa de desenvolvimento o uso de views geralmente é mais rápido na hora de executar o pipeline, principalmente se as tabelas forem muito grandes. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

38 

### Escrevendo testes 

Garantir a integridade dos dados na transformação é parte essencial de qualquer projeto de ETL e o dbt foi pensando com as melhores práticas de engenharia de software em mente, em especial a capacidade de escrever testes sobre os dados de forma direta e consistente. 

Quanto mais cedo incluirmos testes no processo de ETL, mais fácil será a validação dos modelos finais com o cliente. É por isso que recomendamos inverter o processo e escrever testes antes mesmo de escrever os modelos. 

Conceitualmente, há dois tipos de testes no dbt: 

- testes genéricos (antigos testes de schema): são definidos em um arquivo .yaml e permitem realizar testes gerais sobre colunas da tabela, tais como: unicidade, não-nulicidade, valores dentro de uma lista pré definida, relacionamentos, entre outros. O teste falha quando há algum registro que não passa em um teste específico . Ex. há um registro duplicado em uma coluna com teste de unicidade. 

- testes singulares (testes de dados): são consultas sql que devem retornar 0 linhas para passarem no teste. Geralmente são testes baseados em dados validados com o cliente e de grande importância para garantir que os modelos estão gerando resultados consistentes. 

De forma geral, devemos incluir ao menos um testes genérico para cada modelo na sua chave primária (surrogate ou natural). Por exemplo, para garantir que não tenhamos nenhum cliente repetido na tabela de clientes, vamos criar um arquivo dim_customers.yml e incluir dois testes para a chave sk: 

###### **version** : 2 

**models** : 

- **name** : dim_customers **columns** : - **name** : customer_sk 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

39 

**description** : The primary key of the customer 

**tests** : 

- unique 

- not_null 

Para entender como os testes funcionam na prática, precisamos rodar o comando dbt run no terminal. Ao fazê-lo, o dbt converte os testes em consultas SQL apropriadas e retorna o resultado (sucesso ou falha) de forma similar a um modelo: 

$ dbt test 00:07:00  Running with dbt=1.3.0 00:07:00  Found 2 models, 5 tests, 0 snapshots, 0 analyses, 319 macros, 0 operations, 14 seed files, 7 sources, 0 exposures, 0 metrics 00:07:00 00:07:00  Concurrency: 1 threads (target='dev') 00:07:00 00:07:00 1 of 5 START test accepted_values_dim_products_is_discontinued__No__Yes ........ [RUN] 00:07:02  1 of 5 PASS accepted_values_dim_products_is_discontinued__No__Yes .............. [PASS in 1.86s] 00:07:02  2 of 5 START test not_null_dim_products_product_sk ............................. [RUN] 00:07:04  2 of 5 PASS not_null_dim_products_product_sk ................................... [PASS in 1.89s] 00:07:04  3 of 5 START test source_not_null_northwind_orders_order_id .................... [RUN] 00:07:06  3 of 5 PASS source_not_null_northwind_orders_order_id .......................... [PASS in 1.55s] 00:07:06  4 of 5 START test source_unique_northwind_orders_order_id ...................... [RUN] 00:07:07  4 of 5 PASS source_unique_northwind_orders_order_id ............................ [PASS in 1.78s] 00:07:07  5 of 5 START test unique_dim_products_product_sk ............................... [RUN] 00:07:09  5 of 5 PASS unique_dim_products_product_sk ..................................... [PASS in 1.97s] 00:07:09 00:07:09  Finished running 5 tests in 0 hours 0 minutes and 9.67 seconds (9.67s). 00:07:09 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

40 

00:07:09  Completed successfully 

00:07:09 

00:07:09  Done. PASS=5 WARN=0 ERROR=0 SKIP=0 TOTAL=5 

Vemos que nossa tabela dimensão clientes não possui nenhum registro repetido ou nulo na coluna customer_sk. Mas e se fizermos o mesmo teste para a coluna order_id na tabela de pedidos? o que esperamos encontrar? Lembremos que optamos por juntar na tabela fato a tabela de itens por pedido, de modo que podemos ter múltiplas linhas para cada pedido. Ao rodar um teste de unicidade para o id do pedido (order_id), esperamos que esse teste falhe e é exatamente isso que acontece. Vemos que o dbt encontrou 693 linhas repetidas quando esperávamos nenhuma: 

###### $ dbt test 

###### 00:21:52  Running with dbt=1.3.0 

00:21:53  Found 3 models, 7 tests, 0 snapshots, 0 analyses, 319 macros, 0 operations, 14 seed files, 7 sources, 0 exposures, 0 metrics 

00:22:01  5 of 7 FAIL 693 source_unique_northwind_order_details_order_id ................. [FAIL 693 **in** 1.58s] 00:22:01 6 of 7 START test source_unique_northwind_orders_order_id ...................... [RUN] 00:22:03  6 of 7 PASS source_unique_northwind_orders_order_id ............................ [PASS **in** 1.32s] 00:22:03  7 of 7 START test unique_dim_products_product_sk ............................... [RUN] 00:22:05  7 of 7 PASS unique_dim_products_product_sk ..................................... [PASS **in** 2.11s] ... 00:22:05  Completed with 1 error and 0 warnings: 00:22:05 00:22:05 Failure **in** test source_unique_northwind_order_details_order_id (models/staging/sources.yml) 00:22:05    Got 693 results, configured to fail **if** != 0 00:22:05 00:22:05 compiled Code at target/compiled/northwind/models/staging/sources.yml/source_unique_northwind _order_details_order_id.sql 00:22:05 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

41 

00:22:05  Done. PASS=6 WARN=0 ERROR=1 SKIP=0 TOTAL=7 

É comum que durante o processo de modelagem aconteçam transformações que porventura dupliquem registros que deveriam ser únicos (um join equivocado por exemplo) ou que possivelmente existam regras de negócio que não sabíamos de antemão. Para esses casos, escrever testes de forma consistente facilita muito o trabalho de validação e desenvolvimento dos modelos com segurança. Além de unicidade e não-nulidade, outros testes de schemas comuns a serem incluídos nos modelos são: 

- Teste de relacionamento (relationship): os testes de relacionamento servem para garantir relacionamentos entre colunas de modelos distintos, similar ao comportamento de chaves estrangeiras no banco transacional. Geralmente é utilizado para mapear chaves de dimensões dentro das tabelas fato. 

**version** : 2 

**models** : - **name** : fct_order_detail **columns** : - **name** : employee_fk **description** : The foreign key to the employees dimension table **tests** : - **relationships** : **to** : ref('dim_customers') **field** : 'customer_sk' 

- Teste de valores aceitos (accepted_values): esse tipo de teste serve para garantir que os valores de uma coluna estejam em um intervalo pré-definido. Por exemplo, em uma coluna de status de pedido. 

**version** : 2 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

42 

**models** : - **name** : dim_products **columns** : - **name** : is_discontinued **tests** : - **accepted_values** : **values** : ['No','Yes'] 

Na maioria dos casos, a grande dificuldade no processo de modelagem de dados é garantir que indicadores e resultados sejam os mesmos (ou próximos) dos considerados ‘verdadeiros’ pelo cliente. Não raramente o próprio cliente não tem uma visão clara dos passos necessários, fontes de dados e regras de negócios que são aplicadas antes da geração de um indicador em um relatório ou planilha de Excel e é o trabalho do analytics engineer trabalhar de forma integrada com o cliente para extrair essas informações e aplicar no processo de modelagem. Para facilitar esse trabalho podemos utilizar os testes de dados. isto é, consultas SQL arbitrárias em cima dos modelos que garantem que nossos modelos cheguem no resultado desejado. Para evitar outros problemas como dados mutáveis, atraso no ETL etc, o ideal é sempre fixarmos um período retroativo onde temos confiança que os dados não irão se alterar. 

Como exemplo, queremos validar a quantidade de itens em pedidos da nossa tabela de fatos de pedidos (fct_order_detail). Para isso, vamos fazer uma consulta nos dados originais e fixar os pedidos criados em março de 1998 como período de validação. Podemos gerar a consulta diretamente em SQL e logo obtemos uma quantidade de 4065 unidades vendidas. 

Após hipoteticamente confirmarmos com a Northwind que esse número é consistente, podemos utilizar como validação em nosso teste de dados sum_quantity_march_1998.sql. Notamos que a sintaxe do teste é muito próxima de um modelo mas que devemos escrever nossa consulta final como se quiséssemos que ele “desse errado”, isto é, queremos retornar todas as linhas onde o teste não passa ao rodar o dbt test, e o sucesso no teste ocorre quando o resultado da consulta é vazio. 

* If sum of quantity in March-1998 is not 4065, throws an error */ 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

43 

with 

sum_quantity as ( 

SELECT 

sum(quantity) as cnt FROM {{ ref ('fct_order_detail') }} where order_date between '1998-03-01' and '1998-03-31' ) 

select * from sum_quantity where cnt != 4065 

Ao combinarmos o uso de testes genéricos e singulares desde o início do projeto, garantimos a consistência e integridade do ETL mesmo em projetos com centenas de modelos. 

### Documentando o modelo de dados e visualizando as dependências 

A última etapa dentro de um projeto padrão de dbt é a documentação dos modelos e transformações. Essa documentação é feita a partir dos arquivos schema.yml que já utilizamos para escrever nossos testes de schema através de campos de descrição de tabelas e colunas. Ao criarmos as descrições, elas são adicionadas com outras informações que o dbt processa de como as fontes, modelos e testes do projeto estão estruturados. No exemplo abaixo documentamos a tabela dimensão Produtos e cada uma de suas colunas, de preferência na mesma ordem que no modelo final: 

###### **version** : 2 

###### **models** : 

- **name** : dim_products 

**description** : Esta é a tabela dimensão produto da northwind. Ela contém informações sobre os produtos da empresa. 

**columns** : 

- **name** : product_sk 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

44 

**description** : A chave surrogate da dimensão. Deve ser única. **tests** : 

- unique 

- not_null 

- **name** : product_id **description** : A chave natural do produto. 

- **name** : product_name **description** : Nome do produto 

- **name** : units_in_stock **description** : Total de unidades em estoque de um determinado produto. 

- **name** : category_id **description** : A chave natural da categoria do produto. 

- **name** : unit_price **description** : O preço unitário do produto (mais recente) 

- **name** : reorder_level **description** : Ponte de re-estocage do produto 

- **name** : supplier_id 

**description** : A chave natural do forncedor 

- **name** : units_on_order 

**description** : Quantidade mínima por pedido 

- **name** : is_discontinued **description** : Binário. Se o produto foi descontinuado. 

**tests** : 

- **accepted_values** : **values** : ['No','Yes'] 

Embora já seja importante para o entendimento dos modelos junto ao código, é quando utilizamos o comando dbt docs que vemos o diferencial de utilizar o dbt nesse quesito. O comando dbt docs generate gera um arquivo de documentação em formato html que conseguimos visualizar 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

45 

de forma interativa no navegador mesmo em projetos complexos, facilitando a colaboração e compartilhamento da modelagem. A visualização é feita através do dbt docs serve no terminal: 



<!-- Start of picture text -->
Hedbt<br>Overview dim_products<br><!-- End of picture text -->

_Fig. 57_ Exemplo de documentação do dbt 

Além das descrições, o dbt gera uma árvore de dependências dos modelos que facilita o entendimento do ETL: 



_Fig. 58_ Exemplo de Linhagem de dados no dbt 

### Orquestração 

A documentação conclui as etapas básicas que devem constar de qualquer projeto de transformação de dados em dbt. Vale ressaltar que projetos de ETL raramente são lineares: geralmente passamos por diversas iterações de cada etapa do projeto, desde mapeamento de 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

46 

novas fontes, criação dos modelos, testes e documentação. Depois de validados, ainda precisamos apontar os modelos para um banco de dados em produção que será de fato consultado por uma ferramenta de BI ou outro uso pelo cliente, além de garantir que esse processo todo rode na frequência e horário adequado para os fins do projeto, processo também chamado de Orquestração. 

O dbt _open-source_ (também chamado de dbt core) não possui um orquestrador nativo, de modo que a orquestração do projeto precisa ser feita por uma ferramenta externa como o Airflow ou Prefect. Uma outra alternativa é utilizar o serviço do _dbt cloud_ , uma solução SaaS dos criadores do dbt que facilita o deploy de projetos em dbt e que possui um orquestrador incorporado. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

47 

#### Conclusão (opcional) 

Em um espaço de uma lauda, escreva uma conclusão para o conteúdo do módulo abordando os tópicos desenvolvidos. Não é necessário em cursos onde o material é 100% prático ou multimídia. 

Chegamos ao fim de nosso exemplo prático de transformação de dados com dbt e também de nossa Parte 3: Transformando dados com ELT. Espero que esse conteúdo seja útil para sua jornada de Engenharia de Analytics com o ELT e com o _Modern Data Stack_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

48 

#### Material Complementar (obrigatório) 

Forneça no mínimo 4 materiais complementares para que os alunos possam aprimorar seus conhecimentos acerca dos assuntos abordados durante a unidade. Indique sites, livros, vídeos, filmes, leitura de textos em PDF etc., e crie uma pequena contextualização para o(a) aluno(a), explicando qual a relação desse material para a sua formação pessoal e/ou profissional. 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Aula 8 | Introdução ao ETL 

**Descrição:** Gravação |   Introdução ao ETL 

**Link:** https://drive.google.com/file/d/1pW7KfQXXIC4WtXZcJQoMaEzeBlBB-amY/vie w 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Aula 9 | ETL na prática 

**Descrição:** Gravação |   ETL na prática 

**Link:** https://drive.google.com/file/d/1K9bwbGHTd1sgDflOWIqEbimjdP9K5hjO/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Aula 10 | Aulão - DW da Northwind 

**Descrição:** Gravação |   DW da Northwind 

**Link:** 

https://drive.google.com/file/d/1wqc4qPAecSW1qbYbAK_9fPsRCpKITmnF/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

49 

**Título:** Configurando a Instância no Big Query 

**Descrição:** Nesta vídeo aula aprenderemos a configurar uma instância no Big Query 

**Link:** https://drive.google.com/file/d/1jPxMXUupDDP3suUBCZl8__cfwuVLvI78/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Configurando a Instância no Big Query 

**Descrição:** Nesta vídeo aula aprenderemos a configurar uma instância no Big Query 

**Link:** https://drive.google.com/file/d/1jPxMXUupDDP3suUBCZl8__cfwuVLvI78/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Criando as chaves 

**Descrição:** 

**Link:** https://drive.google.com/file/d/1XbNiw-Z-ljNgVKIkU59xrKqrcNxKEL6l/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Configurando a fonte de dados 

**Descrição:** Aula prática de configuração de fonte de dados. 

**Link:** https://drive.google.com/file/d/1G1zbyY24zjRxOhqhdu2Y7rQ8jZ9jynhw/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Configurando o Destino 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

50 

**Descrição:** Aula prática de configuração de destinos. 

**Link:** 

https://drive.google.com/file/d/1_A-UfWmqQy1fgM_imZ0oyKahkP7oFSIa/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Integração dos dados **Descrição:** Aula prática de integração de dados 

**Link:** https://drive.google.com/file/d/1H8j3rKovrTb7roswKQA50Dw6s-q0NTs8/view 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Vídeo 6 | Introdução ao ETL (Invisível) **Descrição:** Nesta aula prática, introduzimos o conceito de ETL. 

**Link:** https://youtu.be/J6BvuFQReRU 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Vídeo 7 | ETL na prática (Invisível) 

**Descrição:** Nesta aula prática, fizemos o ETL na Prática. 

**Link:** https://youtu.be/m-MMe92fAWI 

**Tipo** (marque apenas uma) **:** ☐ Site ☐ Livro   X Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Vídeo 8 | DW da Northwind (Invisível) **Descrição:** Neste aulão ao vivo, montamos o DW da Northwind! **Link:** <u>https://youtu.be/yAebQa64CtU</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

51 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

52 

#### Referências (opcional) 

Lista as referências utilizadas no conteúdo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

53 

