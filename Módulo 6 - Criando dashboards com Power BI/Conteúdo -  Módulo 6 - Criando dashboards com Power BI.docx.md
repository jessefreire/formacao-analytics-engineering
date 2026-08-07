

# Material Teórico 

Curso: Formação em Análise de Dados 

Autoria 

Prof. Esp. <u>Viviane Cechetti</u> 

## Módulo (obrigatório) 

Módulo 6 - Criando dashboards com Power BI 

Temas abordados 

- Ferramentas de BI 

- Introdução ao Power BI 

- Criando relatórios no Power BI 

- Melhorando seus modelos no Power BI 

## Objetivos de Aprendizagem 

Neste módulo apresentaremos como funciona uma das principais ferramentas de BI do mercado, o Power BI. A partir das aulas será possível compreender as diretrizes da ferramenta, bem como a criação de relatórios e outros tópicos relacionados. 

## Apresentação do Módulo 

Caro aluno(a), 

Neste módulo vamos nos aprofundar nos assuntos relacionados às ferramentas de business intelligence, especialmente no Power BI, que será o nosso auxiliar em todo este módulo. Veremos suas particularidades e 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

1 

também como desenvolver de ponta a ponta um relatório na ferramenta, até sua publicação para compartilhamento com outras pessoas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

2 

Desenvolvimento 

### **Aula 00: Apresentação** 

Olá, analista! Seja bem-vindo ao módulo 6 da Formação em Análise de Dados da Indicium Academy. 

Neste módulo vamos nos aprofundar nos assuntos relacionados às ferramentas de business intelligence, especialmente no Power BI, que será o nosso auxiliar em todo este módulo. 

Vamos aprender como trabalhar nesta ferramenta poderosa. Mas, mais do que isso, vamos ter protagonismo nesta atividade. Afinal, por trás de um bom dashboard existe um ótimo analista, que despendeu tempo e usou de toda a sua habilidade para criar visualizações inteligentes, que trazem insights e geram resultados para as organizações. 

Neste módulo veremos as melhores práticas a serem executadas em projetos de dashboards, desde a estrutura das tabelas, seu armazenamento, a criação dos relacionamentos, a elaboração de medidas e outros cálculos. Além, claro, da criação de visualizações que impactem o usuário final. Sairemos deste módulo prontos para desenvolver dashboards incríveis. 

Ah! E é importante te dizer que no material complementar desta aula você terá disponível as tabelas para fazer o desenvolvimento do seu relatório no decorrer de nossas aulas. Para fins de treinamento, este relatório já está com os dados do BanVic carregados em arquivos csv, ok? Para carregar as tabelas em um arquivo do Power BI, basta seguir o passo a passo descrito no material complementar. 

Vamos para o nosso módulo? 

#### Material Complementar 

**Tipo** ☐ Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme   x Arquivo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

3 

**Título:** Arquivos base Banvic 

**Descrição:** Tabelas que serão utilizadas neste módulo para criação do relatório. 

**Link:** adicionar 

**Tipo** ☐ Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme   x Arquivo 

**Título:** Passo a passo para adicionar tabelas csv ao arquivo do Power BI **Descrição:** Passo a passo para adicionar tabelas csv ao arquivo do Power BI 

**Link:** adicionar 

### **Aula 01: Ferramentas de Business Intelligence** 

<mark>(conteúdo baseado em</mark> <u><mark>Microsoft)</mark></u> 

Olá, analista! Seja bem-vindo à primeira aula do nosso módulo sobre Business Intelligence. Nesta aula vamos falar de forma ampla sobre as ferramentas de business intelligence, conhecidas também como ferramentas de BI, ou simplesmente BI. Vamos entender o que elas são, quais são as principais ferramentas do mercado e algumas particularidades. Vamos lá? 

Para iniciar, vale falar um pouco sobre a história da inteligência de negócios. Quando pensamos em “BI”, “dashboard” ou ainda “análise de dados”, tenho quase certeza de que todos nós pensamos em algo muito recente, atual, até mesmo futurístico. Mas será mesmo que o BI é tão novo assim? A inteligência de negócios existe há muitos séculos, desde que o mundo é mundo, o ser humano é responsável e está empenhado em melhorar sua produção, sua margem de lucro e seus negócios - seja ele qual for. A diferença é que hoje contamos com inúmeras ferramentas e tecnologias que nos auxiliam neste processo. 

Mas então, o que é BI nos dias atuais? Segundo a Microsoft, as ferramentas de BI são uma coleção de serviços de software, que se constituiu por um conjunto de processos, técnicas e ferramentas que permitem coletar, organizar, analisar e apresentar dados relevantes para a tomada de decisões estratégicas nas organizações. Os dados podem estar inicialmente em uma planilha no Excel ou em data warehouse. Em nosso dia a dia trabalhando na estrutura do Modern Data Stack, em que temos etapas estruturadas de coleta, limpeza e tratamento dos dados, a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

4 

ferramenta de BI fica responsável pela visualização, apresentação, análise e compartilhamento. 

Entre as funcionalidades que existem dentro de uma ferramenta de BI, existe o dashboard. Um dashboard é uma forma de visualizar os dados de forma gráfica e interativa, que facilita a compreensão e a comunicação das informações. Um dashboard pode ser parte de uma solução de BI, mas não é a única forma de apresentar os dados, já que BI envolve também outras etapas como a integração, o armazenamento, a modelagem, a exploração dos dados e seu compartilhamento. No cotidiano é normal que os termos BI e dashboard se confundam, mas é sempre bom termos claro que o Business Intelligence vai além de um dashboard. 

É dentro de uma ferramenta de BI que os dados são apresentados ao usuário. Esse, por sua vez, pode analisar as informações e obter insights sobre o desempenho de seu negócio. É importante dizer que o “business intelligence”, ou a “inteligência de negócios” não diz o que fazer ou o que vai acontecer. O BI oferece os meios para que as pessoas analisem seus dados, entendendo as tendências e gerando insights. Por isso essas também são chamadas de Ferramentas de Suporte à Decisão. 

Existem inúmeras empresas que trabalham com a criação de ferramentas de BI no mercado. Para escolher a ferramenta correta para o projeto que você está trabalhando é preciso entender quais são as suas necessidades e como a ferramenta escolhida pode auxiliar você a chegar ao seu objetivo. Algumas ferramentas possuem capacidades maiores de processamento de dados, outras possuem preços mais convidativos e outras ainda possuem mais opções de visualizações e personalização. Por isso, é muito importante entender quais são os pontos fundamentais de seu projeto para escolher a ferramenta correta. 

Uma das líderes de mercado hoje é o Power BI, da Microsoft. E essa será a nossa ferramenta a partir das próximas aulas. Esta ferramenta pode acompanhar o analista de dados por uma longa jornada, uma vez que podemos criar simples relatórios que escalam a modelos complexos e de importantes tomadas de decisão. Com o Power BI é possível criar 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

5 

relatórios interativos e visualmente impressionantes para servir como mecanismo de análise e decisão para dar apoio a projetos de setores, áreas ou organizações inteiras. 

Nas próximas aulas vamos nos aprofundar um pouco mais nessa ferramenta: falaremos sobre conceitos e colocaremos a mão na massa para praticar tudo que aprendemos neste módulo. Vejo você na próxima aula! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

6 

**Aula 02: Componentes do Power BI** 

<mark>(conteúdo baseado em</mark> <u><mark>Microsoft</mark></u> <mark>e</mark> <u><mark>Microsoft)</mark></u> 

Olá, analista! Seja bem-vindo à nossa aula sobre os conceitos do Power BI. Nesta aula vamos falar sobre sua estrutura e componentes principais, como sua versão desktop e online, além de entender melhor qual a funcionalidade de cada uma delas. Vamos lá? 

Há dois componentes principais no Power BI: o desktop, que é um aplicativo na área de trabalho e o serviço do Power BI, que é a plataforma online. Todas as funcionalidades da ferramenta encontram-se em um destes componentes. 

Existe um fluxo comum ao criar relatórios com o Power BI. Primeiro, utilizamos o Power BI Desktop para se conectar aos dados e criar o relatório. Em seguida, publicamos o relatório no serviço do Power BI e distribuímos aos consumidores. 

Vamos iniciar pelo Power BI Desktop. O Power BI Desktop é um programa gratuito distribuído pela Microsoft. Ele pode ser adquirido pelo <u>site do Power BI ou pela Microsoft Store. Sugiro que, se possível, você o adquira</u> pela loja da Microsoft, pois assim, sempre terá a versão mais atualizada do aplicativo. Isso é interessante porque todos os meses há atualizações sendo realizadas. 

O programa está disponível no sistema operacional Windows. Se você estiver utilizando Linux ou Mac, é preciso utilizar uma máquina virtual para acessá-lo. A utilização do Power BI Desktop é importante para os desenvolvedores porque algumas funcionalidades só estão disponíveis na versão desktop do programa. Para acessar a versão desktop não é necessário ter uma conta vinculada. 

Na versão desktop criaremos os modelos semânticos e os relatórios. Nas aulas seguintes você verá em maiores detalhes o que isso significa. Mas, por ora, é importante saber que o programa tem como funcionalidade a elaboração de arquivos pbix em sua totalidade, ou seja, é aqui que os desenvolvedores podem usar 100% da capacidade e das personalizações 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

7 

disponíveis do Power BI para criar seus relatórios. 

O Power BI Desktop não tem o objetivo de distribuir relatórios, apenas criá-los. Aqui iremos conectar aos dados, realizar pequenos ajustes aos modelos, criar visuais e iniciar a configuração de RLS, quando necessário. Por fim, publicaremos o arquivo no Power BI Service. 

Agora, vamos ver na prática como o Power BI Desktop se parece. E antes, é importante relembrar que mensalmente o Power BI Desktop recebe atualizações e, por esse motivo, as telas que vou mostrar aqui no curso podem ser ligeiramente diferentes da tela que você tem aí, ok? 

Vamos começar nosso tour pelo Power BI Desktop. Quando acessamos, vemos uma tela em branco, com menus à esquerda, à direita e na parte superior. Também temos na tela a frase “Adicionar dados ao seu relatório”, que também nos indica que estamos em um arquivo vazio. 



<!-- Start of picture text -->
ic : : ara.)<br>7 <®<br>~<br>a5 i a =<br>20 ae + | ®<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Vamos começar pelos menus do lado esquerdo. Aqui nós temos três opções: exibição do relatório, modo de exibição de tabela e exibição do modelo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

8 

Na aba de **relatório** é o local onde criamos nossas visualizações. Aqui é o local onde os dashboards são construídos. Essa é a aba que passamos mais tempo em nossos desenvolvimentos. 

A aba de **dados** é onde conseguimos ver como os nossos dados se parecem, dentro das tabelas ou medidas. 

E a aba de **modelo** é onde atuamos na camada semântica de nossos dados, alterando nomes de tabelas e descrição e criamos e gerenciamos relacionamentos entre tabelas. Normalmente será o ponto de partida quando carregamos os dados para dentro de um modelo. 

Agora, sobre o menu superior, temos: 

**Página inicial** : local onde selecionamos os dados, abrimos o Power Query, atualizamos os dados, adicionamos novos visuais, medidas e, também, publicamos o relatório no serviço do Power BI. A página inicial funciona muito como um menu rápido, contendo as principais funcionalidades da ferramenta. 



<!-- Start of picture text -->
OG, Bom oem FB peeneeean) al &<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

**Inserir** : em Inserir, vamos ter novos elementos visuais, sendo eles páginas, gráficos, elementos de texto, botões, etc. Essa aba só está disponível na parte de criação de relatórios. 



<!-- Start of picture text -->
D Qeucneeran)®? OF €8 fo DBD WAFRea<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

**Modelagem** : em modelagem conseguimos fazer algumas adições aos nossos dados, criando novas medidas, colunas ou até mesmo tabelas. Também é na modelagem que conseguimos alterar os níveis de segurança dos dados, com RLS. Essa aba também só está disponível na parte de criação de relatórios. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

