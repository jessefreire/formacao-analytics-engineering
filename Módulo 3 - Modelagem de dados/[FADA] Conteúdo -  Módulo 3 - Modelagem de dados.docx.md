

# Material Teórico 

Curso: Formação em Análise de Dados 

## Autoria 

Prof. Msc. Renata Assunção Prof. Ana Claudia Garcia 

## Módulo 

Módulo III - Modelagem de dados 

Temas abordados 

- Introdução aos bancos de dados analíticos 

- Conceitos de ETL 

- Data warehouses vs data lakes 

- Modelagem de dados 

- Tabelas Fato 

- Tabelas Dimensão 

- Consultando dados dimensionais 

- Boas práticas de uso do banco de dados analícos para Data Analysts 

## Objetivos de Aprendizagem 

Ao final deste módulo você vai: 

- conseguir identificar os principais **tipos de bancos de dados** ; 

- aprender mais sobre os conceitos de **ETL/ELT;** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

1 

- conhecer e entender as diferenças entre **data warehouse** , **data lake** e **data lake house** ; 

- aprender como **modelar os dados** e a estruturar as **tabelas fato** e **dimensão** ; 

- e vai conhecer as **melhores práticas** para consultar os dados em um **ambiente analítico** . 

Apresentação do Módulo Olá! 

Neste módulo, você verá quais são os principais conceitos que envolvem a **engenharia de dados** . 

Para isso vamos entender como funcionam os **bancos de dados analíticos** , conhecer o processo de **ETL** e ver a diferença entre fazer ETL ou ELT. 

Além disso, você verá como os data warehouses funcionam e entender as **diferenças entre data warehouse, data lake e data lakehouse** . 

Você compreenderá a importância da **modelagem de dados** e como as **tabelas fato** , **dimensão** e **ponte** se relacionam. Para isso precisamos antes conhecer esses tipos de tabelas e entender as suas principais características. 

Ao final, você aprenderá a **consultar dados dimensionais** . 

Conhecerá as principais **boas práticas** para utilizar os bancos analíticos, entendendo o porquê e como as boas práticas irão te ajudar. 

Aproveite as **atividades disponibilizadas** ao longo do curso para testar seu conhecimento e aprender um pouco mais sobre o assunto. 

Bons estudos e até logo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

2 

## Desenvolvimento 

### Aula 1 - Introdução aos bancos de dados analíticos 

Atualmente, a informação é um dos ativos mais valiosos para qualquer organização. A maneira como os dados são coletados, armazenados e gerenciados pode determinar o sucesso ou fracasso de um negócio ou projeto. 

E é aqui que entram os bancos de dados. Saber como armazenar e consultar esse ativo é crucial para fazer uso eficiente dos dados. Para aprofundar o entendimento, iniciaremos pela análise do que ocorre nos bastidores dos bancos de dados. Nesta aula, abordaremos a teoria necessária para a compreensão de conceitos que serão vistos posteriormente neste módulo. 

Antes, vamos relembrar o que já vimos até agora nesse curso. No módulo sobre SQL você ouviu falar sobre os bancos de dados. Entendeu os principais tipos de bancos de dados que existem e para quê cada um deles é destinado. Viu, também, o que é um banco relacional e como utilizar o SQL para se comunicar com ele. 

A partir disso, precisamos entender o que é um banco de dados analítico e para que ele se destina. Vamos iniciar compreendendo as principais diferenças entre os bancos transacionais e os analíticos para alguns critérios. 

#### **Legibilidade dos dados** 

Os bancos transacionais são os bancos de dados que alimentam os sistemas, sites, etc. Considere cada transação da empresa fictícia Banvic, como um documento ou um contrato, que precisa ser guardada em um local específico para consulta futura. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

3 

Em um banco de dados transacional, cada fragmento do contrato pode ser armazenado em um local distinto, de modo que possa ser utilizado em diversas partes do sistema sem perda de desempenho. 

Tal abordagem pode resultar em um modelo de organização altamente complexo, dificultando para o usuário a tarefa de relacionar as tabelas e consultar os dados. 