9 



<!-- Start of picture text -->
3 BBR A B RA oRA<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

**Exibição** : a aba de exibição é responsável pelos padrões de temas do relatório, onde escolhemos qual será a paleta de cores ou as fontes padrão do arquivo. Também é nessa aba que alteramos como vemos a página - ajustando a página a largura ou ao tamanho original, por exemplo. E também é aqui que selecionamos quais abas à direita queremos ver. Assim como as anteriores, essa aba só está disponível na parte de criação de relatórios. 



<!-- Start of picture text -->
Gea fia elt) ol el Genta y|.2..<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

**Otimizar** : já em otimizar, estamos pensando em como melhorar a performance do relatório atual. Para isso temos algumas opções de análise do próprio painel. Assim como as anteriores, essa aba só está disponível na parte de criação de relatórios. 



<!-- Start of picture text -->
he @ a<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

**Ajuda** : por fim, a aba de Ajuda, que contém links interessantes. Aqui podemos ir direto à página de documentação, treinamento ou suporte da Microsoft. 



<!-- Start of picture text -->
Or @808® + & & wR<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

10 

Por fim, temos os nossos menus da lateral direita. As opções apresentadas aqui estão na aba de relatório e são escolhidas na aba superior de exibição. 



<!-- Start of picture text -->
fit ited ood biel Jo. OE, Geet a<br>w : «6<br>a<br>“ Py<br>i<br>i q<br>CCriar visuais com seus dados I co<br>Selecone ou arraste os campos do paine! Dados para a tela do relatério. i a<br>SE | +<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

#### Vamos olhar para os três principais: Dados, Visualização e Filtros. 



<!-- Start of picture text -->
¥ Filtros ® »  Visualizagdes >» Dados »<br>[Deepesqus.Pesquis... | Criar= visual ooQ Pesquisar<br>svsenapiye A z<br>Adicionar os campos de da... BHEbe OY A heRR US iLe Vocé aindanenhum naodado. carregou<br>. Obter dados<br>MMF: @O<br>Filrosem todas aspéginas «= GF @ BI A om<br>Adicionar 0: campos de de.. Sl iy BER<br>Py ER eA<br>la 89 2 ® D<br>Valores<br>Adicionar os campos de da...<br>Drill-through<br>Relatériocruzado  (@_)<br>Manter todosos<br>filtros<br>Adicionar os campos de dr.<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

O primeiro menu é o dados. Nele é possível ver quais as tabelas, colunas e medidas que temos à disposição para a criação de um visual. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

11 

A seguir temos o menu de Visualizações, que é composto por criar visual e formato. Em criar visual organizamos qual eixo cada dado irá pertencer. Esse menu também é disponibilizado diretamente no visual, a partir da função de interação no objeto. E em formato temos todas as possibilidades de personalização do visual. Aqui ajustamos tamanho, título, rótulos, linhas, colunas, o que for necessário. Esse menu também é disponibilizado diretamente no visual, a partir da função de interação no objeto. 

Por fim há o menu de filtros. Essa aba é sempre presente no relatório, indicando quais filtros estão sendo usados a nível de visual - com as próprias colunas e medidas usadas nos gráficos ou até mesmo colunas adicionadas exclusivamente para filtrar aquele visual, até filtros em todas as páginas. Recomendamos muito cuidado ao utilizar esta aba, sendo que seu uso deve ser feito em momentos muito específicos, já que estes filtros, diferente das segmentações que veremos nas próximas aulas, não são explícitos ao usuário, podendo gerar algumas confusões nas análises. 

Esses são os três principais menus que vamos utilizar na criação de visuais. Além desses, temos os menus de seleção, performance, indicadores e segmentação de dados, que possuem usos mais específicos. 

Agora iremos para o Power BI Service. O serviço do Power BI, também chamado simplesmente de Power BI online é a parte SaaS do Power BI. É na sua versão online que publicamos e compartilhamos os relatórios e dashboards criados na versão desktop. Diferente da anterior, como esse é um serviço web, não há restrições quanto ao sistema operacional. 

Para acessar o Power BI Service é necessário ir no endereço app.powerbi.com e nele temos acesso a todos os relatórios compartilhados conosco. Para acessá-lo é preciso ter uma conta vinculada à Microsoft. Essa conta pode ser corporativa ou estudantil e não é possível acessar por uma conta pessoal, por exemplo. Se você não se encaixar em alguma dessas alternativas, você ainda poderá explorar o serviço obtendo uma avaliação gratuita ou inscrevendo-se para uma conta gratuita do Desenvolvedor do Microsoft 365. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

12 

Além da conta, a utilização do Power BI Service também depende de uma licença e, dependendo da licença que você e sua equipe possuem, funcionalidades adicionais são apresentadas. Para entender melhor sobre licenciamento e precificação, há um material ao final desta aula. 

Vamos dar uma olhada como o Power BI Service se parece? 

Assim que acessamos o Power BI, temos visibilidade dos relatórios compartilhados conosco. Os relatórios compartilhados estão dentro de workspaces, que podem ser vistos como containers que separam os objetos por assunto, área, departamento, objetivo, etc. A escolha da separação destes ambientes é do usuário. Essa organização é importante porque algumas funcionalidades e compartilhamentos acontecem a nível de workspace e, se este não estiver bem estruturado, podemos ter problemas com acesso à informação. Como um exemplo, aqui na Indicium a divisão de ambientes de trabalho acontece por área. 



<!-- Start of picture text -->
A<br>57 ho in AN = indessere<br>on Sa . Dados para decisesnebgentes<br>o5<br>2;©<br>~@ o<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Todo usuário inicia com um workspace chamado “Meu workspace”. Um local propício para adicionar os seus desenvolvimentos realizados no desktop. Este ambiente pode ter objetos compartilhados com outros usuários, se todos estiverem com o mesmo nível de licença na ferramenta. Mas, ainda assim, o “Meu workspace” é um local destinado para guardar e testar seus desenvolvimentos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

13 



<!-- Start of picture text -->
AR & Meu workspace<br>® FovesNe | FF CaregsCanegar - — B_Configuracde€ Configuares de worspce Q tese x = ifar eS cs<br>6 GB Nome Tipo Proprietario ‘Atualizado Proxima atualizagio Endosso_ ce<br>co) ho teste Retarério ane Cecheti 290se3, 171035<br>“B QD teste -metas Scorecard mane Cechet 3108/22, 079949 - = -<br>co © teste -metas Conjunto de Dados rane Cechett 31708722, 075949 ND - -<br>2<br>ent teste retori paprado ata preceteh — - - -<br>cy<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Além deste, existem os workspaces compartilhados. Estes sim, são criados com o intuito de que um grupo de pessoas acessem e analisem os dados disponibilizados. Para ter acesso a estes, os usuários devem possuir licenças pagas, do tipo Pró ou Premium. 

Também, é no Power BI Service que os conjuntos de dados são configurados e atualizados de forma periódica. Veremos isso na prática, mas, por enquanto, é importante dizer que na versão online são realizadas algumas configurações a fim de transformar os relatórios criados em produtos de dados. Um exemplo é a configuração do RLS, ou Row Level Security, que compreende a segurança dos dados a nível de linha e faz com que o usuário visualize apenas os dados que são de seu interesse. A configuração do RLS inicia lá no desktop, na aba de modelagem, onde criamos as regras para ele, e a sua finalização só ocorre no Online, quando colocamos os nomes às regras criadas anteriormente. 

É nesse sentido também que dizemos que uma ferramenta complementa a outra. Ambos os produtos têm funcionalidades exclusivas e complementares. O Power BI Desktop é mais indicado para a criação e edição dos relatórios, enquanto o Power BI Service é mais voltado para a colaboração e distribuição dos mesmos. Para aproveitar ao máximo o potencial do Power BI, é recomendável usar os dois em conjunto. 

A partir dos relatórios, o serviço do Power BI também permite criar painéis de alto nível que fazem busca detalhada em relatórios e aplicativos para agrupar facilmente relatórios relacionados aos usuários em um formato 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

14 

simples. Estes painéis são chamados de dashboards, o que pode gerar uma certa confusão. 

E, além dos painéis, conseguimos configurar métricas e envio automático de relatórios via e-mail. Por fim, podemos criar aplicativos no Power BI Service, que tem como objetivo a distribuição de relatórios para audiências maiores, em que, a partir de um único link, os usuários têm acesso a diversos relatórios de um workspace. 

Como comentei no início desta aula, as ferramentas de BI entregam muito mais que relatórios, né? E, agora que vimos um pouco mais sobre as soluções desta ferramenta, fica mais claro entender que o Power BI Desktop e o Power BI Service foram uma grande dupla. Enquanto o Desktop é o nosso ambiente de desenvolvimento, oferecendo mais flexibilidade, desempenho e funcionalidades avançadas, o Power BI Service possui todo o ambiente necessário para a distribuição e o acompanhamento das métricas, de forma simplificada. 

E assim terminamos nossa primeira aula sobre o Power BI. Nos próximos encontros iremos entender mais sobre os componentes que constroem esta ferramenta. Vejo você lá! 

Material Complementar 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Preço Power BI 

**Descrição:** Compare planos e preços de business intelligence 

**Link:** https://www.microsoft.com/pt-br/power-platform/products/power-bi/pricing 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Comparar o Power BI Desktop e o serviço do Power BI 

**Descrição:** Texto com uma visão clara sobre as diferenças entre Power BI Desktop e Power BI Service 

**Link:** 

<u>https://learn.microsoft.com/pt-br/power-bi/fundamentals/service-service-vs-desktop</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

15 

**Aula 03: Fluxo de dados e modelo semântico** 

<mark>(conteúdo baseado em  Conferência com Matthew Roche;  Microsoft learn)</mark> 

Olá, analista! Seja bem-vindo à nossa aula sobre fluxo de dados e modelo semântico. A ideia desta aula é entendermos o que são esses elementos e como utilizá-los. De forma a complementar a aula anterior que contextualizamos os componentes do Power BI, aqui iremos compreender a utilização destes dois elementos importantes e complementares. Vamos lá? 

Sabemos que em estruturas modernas de dados, os dados são limpos, organizados, categorizados e transformados na etapa de ETL, que antecede a etapa de visualização. Para o analista de dados, o primeiro passo realizado no Power BI é a conexão com a fonte de dados, normalmente sendo um data warehouse. Essa conexão pode ocorrer de duas formas: pelo fluxo de dados ou pelo modelo semântico. 

O fluxo de dados do Power BI é uma funcionalidade que permite criar e gerenciar fluxos de informação dentro do serviço do Power BI, ou seja, na sua versão online. 

No ambiente do fluxo de dados podemos criar conjuntos de tabelas que vão ser utilizadas em várias análises, promovendo a reutilização de elementos de dados subjacentes, além de enriquecer os dados com lógicas que podem então ser úteis em mais de um relatório. Para essas mudanças utilizamos a linguagem M, própria do Power BI. Nas próximas aulas veremos um pouco melhor como essa linguagem trabalha. 

Mas lembre-se: sempre queremos que as transformações e criações de novas colunas sejam feitas na etapa de transformação de dados, que antecede o Power BI. As transformações realizadas com linguagem M devem se resumir em mudanças de tipo de dado, tradução de nomes de colunas de linguagem técnica para comercial e outras mudanças nessa mesma proporção. Sempre que for necessário aplicar uma nova regra de negócio aos dados, principalmente se essa for ser utilizada em mais de um projeto, é importante que ela seja feita lá na etapa de ELT. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

16 

Matthew Roche, um executivo da Microsoft comenta em uma de suas palestras que “Dados devem ser transformados o mais próximo da fonte possível e o tão próximo da visualização quanto necessário.”, porque quanto mais próximo da fonte, nesse caso, do data warehouse, teremos uma melhora na performance e no custo, uma vez que a transformação ocorre apenas quando atualizamos os dados da fonte. Além disso, com um dado pronto antes, temos mais oportunidades de reutilização, que gera uma menor manutenção e uma maior consistência das informações, contribuindo para termos uma única fonte de verdade sobre os dados. 

A separação do que deve estar presente em um fluxo de dados se assemelha a definição do que deve estar em cada workspace. Tudo depende de como a organização é construída. Podemos ter fluxos por fonte, por área, por frentes de trabalho e até a nível de tabelas, dependendo da solução escolhida. O importante é utilizarmos com inteligência essas divisões para que sejam claras aos usuários e que não gerem manutenções onerosas aos desenvolvedores. 

Outro benefício de utilizar o fluxo de dados é o menor contato que desenvolvedores de BI terão com a fonte de dados. Se existir uma política que restringe acesso aos dados no data warehouse, o uso do fluxo de dados é uma boa estratégia, porque assim, apenas alguns desenvolvedores fazem a conexão com o DW e esses, por sua vez, serão distribuídos no Power BI de forma controlada aos demais usuários para criarem seus relatórios. 

Por fim, o fluxo de dados também auxilia na menor taxa de atualização redundantes de tabelas. Por exemplo, a tabela de dimensão de datas. Essa é uma tabela utilizada em praticamente todos os relatórios que criamos e, se toda vez que ela for utilizada em um relatório, fazermos uma conexão dela para o Power BI, faremos a sua atualização diversas vezes no mesmo dia, de forma demasiada. Se tivermos ela em um fluxo de dados e utilizarmos ela a partir dele em nossos relatórios, a atualização em relação ao data warehouse acontece apenas quando o fluxo de dados for atualizado, diminuindo assim, os custos. A dimensão de datas normalmente é uma tabela menor, mas imagine isto acontecendo com uma tabela fato, que possui milhões de linhas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

17 

Vamos a um exemplo de utilização do fluxo de dados? A situação é a seguinte: precisamos criar um fluxo de dados que nós e outros analistas de dados do BanVic irão utilizar em relatórios sobre análises de crédito com a visão de colaboradores. Sabemos que no data warehouse existem as seguintes tabelas: dimensão de clientes, dimensão de agências, dimensão de datas, dimensão de colaboradores e fato propostas. 



<!-- Start of picture text -->
Modelo conceitual para fct_propostas<br>dim_colaboradores<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

A estrutura dessas tabelas é definida a partir de um esquema estrela, também chamado de modelo dimensional, que vimos nas aulas anteriores ser o modelo previsto pelo Power BI para uma melhor performance. 

Porém, para esse grupo de analistas e para essa solução entendemos que será necessária apenas uma análise com a dimensão de agências, datas e colaboradores, além da tabela fato proposta, não sendo de interesse a dimensão de clientes. Isso ocorre porque esses relatórios são internos e sobre o montante de propostas realizadas por colaborador. Então, ao invés de criarmos um Fluxo de Dados com todas essas informações, podemos criar um com as tabelas dimensão de agências, data, colaboradores e a fato propostas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

18 



<!-- Start of picture text -->
Modelo conceitual para o Data Flow de analise de crédito por colaborador<br>dim_colaboradores<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

A retirada desta tabela dimensão, além da diminuição do tamanho do fluxo de dados e necessidade de atualização de uma tabela não utilizada, também gera uma maior segurança da informação, uma vez que apenas os dados necessários estão sendo disponibilizados. 

E o que podemos fazer dentro deste fluxo? Como comentei, no fluxo temos o Power Query online e aqui podemos organizar as informações das colunas para uma linguagem natural, a linguagem de negócios. Podemos excluir colunas que não são interessantes ou necessárias para esse fluxo de dados também. A intenção é que nosso fluxo de dados seja útil e tenha as informações na medida certa para os analistas de dados realizarem suas análises e montarem seus relatórios. Ele é uma camada de consolidação dos dados. 

Agora que já vimos como funcionam os fluxo de dados no Power BI, chegou a hora de vermos um pouco mais sobre os modelos semânticos, chamados até um tempo atrás de conjunto de dados. 

E, antes de mais nada, precisamos entender que existem duas formas de trabalhar com o modelo semântico. 

Vamos começar pela forma mais abrangente em organizações de médio e grande porte. Nestes casos, o modelo semântico nos atende como complemento ao fluxo de dados. Ou seja, o modelo semântico vai ter como fonte de dados, o fluxo de dados, em que já consolidamos as 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

19 

informações. Para criar um modelo semântico, vamos precisar do Power BI Desktop e nele, vamos escolher como fonte de dados, o fluxo de dados criado anteriormente. 

O segundo caso de uso é em situações onde não temos um fluxo de dados. Em empresas menores ou soluções mais simples ou antigas, o fluxo de dados não está presente. Mas, atenção! Recomendamos o uso do fluxo de dados por todos os benefícios que podem ser atribuídos a ele, ok? Para estes casos, iniciamos o nosso processo de criação de relatório diretamente por ele, no Power BI Desktop e unificamos as etapas de consolidação dos dados no Power Query a ele. A partir disso, a utilização do modelo semântico é a mesma para as duas formas de trabalho. 

O modelo semântico é o local do relatório onde seus dados estão! Se você já viu um workspace no Power BI, reparou que todo relatório é dividido em duas caixas: modelo semântico e relatório. 



Fonte: Própria autora (2024). 

Na prática, quando temos apenas um relatório vinculado a um modelo semântico, eles são o mesmo arquivo pbix - que é a extensão dos arquivos criados no Power BI Desktop. Mas podemos ter mais de um relatório vinculado e, nesses casos, você vai perceber que o modelo semântico é o local com todas as regras e dados e o relatório possui os gráficos e visuais. 

Por ser o local onde os dados estão armazenados, é no modelo semântico que criamos colunas calculadas e medidas em DAX, além das definições dos relacionamentos entre as tabelas. A combinação das funcionalidades do fluxo de dados e do modelo semântico é uma forma de aproveitar ao máximo as capacidades do Power BI, mantendo a governança e a qualidade dos dados. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

20 

Na próxima aula vamos conversar mais sobre o armazenamento destas tabelas no Power BI. Vejo você lá! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

21 

### **Aula 04: Modo de armazenamento dos dados no Power BI** 

<mark>(conteúdo baseado no</mark> <u><mark>site</mark></u> <mark>do Power BI)</mark> 

Olá, analista! Nesta aula vamos conversar sobre os tipos de armazenamento de dados no Power BI. A forma que realizamos o armazenamento de dados no nosso dashboard significa muito, desde o desenvolvimento até a utilização dos dados quando o arquivo está em produção. Vamos ver em detalhes quais são as opções que a Microsoft disponibiliza e como podemos fazer melhor uso delas. Vamos lá? 

Inicialmente, gostaria de apresentar para você quais são as atuais opções de armazenamento disponíveis. Existem três possibilidades: Import ou Importação, DirectQuery e armazenamento Dual ou Duplo. De forma bem simplificada, no modo Importação teremos as consultas e dados armazenados no modelo ou em cache, no modo DirectQuery teremos todas as consultas realizadas na fonte de dados e, no modo Duplo, os dois formatos estarão acontecendo de forma conjunta. 

Agora, vamos explorar melhor cada um dos modelos, iniciando pelo modo Importação. Esse modelo é utilizado de forma mais frequente, dados os seus benefícios. É comum escolhermos esse como modelo inicial de se trabalhar. Normalmente iremos começar nossos projetos com modo Importação e, esse não sendo mais uma opção, partiremos para os outros dois. 

Quando selecionamos a Importação, estamos indicando que o Power BI faça uma cópia dos dados das tabelas e colunas selecionadas para dentro do modelo. Essa transferência de dados acontece de forma otimizada, fazendo com que os dados fiquem comprimidos no modelo semântico. Quando atualizados, os dados são compactados e otimizados pelo mecanismo de armazenamento VertiPaq. Esse mecanismo consegue realizar uma compactação de 10 vezes no modelo, então um conjunto de dados que inicialmente poderia ter 10GB, após passar pela compactação fica com 1GB. 

Quando falamos em ter uma cópia dos dados dentro do modelo, queremos dizer que toda vez que atualizamos as tabelas em um arquivo, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

22 

carregamos esses dados para dentro, o que leva a um desempenho melhor de consulta, porque os dados estão armazenados no modelo e são otimizados para as consultas analíticas de filtrar, agrupar e resumir. 

Outra característica de usar a Importação é o suporte a todas as fontes de dados, todas as funcionalidades em DAX, M e tabelas calculadas. Apenas nesse modelo é possível utilizar cem por cento das funcionalidades da ferramenta. 

Por fim, temos um volume menor na transferência de dados. Apesar de termos, a cada atualização padrão dos dados, uma chamada ao data warehouse pedindo todos os dados das tabelas, como um “select * from table”, essa chamada é feita apenas algumas vezes no dia. É comum que modelos atualizem, de forma produtiva, uma vez ao dia. Quando usada a Importação pode-se realizar até 48 atualizações agendadas em um modelo semântico por dia. Esse volume, por muitas vezes, pode ser considerado menor, quando comparado a um modelo DirectQuery. 

Porém, além dos benefícios, existem algumas limitações e desvantagens, que nos levam a procurar outras alternativas, como o DirectQuery. Existem três limitações principais que nos levam a utilização desse tipo de conexão: tamanho do modelo, atualização dos dados e questões relacionadas à segurança da informação. 

Quando falamos em tamanho no modelo, precisamos também levar em consideração qual tipo de licença do Power BI estamos trabalhando. Por exemplo, se estivermos em uma capacidade compartilhada, os modelos semânticos, já compactados, não podem passar do de 1GB. Caso contrário, o conjunto não é publicado, nem atualizado no Power BI Service. Existem formas de otimizar um modelo, se precisamos seguir trabalhando no modo Importação. Na aula sobre otimização de modelos no Power BI, você verá em maiores detalhes como fazer. 

Mas, se mesmo com as otimizações, o tamanho do modelo persistir maior que o limite imposto pela Importação, o DirectQuery passa a ser uma boa opção, uma vez que quando usamos esse modelo, estamos indicando para o Power BI  se conectar diretamente à fonte de dados e enviar 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

23 

consultas para obter as informações necessárias. Nesse cenário os modelos contêm apenas os metadados que definem a estrutura e não uma cópia dos dados, como vimos anteriormente. Neste formato, todos os dados permanecem no data warehouse, o que faz com que tamanho deixe de ser um problema e, a cada consulta, troca de filtro, cruzamento de informações, uma nova query é gerada ao data warehouse, que devolve ao relatório novos dados. 

Esta permanência dos dados no data warehouse está alinhada com a segunda vantagem de utilizar o DirectQuery. Uma vez que os dados ficam retidos na fonte, nenhuma cópia é feita para o computador do desenvolvedor e, se por políticas de segurança não for possível ter essa permissão para importar cópias locais dos dados para relatórios, a conexão direta com a fonte de dados é uma solução. 

O terceiro motivo para se utilizar o DirectQuery é quando o volume de atualização dos dados que o modo Importação oferece, não resolve as dores do usuário. No modo importação existe um limite de atualizações diárias que podem acontecer no Power BI Service. Quando estamos em uma capacidade compartilhada esse limite é de 8 vezes e, em uma capacidade dedicada, é de 48 vezes. Vão existir casos que essa frequência não é suficiente. E, quando isso acontecer, o armazenamento por DirectQuery torna-se uma boa opção, porque nesta modalidade, os dados estão sendo lidos em tempo real pelo data warehouse. Lembra quando falei que neste modelo não temos uma cópia dos dados no arquivo? Então, neste modo estamos criando uma conexão direta com a fonte de dados e sempre estaremos lendo a versão mais atual deles, não sendo necessário configurar um agendamento para que essa atualização aconteça. 