<!-- Start of picture text -->
Cor: 125 product. Sane<br>[Baws —a wet ||epee<br>[Pett id supplier.— roc ast.name<br>cpcbaone cconpony. pesca<br>#96fee description picturecategory.name | © *)s28123 suppliercategory id ihe ie aoc title<br>B id Sconackt ooe title of courtesy<br>0c quantity_per_unit fo ~ - - .o] *F address @ birth dare<br>suo crea ties<br>123 units in_stock moc pont code rec adcress p0¢territory. description<br>123 units_on order — eee city 323 region.id<br>123reorderlevel eouney a2¢ region<br>.<br>128 discontinued prove eve postal code $<br>a<br>=<br>eta scourey [reson]<br>\secnn<br>“ Victtesce” | eine<br>a 1B photo —<br>ee . eno k<br>iin 123 reports to \<br>25 dscoue 6 Veep |<br>[senders | too<br>Pee customer_id- a H v -<br>[Samora | 123zeman employeeid tot,<br>[wecntameri6_| regres.<br>F9€A®¢ cc o mpnt a ct:nameny_name 1© shipped date<br>s0¢ == ~~~ 4323 ship via<br>noc contact address tide an weceeeeeecreete 123 freight A<br>oe 8 ship name me<br>0 regioncity ese customer ae stip_address d<br>aA0€ postal.code /#8€ customertypeid id ee2€ ship ship city region [:22shipperid/8e¢ companyname| estempame<br>ae state_abbr<br>sshncury<br>#2¢ country ———S—— se ship postal code A phone eae state_pegion<br><!-- End of picture text -->

Figura 1: Modelo de dados de um banco transacional. 

Além disso, os bancos de dados transacionais, por servirem de base para os sistemas corporativos, não podem correr o risco de indisponibilidade. 

Por essa e outras razões que serão abordadas adiante, as empresas optam por bancos de dados analíticos para realizar consultas estratégicas. Esses bancos de dados são comumente organizados para 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

4 

facilitar a localização e o uso das informações em um repositório conhecido como Data Warehouse. 

O Data Warehouse é um grande armazém de dados, organizado para que os usuários localizem as informações de que necessitam com rapidez e facilidade, permitindo extrair valor dos dados de forma otimizada. 

Para tornar as consultas aos bancos analíticos mais performáticas, a arquitetura do Data Warehouse difere daquela utilizada nos bancos transacionais. 

Entender essa estrutura nos ajudará a entender como um banco de dados analítico busca e processa os dados solicitados. Isso impacta diretamente tanto o tempo de resposta de uma consulta quanto o seu custo para a empresa. 

#### **Processamento dos dados** 

Os bancos de dados transacionais utilizam o processamento OLTP (On-Line Transactional Processing). Esse modelo é ideal para executar transações rápidas, que leem e atualizam volumes reduzidos de dados por vez. 

Já os bancos de dados analíticos empregam o processamento OLAP (On-Line Analytical Processing). Eles são projetados para lidar com consultas complexas que analisam grandes volumes de dados para computar diferentes tipos de agregações. 

Numa escala que compara a complexidade ao objetivo da operação, o OLTP é mais simples e ideal para operações de escrita. Em contrapartida, o OLAP suporta operações mais complexas e é excelente para a leitura de dados, destinando-se, portanto, à realização de consultas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

5 



<!-- Start of picture text -->
@<br>g<br>83<br>OLAP<br>°<br>8<br>Ss.<br>8G<br>a<br>6<br>OLTP<br>P<br>8aE<br>3<br>Ler Escrever<br>Fluxo trabalho<br><!-- End of picture text -->

Title: Fluxo de trabalho. 

Alt tag: 4 quadrantes, divididos entre operação simples e fluxo de trabalho de leitura (OLTP): operação complexa e fluxo de trabalho de escrita (OLAP). 

#### **Armazenamento de dados** 

O armazenamento de dados também é diferente de acordo com o banco que vai ser utilizado. Ou seja, a forma de processamento está diretamente relacionada ao formato de armazenamento que os bancos de dados irão utilizar para organizar suas informações. 

Nos bancos de dados transacionais, os dados são armazenados de forma relacional, em um formato de linha. Isso significa que cada registro completo é armazenado em uma única linha da tabela. 

Por exemplo: em um sistema de vendas, uma linha pode conter todas as informações de uma transação específica, como o ID do cliente, a data da venda, os itens comprados e o valor total. 

Esse formato de armazenamento em linha é eficiente para operações de leitura e escrita rápidas, pois permite que o sistema acesse e atualize todas as informações relacionadas a um registro de uma só vez. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

6 

Essa é uma característica muito importante em ambientes onde a velocidade e a integridade das transações são o foco da operação, como em sistemas bancários ou de comércio eletrônico, por exemplo. 



<!-- Start of picture text -->
==<br>T1254”PeMargarida de Jesus margarida6S@maiicom===]== PF==«(1/0572015«10/08/1984SS © SoPauo = =EESPOS 1<br>1235 Joana da Silva jsitva@mail com PF 02/05/2015ed(25/11/1995 Londrina PR<br>1236 Gabnela Oliveira gabi_oliveira@mail.com PF 02/05/2015 31/01/2000 Piracicaba ‘SP<br>1237 Roberto Garcia garcia_bbto@mail com PF 03/05/2015, 04/10/1978 ‘So Paulo sP<br>1238 Felipe Novais felipe novais@mail.com PF 03/05/2015 22/06/1998 Rio de Janeiro RS<br>1239 Joaquim Pereira Joaguim@emalcom PF 3105/2015 12104979 Campinas sP<br>a ae<br>I['1234"Margarida de Jesus’, ‘margarida65@mail.com’/PF’, | ~SL saaea<br>['01/05/2015','10/08/1984','So(1258,—Joana Ga SIVA,-— ‘-siva@mal.con,aPaulo’'SP}], PF aS ~ — oPH<br>(02/05/2015,'25/11/1995','Londrina,’PR’] oo GEES<br><!-- End of picture text -->

Fonte: Academy. 

Title: Sistema de vendas. 

Alt tag: exemplo de tabela de vendas e como essas informações ficam armazenadas linha por linha no banco de dados. 

No entanto, se você quiser misturar informações de diferentes colunas para compor um resultado específico, por exemplo, saber quantos cadastros de clientes são feitos por mês, no estado do Paraná, o banco de dados OLTP precisará ler todos os dados de cada linha para obter a informação desejada 

Esse processo pode ser custoso e bastante demorado para esse tipo de banco. Para esses casos, o banco analítico é o mais indicado. 

Isso porque os bancos de dados analíticos (OLAP) armazenam os dados em um formato diferente, organizado por colunas. Neste caso o banco pega todos os dados das colunas e vai armazenando junto. Cada coluna é “independente” e pode ser consultada sem que seja necessário olhar para a linha inteira. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

7 

Em bancos OLAP (Data Warehouse), é comum encontrar tabelas muito grandes, com milhões de linhas. 



<!-- Start of picture text -->
i ad<br>1234 Margarida de Jesus ‘margarida65@mail.com PF | o1s2015 | tov08/1984 ‘S80 Paulo SP.<br>1235 Joana da Silva jsitva@mail.com PF | 02/05/2015 | (25/11/1995 Londrina PR<br>1236 Gabriela Oliveira gabi_oliveira@mail com PF | 02/05/2015, | 3101/2000 Piracicaba sp<br>1237 Roberto Garcia garcia_bbto@mail com Pr 03/05/2015, 04/10/1978 ‘S40 Paulo ‘sP<br>1238 Felipe Novais felipe. novais@mail.com PF | oasis | 2206/1996 Rio de Janeiro RJ<br>1239 Joaquim Pereira Joaquim@email.com PF | 03/05/2015, | 12/04/1979 Campinas sP<br>= Data Inclusao<br>Nome "| 01/05/2018';02/05/2015',<br>-----| (02/05/2015','03/05/2015<br>POY =. | 03/05/2015-03'05/2018<br>Email } ><br>SESEE‘RIER|<br>Tipo Cliente<br><!-- End of picture text -->

Fonte: Academy. 

Title tag: banco OLAP (DW). 

Alt tag: exemplo de banco OLAP (DW) em tabela com nome, email, tipo de cliente e data de inclusão e como esta informação fica armazenada em formato colunar no banco de dados. 

O banco de dados não precisa ler sempre todos os dados da coluna para retornar um resultado agregado. Porém, quando realizamos consultas, em especial as mais complexas, envolvendo muitas colunas, é comum que o banco perca eficiência e demore para retornar os dados solicitados. 

Atualmente, os bancos de dados mais modernos possuem nativamente uma estratégia de particionamento dos dados, mas essa configuração também pode ser feita manualmente. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

8 

#### **Particionamento de tabelas** 

O particionamento de tabelas nada mais é do que “quebrar” o armazenamento dos dados das colunas e salvá-los em partes menores. Voltando ao nosso exemplo, digamos que essa tabela de cadastros de clientes seja muito grande, com um alto volume de linhas. 

O ideal, se precisarmos manter todo o histórico disponível no data warehouse, seria particionar essa tabela. O objetivo é fazer com que o banco de dados não precise processar muito mais dados do que necessitaria para retornar o resultado da consulta. 

Um bom exemplo seria particionar a tabela por dia. Cada coluna será quebrada em arquivos menores contendo apenas os dados de cada um dos dias. Cada data warehouse pode permitir o particionamento de uma forma específica, mas o objetivo é sempre o mesmo: dividir em partes menores para otimizar a consulta. 



<!-- Start of picture text -->
Tipo de tabela Particionada<br>Particionada por DAY<br>Particionada no campo _PARTITIONTIME @<br>Expiragao da parti¢ao As particdes nZo expiram<br>Filtro de partigao Nao obrigatorio<br><!-- End of picture text -->

Title: particionamento de tabela. 

Alt tag: Exemplo de como fica a tabela particionada por dia. 

Seguindo o exemplo da imagem acima, se quisermos saber a quantidade de cadastros por estado no dia 02/05/2015 e a nossa tabela estiver particionada por data, apenas os compartimentos que se referem a esse dia serão consultados. Veja que, dessa forma, conseguimos facilitar bastante o trabalho do banco de dados. 

Mas imagino que você possa estar se perguntando se não faria sentido, então, utilizar a coluna com maior cardinalidade da tabela, tendo assim basicamente um arquivo por linha. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

9 

Aqui, teremos dois pontos para justificar por que essa não é uma boa estratégia. Mas, antes, vamos entender o que cardinalidade significa. 

Cardinalidade, no mundo dos dados, refere-se ao número de elementos distintos que podem existir em um conjunto de dados. Ela descreve a natureza das relações entre tabelas. 

Por exemplo: uma relação pode ser 1:1, na qual cada registro em uma tabela corresponde a um único registro em outra tabela. Pode ser 1:n (1: ) e, nesse caso, um registro em uma tabela pode corresponder a múltiplos registros em outra tabela. Pode ainda ser n:n ( : *), e teremos uma situação em que múltiplos registros em uma tabela podem corresponder a múltiplos registros em outra tabela. 

Conhecendo essas possibilidades de relações, é possível criar esquemas que garantam a integridade e eficiência do banco de dados. Assim, é possível evitar redundâncias, manter a consistência dos dados e otimizar o desempenho das consultas. 

Voltando aos pontos sobre o porquê não é uma boa estratégia utilizar a coluna com maior cardinalidade para fazer o particionamento, que mencionamos anteriormente, o primeiro deles diz respeito à quantidade de arquivos que o banco precisará mapear e consultar para conseguir trazer o resultado que você espera. 

Esse processo se tornará lento se ele sempre precisar consultar uma grande quantidade de partições para retornar uma agregação para você. 

O segundo ponto diz respeito à identificação da partição. Digamos que você utilizou o id do cliente para fazer o particionamento. Esse id dificilmente será chamado explicitamente em um filtro ou agrupamento, então não teremos um ganho de eficiência pedindo ao banco de dados para buscar os dados correspondentes aos IDs solicitados. 

Por isso, normalmente escolhemos colunas que são muito utilizadas em filtros e agrupamentos para fazer esse processo. As datas são o tipo mais 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

10 

comum de particionamento, podendo ser feito por dia, mês ou ano, dependendo do uso e da quantidade de dados. 

De forma resumida, os bancos de dados analíticos são sistemas especializados projetados para suportar a análise de dados em larga escala, otimizados para consultas complexas e geração de insights. Seu principal objetivo é auxiliar na tomada de decisões, fornecendo uma visão consolidada e histórica dos dados. Esses sistemas se destacam por serem diferentes dos bancos de dados transacionais, tanto em seu objetivo quanto em sua arquitetura e aplicação. 

Enquanto os bancos de dados transacionais (OLTP) são focados no gerenciamento das operações do dia a dia, como sistemas de vendas ou ERPs, os bancos de dados analíticos (OLAP) são projetados para suportar análises e relatórios mais aprofundados. 

Nos sistemas transacionais, os dados são altamente normalizados para garantir consistência e eficiência na escrita e atualização, enquanto nos sistemas analíticos, a estrutura é frequentemente desnormalizada, o que melhora o desempenho das consultas. 

Além disso, os sistemas transacionais realizam consultas simples e frequentes, enquanto os sistemas analíticos são otimizados para consultas complexas e intensivas, focadas na leitura de grandes volumes de dados. 

Tendo em vista tudo o que falamos, em geral, podemos dizer que eles se diferenciam pelo seu propósito, estrutura, conteúdo e usuários. 

Quando falamos de propósito, o banco transacional se propõe a suportar as operações diárias da organização, como processar transações de vendas, gerenciar inventário, realizar reservas, etc. Já o Data Warehouse, se propõe a dar suporte à análise de dados e à tomada de decisões, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

11 

permitindo que os usuários consultem grandes quantidades de dados históricos e respondam perguntas mais complexas. 

Quando falamos sobre a estrutura das tabelas, o banco transacional geralmente é estruturado em tabelas normalizadas, com muitas relações entre elas, enquanto o DW costuma utilizar uma estrutura dimensional, com fatos e dimensões, que é otimizada para análise de dados. 

Em relação ao conteúdo, o banco transacional se propõe a armazenar dados operacionais correntes e atualizados de um único sistema, enquanto o data warehouse contém dados históricos e normalmente é a consolidação de várias fontes de dados. 

Já em relação aos usuários de cada tipo de banco de dados, o banco transacional possui como usuários, geralmente, colaboradores que realizam operações diárias, como inserir ou atualizar informações em um sistema. No DW, os usuários tendem a ser analistas, gerentes e executivos que precisam de informações para apoiar sua tomada de decisão. 

Como pudemos ver, ambos são importantes para a gestão de dados empresariais. Muitas empresas usam essas duas formas combinadas para gerir e analisar seus dados de maneira eficiente. 

Agora que já conhecemos melhor os bancos de dados, vamos aprender sobre como é o processo de trazer os dados para o Data Warehouse, o que você acha? 

Nos vemos na próxima aula. Até lá! 

### Aula 2 - Conceitos de ETL 



Até o momento, você já conhece como funcionam os **bancos de dados analíticos** . Agora, você vai saber como os dados vão parar lá dentro, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

12 

chegando sempre atualizados nas **ferramentas de BI** utilizadas. Para isso, existe um processo famoso na **engenharia de dados** que chamamos de **ETL** . 

O **ETL** é uma sigla que representa as três importantes etapas do processo de engenharia de dados: **extração (extraction), transformação (transformation) e carga** . 

Essas etapas são essenciais para a integração e transformação de **dados** de várias fontes para um destino específico, normalmente um **data warehouse** . 

Confira mais detalhes sobre cada etapa a seguir: 

- A **extração** envolve a obtenção de **dados** de diversas fontes, como **bancos de dados** , planilhas ou arquivos CSV. O objetivo é coletar os **dados** necessários para análise e processamento que serão armazenados em um repositório único. 

- A **transformação** é a etapa em que os **dados** coletados na extração são transformados para que possam ser integrados e armazenados em uma base de **dados** de destino. Essa etapa envolve limpeza, estruturação e enriquecimento dos **dados** para garantir que eles sejam úteis e relevantes para a análise. 

- A **carga (ou load, como preferir)** é a última etapa do processo de **ETL** , na qual os **dados** transformados são carregados em um destino específico, como um **banco de dados** , um **data warehouse** ou um **data lake** . Isso permite que os usuários finais acessem e usem os dados para análise, geração de relatórios e tomada de decisões. 

A sigla **ETL** não apenas lista suas etapas, mas também representa a ordem em que tradicionalmente essas etapas são realizadas em um projeto. 

O diagrama a seguir apresenta uma estrutura de **ETL** tradicional. Nele, é possível perceber que existem algumas fontes de **dados** que são extraídas 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

13 

e sua transformação é feita logo após a extração. 

Ou seja, nós teremos apenas os **dados** com as transformações já feitas no **banco de dados** . 



<!-- Start of picture text -->
‘~<br>1<br>Arquivos '<br>1<br>1<br><= 1<br>| |— ETL ------>— ee<br>Banco de Dados '<br>'<br>~ '' —<br>------+ Data Warehouse<br>Eventos<br><!-- End of picture text -->

Figura: A casa dos dados. 

Fonte: elaborada por Indicium Academy. 

Title: 

Alt tag: 



Na **abordagem moderna de analytics** , o **ETL** é revisado e uma mudança no processo é proposta: o **ELT** . 

Nesse novo processo, primeiro os dados brutos são carregados para um **data warehouse** e depois transformados dentro do próprio **DW** . 

Mas afinal, qual a vantagem de mudar a ordem dessas letrinhas? 

A justificativa mais forte a favor do **ELT** é trazer pessoas que estão mais próximas do negócio para a construção do **data warehouse** . 

E, com isso, melhorar a experiência de uso do **dado** , facilitar a construção de regras de negócio e por aí vai. 

No **ETL** , geralmente todas as etapas ficam muito dependentes de **engenheiras e os engenheiros de dados** . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

14 

Com o **ELT** , essa pessoa pode olhar melhor para questões de **plataforma de dados** e quem for o **engenheira ou engenheiro de analytics** pode se dedicar a construir o “ **armazém de dados** ” para os analistas de dados das áreas de negócio. 

Com essa divisão, há uma redução na barreira de entrada de profissionais, principalmente para a etapa de transformação de **dados** . 

Dessa forma, o SQL reassumiu seu lugar de destaque como a linguagem universal dos dados. 

Isso porque praticamente não há mais limitações de escalabilidade como acontecia em **bancos de dados relacionais tradicionais** . 

Essa limitação, inclusive, foi um dos propulsores para a criação de diversas tecnologias de processamento de **big data,** como Hadoop, Spark, etc. 

Além disso, com o surgimento dos bancos de dados escaláveis na nuvem, como o Google BigQuery ou o Databricks, o custo de armazenamento de dados caiu drasticamente, diminuindo o problema de se ter dados duplicados entre camadas de dados brutos e transformados. 

Embora existam algumas diferenças de arquitetura e ferramentas utilizadas nos processos de **ELT** modernos, o quadro geral é o mesmo. 

Na etapa de extração, serviços como o Hevo, Fivetran, Kondado e Airbyte permitem “ **mover** ” **dados** de centenas de fontes, como ERPs, CRMs, bancos de dados, REST APIs, entre outros, diretamente para um **data warehouse** na nuvem ou on-premises com um baixo custo técnico. 

Desta forma, a etapa de load é feita simultaneamente à extração. Dentro do **DW** , a **transformação de dados** é feita através de scripts SQL gerenciados por ferramentas, como o **dbt** e **dataform** . 

Diversas alternativas open-source existem para o processo de **ELT** , porém 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

15 

exigem conhecimentos técnicos mais diversos, e geralmente são operadas por engenheiras ou engenheiros de dados especializados. 

Entre essas opções, podemos citar os singer taps, embulk ou mesmo scripts em Spark ou Python. 

Também será necessário orquestrar essas tarefas através de um orquestrador, como o Airflow ou Prefect. 





<!-- Start of picture text -->
Banco de dados ERP i<br>Banco<br>de dados CRM iF Tes Dados Bratos oer Dados Tansformados 7<br>ew X dbt<br>Logs i<br>Riiriow &<br><!-- End of picture text -->

Fonte: elaborada por Indicium Academy. 

Title: Alt tag: 



Outras vantagens dessa arquitetura **ELT** moderna são a modularidade, simplicidade, governança, o versionamento, a separação de ambientes e testes. Vejamos um a um. 

- **Modularidade** : ao separar as regras de negócio das etapas de extração e load, é possível utilizar ferramentas 3rd-party para integração de dados, com baixo investimento, como Stitch, Fivetran, entre outras. Dessa forma, o processo como um todo não fica refém de uma única solução, facilitando a inovação e economia. 

- **Simplicidade** : ao invés de escrever códigos em linguagens complexas, como Java, Python e Scala, a transformação pode ser 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

16 

centralizada em uma só linguagem (SQL), reduzindo custos com treinamento e manutenção, o que facilita o entendimento organizacional e muito mais. 

- **Governança** : um ambiente único simplifica a documentação e governança dos **dados** . Com isso, é possível criar lógicas de permissionamento e gerenciar **dados** sensíveis de forma integrada. 

- **Versionamento** : uma das grandes dificuldades em se trabalhar com bancos de dados era a dificuldade de controle de versionamento, essencial nas boas práticas de engenharia de software modernas. Ferramentas modernas de **ELT** , como o **dbt** , resolvem este problema, pois separam os arquivos de modelos de dados escritos em **SQL** do próprio banco de dados. O versionamento é importante para garantir que mais pessoas possam trabalhar em um mesmo projeto sem que um atrapalhe o outro. Além disso, é essencial para dar mais segurança no desenvolvimento, permitindo voltar a versões anteriores do código de forma rápida e segura, caso a atualização dê problemas. 

- **Separação de ambientes** : o **ELT** permite separar os ambientes de **dados brutos** (sources), **dados em transformação** (staging) e **dados finais** (marts) através de diferentes schemas no **banco de dados** . A partir disso, cada usuário pode ter seu ambiente de desenvolvimento, onde o trabalho colaborativo é facilitado e os erros de produção podem ser evitados. 

- **Testes** : o modelo **ELT** centraliza as boas práticas de testes em um único local no projeto, assim como ocorre em projetos de software modernos. Dessa forma, o analista pode escrever os testes diretamente em SQL, com os dados confiáveis, garantindo a consistência e confiabilidade nos modelos finais. 



#### **Recapitulando:** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

17 

Ao longo desta aula, exploramos detalhadamente o processo de **extração, carga e transformação (ELT)** e sua relevância no cenário moderno para o gerenciamento de dados. 

Com o aumento exponencial na quantidade de **dados** gerados diariamente, a capacidade de extrair dados de várias fontes, carregá-los de maneira eficiente em um **data warehouse** ou **data lake** , e transformá-los conforme necessário para análises é mais crítica do que nunca. 

Isso fez com que o **ELT** se tornasse um componente essencial no gerenciamento de dados de toda organização. 

Agora que já sabemos as principais diferenças entre o ETL e o ELT precisamos definir onde iremos salvar os dados após esse processo. 

Entram em cena os famosos data warehouses. Veremos mais sobre eles na próxima aula. Até lá. 

### Aula 3 - Data warehouses vs data lakes vs data lakehouse 

Existe mais uma forma de armazenar os dados, que chamamos de **data lake** e **data lakehouse** . 

Nos **data warehouses,** há uma grande preocupação com a padronização, qualidade e consistência dos **dados** . Isso porque ele se coloca como essa fonte de verdade, capaz de integrar diferentes fontes de **dados** com o objetivo de representar as áreas de negócio. 

Bancos analíticos modernos, principalmente na nuvem, são altamente escaláveis. 

Isso significa que mais servidores podem ser adicionados conforme a necessidade, sem tempo de inatividade. Essa flexibilidade tem um impacto financeiro alto. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

18 

Um **data warehouse** é composto por uma variedade de componentes, que trabalham juntos para coletar, armazenar, organizar e analisar grandes quantidades de dados de diferentes fontes. 

Os principais componentes de um **data warehouse** são: 

- **fontes de dados** : são o que alimenta o **data warehouse** , como bancos de dados transacionais, arquivos de log, sistemas ERP, CRM, planilhas, entre outros. 

- **camada de extração, carga e transformação (ELT)** : é responsável por extrair dados das fontes, transformá-los em um formato comum e carregá-los no **data warehouse** . Essa camada inclui ferramentas de **ELT** , scripts e processos para coletar, limpar e integrar os dados. 

- **camada de armazenamento** : armazena os **dados** coletados pelo **ELT** . Geralmente, os **dados** são armazenados em um esquema de estrela ou floco de neve, com tabelas fato e dimensão, e são organizados para permitir uma análise eficiente e fácil. 

- **camada de metadados** : é responsável por armazenar informações sobre os **dados** no **data warehouse** , como origem, formato, definições de dados e esquemas de tabela. Isso ajuda a garantir a integridade dos **dados** e facilita a análise e o acesso aos **dados** pelos usuários. 

- **camada de apresentação** : apresenta os dados do **data warehouse** para os usuários finais de maneira compreensível e fácil de usar. Isso pode incluir ferramentas de visualização de dados, dashboards, relatórios e aplicativos de análise. 

E um **data lake,** como funciona? 

Vamos fazer uma analogia aqui. Você pode imaginar o **data lake** como sendo um lago de dados que contém informações de diversos tipos e tamanhos diferentes. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

19 

Ao contrário de um **data warehouse** , que armazena apenas dados estruturados, o **data lake** permite o armazenamento de todos os tipos de dados: estruturados, não estruturados e híbridos. Tudo em um só lugar. 

Portanto, é um repositório muito mais amplo que possibilita análises adicionais e menos restritivas que um **DW** . Essas análises podem ser pesquisas de texto completo, análises de **big data** em tempo real, **machine learning** etc. 

Essa flexibilidade toda vem com seus contras. No **data lake** não há preocupação com a duplicação dos **dados** . É possível ter imagens que se repetem em pastas diferentes, sem a vinculação delas, por exemplo. 

Por isso, é mais provável que tenhamos mais inconsistências nos **dados** em um **data lake** . Aqui, é mais difícil testar os **dados** e garantir que eles sejam valiosos para o negócio. 

Atenção: **dados** de fontes e formatos diferentes não se integram naturalmente. A grande vantagem de um **data warehouse** é justamente a consolidação de **dados** de diversas fontes de informação (sistemas operacionais, planilhas e CRMs) em um local centralizado. Ainda assim, o **data lake** é muito utilizado para trabalhos com **big data** e nos modelos de **machine learning** . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

20 

A seguir, você vai conferir uma tirinha do blog TimoElliott. 



<!-- Start of picture text -->
Como seus lagos de dados lentamente<br>se transformaram em um pantano de<br>dados, lamentou-se de nao ter<br>investido mais em qualidade de dados.<br>Ones, 0,07<br>AW|)! S/Niw| |)! 07<br>RW, aoa<br>N00 WO, W s<br>Wma Sars<br>-e “Ee”<br><!-- End of picture text -->

Title: **Data lake** . 

Alt tag: Charge de um senhor tentando entender como seus **dados** , inicialmente organizados em um **data lake** se transformaram em um pântano de dados ( **data swamp** ). 

A graça dessa tirinha está no fato de que frequentemente vemos empresas com dificuldade de ter um **data lake** organizado e percebendo, em determinado ponto, a dificuldade de garantir sua qualidade. 

E o mais difícil: ter que fazer o esforço de migrar para algo mais estruturado. 

Assim como o **DW** , o **data lake** é composto por alguns elementos que trabalham juntos para coletar, armazenar, gerenciar e analisar grandes quantidades de dados de diferentes fontes. Esses componentes seriam: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

21 

- **fontes de dados** : são elas que alimentam o **data lake** , como bancos de dados transacionais, dados de sensores, registros de servidor, arquivos de log, entre outros. 

- **camada de ingestão** : é responsável por coletar e capturar dados brutos das fontes de dados e armazená-los no **data lake** . Essa camada pode incluir ferramentas de ingestão, como Apache NiFi ou Kafka, scripts e muito mais. 

- **camada de armazenamento** : armazena os dados brutos coletados pela camada de ingestão. Geralmente, os dados são armazenados em seu formato original, sem a necessidade de transformação ou modelagem antecipada. 

- **camada de metadados** : é responsável por armazenar informações sobre os dados no **data lake** , como origem, formato, definições de dados, tags e esquemas de tabela. Isso ajuda a garantir a integridade dos dados e facilita a análise e o acesso aos dados pelos usuários. 

- **camada de processamento** : é responsável por processar os dados brutos e transformá-los em um formato pronto para análise. Essa camada inclui ferramentas para processamento distribuído, como Apache Spark, Hadoop e Presto, além de scripts e processos personalizados. 

- **camada de análise** : é responsável por permitir que os usuários finais acessem e analisem os dados no **data lake** . Isso pode incluir ferramentas de advanced analytics, como Jupyter Notebooks. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

22 



<!-- Start of picture text -->
Dados Estruturados<br>@® |<br>Videos<br>Data Lake "<br>ie EX<br>loT<br>Imagens<br><!-- End of picture text -->

Figura: O lago de dados 

Fonte: elaborada por Indicium Academy 

Title: **O lago dos dados** . 

Alt tag: Ao redor do **data lake (lago de dados)** estão exemplos de dados armazenados dentro dele. São: imagens, IoT, vídeos, dados estruturados, etc. 

Embora seja possível consultar **dados** diretamente de um **data lake** , seu objetivo não é servir como uma camada final de consulta para uma **ferramenta de BI** , por exemplo. 

Sua função está mais para servir como uma camada intermediária que permite outras aplicações de **análise de dados** . 

Em alguns casos, o **data lake** pode ser uma camada intermediária entre os dados brutos e um **data warehouse** , permitindo o melhor dos dois mundos em termos de armazenamento e integração de dados. 

No entanto, é sempre bom lembrar que o gerenciamento de data lakes e de **data warehouses** é uma tarefa complexa, mesmo quando utilizamos serviços gerenciados na nuvem. 

Pensando na união dessas duas formas de armazenamento, a junção do 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

23 

**data warehouse** com o **data lake** trouxe para o jogo o **data lakehouse** . 

Ele é uma arquitetura moderna de gerenciamento de **dados** que combina elementos de **data lakes** e **data warehouses** , oferecendo uma solução integrada para armazenar, gerenciar e analisar grandes volumes de dados. 

Essa arquitetura é projetada para fornecer a flexibilidade de um **data lake** com a robustez e o desempenho de um **data warehouse** , atendendo às demandas crescentes de dados das organizações. 

Os **data lakes** são projetados para armazenar grandes volumes de **dados** brutos e não estruturados em seu formato nativo. 

Eles suportam diversos tipos de dados, como arquivos de texto, imagens, vídeos, dados de sensores, logs. Para isso, utilizam tecnologias de armazenamento distribuído ou ainda sistemas de armazenamento em nuvem, que proporcionam armazenamento barato e escalável. 

O **data lakehouse** unifica dados estruturados, semiestruturados e não estruturados em uma única plataforma, eliminando a necessidade de manter sistemas separados para **data lakes** e **data warehouses** . 

Ele combina o armazenamento de baixo custo e a escalabilidade dos **data lakes** com o desempenho e a confiabilidade dos **data warehouses** oferecendo recursos avançados de processamento e **análise de dados** . 

Essa unificação permite a ingestão de **dados** brutos e a transformação desses **dados** conforme necessário, suportando diversas ferramentas e frameworks de análise, incluindo **SQL** , **machine learning** e processamento de **big data** . 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

24 



<!-- Start of picture text -->
all ' 5<br>TAN o<br>—— e000 Si<br>BI Streaming Data Machine<br>Analytics Science Learning<br>IN . =<br>es<br>Dados estruturados Dados semi-estruturados Dados nao estruturados<br><!-- End of picture text -->

Title: **BI, Streaming Analytics, Data Science e Machine Learning.** Alt tag: Estrutura de um data lake house, os tipos de dados que ele armazena (estruturados, semi-estruturados e não estruturados) e as ferramentas que podem consumir esses dados. 

Uma das principais características do **data lakehouse** é a implementação de políticas de **governança de dados** para garantir a qualidade, segurança e conformidade deles. 

Utilizando mecanismos de transação **ACID** , ele assegura a integridade dos **dados** . 

Técnicas de indexação, caching e otimização de consultas são empregadas para oferecer um desempenho elevado em consultas e análises, permitindo tanto processamento em tempo real quanto batch. 

Os benefícios do **data lakehouse** são numerosos. A unificação desses sistemas de dados reduz os custos operacionais e de manutenção associados a manter infraestruturas separadas para **data lakes** e **data warehouses** . 

Além disso, ele oferece acesso rápido e fácil a todos os tipos de **dados** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

25 

melhorando a tomada de decisões por meio de análises mais abrangentes e informadas. 

A capacidade de lidar com grandes volumes de **dados** e escalar conforme necessário torna o **data lakehouse** ideal para empresas que enfrentam crescentes demandas de **dados** . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

26 



### Aula 4 - Modelagem de dados 

A modelagem de dados é o processo de representar e organizar as informações de um sistema ou contexto de negócios por meio de modelos conceituais, lógicos e físicos. É a criação de um modelo abstrato que representa a estrutura lógica dos dados, suas **inter-relações** e as regras que governam seu comportamento. Esse modelo serve como um mapa que guia a implementação e o gerenciamento de bancos de dados, garantindo que os dados sejam organizados de maneira eficiente e possam ser acessados e manipulados conforme necessário. Esta etapa tem como objetivo principal descrever as entidades (objetos, conceitos ou coisas) relevantes para o domínio em questão, bem como os relacionamentos entre essas entidades. 

A importância da modelagem de dados reside em sua capacidade de fornecer uma representação clara e compreensível dos dados para todos os stakeholders, desde desenvolvedores até os analistas de negócios. Ela facilita a comunicação entre as equipes técnicas e de negócios, assegurando que todos tenham uma visão compartilhada de como os dados são organizados e utilizados. Além disso, a modelagem de dados ajuda a identificar redundâncias e inconsistências nos dados, permitindo que as organizações otimizem o armazenamento e a recuperação das informações. Existem diferentes abordagens e técnicas para a modelagem de dados, cada **uma** servindo a propósitos diferentes, sendo as mais comuns a modelagem conceitual, a modelagem lógica e a modelagem física. 

Na modelagem conceitual, são identificados os principais conceitos e relacionamentos do domínio, geralmente utilizando diagramas de 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

27 

entidade-relacionamento (DER) ou modelos de entidade e atributo. Nessa etapa, ainda não estamos interessados em detalhar quais colunas cada tabela terá. Apenas criamos um desenho, um rascunho, de quais assuntos teremos no modelo final. 

A ideia é pensar, de acordo com o negócio em que estamos trabalhando, quais tabelas fariam sentido termos para compor um DW. Por exemplo, se estamos falando do BanVic, nosso banco fictício, e estamos trabalhando com o pessoal do crédito, faria sentido termos uma tabela de clientes, de agências, de colaboradores, de datas e uma tabela sobre as propostas de crédito. Um exemplo de modelagem conceitual para esse exemplo seria: 



<!-- Start of picture text -->
| Agéncias |<br>| Clientes |aa Propostas Crédito a Colaboradores |<br>| Datas |<br><!-- End of picture text -->

A modelagem lógica envolve a tradução do modelo conceitual para um esquema de banco de dados, utilizando uma linguagem de modelagem como o Modelo Relacional. Nesta etapa, já buscamos mais detalhes sobre as tabelas que irão compor o modelo. Sinalizamos qual coluna será a chave primária, quem será a chave estrangeira quando for o caso, e quais serão as colunas que farão parte da tabela final. Outro ponto bastante importante que esse desenho nos mostra são os relacionamentos. Dessa 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

28 

forma, conseguimos, visualmente, entender como as tabelas se conectam. Esse tipo de desenho facilita o entendimento do DW, uma vez que você não precisa acessar tabela por tabela e entender quais informações estão em cada uma e como elas se relacionam. Tudo isso parece muito simples e bobo. Simples ele de fato é, mas bobo jamais. Conforme o DW vai ganhando corpo e o número de tabelas vai aumentando, esse mapa é cada vez mais essencial para que as pessoas, em especial o usuário de negócio, **consigam** se localizar e encontrar a informação necessária. Como exemplo de modelo lógico para o nosso caso do crédito, **lembram dele? Temos** o seguinte diagrama abaixo. Cada tabela mostra a sua composição de colunas e ainda sinaliza onde estariam as chaves de relacionamento. 



<!-- Start of picture text -->
= ean =| makgim_agenciae<br>xm —<br>data_cast nome<br>da wt propostas | endereca<br>dia_semana FK datetk cidade<br>nome _dia FK | agencla_tk ut<br>dia_sno FK clientets cop<br>semana FK | colaboradorfs data_abertura<br>mes data_entrads_proposta Spe_agencia<br>nome_mes taxa_juros_mensal . os<br>vimestre valor_proposis ‘ox [umes |<br>pony valor_financiaments con cone<br>fin_semana valor_entrada end_pgencia<br>[rx | souponcoras | quantidade_parcelas sumone<br>cad_colaborador “ nome_ciente<br>sos apenci siatus_proposta | a<br>nome_colaboradse tpo_diente<br>email fipo_conta<br>opt data_inclusaa<br>data_nascimento data_abertura<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

29 

Por fim, a modelagem física aborda os aspectos de implementação do modelo em um sistema específico, definindo detalhes como tipos de dados, índices e restrições de integridade. Esse tipo de modelagem é mais técnica e está intimamente relacionada com a própria criação da tabela. Aqui, já não temos um desenho, temos uma sequência de códigos que criam a tabela de fato. Cada linha de código informa o nome da coluna, o tipo de dado que ela irá ter e ainda pode trazer algum critério de restrição para o dado. 



<!-- Start of picture text -->
1 |<br>REATE TABLE agencias<br>cod_agencia INTEG LL,<br>nome T T,<br>endereco TEXT,<br>cidade TEXT,<br>uf ,<br>data_abertura ><br>tipo_agencia 5<br>cod_agencia<br>CREATE TABLE clientes<br>cod_cliente INTEGER F<br>primeiro_nome TEXT,<br>ultimo_nome TEXT,<br>email :<br>tipo_cliente TEXT,<br>data_inclusao ,<br>cpfcnpj ><br>data_nascimento DATE,<br>endereco XT,<br>cep 5<br>PRIMARY KEY (cod_cliente<br><!-- End of picture text -->

#### Os principais benefícios da modelagem de dados são: 

Clareza e Consistência: Fornece uma representação clara e consistente dos dados, facilitando o entendimento entre todos os envolvidos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

30 

Eficiência: Ajuda a otimizar o uso do espaço de armazenamento e melhorar o desempenho dos sistemas de banco de dados. 

Flexibilidade: Facilita a adaptação a mudanças nas necessidades de negócios, permitindo ajustes na estrutura de dados sem comprometer a integridade dos dados existentes. 

Qualidade dos Dados: Promove a integridade e precisão dos dados, reduzindo erros e redundâncias. Quando você **para** para construir uma base de dados para sua análise, ainda que no Excel, e define que cada linha será um objeto e cada coluna será um atributo daquele objeto que você irá analisar, você está modelando de alguma forma o seu dado. Porém, talvez você não pare para pensar qual a melhor estratégia de construir aquela base de dados no longo prazo ou qual o formato vai ser mais performático para uso, por exemplo. 

Quando falamos de um data warehouse, que vai ter dados de muitas fontes, várias áreas da empresa, **e com o qual** muitas pessoas precisarão trabalhar, nós temos que pensar com mais calma qual a melhor abordagem para organizar esse grande armazém de dados. 

Existem algumas propostas de arquiteturas de data warehouses por aí, mas a mais conhecida e discutida é a proposta de **Kimball** . 

A proposta de **Kimball** consiste em organizar o banco de dados analíticos por data marts, que podem ser áreas de negócio, por exemplo, utilizando um modelo dimensional para cada mart. Este modelo irá se estruturar em um formato de esquema estrela ou floco de neve, que são normalmente chamados pelos seus nomes em inglês: Star Schema ou Snowflake. 

O esquema dimensional é uma estrutura de dados composta por tabelas fato e tabelas **dimensão** , que permitem organizar e relacionar os dados de forma a facilitar **a análise dos mesmos** . Esse esquema permite que os dados possam ser conectados “com poucos joins”. 

O Star Schema possui uma tabela fato central, cercada por tabelas 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

31 

**dimensão** , enquanto **o** Snowflake Schema **tem** tabelas **dimensão** normalizadas, com níveis adicionais de relacionamentos. Tabelas normalizadas são tabelas que evitam a repetição de informações no banco de dados. Resumindo, os atributos e valores posteriores **à** primeira forma são atômicos, isto é, são dados que não podem ser modificados nem divididos, pois estão em sua forma mínima. No banco de dados analítico, ter muitas tabelas normalizadas não é muito eficiente e pode tornar o modelo de dados muito complexo. 

Por exemplo: um cliente pode ter mudado de cidade e nós querermos manter os dois registros no nosso banco de dados analíticos. 

Na forma normalizada, teremos uma tabela para clientes e outra para os endereços. Dessa forma, a tabela de clientes terá apenas uma linha por cliente e a tabela **de** endereço, apenas uma linha por endereço. Por isso, o star schema muitas vezes é preferido. Em empresas maiores, pode fazer sentido ter relações entre diferentes esquemas estrela, gerando os esquemas de constelação. O esquema em estrela (star schema) é um tipo de modelagem que tem como objetivo organizar os dados em uma estrutura simples e intuitiva. 

Esse modelo é composto por uma tabela central, a **tabela fato** , que armazena as métricas ou medidas de negócio, e várias tabelas **dimensão** que **contêm** os atributos que descrevem as métricas do negócio. O esquema em estrela é amplamente utilizado em data warehousing devido à sua simplicidade, facilidade de compreensão e desempenho otimizado para consultas analíticas. Ele permite a análise multidimensional de dados, facilitando a exploração e a extração de informações relevantes para suporte à tomada de decisão em uma organização. Além disso, esse é o formato indicado para uso dentro do Power BI, pela própria plataforma. 

É importante observar que, embora o star schema seja adequado para análise de dados e recomendado para uso no Power BI, ele pode não ser 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

32 

apropriado para todos os cenários de modelagem de dados. As principais características do star schema são: 

**Tabela fato (Fact Table):** É a tabela central do esquema que armazena as métricas ou medidas de negócio. Cada registro na tabela fato representa uma instância de um evento de negócio ou transação. Geralmente, as métricas são numéricas e quantificam o desempenho ou resultados das atividades do negócio. 

**Tabelas dimensão (Dimension Tables):** São tabelas que contêm os atributos que descrevem os fatos do negócio. Cada tabela de dimensão está relacionada à tabela de fato por meio de chaves estrangeiras. Os atributos nas tabelas dimensão fornecem contextos e informações adicionais sobre as métricas na tabela fato. Exemplos de dimensões podem ser tempo, localização, produtos, clientes, entre outros. 

**Chave estrangeira (Foreign Key):** São os campos nas tabelas fato que se relacionam com as chaves primárias das tabelas de dimensão. Essas chaves estrangeiras estabelecem a conexão entre a tabela fato e as tabelas dimensão, permitindo a análise e o cruzamento de dados através das dimensões. 

**Chave primária (Primary Key): é** um atributo ou um conjunto de atributos que serve como identificador único para cada registro na tabela. A chave primária garante que cada linha seja única e não nula, proporcionando uma maneira eficiente de acessar e manipular dados. Em muitos casos, uma chave primária é um único campo, como um número de identificação (ID) ou código exclusivo. No entanto, pode também ser composta por mais de um campo (chave composta) quando necessário. 

**Estrutura de Estrela:** O esquema em estrela possui uma estrutura estrelada, onde a tabela fato está localizada no centro, e as tabelas dimensão se conectam a ela, formando uma configuração semelhante a uma estrela. Essa estrutura facilita o acesso rápido aos dados e a execução de consultas analíticas eficientes. O esquema floco de neve, ou 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

33 

snowflake, é uma abordagem de modelagem de dados usada em data warehouses que visa normalizar a estrutura de dados para otimizar consultas analíticas. 

É uma extensão do esquema estrela, diferenciando-se por normalizar ainda mais as dimensões, resultando em uma estrutura que se assemelha a um floco de neve. Essa normalização envolve a divisão das tabelas **dimensão** em tabelas adicionais, eliminando ainda mais a redundância e promovendo uma organização mais eficiente dos dados. No esquema snowflake, as tabelas **dimensão** são divididas em subdimensões, de forma que os dados são normalizados até a terceira forma normal ou superior. 

Por exemplo, uma tabela de dimensão de "localização" que contém país, estado e cidade pode ser dividida em três tabelas separadas: uma para país, outra para estado e uma terceira para cidade. Cada tabela de dimensão está conectada diretamente à tabela fato por meio de chaves primárias e estrangeiras, mas também pode estar ligada a outras tabelas de dimensão conforme necessário. 

Vantagens do Modelo Snowflake: 

**Redução de Redundância:** Ao dividir as tabelas dimensão, o esquema snowflake minimiza a duplicação de dados, resultando em um uso mais eficiente do armazenamento. 

**Flexibilidade e Manutenção:** A normalização torna as tabelas dimensão mais flexíveis para atualizações e manutenção. Mudanças nos atributos são mais fáceis de gerenciar sem impactar os dados não relacionados. 

**Otimização de Consultas:** Embora as consultas possam ser mais complexas devido ao aumento do número de tabelas, o esquema Snowflake pode melhorar o desempenho das consultas ao reduzir o tamanho das tabelas dimensão. Veremos mais sobre esses tipos de tabela nas próximas aulas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

34 

### Aula 5 - Tabelas Fato 

Nos data warehouses, as tabelas são organizadas seguindo esquemas de dados bem definidos, sendo o esquema estrela um dos mais comuns. Neste modelo, as tabelas fato e dimensão estão dispostas de forma que cada tabela fato se conecta diretamente a várias tabelas dimensão, criando uma estrutura que se assemelha a uma estrela. Essa configuração facilita a consulta de dados, pois requer apenas uma junção direta para unir as informações. 

As tabelas fato são um componente central em data warehouses, usadas para armazenar dados quantitativos ou métricas de negócios. Elas contêm fatos ou medidas que representam eventos de negócios, como vendas, transações ou atividades. As tabelas fato são caracterizadas por suas colunas que armazenam valores numéricos, os quais podem ser agregados para análises, como somas, médias ou contagens. 

Considere a seguinte situação: quando um cliente usa um cartão de banco, ele gera um evento que ocorre em um determinado momento, em um local específico, e é realizado por alguém. O valor transacionado durante esse evento compõe os indicadores de desempenho de áreas específicas do banco. Esse evento é registrado em uma tabela fato, onde cada linha representa uma ocorrência única de tal evento. 

As tabelas fato armazenam dados numéricos sobre transações ou atividades empresariais. Elas são frequentemente grandes e contêm muitos registros, organizados em torno de um evento central ou uma medida de negócio, como vendas ou receita. Cada linha na tabela fato representa uma instância deste evento, geralmente associada a uma data e hora específicas. 

Essas tabelas são criadas a partir de perguntas de negócios, como: "Quais são os eventos ou processos envolvidos nos KPIs que a empresa monitora 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

35 

ou deseja monitorar?" Assim, as tabelas fato contêm medidas derivadas de eventos mensuráveis do mundo real e chaves estrangeiras que se relacionam com tabelas de dimensão, fornecendo informações adicionais sobre esses eventos. 

As principais características deste tipo de tabela são: 

Medidas Numéricas: As tabelas fato contêm medidas que podem ser agregadas e analisadas, como vendas totais, lucros ou quantidades. 

Chaves Estrangeiras: Incluem chaves estrangeiras que se referem a tabelas dimensão, permitindo que as métricas sejam relacionadas a contextos descritivos. 

Granularidade: A granularidade refere-se ao nível de detalhe dos dados armazenados, podendo ser diária, mensal ou até por transação individual, conforme os requisitos do negócio. Quando na menor granularidade, cada linha da tabela fato corresponde a um evento específico que está sendo monitorado. 

Existem dois tipos principais de tabelas fato: 

<u>Tabela Fato Transacional: armazena informações detalhadas de cada</u> transação realizada, no nível individual. Este tipo de tabela contém medidas transacionais que podem ser agregadas em diferentes níveis de granularidade. As tabelas fato transacionais são úteis quando é necessário rastrear e analisar transações com alto nível de detalhe, como vendas individuais por produto e cliente. No entanto, podem se tornar muito densas em casos de volumes intensos de eventos, como transações frequentes de cartões de crédito, ou muito espaçadas, como registros de entrada e saída de funcionários. 

<u>Tabela Fato Agregada: armazena informações agregadas em níveis mais</u> altos de granularidade. Este tipo de tabela é criada pela agregação de várias transações e é usada para melhorar o desempenho e a eficiência das consultas, pois contém informações pré-calculadas com diferentes 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

36 

níveis de agregação. Por exemplo, uma tabela fato agregada pode armazenar dados de vendas totais por produto e por mês. 

As tabelas fato são projetadas para otimizar o desempenho das consultas analíticas, permitindo a agregação e sumarização de dados em diferentes níveis de granularidade de forma eficiente. 

No entanto, para descrever completamente os eventos registrados, essas tabelas devem ser associadas a tabelas de dimensão, que oferecem contexto e detalhes adicionais. Exploraremos as tabelas de dimensão em mais detalhes na próxima aula. 

### Aula 6 - Tabelas Dimensão 

Anteriormente nós aprendemos sobre as tabelas fato. Vimos que estas tabelas registram as métricas do negócio. Mas, se quisermos qualificar essas métricas, como podemos fazer? 

Aí entram em jogo as tabelas dimensão. Vamos ver como elas funcionam? 

As tabelas dimensão fornecem informações contextuais e descritivas que ajudam a analisar os dados da tabela fato. Elas contêm as informações que fornecem o contexto das transações de negócios. As tabelas dimensão geralmente contêm informações que podem ser usadas para filtrar, agrupar ou classificar os dados nas tabelas fato. Elas nos respondem: Quando aconteceu? Quem realizou o evento? Onde foi realizado? Por quê aconteceu? e Como aconteceu?. 

Dimensões são, portanto, informações de negócios que descrevem os fatos; por exemplo, cidade, estabelecimento, produto, clientes, datas, etc. É comum que uma mesma tabela de dimensões possa estar relacionada a muitas tabelas fatos, relação essa que é feita por uma chave (código que representa uma informação). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

37 

De acordo com Kimball, devemos despender mais tempo nos preocupando com governança e desenvolvimento das dimensões, já que esses são os motores da experiência com o DW/BI. 

E esse tipo de tabela contém: 

<u>Chave única: as tabelas dimensão são projetadas com uma chave única,</u> também conhecida como chave primária, que é um valor único usado para identificar exclusivamente cada registro na tabela. Cada linha da tabela fato pode se ligar com apenas uma linha da tabela dimensão, do contrário a tabela irá duplicar. Por isso não utilizamos muito a chave primária de uma tabela como chave única da dimensão. Segura um pouquinho que já vou explicar um pouco melhor esse ponto. 

<u>Contexto: as tabelas dimensão contêm atributos, que são informações</u> descritivas e contextuais usadas para classificar ou agrupar os dados nas tabelas fato. Exemplos de atributos podem incluir nome, descrição, categoria, status, região geográfica, entre outros. 

<u>Hierarquias: as tabelas dimensão podem ser organizadas em hierarquias,</u> que são estruturas de dados que representam relações hierárquicas entre atributos. Por exemplo, uma tabela dimensão de tempo pode incluir hierarquias que representam anos, trimestres, meses, semanas e dias. Ou o CNAE de um estabelecimento que possui uma hierarquia de classificação que vai do próprio CNAE, que é o nível mais baixo, até a Seção, que é o nível mais alto. 

Sabemos que a tabela fato, por medir os processos da empresa, tem atualização todos os dias, em alguns casos até várias vezes ao dia. Mas, e as tabelas dimensão, como são atualizadas? 

Existem algumas formas de manter uma dimensão atualizada. Muitas vezes iremos querer manter um histórico de alterações nos parâmetros da nossa dimensão. Para isso usa-se muito a dimensão de mudança lenta, ou mais popularmente conhecida como Slowly Change Dimension ou 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

38 

#### apenas SCD. 

Slow Change Dimension (SCD) é um conceito de modelagem dimensional que se refere ao gerenciamento de mudanças em uma dimensão ao longo do tempo. As dimensões são normalmente estáticas e mudam com pouca frequência, mas em alguns casos, elas precisam ser atualizadas para refletir mudanças na realidade. 

A SCD é usada para lidar com essas mudanças. É uma técnica importante na modelagem dimensional, pois permite que as informações sejam atualizadas e gerenciadas de maneira eficiente e precisa. 

Existem seis tipos de SCD, mas detalharemos apenas 2 que são os mais comuns: 

<u>SCD Tipo 1 (SCD1): este tipo de dimensão substitui completamente o</u> registro anterior pelo novo registro, sem manter o histórico das mudanças. É útil quando os dados da dimensão mudam com pouca frequência e não há necessidade de manter o histórico. Podemos simplesmente ter sempre a versão mais atualizada dos dados na tabela. 

<u>SCD Tipo 2 (SCD2): este tipo de dimensão mantém um histórico completo</u> das mudanças, criando uma nova linha na dimensão sempre que ocorre uma alteração. Cada linha na dimensão contém um **período de validade** , que indica o intervalo de tempo em que a linha era válida. Esse tipo de dimensão é adequada quando é importante rastrear as mudanças ao longo do tempo. 

Digamos que o cliente tenha aberto sua primeira conta na agência de Manaus, onde negociou seus contratos por cerca de 5 anos. Depois ele se mudou para São Paulo onde resolveu não seguir com os serviços. Não ter o histórico de que esse cliente morava em Manaus no período dos negócios dele pode prejudicar a análise e levar a mudanças de indicadores conquistados anteriormente. 

Retomando o ponto sobre usar ou não apenas o ID para formar a chave 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

39 

primária da tabela: a necessidade de rastreabilidade é a razão pela qual não utilizamos o ID como a única chave nas tabelas de dimensão. 

Para que você entenda melhor o que estamos falando, voltemos à nossa tabela. No exemplo, temos a coluna ID do cliente que seria a Chave Primária ou Primary Key, como preferir chamar. Nesse nosso exemplo, a chave se repete por causa da alteração. Para isso construímos uma Surrogate Key, que combina as colunas que deveriam tornar aquela linha única para gerar a chave. 

Poderia também ser o caso de termos várias fontes associadas na mesma dimensão, com mais de uma chave primária possível. A surrogate key poderia juntar as duas chaves primárias, por exemplo, e tornar a chave da tabela agnóstica à fonte. 

Para finalizar, em alguns momentos você poderá se deparar com dimensões muito simples que poderiam ser basicamente uma chave e um texto. Ou ainda um atributo da dimensão que poderia muito bem ser outra dimensão ligada a ela. Como por exemplo endereços. 

Como mencionamos na seção de modelagem de dados, o modelo Snowflake pode se tornar rapidamente complexo devido à existência de subdimensões. Por essa razão, muitas vezes opta-se por integrar essas subdimensões na dimensão principal ou até mesmo na tabela fato, facilitando assim o uso e a compreensão dos dados. 

Quando lidamos com dimensões que possuem poucos atributos, também é comum integrá-las nas tabelas fato ou em outras dimensões para simplificar o modelo. Por exemplo, o status de uma transação, que é um atributo do evento de transação com poucos desdobramentos, geralmente é mantido na tabela fato. Essa prática de integrar pequenas dimensões diretamente na tabela fato é conhecida como dimensão degenerada. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

40 

### Aula 7 - Tabelas Ponte 

Com frequência, encontramos a necessidade de lidar com relacionamentos complexos entre tabelas em um modelo dimensional, especialmente aqueles de muitos-para-muitos. Uma solução eficiente para resolver esses casos é a **Bridge Table** . 

Nesta aula, exploraremos o que é uma **Bridge Table** , quando utilizá-la e como implementá-la. Uma **Bridge Table** (também conhecida como Tabela de Ponte ou Puppini Table) é uma tabela auxiliar criada para resolver relacionamentos muitos-para-muitos entre tabelas fato и dimensão. 

Esses relacionamentos não podem ser representados diretamente em um esquema dimensional tradicional, como o esquema estrela ou floco de neve. O nome "Puppini Table" é uma homenagem a Ralph Puppini, que popularizou o uso de tabelas de ponte em modelagem dimensional para resolver problemas de relacionamentos muitos-para-muitos em bancos analíticos. Esse termo é mais comum em determinados círculos acadêmicos ou na literatura sobre modelagem dimensional. 

A **Bridge Table** funciona como uma “ponte” entre tabelas, conectando-as de forma eficiente e permitindo que os dados sejam analisados corretamente. Ela não possui valor de negócio próprio, sendo utilizada exclusivamente para ativar os relacionamentos necessários. 

Além disso, a **Bridge Table** é útil para conectar tabelas com granularidades diferentes, garantindo que os relacionamentos sejam modelados de maneira consistente e compreensível para as ferramentas de BI. Pensando no nosso banco fictício, o **BanVic.** 

**Imagine** que um cliente pode interagir com diferentes colaboradores ao longo do tempo (em propostas de crédito ou transações). **No decorrer do tempo,** um colaborador pode atender **a** vários clientes, em diferentes momentos e para diferentes tipos de operações. Para resolver isso, você 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

41 

pode criar uma **Bridge Table** que relacione Clientes, Colaboradores e Datas. Para a correta construção de uma **Bridge Table** , precisamos atender **a** um **pré-requisito: cada** uma das tabelas que precisam se relacionar via bridge deve ter uma coluna de chave primária. **Caso contrário, a bridge** não funcionará corretamente. 

Em termos bem simples, podemos dizer que a **Bridge Table** funciona como uma grande tabela de "de-para", ligando duas outras tabelas que possuem uma relação de muitos-para-muitos. 

Ela contém apenas as chaves primárias das tabelas e atua como uma ponte entre elas. Ou seja, a **Bridge Table** indica que a chave primária de uma tabela se relaciona com a chave (ou chaves) de outra tabela, criando uma ligação clara entre as duas. 

Além disso, a **Bridge Table** pode atuar como o centro de um star schema, conectando dimensões em comum entre as tabelas envolvidas. Sua principal função é conectar tabelas com diferentes granularidades, simplificando os joins necessários para análises e garantindo que as relações sejam modeladas corretamente. 

#### A **Bridge Table** é especialmente útil quando: 

- Existe um relacionamento muitos-para-muitos entre tabelas fato e dimensão; 

- É necessário conectar tabelas com diferentes granularidades; 

- Há um número elevado de combinações possíveis entre os dados. Para construir uma **Bridge Table** , podemos pensar em duas etapas: 

1. Garantir que todas as tabelas que serão ligadas possuem uma coluna de chave única; se **elas não tiverem,** será necessário criar uma surrogate key. 

2. Investigar as colunas em comum e planejar como as ligações serão feitas. **Com isso, é** possível criar uma tabela que vai servir de ligação entre outras tabelas do modelo. Além disso, dada a construção da bridge, a cardinalidade da relação de cada tabela com a bridge vai 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

42 

ser de um-para-muitos, garantindo que a ferramenta de BI consiga traçar a relação exata entre elas. Por fim, a bridge ainda vai servir como elemento central de ligação de todas as tabelas. 

Os principais benefícios da **Bridge Table** são: 

- **Simplicidade nos joins:** Reduz a complexidade dos relacionamentos, facilitando consultas e relatórios. 

- **Escalabilidade:** Lida bem com grandes volumes de dados e múltiplos relacionamentos. 

- **Flexibilidade:** Permite conectar tabelas com granularidades diferentes. 

- **Aprimoramento de Análises:** As ferramentas de BI podem aproveitar a tabela para traçar relações complexas e fornecer insights mais precisos. Mas toda essa facilidade possui seus pontos de atenção, são eles: 

- **Desempenho:** Embora a **Bridge Table** simplifique os relacionamentos, sua construção aumenta a quantidade de joins, impactando a performance em bancos muito grandes. 

- **Manutenção:** Atualizar as chaves e relações exige cuidados para evitar inconsistências nos dados. 

● **Complexidade Adicional:** Apesar de resolver problemas de modelagem, a inclusão de uma **Bridge Table** adiciona mais uma camada de abstração ao modelo. Como vimos, a **Bridge Table** é uma tabela indispensável quando precisamos lidar com relacionamentos complexos na modelagem dimensional, permitindo resolver desafios que surgem em cenários muitos-para-muitos. Apesar de adicionar um nível extra de complexidade ao modelo, sua implementação se faz necessária se quisermos garantir flexibilidade e robustez ao nosso modelo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

43 

### Aula 8 - Boas práticas de uso do banco de dados analícos 

Diferente dos bancos de dados transacionais, os bancos de dados analíticos, e aqui entra o Databricks, são projetados para suportar consultas complexas e análises multidimensionais, facilitando a exploração e o entendimento dos dados. Compreender como estruturar e otimizar suas consultas no Databricks é importante para obter resultados precisos e eficientes sem extrapolar gastos de processamento e sem sobrecarregar o ambiente. 

O Databricks, com sua arquitetura Lakehouse baseada em Delta Lake e Unity Catalog, oferece um ambiente poderoso para análise. As melhores práticas buscam otimizar a performance, a governança e a eficiência de custos. Muitas dessas otimizações ocorrem automaticamente, você se beneficia simplesmente usando o Databricks. 

Algumas práticas são recomendadas pelo próprio Databricks que, em conjunto com a estrutura desenhada para o DW, trazem segurança, governança e performance para as consultas realizadas. Vamos falar aqui sobre as principais otimizações sugeridas. 

No Databricks, o lakehouse tem o formato de Delta Lake. Nesse modelo, temos uma camada de armazenamento de formato aberto que garante confiabilidade, segurança e performance ao data lake. O Delta, por si só, garante transações do tipo ACID (Atomicidade, Consistência, Isolamento e Durabilidade). 

- **Atomicidade** significa que todas as transações são bem-sucedidas ou falham completamente. 

- As garantias de **consistência** estão relacionadas a como um determinado estado dos dados é observado por operações simultâneas. 

- O **isolamento** refere-se a como as operações simultâneas podem entrar em conflito umas com as outras. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

44 

- **Durabilidade** significa que as mudanças comprometidas são permanentes. 

**Controle de acesso:** Utilize o Unity Catalog para implementar RBAC (Role-Based Access Control). Crie papéis e permissões granulares para controlar o acesso a tabelas, colunas e até linhas específicas. Desta forma, é mais fácil gerenciar permissões de acesso de forma centralizada em todos os workspaces, garantindo que apenas usuários autorizados acessem dados específicos. 

**Criptografia e governança:** O Databricks já garante criptografia em trânsito e em repouso. Combine isso com políticas de linhagem e auditoria no Unity Catalog para proteger informações sensíveis, além de poder rastrear a origem e as transformações de seus dados, o que é essencial para auditoria e confiança nas análises. 

**Otimização de consultas no Databricks:** O Databricks utiliza armazenamento colunar, que permite ler apenas as colunas necessárias. Ao escrever consultas, selecione apenas os campos relevantes nas queries para reduzir o volume de dados processados. Você pode utilizar algumas técnicas para ajudar aqui. 

- <u>Optimize: ao invés de criar inúmeros pequenos arquivos Parquet</u> para salvar os dados, o Databricks sugere que sejam criados arquivos entre 16MB e 1GB. Essa configuração pode ser feita com o Optimize. Por padrão os arquivos terão sempre 1GB, mas você pode configurar para serem menores se for o caso. 

- <u>Z-Ordering: o Databricks oferece o recurso de Z-Ordering, que</u> organiza dados de acordo com colunas frequentemente usadas em filtros, melhorando o desempenho de leitura em grandes tabelas Delta. 

- <u>Auto-optimize: como o nome já sugere, essa feature compacta</u> automaticamente os arquivos para terem, por padrão, 128MB de 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

45 

tamanho. Tanto o Optimize quanto o Auto-optimize são configuráveis. 

- <u>Particionamento: você pode acelerar o tempo das consultas</u> particionando as tabelas de forma adequada. Isso inclui particionar a tabela por colunas com baixa cardinalidade ou por colunas que são frequentemente utilizadas em filtros. 

- <u>Delta Cache: outra forma de acelerar a leitura dos dados é</u> utilizando o delta cache. Assim é possível criar cópias dos dados remotamente nos discos locais facilitando a consulta aos dados. 

<u>Cost-based optimizer:</u> O Databricks possui uma feature chamada CBO (Cost-based optimizer) que auxilia no planejamento de execução das queries. Ele usa as estatísticas das colunas para planejar a forma mais econômica de executar os joins entre as tabelas. Além disso, sempre que possível, reduza o número de joins complexos e mantenha o modelo de dados e a lógica do código da forma mais clara e simples. Considere sempre usar CTEs para simplificar a lógica. 

<u>Arquitetura Serverless: Sempre que possível, utilize o SQL Warehouse</u> Serverless para obter inicialização de cluster quase instantânea, autoescalonamento eficiente e menor custo operacional, assim você paga apenas pelo que usa. 

<u>Suspensão automática de clusters:</u> Configure os clusters para parar automaticamente quando não estiverem em uso, economizando créditos/custos. Eles podem ser reiniciados rapidamente quando necessário. 

<u>Monitoramento de workloads: Use o Query Profile e o Spark UI para</u> identificar gargalos de desempenho. Analise métricas como tempo de shuffle, uso de memória e paralelismo para ajustar jobs e queries. 

<u>Gerenciamento de custos: O Databricks cobra pelo tempo de execução do</u> cluster e pelo armazenamento. Configure políticas de auto-termination, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

46 

use spot instances quando possível e ajuste o tamanho dos clusters para evitar desperdícios. 

O Databricks Lakehouse oferece um ambiente eficiente e flexível para análises, unindo o melhor do Data Lake e do Data Warehouse. Aqui foram apresentadas algumas boas práticas e otimizações possíveis de serem feitas, mas isso não significa que esgotamos todas as possibilidades existentes. 

Seguindo essas recomendações, desde a otimização de consultas, gerenciamento de clusters até o uso de Delta Lake, conseguimos maximizar performance, segurança e custo-benefício. 

À medida que você continua a explorar e otimizar consultas no Databricks, a aplicação dessas boas práticas garantirá que você tire o máximo proveito do potencial da plataforma, apoiando suas decisões de negócio orientadas por dados. 

E assim concluímos o módulo “Modelagem de dados” do Curso de Formação em Análise de Dados. Neste módulo, entendemos como funcionam os bancos de dados analíticos e quais tabelas os compõem. 

Vimos, também, o quão importante é a modelagem de dados para facilitar o entendimento de quais são as tabelas que temos no nosso data warehouse e como elas se relacionam. 

Passamos pelos principais tipos de tabela que formam o DW e como elas podem se estruturar em diferentes esquemas. E conhecemos algumas boas práticas de como trabalhar com esse tipo de banco de dados. 

Espero que você tenha aproveitado esse módulo. 

Obrigada por ter me acompanhado até aqui. 

Nos vemos em outras aulas. Abraço! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

47 