Ok, agora que entendemos que a Importação é o nosso padrão de conexão e, quando ela não for possível devemos ir para o DirectQuery você pode estar se perguntando: mas e se eu tiver apenas algumas tabelas volumosas demais, ou que necessitam de uma atualização mais constante no meu modelo, será que preciso modificar todas as minhas tabelas, aumentando o custo e perdendo desempenho do modelo? 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

24 

Bom, para casos como esse podemos utilizar os modelos compostos, onde teremos uma conexão Dual ou Dupla. No modo Duplo, você pode identificar alguns dados a serem importados diretamente e outros dados que devem ser consultados, via DirectQuery. O modo Duplo fornece flexibilidade ao modelo, porque podemos utilizar em tabelas maiores o poder do DirectQuery, com sua infinidade de linhas e taxa de atualização, combinada com tabelas Importadas, que possuem velocidade para realizar as consultas analíticas, melhorando o desempenho do modelo. 

Podemos sintetizar esta aula em um árvore de decisão, com quatro perguntas norteadoras: 

1. Preciso ter à disposição todas as fontes de dados disponíveis? Se a resposta for Sim, escolhemos o modo de Importação. 

2. Se for não, seguimos para o próximo passo. Preciso ter todas as funções DAX, funções em M e a opção de trabalhar com tabelas calculadas? Se a resposta for sim, escolhemos o modo de Importação. 

3. Agora, se ainda assim não tivermos essa necessidade, seguimos para a terceira pergunta. Preciso ter uma atualização em tempo real dos dados? Se a resposta for sim, devemos seguir com o DirectQuery. 

4. Mas, se a resposta for não, vamos a nossa quarta pergunta. Preciso de espaço para grandes volumes de dados? Se aqui, a resposta for não, vamos para o modo Importação. E, se a resposta for sim, podemos seguir para o modelo Duplo, que combina os dois formatos em um único arquivo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

25 



<!-- Start of picture text -->
Preciso ter a disposigao fontes de sim<br>dados especificas?<br>wio }<br>Preciso de todas as fungdes DAX, sm<br>Me tabelas calculadas?<br>Nao t<br>F<br>DirectQuery —_—sim Preciso dealdo atualizagéoeG em tempoPp Importagao=,<br>Néo 1<br>Duplo <_<"sim __ Precisovolumesde espaco de dados?para grandes Nao<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Para o exemplo prático que teremos em nosso curso, com dados do BanVic, utilizaremos o modo de importação, por estarmos trabalhando com dados que não possuem nem um grande volume a ponto das cotas de importação não suportarem, e também por não estarmos trabalhando com dados de atualização em tempo real. 

Nesta aula vimos de forma detalhada todos os modos de armazenamento que temos disponíveis no Power BI. Lembre-se que este planejamento define questões importantes referentes ao desempenho dos seus modelos, e, cada uma das estruturas que vimos possui benefícios e também limitações. O mais importante aqui, é sabermos escolher de forma inteligente o modo que melhor será aproveitado pelos usuários nos relatórios finais. Vejo você na próxima aula! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

26 

### **Aula 05: Estrutura das tabelas em um modelo semântico** 

Olá, analista! Nesta aula veremos como estruturar um modelo semântico no Power BI. Sairemos daqui com um entendimento claro sobre as melhores práticas relacionadas a distribuição das tabelas, ao relacionamento entre elas, a cardinalidade e como a direção dos filtros pode influenciar suas visualizações finais. Nesta aula vamos começar a colocar a mão na massa no Power BI Desktop. Vamos lá? 

A forma como construímos um modelo semântico no Power BI é muito importante. Assim como o modo de armazenamento, a distribuição das tabelas e suas relações contribuem para o desempenho dos relatórios. Modelos simples e otimizados levam a relatórios rápidos e fáceis de se utilizar. Modelos complexos e repetitivos levam a relatórios não funcionais e de difícil manutenção. Por isso é importante atentarmos à sua estrutura, focando sempre em termos uma experiência melhor na exploração e agregação das informações. 

Modelos de dados podem se tornar complexos rapidamente, com diversas ligações, inúmeras colunas, criando um verdadeiro emaranhado de informações. Como analistas de dados, é nosso dever trabalhar de forma a entregar tabelas concisas, que possuam colunas suficientes para as análises. Tabelas que sejam úteis e que levem os usuários à busca por insights, que os ajude, mais do que os atrapalhe. Não existe uma fórmula que dirá quantas colunas uma tabela deve ter, ou quantas tabelas um modelo deve conter e existem situações que são necessárias mais tabelas, mais colunas, mas sempre devemos estar atentos a entregar aquilo que gere valor, e não apenas a informação por ela mesma. 

Cada ferramenta de BI possui suas particularidades e, neste sentido, o Power BI tem por definição que a melhor forma de estruturar as tabelas dentro dos modelos semânticos é utilizando um Esquema Estrela, também conhecido Star Schema. No módulo de Modelagem de dados você viu como é uma estrutura de tabelas fato e dimensão. Você também viu que as tabelas fato contêm os valores de um evento, enquanto a tabela dimensão contêm os detalhes sobre os dados quantificados nas tabelas 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

27 

fato. A ligação entre elas acontece por chaves, onde teremos um valor único na dimensão que combina com um ou mais valores na tabela fato. 

Esta ligação entre tabelas é o que chamamos de relacionamento. No Power BI é essencial que saibamos como as tabelas se relacionam entre si, uma vez que a partir desta conexão que conseguimos alavancar nossas visualizações para outro patamar, já que os valores agregados das tabelas fato, combinado com os detalhes entregues pelas dimensões, darão aos nossos relatórios as informações necessárias para que decisões sejam tomadas. 

O primeiro tipo de relacionamento, o mais comum, é o recomendado a se fazer, principalmente quando trabalhamos com um Esquema Estrela é o relacionamento um para muitos, que por muitas vezes é descrito como Um, dois pontos, asterisco (1:*). Neste modelo teremos uma linha da tabela dimensão se conectando com uma ou mais linhas na tabela fato. É o caso de ligarmos a tabela de dimensão de datas, que está na granularidade de dia, mês e ano, com a tabela fato transações, que traz todas as informações do evento de transação, também por data completa. 

Na prática, teremos a seguinte situação: na tabela dimensão de datas teremos uma linha para o dia 01/03/2025. E, essa linha se conecta com a tabela fato transação em diversas outras linhas, uma para cada transação que ocorreu nesta data do BanVic, trazendo assim todas as informações dos eventos de transação para esta data. Tudo isso a partir de um relacionamento de um registro para muitos. 

Existe também o relacionamento um para um. Aqui teremos a relação entre duas tabelas com valores exclusivos. Voltemos ao exemplo anterior para entender como essa situação pode ocorrer, ok? 

Imagine que para cada dia registrado, tenha ocorrido apenas uma transação. Desta forma, tanto a tabela dimensão de datas quanto a fato transações, teria um registro para o dia 1, 2, 3, e assim por diante. Esse tipo de relacionamento acaba não sendo recomendado porque armazena informações de forma redundante, não sendo necessária a utilização de uma tabela dimensional. Neste caso é preferível combinar as tabelas em 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

28 

uma só, porque a ideia de usarmos uma tabela dimensão é não ficarmos repetindo as características de um dados para diversas linhas da tabela fato. Mas, como aqui estamos apenas com um registro para cada data, essa informação não se repetiria. 

O terceiro tipo de relacionamento é o muitos para muitos. Aqui, estamos com a situação oposta a anterior, já que não temos valores exclusivos em nenhuma das duas tabelas relacionadas. É como se tivéssemos, na tabela de datas mais de uma linha para cada dia, e, relacionando com a tabela fato transação, não teríamos uma data única em nenhum dos lados. Esse relacionamento também não é recomendado, uma vez que a falta de valores exclusivos gera ambiguidade, onde não é possível ter certeza sobre o caminho do dado. Isso pode gerar resultados incorretos nas consultas analíticas e perda de desempenho nos modelos. 

Para manejar esta situação, podemos repensar na modelagem das tabelas em si, ou criar tabelas intermediárias, chamadas de Bridge Tables. Esse tipo de tabela constrói um elo entre as tabelas com relacionamento de muitos para muitos, criando um caminho claro e definido entre elas, transformando-se em dois relacionamentos um para muitos. Este tipo de tabela torna-se relevante quando estamos em modelos mais complexos, onde a ambiguidade começa a se tornar um problema, seja por relacionamento ou até por múltiplos caminhos que o dado pode fazer para chegar a uma tabela e outra, que é o nosso próximo tópico. 

Vamos criar os relacionamentos do nosso exemplo do Banvic? No arquivo anexado à primeira aula deste módulo você recebeu o arquivo base do Banvic com seis tabelas: dim_clientes, dim_colaboradores, dim_agencias, dim_dates e fact_transacoes. Para o exemplo do curso, trabalharemos diretamente com este arquivo, sem a utilização de um fluxo de dados ou conexão online. A partir dele vamos desenvolver o nosso dashboard nas próximas aulas. 

O primeiro passo é criar o relacionamento entre as tabelas fatos e dimensões. Aqui, utilizaremos sempre a ordem e um para muitos, saindo da tabela dimensão para a fato, com direção do filtro única. Começaremos então abrindo a aba Exibição do Modelo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

29 



<!-- Start of picture text -->
Baim ctentes o ain cats os © simagencas os<br>ep Ean _agencia<br>cia B anacan<br>Eiretcod.agencia Xdads E codieagencia<br>E code E same diate<br> cod,colaborador E dia_semana vendereco<br>oes finsemane Nome dlc<br>©8 ssn aan senra nctino Enevane da ”to.genca<br>fecoher = tents seca<br>B te. tanacoes os<br>se.<br>see<br>& cod.transacao<br>it<br>BEnomearomasmums reco<br>EF ceste rennn<br>teat=<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Para criar o relacionamento entre as tabelas você pode arrastar a coluna de chaves de uma tabela a outra ou clicando no menu superior em Página Inicial > Gerenciar relações > Novo relacionamento. 

Faremos juntos um exemplo mas, no material complementar deixarei a listagem dos relacionamentos a serem feitos. Vamos fazer a conexão entre as tabelas de clientes e de transação, uma vez que toda transação realizada no banco, deve ter um cliente envolvido. Na primeira tabela, colocaremos a dim_clientes e selecionaremos a coluna cliente_sk, que identifica uma única linha na tabela. Na tabela de Para, selecionaremos a tabela fact_transacoes e a coluna cliente_fk, que liga com todos os detalhamentos dos clientes trazidos na dimensão. Aqui conferimos a cardinalidade de um para muitos e a direção do filtro, também deixaremos este relacionamento ativo. Depois disso é só salvar e continuar adicionando os demais relacionamentos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

30 



<!-- Start of picture text -->
< Novo relacionamento x<br>Selecione tabelas e colunas relacionadas umas as outras.<br>Da tabela<br>dim_clientes v<br>cep cidade cliente_sk codagencia cod.cliente __cod.colabora...._cpfenpj<br>50946020 Pires/ Pl b446bdd5d86... | 7 587 20 903.2518<br>30966116 Ventosa 0891 738a12b66c2... | 7 353 20 803.219..|<br>Para a tabela<br>fct_transacoes v<br>agencia_fk cliente_fk cod_transacao datafk datatransacao nome_transac.... num_cont<br>34e783be9b0... |debedf67de2c... | 52015 480a2dbac08... 29/12/2022 2..  Pix-Realizado 962 Py<br>34e783be9b0... | 51549226067... | 66595 480a2dbac08... 29/12/2022 2... Pix-Realizado 202 -|<br>Cardinalidade Direcao do filtro cruzado<br>Um para muitos (1:*) v Unico v<br>Ativar este relacionamento<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Talvez você já tenha se atentado a isso, mas vale explicar: sempre que falamos sobre relacionamento, falamos o termo de um ou muitos **para** muitos. No Power BI, esse é outro conceito importante, o de direcionalidade de um relacionamento. Existem duas possibilidades: a direção única de filtro cruzado e a de ambas as direções de filtro cruzado ou filtragem cruzada bidirecional. 

Por padrão, o relacionamento ocorre da dimensão para a tabela fato, ou seja, a direção única de filtro cruzado. Vamos voltar ao nosso modelo? Vamos focar em três tabelas: a dimensão de agências, a dimensão de clientes e a fato transações. Como vimos anteriormente, teremos uma ligação de um para muitos das tabelas dimensionais para a tabela fato. Podemos ver que além da demonstração visual de uma linha ligando as 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

31 

tabelas com o número 1 e o símbolo do *, temos uma seta, indicando que o filtro vai da dimensão para a fato, ou seja, a Tabela de Agências e a Tabela de Clientes filtram a Tabela de Transações, mas a Tabela de Transações não filtra as Tabelas de Clientes e de Agências. Também, apesar da ligação indireta pela tabela fato, uma tabela dimensão não filtra a outra, porque ambas estão apenas filtrando, e não sendo filtradas. 



<!-- Start of picture text -->
(8) dim_cientes ” .<br>iB}dim_agencias on<br>cep<br>cidade abertura;<br>diente_sk cia<br>een<br>cod_agencia foe\cia_sk<br>cod_cliente “cidade<br>cod_colaborador<br>- cod_agencia<br>cpfenpj<br>data_abertura endereco<br>‘at (B fact transacoes ~ Sp7 sgenca7<br>Recolher agencia.fk af A<br>LI cliente_fk iT]<br>© cod_transacao<br>datafk<br>nome_transacao<br> num_conta<br> saldo<br>valor trancaran,<br>Recolher~<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Se você tiver dúvidas sobre a direção do filtro, acompanhe para onde a seta do relacionamento entre as tabelas vai para entender em qual direção o filtro irá. 

Este direcionamento é seguro porque sabemos seu padrão. Porém, por muitas vezes queremos ir além, queremos que o dado percorra todo o caminho, de uma dimensão à outra. Ou, queremos que a tabela fato possa filtrar uma tabela dimensão. Neste caso, podemos mudar a direção para ambas, em gerenciar relações e editar relacionamento, alterando a direção do filtro cruzado para ambos. Para o nosso exemplo, vamos mudar a direção do filtro da Dimensão de Agências para a Fato Transações, deixando-a com direção de filtro cruzado Ambas. Para isso, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

32 

podemos ir na edição do relacionamento, ou, com a linha selecionada, ajustar essa configuração nas Propriedades, à direita da nossa tela. 



<!-- Start of picture text -->
Cardinalidade Diregdo do filtro cruzado<br>Mus paraun z<br>@ Ativar este relacionamento [ Ablicar filtro de seguranca em ambos os<br>sentidos<br>(-) Pressuponha integridade referencial<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Agora, temos um modelo onde dados de uma tabela dimensão podemos filtrar a tabela fato e esta pode filtrar outra dimensão, ou seja, o dado pode percorrer o caminho da Dimensão de clientes até a Dimensão de Agências, a partir da Fato Transação. Essa configuração traz um poder ainda maior para as análises a serem realizadas. 



<!-- Start of picture text -->
(8) dim cientes |<br>cep<br>cidade abertura-<br>‘cod_agencia<br>dliente_sk | agencia_sk<br>cod_cliente me<br>cidade<br>cod_colaborador<br>epfenpja cod_agencia<br>data_abertura endereco. .<br>oes (©) fact transacoes os Spe agenci<br>Recolher agencia_fk ecolnera ©<br>ao cliente fk. 7}<br>& cod_transacao<br>datatk<br>nome_transacao<br>= num_conta<br>© saldo<br>valor trancacan,<br>Recolher ~<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Quando usamos a filtragem cruzada bidirecional precisamos ter certeza de que nosso modelo faz sentido neste formato, para não termos a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

33 

ambiguidade comentada anteriormente, onde não entendemos ao certo qual é o caminho que o dado faz de uma tabela a outra. Também é importante comentar que em modelos maiores, podemos ter uma diminuição no desempenho. Então, atente-se a utilizar quando for pertinente. Você pode, também, criar este tipo de direcionamento específico para uma medida, a partir de funções DAX, como a Crossfilter, que está detalhada no material complementar desta aula. 

Outra particularidade que pode ocorrer com os nossos dados e seus relacionamentos é termos uma dimensão com função múltipla. Uma dimensão com função múltipla é aquela que possui várias colunas se relacionando com uma mesma tabela fato. Por padrão o Power BI não permite que tenhamos mais de um relacionamento ativo entre duas tabelas e, por isso, aquelas que não estão ativas, estarão com a linha pontilhada ao invés de contínua. 

Quando nos deparamos com uma situação destas, é necessário criar os relacionamentos entre as tabelas, deixar ativo apenas o que for pertinente e, quando houver necessidade de utilizar os demais relacionamentos, ativá-lo a partir da criação de medidas e utilização da função DAX Userelationship, que está detalhada no material complementar desta aula. 

Nesta aula vimos o poder de uma boa modelagem de dados. Termos dados bem estruturados chegando em nosso relatório é essencial se quisermos boa performance e usabilidade. Tabelas em Esquema Estrela, com relacionamentos e cardinalidade bem definidos são sinônimos de relatórios bem construídos. Vejo você na próxima aula! 

#### Material Complementar 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** CROSSFILTER 

**Descrição:** DAX - Função CROSSFILTER 

**Link:** <u>https://learn.microsoft.com/pt-br/dax/crossfilter-function-dax</u> 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

34 

**Título:** USERELATIONSHIP **Descrição:** DAX - Função USERELATIONSHIP 

**Link:** <u>https://learn.microsoft.com/pt-br/dax/userelationship-function-dax</u> 

**Tipo** ☐ Site ☐ Livro ☐ Vídeo   x Leitura ☐ Filme ☐ Visite **Título:** Lista de relacionamentos para o arquivo base no Power BI **Descrição:** Lista de relacionamentos para o arquivo base no Power BI **Link:** <u>[FADA] [Módulo 6] [Aula 5] Material complementar</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

35 

### **Aula 06: Power Query e Linguagem M** 

E aí, como está a sua jornada até aqui? Nesta aula nós vamos conversar sobre os conceitos de Power Query e Linguagem M. 

Na aula sobre fluxo de dados e modelos semânticos comentamos que quando selecionamos as tabelas para dentro do Power BI podemos realizar alterações nas colunas com intuito de termos um modelo melhor para trabalhar na construção dos relatórios. Essas alterações são feitas no Power Query por meio da Linguagem M. 

Vamos então começar pelo início, respondendo o que é o Power Query. O Power Query surgiu como um suplemento do Excel, servindo como uma solução de transformação de dados na ferramenta. Ele foi adicionado também ao Power BI, com o mesmo intuito. No editor do Power Query é possível renomear colunas e tabelas, alterar o texto para números, remover linhas, definir a primeira linha como cabeçalho, entre outras funcionalidades. 

Mas hoje em dia, com a utilização de um processo moderno de extração, carregamento e transformação de dados utilizando data warehouses, a ferramenta de BI pode focar apenas na visualização, deixando a transformação sempre mais próxima da fonte de dados. Por isso, a utilização do Power Query se dá principalmente em ajustes nas tabelas finais, com o objetivo de padronizar nomenclatura de colunas para uma linguagem natural, ou seja, uma linguagem para o usuário de negócio e também para eventuais exclusões de colunas que não são necessárias para aquela solução de visualização. 

Podemos utilizar o Power Query tanto no Power BI Service quanto no Desktop. Quando usarmos na nuvem, estamos usando-o por meio do fluxo de dados. Vamos ver como funciona o Power Query? 

Iniciamos com o Power BI Desktop aberto, no arquivo do BanVic, que estamos utilizando desde a última aula. É importante lembrar que, para simplificar, os dados já estão no arquivo, importados por tabelas csv. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

36 

#### Quando acessarmos o Power Query, essa é a interface que temos. 



<!-- Start of picture text -->
Ae 0 - a<br>inal | Tantomar Addons ohne tabido_Fenanetas Au e<br>mm A Py Byromiedets yg) HL) apne<br>RORE ff § 2B to. Bi) 1h Siwemmnumeconecneanesdon to _— =eremnntatsoit otto<br>fess |eee, boa |eter) peter] yee emer: 0 eset 0S Mersami ne"Be cng<br>| Const < ‘i | = Tee.traatoratolomtype(srCebecslnos Proviso", ((eliente se, tye text, {Ted cert, | Conf. Conia x<br>TlBi tatimimagens certs eras (E2521 tossoretesaesoneste850053. DeRRSTOS  ocr ai3[=]1%p coa_agenia [=]37 % codcotborador —[=]1%y=2 mum.conta =,ah=) 4 PROPRIEDADES:Nome(drs<br>eae Doman ESSESTISS. as , “ 1) Teds opener<br>3 ctasicameaiasoe. @ 7 x p | CIE<br>6 oxeenreneaisesnsusiiet a 2 5 a Fonte *<br>1 oxererasoneatoerenic. = ‘ 2 = Cateatos omovies<br>& carreciootesee Tie. we > « xP Tpeatendo<br>11 exencuiesimacouRnDaste 10 > » “<br>1213 xeaesoesnssm@etsTS.ueetsaenoiecteentee ss” 2‘ 6a »%<br>11 outspeniowonceseer2040tsecrastaoetaasi ws > » «<br>16171s192 tenorstseinesnseeale®sisraneiaanoea5estssncmessneerssse64esmoaseiseseaseouctcmentesssoeomseaseecta8sisan Fra“622 2°1??? %”ssx»»2” “Fi&i‘<<br>21 esouoratessesS9i507. Ds 2 = ®<br>2223 WSesateresiasesscaeToreeseuneuserastniaames asw 77 “« By“<br>{8COUNAS S98LNHAS CrePa per cua com ae peas Ds > WSUALZAGO BOK 205<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

No cabeçalho temos várias opções de edição de colunas, com a página inicial contendo os principais atalhos e formatações específicas em cada aba seguinte, como a de transformar, adicionar coluna, exibição e outras. 

PEGE crsincar 

Fonte: Própria autora (2024). 

Na lateral direita podemos ver as propriedades como o nome da tabela e as etapas aplicadas. As etapas aplicadas funcionam como um histórico de todos os passos que são aplicados naquela tabela. Lembrando que toda vez que atualizamos os dados do arquivo, esse passo a passo é realizado. 

E na lateral esquerda vamos ter as consultas. Quando não aplicamos nenhum tipo de transformação no dado que chega até o Power BI, as consultas se assemelha às tabelas. 

A edição dos dados pode acontecer pelo menu superior e também clicando com o botão direito em cima do cabeçalho da coluna. Outro 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

37 

local que também podemos editar os dados é a partir do Editor Avançado. O Editor avançado é o único local de todos esses que mostrei que você vai precisar da linguagem M para conseguir desenvolver. 



<!-- Start of picture text -->
Spler® Fontes Recents» Dados ‘Yonts'desodes" Parkmcwos~ VsualenloG5 Gerencar> Colmar» Cates Unis Cana» pee 2, usta Vtores Compinet 1 azure Machine Leeming<br><!-- End of picture text -->



<!-- Start of picture text -->
Fonte: Própria autora (2024).<br><!-- End of picture text -->



<!-- Start of picture text -->
I Esitor Avancado a x<br>dim_clientes er ae)<br>rc<br>Y Nenhum<br>eno de sintare detects,<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Ainda assim, todas as alterações feitas nesta etapa acontecem por meio da linguagem M. O nome formal da linguagem é Power Query Formula Language, mas é amplamente conhecida como M por ser uma linguagem que **manipula/modela** dados. 

Como comentado anteriormente, o Power Query possui várias opções de edição por botões e menu, que acaba abstraindo muito a necessidade de entender a sintaxe da linguagem M, sendo interessante apenas conhecer a interface do Power Query e onde conseguimos realizar as edições. 

Dentro de uma estrutura moderna de dados a indicação para utilização da Linguagem M e Power Query se dá na verificação e alteração, se necessário, do tipo do dado. Como um exemplo, a mudança de uma coluna de valores está como texto e deveria ser um numeral. Também 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

38 

podemos realizar a exclusão de colunas que não são necessárias. Como por exemplo a coluna de CPF de colaboradores. 

Vamos para o nosso arquivo, realizar algumas destas mudanças? Ao abrir o Power Query do BanVic, clicando em “Transformar Dados” na Página Inicial, iremos até a dimensão de agência e, na coluna agência, após dar dois cliques, renomeamos para Nome da Agência, assim conseguimos diferenciar com a coluna nome que temos na dimensão de clientes. Faremos o mesmo na dimensão de clientes e, ao invés de nome_cliente, teremos Nome do Cliente. 

Quando realizamos essas modificações, etapas são aplicadas ao modelo. Podemos observar isso pela nova linha à direita do nosso Power Query: 



<!-- Start of picture text -->
dae<br>TEBE evens roe Aton catne ide rns au e<br>Roe 8 8 Bm MK Be th dectmmmemcnem: Semmwomee- seem<br>SRE: AALS.<br>Sah SMETANA EE MSE 4 star tos evar iors weaning<br>comm J | = tte tno iain (Crome ere, “honed ete) Conta x<br>|31B smspecinenemtn i2 cassieSanamewe ete =o ett 7: nome 5> oe 1 A wethoweae Aommaemngcaroes |= ormcones(20.5<br>— 5 sitetoemabeaae ™ : > 1 tines cn nia<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Estas etapas aplicadas são camadas de transformação acontecendo nos dados e, por isso, sempre que possível, deve-se manter camadas iguais, juntas. Você pode renomear quantas colunas julgar necessário, sempre levando em consideração a máxima de traduzir o nome destas colunas do modelo lógico para um modelo de negócio, para que quando criarmos visualizações com essas colunas já tenhamos a nomenclatura correta, diminuindo a chance de erros sintáticos e deixando os nomes mais próximos daqueles que o usuário conhece aqueles dados por. Da mesma forma que fizemos para o relacionamentos, sinta-se à vontade para pausar a aula e renomear as colunas que você achar importante. 

E, além de renomear, podemos usar o Power Query para modificar o tipo de dado, transformando-o em moeda, por exemplo. O importante é lembrar que, apesar do poder do Power Query, queremos que as transformações estejam no DW, por motivos de escalabilidade e 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

39 

segurança. Por isso, mantenha-as simples nesta etapa. Quando finalizar as suas modificações no Power Query, clique em Fechar e Aplicar para voltar a aba do Power BI. 

Em resumo, devemos utilizar o Power Query apenas para aquilo que não é possível ser feito nas etapas de transformação de dados e podemos utilizá-lo para facilitar nosso trabalho com a leitura das colunas para as próximas etapas. Na próxima aula iremos conversar sobre outra linguagem muito importante no Power BI: a linguagem DAX. Vejo você lá! 

#### Material Complementar 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Conectar-se aos dados 

**Descrição:** Passo a passo de como se conectar a fontes de dados no Power BI 

**Link:** <u>https://learn.microsoft.com/pt-br/power-bi/connect-data/desktop-connect-to-data</u> 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Quick tour of the Power Query M formula language 

**Descrição:** Link da aba de tutorial da Microsoft sobre a Linguagem M para Power Query **Link:** 

<u>https://learn.microsoft.com/en-us/powerquery-m/quick-tour-of-the-power-query-m-fo</u> 

<u>rmula-language</u> 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Power Query M function reference 

**Descrição:** Link da aba de referências de funções da Linguagem M para Power Query 

**Link:** 

<u>https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

40 

**Aula 07: Linguagem DAX** 

##### <mark>(Material:  Microsoft learn; Microsoft learn;</mark> <u><mark>Microsoft learn)</mark></u> 

Olá, analista! Nesta aula vamos conversar sobre DAX, a linguagem utilizada no Power BI para criar medidas e colunas calculadas dentro dos modelos semânticos. 

E, para começar, vamos entender o que é DAX. DAX significa Data Analysis Expressions. O nome já nos indica que essa é uma linguagem propícia para análises, certo? Ela, assim como a linguagem M, surgiu para mais do que uma solução da Microsoft, e hoje podemos utilizar DAX no Power BI e também no Power Pivot do Excel. No Power BI se referenciam colunas e no Excel um intervalo de células, desta forma o contexto que trabalha-se em cada ferramenta muda um pouco, mas a sintaxe das expressões se assemelham. E, falando em funções, hoje existem mais de 200 funções e operadores disponíveis no Power BI. 

Dada essa quantidade de funções, é compreensível que ao iniciar nossa jornada não saibamos como utilizar uma boa parte delas. Nesta aula vamos passar pelos principais conceitos da linguagem e, se puder deixar uma dica: aprenda como DAX funciona e a medida que novos desafios surgirem, você saberá buscar por novas soluções. No material complementar deixarei dois sites que vão lhe ajudar nesta jornada de conhecer as funções e suas aplicações, não deixe de conferir. Agora que entendemos o que é o DAX, vamos entender para que exatamente utilizamos ele. A linguagem DAX é essencial para os analistas que trabalham com Power BI, uma vez que ela é utilizada para criar medidas, colunas calculadas, tabelas calculadas e também nas queries de segurança a nível de linhas - o RLS. E, quando falamos em medidas e colunas calculadas, é comum que algumas dúvidas apareçam. Normalmente surgem questionamentos como: Qual a melhor opção? Quando devo criar uma coluna e quando devo criar uma medida? 

Em geral, as medidas são cálculos mais dinâmicos e que dependem do contexto de filtro para gerar resultados, ou seja, elas só ganham contexto ao serem inseridas em um visual. As medidas não ocupam espaço físico 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

41 

no modelo semântico porque só são processadas quando estão sendo utilizadas em visualizações. 

Já as colunas calculadas e também as tabelas calculadas são estáticas e calculadas a nível de linha. Por serem parte de uma tabela, elas são armazenadas no modelo de dados, ou seja, o fato de elas existirem no modelo, elas pesam no arquivo final. Quando adicionamos uma coluna calculada em um modelo em que a tabela possui modo de armazenamento Importar, a fórmula é avaliada quando o modelo semântico é atualizado e aumenta o tamanho do armazenamento do seu modelo. Quando adicionada a uma tabela de modo de armazenamento DirectQuery, a fórmula é avaliada pelo banco de dados de origem subjacente quando a tabela é consultada. 

É comum utilizarmos colunas calculadas quando queremos classificar ou categorizar algum dado, como por exemplo, definir que um cliente está na categoria gold do Banvic pois seu saldo ultrapassa um limite pré-determinado. 

Dadas algumas exceções, optamos por não criar colunas ou tabelas calculadas no Power BI, deixando isso para a etapa de transformação. Lembra daquela frase sobre a importância dos dados estarem transformados o mais próximo da fonte possível e o mais perto da visualização quanto necessário? Aqui usaremos essa máxima. Não queremos transformar, nem criar colunas na camada de BI, apenas se for estritamente necessário. 

As medidas não fazem parte desta lógica. Por agregar e cruzar informações de tabelas distintas, a criação de medidas no Power BI é uma boa prática se quisermos relatórios completos e cheios de insights valiosos.  No Power BI existem dois tipos de medidas: as implícitas e as explícitas. As medidas implícitas são aplicadas diretamente nas colunas quando utilizadas em visuais. São aquelas opções que aparecem quando adicionamos um campo a ser agrupado em um visual, como contagem, soma, mínimo, máximo e assim por diante. Já as medidas explícitas são os cálculos de modelo escritos em DAX que comumente são chamados de medidas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

42 

Vamos para o nosso arquivo do BanVic, para vermos na prática como se dá a criação das medidas DAX? 

Com o nosso relatório aberto, vamos inicialmente organizar onde as medidas serão criadas. Lembrando que elas não ocupam espaço físico no modelo, mas, como uma medida pode referenciar mais de uma tabela, o lugar ideal é que elas estejam todas em um local único, para facilitar a organização de quem irá utilizar esse modelo depois. Para isso vamos criar uma tabela virtual. 

Estamos na parte de Exibição de Modelo do Power BI e vamos à Modelagem > Nova tabela. Vamos chamar essa tabela de Medidas. O importante aqui é não deixar o nome dela como “Tabela”, pois se for esse o caso, ela não será criada. 



<!-- Start of picture text -->
Arquivo Pagina Inicial Inserir Modelagem Exibigaéo Otimizar Ajuda Ferramentas externas. Ferramentas da tabela<br>By i; Ba BB A 6B AM Td RA<br>Gerencar Nova Medida Nova. Nova Novo Gerencar Exbir Configragdo<br>relagdes medida rdpida coluna Atabela parametrov  fungdes como R dePe Idioma¥  linguistco_Esquema<br>cos<br>fetes v<br>eaigas =<br>| aX caerscs —_—_anctearpigna_rrimeros_|__ Sepa per<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Pronto, agora temos na parte de Dados uma nova tabela, virtual, chamada Medidas. E todas as medidas que criarmos a partir de agora ficarão nesse local. 



<!-- Start of picture text -->
Dados oc0 >)<br>Q Pesquisar<br>>  dim_agencias<br>> @ dim clientes<br>> B dim_datas<br>> ® fact_transacoes<br>| > & Medidas<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

43 

Antes de escrever nossa primeira medida, vamos entender um pouco melhor sobre as funções utilizadas. Para ela escolhi duas funções: Calculate e Filter. 

A função Calculate é uma das mais importantes e flexíveis em DAX. Ela tem a capacidade de criar novos contextos a uma medida, a partir de filtros adicionados a ela. 

A função Filter cria uma nova tabela, filtrada, a partir de condições específicas para retornar linhas que atendam a um determinado critério. 

Vamos usar a função Calculate para filtrar cenários mais simples e quando queremos ou precisamos de cenários mais complexos, utilizaremos a função Filter combinada. Vamos ver na prática como isso funciona? 

Com nosso Power BI aberto, vamos primeiro entender nosso dado. Ao final desta etapa queremos uma medida que nos traga a quantidade de transações que aconteceram via Pix no banco em um período específico. E antes de irmos ao DAX, vamos entender o que precisamos para criá-lo. Para isso, vamos criar uma visualização de tabela com a coluna nome_transacao e contagem distinta de cod_transacao da tabela Fato Transações. Ao adicionar as duas colunas na visualização, precisamos mudar a medida implícita de “soma” para “contagem distinta” na coluna do codigo da transação, assim, teremos quantas transações de cada tipo ocorreram no banco. Por aqui, vemos 13.164 para Pix - Realizado, 5.131 para Pix - Recebido e 90 para Pix Saque. Então, nossa medida do Calculate precisa ter o somatório destes três valores, 18.388 transações. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

44 



<!-- Start of picture text -->
1 supestes<br>PME MEMe<br>S| hes RA Be Me be bl Let<br>QOHGBYAa<br>{10 9| nome transacao °Contagem de cod_transacaoVB“,. OBSF@FaPRasREE er Py<br>A | Compra crédito 24977 RWeD-<br>Compra Débito 17662 Colunas<br>Depésito em espécie 4866 f = = = -<br>° Estorno de Debito 403 |? ——_ Bails<br>Pagamento de boeto 52 ——— |<br>‘Pix-Realizado13104<br>(Pix-Recebido81384<br>(i Sq SO<br>é Total ° 71999 6<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Para criar uma nova medida, deixe selecionada a nova tabela virtual “Medidas” e, em Modelagem clique em Nova medida. 

O nome da nossa medida será Transacoes_PIX. Ela precisa ser clara e direta, além de manter a mesma lógica por todas as demais medidas do modelo, no nosso caso, com nomenclatura em português, primeira letra maiúscula e separando as palavras com um underline. 

Após a escolha do nome, clique shift + enter para pular uma linha e idente com um parágrafo para organizar a medida. Esta etapa é opcional, mas sempre preze por ter um código legível, isso facilitará a sua vida no futuro. 

Agora, escrevemos CALCULATE e observe que ao escrever, já temos uma orientação de como devemos utilizá-lo no modelo. Todas as funções apresentam esse “How to”, que nos auxilia muito no processo. 



<!-- Start of picture text -->
J: CALCULATE(Expressao, [Filtrar1],: ...)<br>Avalia um expressao em um contexto modificado por<br>' filtros.<br>CALCULATE(<br><!-- End of picture text -->

Fonte: Própria autora (2024). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

45 

Seguindo esta lógica, a expressão que vamos utilizar aqui é a contagem distinta da coluna cod_transacao, então utilizaremos a função DISTINCTCOUNT, abriremos parênteses e na próxima linha, com nova identação adicionamos a coluna cod_transacao. Fechamos parênteses para fechar esta etapa da contagem distinta e pulando para nova linha, com uma identação a menos, voltamos à função CALCULATE, mas agora na segunda etapa, de filtrar a expressão. Aqui, escolhemos a coluna nome_transacao da mesma tabela fato e adicionaremos aquelas três categorias que exemplificam as transações PIX: Pix Realizado, Recebido e Saque. Como são três, utilizaremos o operador lógico IN, que cria uma lista a partir das chaves adicionadas após sua chamada. Com isso, finalizamos a função CALCULATE, indo para a próxima linha e fechando o parênteses aberto a linha dois. 

Transacoes_PIX = 

CALCULATE( DISTINCTCOUNT( 

fact_transacoes[cod_transacao]) 

, fact_transacoes[nome_transacao] IN {"Pix - Realizado", "Pix - Recebido", "Pix Saque"} ) 



Adicionando o produto desta função DAX em um card, temos o valor de 18 mil. Ainda podemos melhorar sua legibilidade exclusivamente ao visual do card, podemos ir em Formato > Visual > Valor do balão e, em “Exibir Unidades” selecionar a opção nenhum. Assim, conseguimos ver o valor completo de 18388. Podemos melhorar ainda mais, adicionando o ponto do milhar à nova medida. 

Agora podemos modificar a medida usando FILTER. Vamos dizer que queremos na verdade saber o volume das transações PIX no ano de 2021. Para isso, vamos filtrar a nossa função CALCULATE para este período também. Para isso, vamos copiar a medida anterior e criar uma nova, Trnsacoes_PIX_2021, e vamos adicionar uma nova etapa de filtro na função, logo após aquela que chamamos a lista de nome_transacao, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

46 

com FILTER. FILTER pede para adicionarmos uma tabela e depois a coluna e o filtro esperado. Isso porque esta função cria uma tabela filtrada e a partir dela que o cálculo acontece. Aqui, vamos chamar a nossa dimensão de datas e a coluna ano = 2021. 

Transacoes_PIX = CALCULATE( DISTINCTCOUNT( fact_transacoes[cod_transacao]) , fact_transacoes[nome_transacao] IN {"Pix - Realizado", "Pix - Recebido", "Pix Saque"} , FILTER( dim_datas , dim_datas[ano] = 2021 ) ) 

Visualizando o nosso card, podemos ver que agora temos 3.151 transações PIX no ano de 2021. 

Agora, vamos ver mais duas funções importantes e que com certeza estarão presentes em seu dia a dia. As funções DIVIDE e as variáveis. 

Iniciamos pela função DIVIDE. Divisões no Power BI podem ser feitas utilizando a tradicional barra (/), no entanto, é mais comum e recomendável o uso da função DIVIDE(). A razão é que, além de melhor leitura, a função lida com o erro de modo automático quando o denominador é zero. 

As variáveis são fundamentais para o desenvolvimento de medidas organizadas e mais complexas no Power BI. É comum que uma medida seja construída a partir do cálculo de outras medidas. Se essas métricas intermediárias não forem usadas em nenhum outro lugar senão uma medida específica, deve-se considerar a utilização de variáveis. O uso de variáveis evita a criação desnecessária de medidas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

47 

Vamos entender um pouco melhor sobre essas três características da utilização de variáveis: 

Melhora de desempenho: como nós referenciamos uma fórmula já criada, o Power BI não precisa calcular duas vezes a mesma medida. E é isso que iremos fazer nessa nossa medida de porcentagem de propostas aprovadas. 

Melhora a legibilidade: ao invés de termos linhas e mais linhas de código, podemos apenas chamar a nossa medida de forma clara. 

Simplifica a depuração: Se for preciso entender o que está dando errado na nossa medida, fica muito mais simples analisar quando já temos ela de forma estruturada, podemos verificar os resultados de cada variável para saber onde está o erro. 

Vamos a um exemplo utilizando DIVIDE e variáveis? 

Voltando ao nosso arquivo do Power BI, vamos fazer o seguinte exercício: queremos saber qual o percentual transacionado que a Agência Digital tem em relação a toda a operação. 

Para isso vamos começar criando uma tabela com a coluna Nome da Agência da dimensão de agências e Soma de valor_transacao, da tabela fato. Aqui já vemos que a agência digital tem um percentual alto em relação às demais, já que ela é a única agência que passa de 10 milhões em valor. Mas, para termos certeza disso, vamos ao cálculo. 

Iniciamos com o nome, seguindo a mesma lógica dos anteriores. E, após o shift+enter, vamos adicionar o código VAR que significa variável. A primeira variável vai ser sobre o total de transações, então será um simples somatório do valor_transacao, a partir da função SUM. 

A segunda variável será sobre as transações digitais, então vamos voltar para a nossa função CALCULATE, já que queremos fazer o mesmo SUM da 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

48 

variável anterior, mas modificando o filtro para termos apenas a agência digital sendo contabilizada. 

Agora que já criamos as duas variáveis, precisamos calcular quanto a Transacoes_Digital é em relação ao seu todo, a variável Tarnsacoes_ALL. Para isso, vamos usar a última etapa do uso de variáveis, a função RETURN. Sempre que usamos VAR, usamos RETURN para finalizar e retornar o cálculo final com base nas variáveis anteriores. Para isso, em nosso RETURN, utilizaremos a função DIVIDE. Aquela que acabamos de ver que é usada para dividir valores de forma mais segura no Power BI. Em DIVIDE usaremos Transacoes_Digital como numerador e Transacoes_ALL como demoninador. 

O resultado final deste cálculo é um percentual, então, com a medida selecionada em Dados, vamos “Ferramentas de Medida” e, em Formatação, adicionaremos o símbolo de Percentual. 

Transacoes_Digital = VAR Transacoes_ALL = SUM(fact_transacoes[valor_transacao]) 

VAR Transacoes_Digital = CALCULATE( SUM(fact_transacoes[valor_transacao]) , dim_agencias[Nome da Agência] = "Agência Digital" ) RETURN DIVIDE( Transacoes_Digital , Transacoes_ALL ) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

49 

Agora, adicionando esta medida em um card, vemos que as transações digitais constituem 45,05% do total de valor transacionado pelo BanVic. 

Para deixar essa medida com todas as informações necessárias, podemos documentá-la. Assim, quando outras pessoas utilizarem seu relatório, elas também entenderão o cálculo que está por trás daqueles valores. 

Para isso vamos à Exibição do modelo e, selecionando uma das medidas que criamos, em Propriedades > Descrição. Aqui iremos adicionar o seguinte texto “Medida traz o percentual de transações PIX sob todo o somatório de transações do BanVic”. Agora, quando passamos o mouse em cima da medida, temos a lógica por trás de sua criação. Tudo isso auxilia muito a sua utilização em relatórios futuros. 

Até agora vimos algumas funções em DAX muito importantes. Mas como comentei no início desta aula, existem mais de 200 funções disponíveis! É muita coisa, né? Então, agora vamos ver as principais classificações de funções que com certeza vão te ajudar a entender as possibilidades que DAX nos dá no dia a dia. 

Funções de Agregação: são as funções básicas, aquelas usadas desde as medidas implícitas até as mais complexas. Essas funções calculam contagem, soma, média, mínimo ou máximo para todas as linhas em uma coluna ou tabela, conforme definido pela expressão. 

Funções de Data e hora: Essas manipulam e calculam datas e horas, ou seja, com base em uma data essas funções auxiliam na criação de colunas como dia, diferença entre dias, meses, anos, horas, etc. 

Funções de inteligência de dados temporais: Com base em colunas de data ou data e hora, ou ainda em colunas criadas pela função anterior, as medidas de inteligência temporal são usadas para manipular dados, criar e comparar cálculos temporais. São funções especializadas em cálculos de análise de tempo. Aqui vamos ter medidas como firstdate, previousyear, sameperiodolastyear, etc. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

50 

Funções lógicas: estas retornam informações sobre os valores a partir de uma condicionante, ou seja, executam uma operação lógica. Se assemelha à ideia do case-when que usamos no SQL. Existem algumas mas as principais são as declarações IF que seleciona uma saída a partir de uma condicional e SWITCH, que é utilizada quando temos mais que duas condicionais. 

Funções de relação: estas gerenciam a relação entre tabelas, para além do relacionamento feito a nível de camada semântica. Elas buscam e manipulam dados de tabelas relacionadas. As principais funções são a USERELATIONSHIP que ativa a relação entre duas tabelas e partir de colunas especificadas na função e a CROSSFILTER, que muda a direção do filtro cruzado entre duas tabelas. 

Funções iteradoras: Essas funções, também chamadas de função “X”, fazem com que medidas se comportem como colunas convencionais. As funções iterantes ou iteradoras diferem das funções agregadoras por operarem a nível de linha e coluna, enquanto as funções agregadoras operam apenas ao nível da coluna. São exemplos de funções iteradoras: SUMX, MINX, MAXX, AVERAGEX, COUNTX, RANKX. 

Essas são as principais classificações de funções DAX que temos. O importante é conhecê-las e sempre que puder, utilizá-las, adicionando mais ao seu repertório. Nesta aula vimos como o DAX funciona na prática e como esta linguagem eleva o nível dos relatórios no Power BI. Na próxima aula iremos criar o nosso relatório. Vejo você lá! 

Material Complementar 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** The DAX Guide 

**Descrição:** Link de um glossário sobre funções DAX. **Link:** <u>https://dax.guide/</u> 

**Tipo** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** DAX function reference 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

51 

**Descrição:** Link de um glossário sobre funções DAX, da Microsoft. **Link:** <u>https://learn.microsoft.com/en-us/dax/dax-function-reference</u> 

**Tipo** ☐ Site ☐ Livro ☐ Vídeo   x Leitura ☐ Filme ☐ Visite **Título:** Lista de relacionamentos para o arquivo base no Power BI **Descrição:** Lista de relacionamentos para o arquivo base no Power BI 

**Link:** <u>[FADA] [Módulo 6] [Aula 07] Material Complementar</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

52 

### **Aula 08: Criação de relatórios** 

Na aula de hoje vamos construir nosso relatório de transações. A base deste relatório é o mock-up criado no módulo anterior. E nosso objetivo é criar as visualizações no Power BI, utilizando o fundo que foi exportado lá. Se você precisar deste fundo, ele está no material complementar desta aula. 

Para iniciar, vamos escolher um estilo que vai combinar com o fundo que vamos colocar no nosso dash. Para isso, vamos à Exibição e, em Temas, vamos escolher “Storm”. Agora, vamos fazer o upload do fundo no nosso arquivo do Power BI, onde os dados do BanVic estão. Para isso vamos adicionar a tela de fundo. Para isso, vamos selecionar Tela de Fundo e, em procurar, vamos fazer upload do arquivo svg do mock. É preciso deixar a transparência em 0% também e o Ajuste da Imagem na opção Ajuste. Vamos fazer isso para as duas páginas criadas: Visão Geral e Tipos de transação. 

Para fazer isso na segunda página, vamos criar uma nova página e repetir o processo de adicionar a tela de fundo, agora da página de tipos de transação, e ajustar a imagem e a transparência. 

Com a Tela de Fundo em seu devido lugar, vamos voltar à primeira página e entender a estrutura do nosso painel. Na primeira parte do nosso dash teremos as informações iniciais, como a logo do BanVic, o título do dashboard, para situar o usuário sobre a temática desta página, bem como a última data que temos de dados. A logo e os títulos trouxemos do Figma e a última data de transferência, vamos adicionar um card com a medida implícita de último valor da coluna data_transacao, da tabela fato. 

A segunda parte refere-se aos filtros. Os filtros são importantes para criarmos a interação inicial do dashboard. A partir deles, os usuários podem personalizar a visualização para períodos e categorias específicas. Para adicionar, vamos clicar no visual de segmentação de dados e 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

53 

selecionar a coluna de interesse. No nosso exemplo, vamos pensar em como o nosso usuário pode usar os filtros: 

- Data: é recomendável iniciar com um filtro de data, para navegarmos por diversos períodos na análise. Esse é praticamente um filtro padrão, presente em quase toda solução de dashboard. 

- Nome da Agência: podemos filtrar por agência para verificar como cada uma das agências está performando em relação às transferências. Também, podemos ter gestores que trabalham para mais de uma agência querendo verificar os números de forma separada. 

- Nome do Cliente: podemos analisar o perfil de um cliente em relação às suas transações, para que possamos oferecer um cartão de crédito novo, por exemplo. 

- Tipo de transação: podemos ver todo o dashboard a partir da perspectiva de um ou um grupo de transações. 

Também vamos criar na seção de filtros o botão acionável para limpar filtros, que já foi pensado na etapa de mockup. Para isso, vamos em Inserir > Botões > Limpar todas as segmentações e, com ele na tela, vamos editar para tirar bordas e textos, já que seu design foi previamente desenhado. Ainda na aba de Formatar, conseguimos ver que a ação que este botão tem é de limpar as segmentações do painel. Essa é uma ótima prática para que sempre que seu usuário possa estar perdido em relação ao que está vendo na tela, ele tenha um ponto de partida para voltar. 

A terceira parte refere-se aos Indicadores. Os indicadores são os primeiros e muitas vezes os mais importantes gráficos de um dashboard. Porque é a partir deles que vamos iniciar a nossa narrativa com os dados. Precisamos escolher aqueles indicadores que terão um efeito automático sobre o leitor, engajando-o na leitura do restante dos gráficos. 

Pensando em um painel sobre transferências, a escolha para esse nosso dashboard foi de apresentar o total transacionado a partir da soma do valor_transacao, a quantidade de transações a partir da contagem distinta do cod_transacao, a média do valor transacionado com a média do valor_transacao e o percentual de transações digitais, a partir da 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

54 

medida que criamos na aula sobre DAX. Tirando esta última, as primeiras três medidas são implícitas, utilizando apenas as opções dadas pela ferramenta: soma, contagem distinta e média. 

Com os nossos indicadores principais no nosso dashboard, vamos pensar em uma análise temporal. Assim como vimos em aulas anteriores, a melhor opção de elemento gráfico para esse tipo de análise é o gráfico de linhas, porque nos dá a visão de continuidade sobre uma série. Para o nosso exemplo, vamos escolher o valor de transação por ano. Com isso teremos uma evolução sobre essa medida. Pensando nas melhores práticas de dataviz, vamos limpar um pouco esta visualização, deixando tanto no eixo X e Y apenas os valores dos eixos, mas não seus títulos, porque isso já está presente no título. E, por se tratar de um gráfico de linhas, não precisamos ter os valores junto dos rótulos, apenas nos eixos. 

E, para finalizar, vamos adicionar uma matriz. Esta matriz irá detalhar os nossos dados na visão de agência e responder algumas questões que podem ficar apenas visualizando os demais gráficos. Nesta visualização vamos adicionar a coluna de estados, UF e a coluna de Nome da Agência nas Linhas e em Valores vamos adicionar o somatório do valor de transação e a média deste valor. Vamos adicionar também a quantidade de transação e, com base na medida que criamos na aula de DAX, vamos adicionar a quantidade de transação para PIX, TED, DOC e Outros. No material complementar desta aula, adicionei as fórmulas para as medidas utilizadas. Para finalizar, vamos adicionar a última data que teve uma transação para cada agência. 

Agora vamos à nossa segunda página. Este será um detalhamento com dois gráficos de barra: uma contagem distinta de transação por tipo de transação e a soma do valor transacionado também pelo tipo de transação. Estes dois gráficos de barra horizontal nos dão essa ideia de ranking em relação às medidas adicionadas. Aqui, iremos manter os valores nos rótulos, mas vamos tirar todos os títulos de eixo e valor no eixo X, deixando apenas os valores no eixo Y, para identificar o tipo de transação. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

55 

Para finalizar esta página, vamos voltar a anterior e copiar filtros e última data de atualização. Assim as duas páginas estão sincronizadas. 

Vamos, por fim, criar a navegação entre elas. Para isso, na página de visão geral vamos criar um botão em branco onde a ação será Navegação de Página, que irá para a página de Tipo de transação e faremos o mesmo caminho inverso. 

E assim temos um painel sobre transações concluído. A partir daqui o analista de dados pode usar sua criatividade para aumentar e melhorar os gráficos, a fim de tirarmos insights valiosos para o usuário final. Espero que tenha gostado desta aula e vejo você na próxima! 

#### Material Complementar 

**Tipo** ☐ Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme   X Arquivo 

**Título:** Arquivo background Power BI .svg 

**Descrição:** Arquivo de background criado no Figma **Link:** <u>[FADA] [Módulo 6] [Aula 8] Material complementar</u> 

**Tipo** ☐ Site ☐ Livro ☐ Vídeo   x Leitura ☐ Filme ☐ Visite 

**Título:** Lista de relacionamentos para o arquivo base no Power BI 

**Descrição:** Lista de relacionamentos para o arquivo base no Power BI 

**Link:** <u>[FADA] [Módulo 6] [Aula 08] Material Complementar</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

56 

### **Aula 09: Otimização de modelos no Power BI** 

Olá, analista! Chegamos a última aula do nosso módulo Criando dashboards com Power BI. Até aqui vimos muitos pontos relacionados à ferramenta de BI, além de todas as etapas relacionadas à elaboração de dashboards. Nesta aula nós vamos ver como otimizar os modelos que são criados na ferramenta. 

Como profissionais de dados devemos sempre buscar trabalhar de forma otimizada em nossos produtos. E é cada vez mais comum termos modelos semânticos maiores e mais pesados e, com isso, começamos a nos deparar com problemas de desempenho e até mesmo entraves na hora de publicar e atualizar os arquivos. 

Quando trabalhamos com modelos semânticos menores, contamos com arquivos que usam menos memória e possuem maior rapidez na atualização e utilização. Existe uma sequência de procedimentos que podem ser executados para que os modelos do Power BI não tenham problemas de desempenho ou atualização. 

Vamos iniciar pelas premissas fundamentais. A primeira é sobre o uso do Star Schema, que já vimos em outras aulas. A Microsoft define este esquema como altamente relevante para o desenvolvimento de modelos no Power BI otimizados para desempenho e usabilidade. E isso está ligado principalmente à cardinalidade das tabelas, que, quando utilizadas em 1:muitos, performam melhor. 

Outra premissa fundamental encontra-se em analisar medidas e visuais. Queremos manter um modelo semântico simples, mas é possível que ele se torne complexo com o tempo. Analisar as medidas, os relacionamentos e os visuais é imprescindível se você deseja um modelo com bom desempenho. Para isso, pode-se utilizar o Performance Analyzer, no Power BI Desktop. E, com a análise realizada, existem duas possibilidades de melhorias: nos visuais e nas consultas DAX. 

Em relação aos visuais, é uma boa prática não criar de forma demasiada os elementos na própria ferramenta de BI. É interessante que de forma 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

57 

majoritária eles sejam construídos em outras ferramentas, como o Figma, uma vez que quando  levada ao dashboard, todas as camadas criadas na imagem estejam apenas um único arquivo. Além destes, existem os gráficos criados no dashboard. Preocupe-se em ter menos visuais em suas páginas. Considere se um visual é realmente necessário e se ele agrega valor para o usuário final. Se a resposta for não, você deverá remover esse visual. Em vez de usar vários visuais na página, leve em consideração outras maneiras de dar detalhes adicionais, como páginas detalhadas e dicas de ferramenta da página do relatório. 

Em relação às consultas DAX, tenha em mente que uma consulta não deve levar mais que 0,12 segundos para ser calculada em seu dashboard. Se estiver com valores acima deste teto, procure formas de otimizar seus cálculos. 

Outra premissa é retirar o recurso de data e hora automática. Por padrão este recurso é habilitado globalmente, o que significa que o Power BI Desktop cria automaticamente uma tabela calculada oculta para cada coluna de data, desde que determinadas condições sejam atendidas. As novas tabelas ocultas vão além das tabelas que você já tem no modelo semântico. 

Você deve diminuir ao máximo as tabelas e colunas calculadas. Já comentamos outras vezes mas é importante lembrar aqui. Não é recomendada a criação de tabelas e colunas calculadas na ferramenta de BI. Se existir uma lógica a ser aplicada neste nível, lembre-se que normalmente é possível e melhor se levar para as etapas anteriores à transformação. Diferente das medidas em DAX, tabelas e colunas calculadas ocupam espaço na memória do arquivo pbix e influenciam no seu desempenho. 

Partindo para as estratégias de diminuir a quantidade de dados nas tabelas temos a filtragem vertical. Esta refere-se a retirada de colunas desnecessárias do modelo. É importante que desde o início do desenvolvimento de um dashboard seja levada em consideração a importação apenas das colunas necessárias.Para evitar excluir colunas no Editor do Power Query, você deve tentar resolvê-las na origem ao carregar 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

58 

dados no Power BI Desktop. Considere se você realmente precisa de cada coluna e tente identificar o benefício que cada uma adiciona ao modelo semântico. Se achar que uma coluna não agrega valor, você deverá removê-la do modelo semântico. 

A filtragem horizontal consiste em retirar as linhas que não são necessárias no modelo. As tabelas do modelo devem ser carregadas com o menor número de linhas possível. Podemos filtrar as informações por uma dimensão ou por tempo. A filtragem por tempo envolve limitar a quantidade de histórico de dados carregado em tabelas de fato. Não carregue automaticamente todo o histórico disponível, a menos que seja um requisito de relatório conhecido. 

Entre os procedimentos de diminuição de dados, agrupar e resumir é o que possui maior impacto. Por muitas vezes o Data Warehouse apresenta informações em tabelas fato que não necessariamente serão utilizados na mesma granularidade na visualização. Portanto, a redução da granularidade das tabelas em agregações pode ser útil em muitos momentos. Porém, é importante destacar que este procedimento leva a perda de alguns detalhamentos. 



Todas as soluções propostas até então são utilizadas em modelos semânticos que possuem os dados importados para a memória do arquivo. Se nenhuma solução apresentada até aqui for suficiente, surge a possibilidade de trocar a conexão para Direct Query. O Direct Query responde ao problema de tamanho do modelo, mas em contrapartida diminui o desempenho do modelo. Nesse cenário os modelos contêm apenas os metadados que definem a estrutura e não uma cópia dos dados, como vimos anteriormente. Neste formato, todos os dados permanecem no data warehouse e, a cada consulta, troca de filtro, cruzamento de informações, uma nova query é gerada ao data warehouse, que devolve ao relatório novos dados. 

Nesta aula aprendemos algumas técnicas importantes para otimizar nossos modelos de dados no Power BI. Espero que tenha gostado de tudo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

59 

que vimos até aqui e que as aulas tenham te ajudado na jornada da análise de dados. Nos vemos em breve! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

60 

