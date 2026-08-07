

# Material Teórico 

Curso: Formação em Análise de Dados 

Autoria 

Prof. Msc. Daniel Avancini Prof. Msc. Renata Assunção 

Módulo 

Módulo VII - **Estatística aplicada à análise de dados** 

## Temas abordados 

- Análise descritiva 

- Medidas de tendência central e dispersão 

- Histograma e demais gráficos 

- Amostra 

- Distribuições e estatística inferencial 

- Experimento e teste de hipóteses 

## Objetivos de Aprendizagem 

Ao final deste módulo, você será capaz de: 

1. Compreender a importância da **análise descritiva** para conhecer e explorar o conjunto de dados. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

1 

2. Utilizar adequadamente as **medidas de tendência central e dispersão** para analisar o comportamento dos dados. 

3. Identificar o **tipo de gráfico** mais adequado para comunicar diferentes tipos de resultados. 

4. Reconhecer a importância das **amostras** de dados e como elas são usadas nas análises. 

5. Entender as **distribuições de dados** e aplicar **estatísticas inferenciais** para fazer previsões e inferências sobre populações com base em amostras. 

6. Conduzir **experimentos** e realizar **testes de hipóteses** para validar suposições e obter conclusões fundamentadas a partir dos dados amostrais. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

2 

Apresentação do Módulo 

Olá, Aluno! Seja muito bem-vindo ao módulo de estatística aplicada à análise de dados. 

Antes de mais nada, vou me apresentar. 

Eu me chamo Renata e serei sua professora neste módulo. Sou oceanógrafa de formação e tenho mestrado em pesca e aquicultura onde trabalhei com o desenvolvimento de modelos de dados para descrever informações sobre um tipo específico de pescaria. Atuo como tech lead no time de Data Analytics da Indicium. Quero mostrar para você que a estatística é uma das ferramentas mais poderosas para o profissional de dados. 

Até o momento tivemos uma introdução à análise de dados, aprendemos a usar SQL para fazer consultas em um banco de dados e nos data warehouses e vimos como criar uma boa história para apresentar os resultados encontrados nas nossas análises. 

Neste módulo vamos ver os principais conceitos de Estatística aplicada a Análise de Dados. 

Veremos como utilizar técnicas estatísticas como a Análise Descritiva, Medidas Resumo e Gráficos para realizar a Análise Exploratória de dados. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

3 

Também faremos uma introdução à teoria da probabilidade, essencial para o entendimento dos fenômenos aleatórios. Você já se perguntou de onde vem a tão famosa distribuição normal? 

Na terceira e última parte do módulo, aprenderemos sobre as principais técnicas de inferência estatística. São elas que nos permitem responder perguntas de negócio com precisão mesmo utilizando pequenas amostras de dados e extrapolar nossas conclusões para conjuntos de dados muito maiores. 

Aproveite as atividades disponibilizadas ao longo do curso para testar seu conhecimento e aprender um pouco mais sobre o assunto. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

4 

## Introdução 

### 0.1 Introdução ao Módulo 

#### **O que é a estatística** 

Nunca foi tão fácil coletar e analisar dados. As tecnologias de Big Data e da computação em nuvem processam bilhões de pontos a cada segundo. Mas será que nossa tomada de decisão está melhor hoje do que no passado? Imersos em um oceano de informação, conseguimos extrair o verdadeiro _insight_ que nos permitirá ganhar uma vantagem sobre nossos concorrentes? 

Curiosamente, a principal ferramenta que nos permite gerar conhecimento a partir dos dados não surgiu com o smartphone ou mesmo com a computação. Na verdade, essa ferramenta já existe há séculos e tem sua origem em um problema muito mais mundano: os jogos de azar. Seu nome: Estatística. 

A estatística é o elo entre o rigor da matemática e a complexidade do mundo real. Do estudo da eficácia de vacinas e pesquisas eleitorais aos novíssimos modelos da IA Generativa, as técnicas estatísticas são a base da nossa capacidade de não apenas descrever o “que foi”, mas prever o “que será” e o “que poderia ter sido”. 

#### **Porque a estatística é importante** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

5 

Enquanto não seria exagerado dizer que a estatística é a pedra fundamental da ciência aplicada, seu uso nos ambientes de negócio ainda é pouco difundido. No entanto, a popularização de técnicas de construção de experimentos, modelos de inteligência artificial etc. fazem com que o domínio dos fundamentos da estatística seja uma necessidade do profissional de dados moderno. 

#### **Aleatoriedade à nossa volta** 

Um ponto central da estatística é de que sempre existe algum grau de incerteza na variação em um conjunto de dados. Seja em um jogo de dados ou em um modelo de risco de crédito, não temos como afirmar com exatidão o resultado de cada lançamento de dado ou se nosso cliente se tornará ou não inadimplente. No entanto, com um número suficiente de repetições, ou “dados”, é possível calcular a probabilidade de cada resultado. Desta forma conseguimos “quantificar” a incerteza. 

Este resultado decorre da chamada _Lei dos Grandes Números_ , um dos resultados mais poderosos da estatística. É essa lei que garante que um Cassino nunca perderá dinheiro no agregado, mesmo que possa perder um jogo aqui e ali. É também a base dos modelos atuariais utilizados pelas seguradoras e por modelos de risco de crédito dos bancos. 

#### **Como pensar de forma probabilística** 

A Lei dos Grandes Números não garante que uma pequena amostra de dados coincida com o resultado esperado. Infelizmente, em muitos casos reais não podemos nos dar ao luxo de “pagar para ver” enquanto a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

6 

estatística faz o seu trabalho. Por isso, precisamos entender como a inferência estatística nos permite interpretar resultados de pequenas amostras de dados para responder perguntas sobre o todo. 

Precisamos, sobretudo, aprender a pensar de forma probabilística. Entender que quando levamos em conta a incerteza, 2+2 _nem sempre_ será 4. Que os bons resultados de uma ação de marketing podem ter sido apenas obra do acaso e provavelmente não irão se repetir futuramente. Uma afirmação precisa estar acompanhada com uma medida da confiança que temos nela. 

#### **Precisão vs Acurácia** 

“ _It is easy to lie with statistics, but easier to lie without them._ “ Frederick Mosteller 

Infelizmente, é fácil mentir com estatística. Se bem utilizada, a estatística é uma das alavancas mais poderosas já desenvolvidas pelos seres humanos. No entanto, seu bom uso depende de um entendimento de suas limitações e premissas. Em especial, a estatística é apenas uma ferramenta e precisa ser acompanhada de um conhecimento científico ou de negócio que a sustente. 

Quando calculamos uma distribuição de probabilidade ou rodamos um modelo de regressão, sempre obteremos _algum_ resultado matemático. Mesmo que ele não faça sentido algum! Pior, nós humanos temos uma tendência de acreditar em números supostamente precisos, nos levando a tomar decisões ainda mais equivocadas do que não utilizar dado 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

7 

algum. Por isso, é importante entender que: _precisão_ não significa _acurácia_ . 

Vou dar um exemplo que se tornará mais claro ao longo deste curso. A distribuição normal de probabilidade, a famosa curva de sino, é provavelmente a mais popular distribuição de probabilidade. É muito comum encontrar estimativas de probabilidade e testes de hipóteses utilizando a distribuição normal em artigos científicos, análises financeiras, modelos de aprendizado de máquina etc. Mas e se as condições para normalidade dos dados não forem satisfeitas? Bom, aí essas estatísticas, ainda que _precisas,_ estarão totalmente erradas! 

#### **Sobre o uso de fórmulas e letras gregas** 

A estatística é parte da matemática e possui uma série de convenções e símbolos. Você provavelmente não precisará lembrá-los ou utilizá-los no dia-a-dia mas eles são úteis para entendimento das equações e leitura de resultados. Tentaremos usá-los somente quando for necessário. 

#### **Pacotes estatísticos e exemplos em python** 

Durante séculos, os estatísticos precisaram usar apenas papel e caneta para realizarem os cálculos complexos que geraram as populares distribuições de probabilidade utilizadas até hoje. Para nossa sorte, hoje qualquer computador pessoal ou mesmo um celular consegue executar cálculos estatísticos avançados. 

Existem dezenas de softwares estatísticos especializados como SAS, SPSS, Stata etc. e pacotes em linguagens de programação como R e Python. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

8 

Neste curso tentaremos mostrar exemplos de cada conceito apresentado utilizando a linguagem Python de forma intuitiva para você poder aplicar os tópicos no seu dia-a-dia. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

9 

## Desenvolvimento 

## Parte 1: Análise Exploratória de Dados 

### Aula 1.1: Análise descritiva 

A análise descritiva, como o nome indica, consiste em descrever as principais tendências nos dados. Este método é baseado em uma ou várias questões de pesquisa e não tem hipótese. O foco da análise descritiva é compreender se, por trás de um ou mais fenômenos que se repetem, existem tendências ou padrões que possam ser mapeados. 

Uma análise descritiva básica envolve o cálculo de medidas simples de composição e distribuição de variáveis. Dependendo do tipo de dados, podem ser proporções, taxas ou médias. Além disso, quando necessário, como no caso de pesquisas por amostragem, medidas de associação entre variáveis podem ser usadas para decidir se as diferenças observadas entre os grupos são estatisticamente significativas ou não. 

De forma mais teórica a análise descritiva é uma área da estatística que lida com a descrição e o resumo de dados numéricos. É uma técnica usada para resumir e descrever as características dos dados, fornecendo uma visão geral das informações que estão sendo analisadas. 

Em outras palavras, a análise descritiva se preocupa em fornecer informações úteis sobre um conjunto de dados. Além disso, ela é uma ferramenta muito eficaz quando se busca retratar tendências e comportamentos nos conjuntos de dados de eventos que já ocorreram. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

10 

Por meio desta técnica é possível entender padrões e identificar eventos que fogem aos padrões identificados, os famosos outliers. 

Geralmente as análises descritivas são as primeiras manipulações realizadas em um estudo quantitativo e tem como principal objetivo resumir, sumarizar e explorar o comportamento dos dados. Isso pode ser feito através de tabelas de frequências, gráficos e medidas de resumo numérico. Ela inclui várias técnicas e medidas para analisar os dados, tais como medidas de tendência central (como a média, a mediana e a moda), medidas de dispersão (como o desvio padrão e a amplitude), análise de frequência, gráficos e tabelas. 

A análise descritiva é amplamente utilizada em diversas áreas, como em pesquisas de opinião, análises de mercado, ciências sociais e ciências da saúde. Ela é útil para resumir e comunicar as informações dos dados de forma clara e objetiva, permitindo que as pessoas tomem decisões informadas com base nos resultados obtidos. 

É importante notar que a análise descritiva não faz inferências sobre a população com base em uma amostra de dados. Para fazer inferências estatísticas, é necessário utilizar a estatística inferencial, que é outra área da estatística. 

Um exemplo de aplicação da análise descritiva é na análise de dados dos colaboradores de uma empresa. Suponha que uma empresa queira entender melhor quem são seus colaboradores, onde estão distribuídos, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

11 

qual o grau de escolaridade deles, sua faixa salarial e como ela tem variado ao longo do tempo. 

A análise descritiva pode ser usada para analisar esses dados. Por exemplo, podemos calcular a média dos salários, a mediana e o desvio padrão para entender melhor essa distribuição. 

Além disso, podemos usar gráficos para visualizar esses dados. Um gráfico de barras, por exemplo, pode ser usado para mostrar a quantidade de colaboradores por grau de escolaridade. Um box plot pode ser usado para mostrar a mediana, os quartis e os valores extremos dos salários. 

Algumas das vantagens da análise descritiva são: 

- ➢ Os resultados são objetivos e neutros; 

- ➢ Traz imparcialidade a um estudo, evitando que se formem juízos de valor; 

- ➢ É considerado expansivo em comparação a outros métodos quantitativos e oferece uma visão ampla de um fenômeno; 

- ➢ Permite criar hipóteses a partir dos dados. 

Mas como nem tudo são flores, este método apresenta algumas limitações, tais como: 

- ➢ Dificuldade de generalizar os resultados para outras populações ou contextos; 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

12 

- ➢ Ela não permite testar hipóteses ou estabelecer relações causais entre as variáveis; 

- ➢ Ela pode ser influenciada por fatores externos que afetam a qualidade dos dados, como erros de medição, amostragem ou coleta; 

- ➢ Ela pode ser insuficiente para explicar fenômenos complexos que exigem análises mais profundas e sofisticadas. 

Como dito anteriormente, a análise descritiva é a porta de entrada para análises mais complexas. Isso porque precisamos conhecer bem o nosso dado para então conseguir propor análises que façam sentido e que resultem em informação de qualidade. 

Nas próximas aulas nós vamos conhecer um pouco mais sobre as técnicas de análise descritiva e como utilizar as ferramentas que ela nos disponibiliza. 

### Aula 1.2: Medidas de tendência central 

As medidas de tendência central são valores que representam, de alguma forma, o centro ou a "média" de um conjunto de dados. Essas medidas são usadas na estatística para resumir e descrever conjuntos de dados e são uma parte importante da análise descritiva. 

Vamos imaginar que em uma pesquisa interna do BanVic, queremos entender se nossos colaboradores são “altos”, “baixos” ou estão “na 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

13 

média”. Este é um caso onde a Estatística faz parte do nosso cotidiano, mesmo que não a reconheçamos diretamente! 

Tabela 01: Altura dos colaboradores do BanVic. 

|**Colaborador**|**Altura ( )**<br>𝑥𝑖|
|---|---|
|1|1,88|
|2|1,8|
|3|1,68|
|4|1,5|
|5|1,79|
|6|1,78|
|7|1,69|
|8|1,72|
|9|1,79|
|10|1,77|



Nossa própria intuição nos diz que precisamos construir alguma medida que resuma a altura dos colaboradores para poder responder a esta pergunta. A medida mais utilizada é a própria média simples ou média aritmética, somando a altura de todos os colaboradores (Tabela 01) e dividindo pelo número total de colaboradores, 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

14 

Você pode calcular a média de altura e obter o valor de 1,74m. Uma outra medida interessante pode ser obtida ao ordenar nosso conjunto de dados e selecionar o valor que ocupa a posição central. Você pode fazer esse exercício manualmente e verá que este valor, chamado de mediana, será de 1,775m (como o conjunto de dados é par, a mediana é a média dos dois valores centrais). Podemos ainda simplesmente contar o valor que mais se repete nos dados, a que chamaremos de moda. Em nosso exemplo, a moda é 1,79m (linha laranja na figura 01 abaixo). 



<!-- Start of picture text -->
2.00<br>175<br>1.50<br>1.25<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>150 155 1.60 165 1.70 175 1.80 185 1.90<br><!-- End of picture text -->

Figura 01: Média, Mediana e moda. 

#### **Exemplo 5.1: Cálculo da média, moda e mediana** 

O código Python abaixo demonstra como calcular as estatísticas de tendência central: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

15 

Python #5.1a import statistics as stat altura = [1.88, 1.8, 1.68, 1.5, 1.79, 1.78, 1.69, 1.72, 1.79, 1.77] print("Média de altura é", stat.mean(altura)) print("Mediana de altura é", stat.median(altura)) print("Moda de altura é", stat.mode(altura)) 

O uso das diferentes medidas de tendência central, ou medidas de posição, dependerá das características do conjunto de dados que analisamos. Quanto mais “assimétricos” os dados, maior a diferença entre cada medida. Um exemplo comum é a renda. O IBGE realiza trimestralmente através da PNAD Contínua uma coleta de dados sobre a força de trabalho que inclui variáveis de renda, desemprego entre outras. Na tabela abaixo é possível ver que o rendimento domiciliar per capita médio em 2021 no Brasil era de R$ 1353,00. E o mediano? R$810, cerca de 40% menor! (Tabela 02). 

Tabela 02: Rendimento domiciliar _per capita_ médio e mediano das pessoas segundo as Grandes Regiões - 2012 a 2021. Fonte: www.ipea.gov.br 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

16 



<!-- Start of picture text -->
GrandesRegides Rendimento domiciliar per capita das pessoas (RS) dosimoso(mp 5  || eoumuulada20212012Variagéo(%)<br>Médio<br>Brasil 1417 1464 1505 1458 1439 1445 1498 1520 1456 1353 69 45<br>Norte 968 971 984 964 893 927 1002 945 966 871 98 (410.0<br>Nordeste 870 908 955 948 906 922 915 955 963 843 ()125 43,1<br>Sudeste 1742 1765 1818 1746 1761 1724 1830 1852 1742 1645 56 15.6<br>Sul 1734 1795 1826 1768 1733 1792 1810 1856 1738 1656 47 45<br>Centro-Oeste 1663 1734 1737 1666 1628 1701 1721 1714 1626 1534 57 78<br>Mediano<br>Brasil 842 888 (929 904 862 872 894 919 903 B10 ()103 38<br>Norte 552 564 598 579 536 559 870 S61 632 839 ()147 24<br>Nordeste 511 540 S71 863 S42 555 551 S57 594 806 (.) 148 11,0<br>Sudeste 1042 1075 1098 1072 1071 1074 1100 1112 1084 1019 60 2.2<br>Sul 1139 1206 1235 1227 1776 1207 1184 1249 1199 1139 50 0.0<br>Centro-Oeste 976 1048 1067 1028 1009 1042 1084 1103 1062 957 99 19<br>Fonte: IBGE, Pesquisa Nacional por Amostra de Domicilios Continua 2012-2021.<br>Notas: 1 Dados consolidados de primeiras visitas em 2012 e 2019 e de quintas visitas em 2020 e 2021.<br>2. Rendimentos deflacionados para reais médios de 2021.<br><!-- End of picture text -->

#### **Exemplo: Valor médio de transação do BanVic** 

Agora vamos usar os dados reais de transação do BanVic para mostrar a importância de entender a diferença entre Média e Mediana. Nossos dados contém todas as transações de débito do banco (ou seja, com valor negativo). 

Python # Read data import pandas as pd import sqlite3 import random as rd import matplotlib.pyplot as plt import numpy as np #Create connection cnx = sqlite3.connect('../../banvic.db') 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

17 

df = pd.read_sql_query("SELECT * FROM transacoes where valor_transacao < 0", cnx) 

Em seguida, calculamos a média e mediana. Note que a média é quase cinco vezes maior que a mediana (por que?): 

Python # Calcular a média e mediana media_transacao = df['valor_transacao'].mean() mediana_transacao = df['valor_transacao'].median() print("média", media_transacao) print("mediana",mediana_transacao) 

Podemos visualizar os dados através de um gráfico do tipo histograma (veremos com mais detalhes o que esse gráfico significa em uma próxima 

aula): 

Python # Criar histograma dados_filtrados = df[df.valor_transacao > -1000] dados_filtrados min(dados_filtrados["valor_transacao"]) plt.hist(dados_filtrados["valor_transacao"], bins=np.arange(min(dados_filtrados["valor_transacao"]), max(dados_filtrados["valor_transacao"]) + 10, 10), align='right') 

#Adicionar média e mediana plt.axvline(media_transacao,ymin = 0, ymax=1, color="red") plt.axvline(mediana_transacao,ymin = 0, ymax=1, color="blue") 

No gráfico conseguimos ver que a distribuição do valor da transação é concentrado em valores de até 100 reais, mas também há valores maiores 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

18 

em menor quantidade mas que impactam a média. Nestes casos, dizemos que a distribuição dos dados é _assimétrica_ e com _cauda longa_ . 



<!-- Start of picture text -->
8000<br>7000<br>6000<br>5000<br>4000<br>3000<br>2000<br>1000<br>te)<br>-1000 —800 —600 —400 -200 (0)<br><!-- End of picture text -->

#### **Código completo** : 

Python # Read data import pandas as pd import sqlite3 import random as rd import matplotlib.pyplot as plt import numpy as np 

#Create connection cnx = sqlite3.connect('../../banvic.db') 

df = pd.read_sql_query("SELECT * FROM transacoes where valor_transacao < 0", cnx) 

print("média",df['valor_transacao'].mean()) print("mediana",df['valor_transacao'].median()) 

dados_filtrados = df[df.valor_transacao > -1000] 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

19 

dados_filtrados min(dados_filtrados["valor_transacao"]) plt.hist(dados_filtrados["valor_transacao"], bins=np.arange(min(dados_filtrados["valor_transacao"]), max(dados_filtrados["valor_transacao"]) + 10, 10), align='right') plt.axvline(df['valor_transacao'].mean(),ymin = 0, ymax=1, color="red") plt.axvline(df['valor_transacao'].median(),ymin = 0, ymax=1, color="blue") 

Vamos recapitular. As três principais medidas de tendência central são: 

- ➢ Média: é a soma de todos os valores do conjunto de dados dividida pelo número de valores. É uma medida útil para descrever a média geral dos dados. 

- ➢ Mediana: é o valor que divide o conjunto de dados ao meio, ou seja, 50% dos dados estão acima dela e 50% abaixo dela. É uma medida útil para descrever o valor central em conjuntos de dados com valores extremos ou "outliers". 

- ➢ Moda: é o valor que ocorre com mais frequência no conjunto de dados. É uma medida útil para descrever os valores mais comuns em um conjunto de dados. 

### Aula 1.4: Medidas de Dispersão 

Médias e outras medidas de tendência central são importantes mas não contam toda a história. Na maioria dos casos, não queremos apenas resumir um conjunto de dados por seu valor médio, mas também 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

20 

entender como os dados estão distribuídos em relação a ele. Mais do que isso, em geral essas medidas só terão realmente sentido quando comparadas com outros conjuntos de dados. 

Uma das medidas de dispersão mais usual é simplesmente a diferença entre o maior e o menor valor de um conjunto de dados, chamada de amplitude. Vamos retomar a tabela abaixo que registra a altura de 10 colaboradores de uma agência do BanVic (Tabela 03): 

Tabela 03: Altura dos colaboradores do BanVic. 

|**Colaborador**|**Altura ( )**<br>𝑥𝑖|
|---|---|
|1|1,88|
|2|1,8|
|3|1,68|
|4|1,50|
|5|1,79|
|6|1,78|
|7|1,69|
|8|1,72|
|9|1,79|
|10|1,77|



Para calcular a amplitude basta tirar a diferença entre a maior altura (1,88m) e a menor (1,50m). O resultado é uma amplitude de 38cm. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

21 

Outra forma direta de construirmos uma medida de dispersão seria calcular a distância de cada altura em relação à média. O problema é que a soma desses desvios sempre dará zero e a média dessa soma também dará zero. Por isso, o desvio médio simples ou desvio simples é calculado tomando a média dos valores absolutos dos desvios em relação a média como na tabela abaixo (Tabela 04): 

Tabela 04: Altura dos colaboradores do BanVic, bem como o desvio simples e desvio absoluto das alturas em relação a média. 

|**Colaborado**||||
|---|---|---|---|
|**r**|**Altura ( )**<br>𝑥𝑖|𝑥𝑖−𝑥<sup>‾</sup>||𝑥𝑖−𝑥|<sup>‾</sup>|
|1|1,88|0,14|0,14|
|2|1,8|0,06|0,06|
|3|1,68|-0,06|0,06|
|4|1,5|-0,24|0,24|
|5|1,79|0,05|0,05|
|6|1,78|0,04|0,04|
|7|1,69|-0,05|0,05|
|8|1,72|-0,02|0,02|
|9|1,79|0,05|0,05|
|10|1,77|0,03|0,03|



A fórmula do desvio simples é dada por: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

22 



Utilizando uma planilha eletrônica ou uma calculadora rapidamente chegamos a um desvio médio de 0,06m ou 6cm. Grande ou pequeno? Depende! 

Uma outra forma de obter valores sempre positivos é utilizar o quadrado dos desvios em relação à média. A média do quadrado dos desvios é chamada de variância e é uma das medidas mais importantes da estatística. Sua fórmula é definida como: 



A unidade de medida da variância não é fácil de interpretar por si só (“centímetros quadrados”). Por isso, é conveniente construir uma outra medida que mantenha a mesma unidade dos dados originais ao tirarmos a raiz quadrada da variância. Essa medida é o chamado desvio padrão e sua fórmula é 



Vamos seguir nosso exemplo da altura dos colaboradores. Para facilitar nosso cálculo podemos adicionar uma nova coluna na tabela com o 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

23 

quadro dos desvios da altura de cada colaborador em relação à média (Tabela 05). 

Tabela 05: Altura dos colaboradores do BanVic, bem como o desvio simples, o desvio absoluto das alturas e o quadrado dos desvios em relação a média. 

|**Colaborador**|**Altura (x)**|𝑥𝑖−𝑥<sup>‾</sup>||𝑥𝑖−𝑥|<sup>‾</sup>|(𝑥𝑖−𝑥)<br>2<br>‾|
|---|---|---|---|---|
|1|1,88|0,14|0,14|0,0196|
|2|1,8|0,06|0,06|0,0036|
|3|1,68|-0,06|0,06|0,0036|
|4|1,5|-0,24|0,24|0,0576|
|5|1,79|0,05|0,05|0,0025|
|6|1,78|0,04|0,04|0,0016|
|7|1,69|-0,05|0,05|0,0025|
|8|1,72|-0,02|0,02|0,0004|
|9|1,79|0,05|0,05|0,0025|
|10|1,77|0,03|0,03|0,0009|



Para calcular a variância, começamos realizando a soma do quadrado dos desvios e depois dividimos pelo número de indivíduos (n = 10) 



Para calcular o desvio padrão, basta tirarmos a raiz quadrada da variância 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

24 

𝑑𝑒𝑠𝑣𝑖𝑜 𝑝𝑎𝑑𝑟ã𝑜 (𝑑𝑝) = 0, 00948 = 0, 097 

Ou seja, o desvio padrão da altura dos colaboradores de uma agência do BanVic é de aproximadamente 9,7cm. Nas próximas aulas, descobriremos que dominar os segredos da média e do desvio padrão de um conjunto de dados abre portas para uma infinidade de inferências reveladoras sobre essas informações. 

Para finalizar nossa aula sobre medidas de dispersão, é importante mencionar o coeficiente de variação. Seu uso é especialmente interessante se queremos comparar a variação entre dois conjuntos de dados que possuem dimensões distintas, por exemplo, altura e peso. O que varia mais entre os colaboradores do BanVic? Como não podemos comparar centímetros com quilos, podemos definir uma medida “adimensional” 

𝑐𝑜𝑒𝑓. 𝑣𝑎𝑟𝑖𝑎çã𝑜(𝑐𝑣) =<sup>𝑑𝑝</sup> 𝑥<sup>‾</sup> 

Em geral, o coeficiente de variação é apresentado como uma porcentagem. 

Vamos recapitular: 

- ➢ As medidas de dispersão indicam a variabilidade dos dados observados, ou seja, o quanto os valores observados são próximos ou distantes entre si. 

- ➢ A amplitude mede a diferença entre o maior e o menor valor em um conjunto de dados; 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

25 

- ➢ O desvio médio calcula a média dos desvios absolutos em relação à média; 

- ➢ A variância é uma das medidas mais importantes da estatística e é calculada pela média da soma dos quadrados dos desvios em relação à média; 

- ➢ O desvio padrão é a raiz quadrada da variância; 

- ➢ O coeficiente de variação não tem dimensão e é geralmente usado para comparar entre conjuntos de dados com medidas distintas (por exemplo, peso e altura). 

#### **Exemplo 5.2: Variância e Desvio-padrão** 

Para calcular a variância e desvio padrão no Python usamos as funções _pvariance e pstdev_ do pacote _statistics_ : 

Python import statistics as stat altura = [1.88, 1.8, 1.68, 1.5, 1.79, 1.78, 1.69, 1.72, 1.79, 1.77] print("A variância é", stat.pvariance(altura)) print("O desvio padrão é", stat.pstdev(altura)) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

26 

### Aula 1.5: Medidas de Associação 

Em Abril de 2023, uma notícia publicada em um portal online tinha como título “Comportamento do preço do bitcoin atinge maior _correlação_ com o ouro da história” (Exame, 2023, Figura 02). Mas o que exatamente significa dizer que o preço de algo atingiu _maior correlação_ com outro preço? 



<!-- Start of picture text -->
= Q exame. FUTURE OF MONEY €<br>Future of Money<br>Home > Future of Money<br>Comportamento do preco do bitcoin atinge<br>maior correlagdo com 0 ouro da historia<br>Criptomoeda teve melhor trimestre em dois anos, e analistas atribuem parte da sua alta ao<br>fortalecimento da tese de que ativo seria reserva de valor<br>QORB@av< Modo escuro<br><!-- End of picture text -->

Figura 02: Recorte da reportagem da Exame anunciando correlação entre o preço do bitcoin e do ouro. Fonte: Exame, 2023. 

Imediatamente pensamos em alguma medida de associação, de similaridade de comportamento. Na Figura 03 abaixo vemos que em um período de 3 meses entre dezembro de 2022 e Fevereiro de 2023, a cotação do Bitcoin e do Ouro parecem ter um comportamento parecido. Mas quão parecido? Essa é a ideia por trás da medida de correlação. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

27 



<!-- Start of picture text -->
—— Bitcoin<br>—— Ouro<br>24000<br>19.5<br>23000<br>19.0<br>22000<br>21000 18.5<br>20000 18.0<br>19000 175<br>18000 17.0<br>17000 16.5<br>ay gpS 2Ad 7a pF?i e 5 _ yta oo.<br>oo oo ow ow wo oe om om ow<br>er 4 ¥ ¥ pr wr af ¥ ¥<br><!-- End of picture text -->

Figura 03: Cotação semanal do Bitcoin e do Ouro (vs dólar) entre 01/12/2022  e 01/02/23. 

#### **Exemplo 5.3: Correlação entre ouro e bitcoin** 

Neste exemplo vamos utilizar o pacote _yfinance_ para obter valores de cotação do Ouro e Bitcoin diretamente: 

Python import yfinance as yf import matplotlib.pyplot as plt # Obter cotação bitcoin = yf.Ticker("BTC-USD") gold = yf.Ticker("GOLD") 

# Trazer dados históricos bitcoin = bitcoin.history(start = '2022-12-01',end='2023-02-01' ,interval='1wk') gold = gold.history(start = '2022-12-01',end='2023-02-01',interval='1wk') 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

28 

# Plotar as séries fig = plt.figure() plt.plot(bitcoin[["Close"]], marker = ".", label="Bitcoin") plt.twinx() plt.plot(gold[["Close"]], color="red", marker = ".",label="Ouro") fig.legend(loc="upper left") 

Vamos construir a intuição por trás da medida de correlação retomando nosso exemplo da nossa pesquisa sobre os colaboradores do BanVic. Agora além da altura, também resolvemos medir o peso de cada colaborador como na tabela abaixo (Tabela 06): 

Tabela 06: Altura e peso dos colaboradores do BanVic. 

|**Colaborador**|**Altura (x)**|**Peso (y)**|
|---|---|---|
|1|1,88|95|
|2|1,8|90|
|3|1,68|77|
|4|1,5|55|
|5|1,79|70|
|6|1,78|103|
|7|1,69|68|
|8|1,72|75|
|9|1,79|70|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

29 

|10|1,77|70|
|---|---|---|
|Média|**1,74**|**77,3**|
|Desvio-padrã|||
|o|**0,097**|**13,726**|



Podemos formular conclusões intuitivas e qualitativas sobre os dados construindo um gráfico chamado de diagrama de dispersão. Como os pontos da figura apresentam certo padrão, podemos concluir se há ou não uma relação entre x e y, no nosso exemplo entre a altura e o peso dos funcionários. A figura 04 exibe um padrão de valores crescentes de y que correspondem a valores crescentes de x, o que nos leva a crer que colaboradores mais altos são também mais pesados. 



<!-- Start of picture text -->
125<br>100 s<br>e<br>e<br>75 oe<br>3 e ee<br>g e<br>& 50<br>25<br>o<br>15 1.6 17 1.8<br>Altura (x)<br><!-- End of picture text -->

Figura 04: Gráfico de dispersão das alturas e dos pesos dos colaboradores do BanVic. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

30 

Neste caso, quanto mais próximos a uma linha reta estiverem o padrão de pontos, a relação entre x e y é mais forte e definimos como uma forte correlação positiva. Um cenário distinto ocorre quando os valores de y decrescem quando os valores de x crescem e neste caso teremos uma correlação negativa 

A análise de correlação é útil sempre que há interesse em determinar se existe qualquer associação (relação) entre duas ou mais variáveis quantitativas, permitindo ainda avaliar o grau e a natureza dessa relação. Uma das razões de sua popularidade é que seu valor sempre estará entre -1 e 1. Além disso, ele não possui unidade (é adimensional), logo podemos comparar quaisquer duas variáveis entre si utilizando o coeficiente de correlação. Essa facilidade de comparação, no entanto,  é tanto um dádiva como uma sina, causando muitas análises equivocadas, ou espúrias,  como veremos a seguir. 

Para calcular o coeficiente de correlação, iniciamos calculando a média e o desvio padrão das duas variáveis.  Em seguida, convertemos os dados das duas variáveis em _desvios-padrão_ (Colunas D e E) de modo que conseguimos comparar a distância de cada variável em uma mesma unidade de medida. Ou seja, ao invés de dizermos que um colaborador é 10cm mais alto que a média, podemos dizer que ele é aproximadamente 1 desvio padrão mais alto que a média. Fazemos o mesmo para o peso. 

Em seguida, multiplicamos o Peso e Altura _padronizados_ (Coluna F). Valores altos dessa multiplicação indicam que tanto peso como altura 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

31 

estão relativamente longe da média. Por fim, somamos os produtos calculados e dividimos pelo número de observações para obter que a correlação entre Peso e Altura na nossa agência do BanVic é de 0,68 (Tabela 07). 

Tabela 07: Tabela com os valores de altura e peso dos colaboradores do BanVic, bem como o valor médio e a correlação calculada para este conjunto de dados. 

|A|B|C|D|E|F|
|---|---|---|---|---|---|
|**Colaborador**|**Altura ( )**<br>𝑥|**Peso ( )**<br>𝑦|(𝑥 −𝑥<sup>‾</sup>)/σ𝑥|(𝑦 −𝑦<sup>‾</sup>)/σ𝑦|(𝑥 −𝑥<sup>‾</sup> )<br>σ𝑥<br>(𝑦−𝑦<sup>‾</sup> )<br>σ𝑦|
|1|1,88|95|1,44|1,29|1,85|
|2|1,8|90|0,62|0,93|0,57|
|3|1,68|77|-0,62|-0,02|0,01|
|4|1,5|55|-2,46|-1,62|4,00|
|5|1,79|70|0,51|-0,53|-0,27|
|6|1,78|103|0,41|1,87|0,77|
|7|1,69|68|-0,51|-0,68|0,35|
|8|1,72|75|-0,21|-0,17|0,03|
|9|1,79|70|0,51|-0,53|-0,27|
|10|1,77|70|0,31|-0,53|-0,16|
|**Média**|**1,74**|**77,3**||**Total**|**6,88**|
|**Desvio-padrão**|**0,097**|**13,726**||**Correlação**|**0,688**|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

32 

Formalmente, o coeficiente de correlação é geralmente apresentado pela letra grega ρ𝑋,𝑌("𝑟ô") e sua fórmula é dada por: 



onde o numerador é a também chamada covariância 



A correlação é sempre um número entre -1 e 1. Quando a correlação é zero, dizemos que não existe dependência linear entre as variáveis. Esse é um dos pontos de confusão na interpretação da correlação, com muitas pessoas confundindo a não existência de uma dependência _linear_ com _independência_ . 

De fato, como vimos no início da aula, o coeficiente de correlação é uma medida estatística muito popular, presente em relatórios, notícias, comentários esportivos e muito mais. Infelizmente, sua popularidade também gera muitas análises equivocadas. Vamos falar de algumas delas. 

#### **Correlação não é causalidade** 

Apesar de ser uma das armas mais poderosas que possuímos para interpretar os dados à nossa volta, a estatística depende de um senso crítico para interpretar os resultados _matemáticos_ que ela produz. O 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

33 

coeficiente de correlação, por exemplo, nada nos diz sobre as características do fenômeno observado e precisa ser complementado pelo conhecimento científico ou de negócio. 

Um exemplo claro é do agricultor que resolveu medir a correlação entre a incidência solar e a produtividade da sua produção agrícola. Ao obter uma alta correlação entre as duas variáveis, precisamos definir o sentido da relação: seria a incidência solar que aumenta a produtividade, ou a produtividade que faz o sol ficar mais forte (Figura 05)? 



<!-- Start of picture text -->
Sol faz a terra produzir mais :<br>—<br>Terra produz mais Sol ANS<br>+<br><!-- End of picture text -->

Figura 05: Correlação não é causalidade. 

Se neste exemplo a resposta parece óbvia, isso é raramente verdade quando lidamos com fenômenos complexos em um ambiente de negócios. Por isso, é importante interpretar com cautela os resultados obtidos através do coeficiente de correlação e outras medidas estatísticas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

34 

### **Correlação espúria** 

Outra confusão comum é visualizar relações onde elas simplesmente não existem ou possuem outras causas externas. Como veremos nas aulas sobre probabilidade, se procurarmos o suficiente, é comum visualizar padrões em eventos que ocorrem simplesmente pela chance. Existe até um termo para isso, a _apofenia,_ uma tendência nossa de darmos significância para estímulos que foram gerados de forma aleatória. Quem nunca viu um rosto em uma nuvem? 

Dizemos que existe uma correlação _espúria_ quando duas variáveis apresentam uma forte associação sem motivo algum. Existe até um site que apresenta algumas dessas correlações mais inusitadas como essa da Figura 06 abaixo. Você já imaginou que a correlação entre o consumo per capita de Mussarela e o número de doutores em Engenharia Civil nos EUA é de 0,95?! Os engenheiros devem ser viciados em queijo! 



<!-- Start of picture text -->
12s 2000 1000 degrees<br>¢ Engineering doctorates: 480 degrees<br>2 ums soodegees €<br>3 10s 600 degrees<br>ots 400 degrees<br>200 2001 2002 2003 2004 2e0s 2006 2007 2008 2008<br>-@ Engineering doctorates Mozzarella cheese consumption<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

35 

Figura 06: Consumo per capita de Mussarela e o número de doutores em Engenharia Civil nos EUA. Fonte: <u>tylervigen.com.</u> 

A correlação também é muito influenciada pela escolha da amostra analisada. Lembra do exemplo do Bitcoin e do Ouro? Para um período mais longo vemos que a relação entre as variáveis não é sempre tão bem comportada, ainda que a correlação em um período mais longo se aproxime de 0,77 (Figura 07). Na prática, tanto Bitcoin como Ouro são influenciados por uma enorme quantidade de outros fatores como a taxa de juros, inflação, cotação da bolsa entre outras variáveis. Para poder medir a influência de muitas variáveis simultaneamente, é possível usar uma outra técnica que veremos futuramente: a análise de regressão. 



<!-- Start of picture text -->
—— Bitcoin<br>—-— Ouro<br>45000 24<br>40000 22<br>35000 30<br>30000<br>18<br>25000 °<br>16<br>20000<br>14<br>> 18 0 91 10? Ws ,0> 1.0? ,09 Ao)<br>1 gt ot a Ws 2: 3 a3 3 3<br>gr oF ag gph ash get gph? gg?” ag?” oot<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

36 

Figura 07: Cotação semanal do Bitcoin e do Ouro (vs dólar) entre 01/01/2022 e 01/02/23. 

Outra forma comum de identificar correlação é através do gráfico de dispersão (onde omitimos a variável tempo) (Figura 08): 



<!-- Start of picture text -->
e<br>24 e e<br>», ° e<br>22 e<br>o 3<br>20<br>e e a e<br>e ee %@<br>18 ee ee e e<br>° e Pod e e<br>. *<br>167 § ee 0 e<br>e  °<br>3 o><br>14 ee°°<br>20000 25000 30000 35000 40000 45000<br><!-- End of picture text -->

Figura 08: Cotação semanal do Bitcoin e do Ouro (vs dólar) entre 01/12/2022 e 01/02/23. 

Vamos recapitular: 

- As medidas de associação nos ajudam a entender como duas variáveis se relacionam; 

- O coeficiente de correlação é uma medida de associação muito popular; 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

37 

- O valor do coeficiente de correlação é sempre entre -1 e 1. Uma correlação próxima de zero indica ausência de associação linear entre duas variáveis. 

- Correlação não significa causalidade; 

- Existem muitas variáveis correlacionadas por motivos aleatórios, a chamada correlação espúria. 

### Aula 1.6: Visualização de dados 

A visualização gráfica de dados também é parte da estatística, ainda que hoje esse conhecimento tenha sido disseminado nas mais diversas áreas. Nesta aula falaremos sobre alguns gráficos comuns em análise estatística e sua interpretação. 

#### **Histogramas** 

Os histogramas são gráficos de colunas em que cada coluna representa uma classe de valores observados, e a altura da coluna representa a frequência desses valores nos dados (Figura 09). São construídos a partir de uma tabela de frequência. 

Cada histograma tem três partes: 

- classe: são as barras indicadoras dos valores da estatística, com limites mínimos e máximos. Por exemplo, valores de transação de Pix. 

- intervalo: o tamanho de cada uma das barras.  Por exemplo, 40 reais 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

38 

- frequência/densidade: o número de ocorrências de cada classe ou a probabilidade de ocorrência (de modo que a soma das classes seja 1). 

Vemos que o gráfico abaixo possui 40 classes com um intervalo de 50 reais. Notamos que a maior frequência de valores de transação com pix é concentrada entre 50 e 400 reais. Também podemos notar que a distribuição do valor das transações não é simétrica, há uma grande concentração na direita e depois uma “cauda” com frequências cada vez menores. 



<!-- Start of picture text -->
1200<br>1000<br>2 800<br>y<<br>oO seas<br>3 Frequéncia<br>3 600 ou<br>& Densidade<br>400<br>200 Classe<br>0 u<br>-2000 -1750 —1500 -1250 -1000 -750 -500 -250 te)<br>Valor da Transacao= Intervalo<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

39 

Figura 09. Exemplo de Histograma para a variável “Valor Transação” de Pix. 

#### **Exemplo 5.4: Histograma** 

Para construir um histograma simples em Python, podemos usar a função _hist_ do pacote _matplotlib_ : 

Python # Exemplo 5.4 - Histograma import matplotlib.pyplot as plt import pandas as pd import sqlite3 import random as rd #Create connection cnx = sqlite3.connect('../../banvic.db') df = pd.read_sql_query("SELECT * FROM transacoes", cnx) plt.hist(df[(df['nome_transacao']=='Pix - Realizado')]['valor_transacao'], rwidth=0.85, range=(-2000,0), bins=40) plt.xlabel('Valor da Transação') plt.ylabel('Frequência') 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

40 

### **Gráfico de dispersão** 

Gráficos de dispersão são ferramentas muito úteis na análise de dados, permitindo visualizar e explorar a relação entre duas variáveis contínuas de forma clara e intuitiva (Figura 10). São muito utilizados para identificar associações, padrões e tendências entre as variáveis estudadas. Além disso, os gráficos de dispersão são frequentemente utilizados para traçar retas de regressão, que ajudam a quantificar e modelar a relação entre as variáveis, permitindo previsões e insights valiosos para tomada de decisões. 



<!-- Start of picture text -->
100<br>95<br>90<br>85<br>80<br>2 4 6 8 10 12 14 16<br><!-- End of picture text -->

Figura 10: Exemplo de gráfico de dispersão. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

41 

#### **Exemplo 5.5: Gráfico de dispersão** 

Para gerar um gráfico de dispersão no Python podemos usar o código abaixo: 

Python import matplotlib.pyplot as plt x =[5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6] y =[99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86] plt.scatter(x, y, c ="blue") 

### **Boxplot** 

O boxplot, ou diagrama de caixa, é um gráfico muito popular na estatística porque permite visualizar a distribuição e os valores discrepantes dos dados em um único gráfico. A Figura 11 abaixo descreve os elementos de um Boxplot. Analisando o gráfico de baixo para cima: 

- a primeira linha horizontal representa o valor mínimo, sem considerar os valores que ultrapassam o desvio interquartílico; 

- a segunda linha horizontal representa o primeiro quartil; 

- a linha mais grossa no meio da caixa representa a mediana; 

- a terceira linha horizontal representa o terceiro quartil; 

- a última linha horizontal representa o valor máximo, sem considerar os valores que ultrapassam o desvio interquartílico 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

42 

O desvio interquartílico é definido como 1.5 vezes o terceiro quartil menos o primeiro quartil. É um valor de referência e cria a chamada barreira de valores atípicos. 



<!-- Start of picture text -->
Maior valor<br>—— <—— observado menor<br>: ou igual a. Q3 +<br>H 1,510<br>30 Quartil :<br>(Q3)<br>Mediana<br>Amplitude<br>Interquartil<br>(IQ)<br>10 Quartil<br>(Q1) H<br>: Menor valor<br>—— <— observado maior ou<br>Oo igual a Q1 - 1,51Q<br>\ Valor Extremo<br>(outlier)<br><!-- End of picture text -->

Figura 11. Elementos de um boxplot. 

Vamos ver um exemplo de um Boxplot utilizando dados do BanVic. O gráfico abaixo (Figura 12) apresenta a distribuição do Valor da Transação de quatro tipos de operação: Compra Débito, Compra Crédito, Pix - Realizado e Saque (valores maiores que 1000 reais foram filtrados para facilitar a visualização). Notamos que a mediana da transação com Pix é acima da mediana dos demais tipos de transação. No entanto, nos quatro 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

43 

tipos de transação há valores extremos altos. Também podemos identificar que a amplitude interquartil (IQ) da transação com PIX é maior que das demais transações. 



<!-- Start of picture text -->
0<br>—200<br>°<br>-400<br>‘ S<br>ac<br>Ec<br>—600<br>s<br>- $<br>-800 t ry<br>U7<br>-1000 , ¢<br>Compra Débito Compra Crédito Pix - Realizado Saque<br>Tipo de Transacao<br><!-- End of picture text -->

Figura 12. Exemplo de Boxplot para a variável “Valor Transação”. 

#### **Exemplo 5.6 - Boxplot** 

O código abaixo mostra como gerar um boxplot no Python como na Figura 12: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

44 

Python # Exemplo 5.6 - Boxplot import seaborn as sns import pandas as pd import sqlite3 #Create connection cnx = sqlite3.connect('../../banvic.db') 

df = pd.read_sql_query("SELECT * FROM transacoes where valor_transacao > -1000", cnx) 

# Filtrar dados df = df[df['nome_transacao'].isin(['Pix - Realizado','Saque','Compra Crédito','Compra Débito'])] 

# Construir Boxplot sns.boxplot(x="nome_transacao", y="valor_transacao", data=df) plt.xlabel('Tipo de Transação') plt.ylabel('Valor Transação') 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

45 

## Parte 2: Probabilidade 

### Aula 2.1: Fenômenos Aleatórios 

Até agora discutimos como descrever e caracterizar conjuntos de dados através de métodos como tabelas de frequência e gráficos. Essas técnicas, ainda que simples, são parte essencial da análise de dados. 

Por exemplo, será que podemos usar a análise descritiva para responder à pergunta sobre qual o valor médio das transações realizadas por PIX no BanVic? A resposta é obviamente sim! Como vimos anteriormente neste módulo, através de uma simples função em um software estatístico obtemos que o valor médio das transações do PIX no BanVic foi de R$ 513,28. 

Agora, imagine que nosso objetivo se torne prever o valor da próxima transação realizada por PIX? Será que esse valor será exatamente R$ 513,28? Provavelmente não. Por outro lado, há uma grande chance de que a média das próximas 1000 transações realizadas por PIX seja muito próxima do valor que obtivemos no passado. Em estatística, os fenômenos aleatórios são aqueles que mesmo repetidos sob as mesmas condições, geram resultados diferentes, por exemplo o lançamento de uma moeda. Exatamente o caso do valor de uma transação financeira! Já um fenômeno é dito determinístico quando repetido inúmeras vezes, em condições semelhantes, conduz a resultados idênticos, por exemplo leis da física. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

46 

Na prática, a maior parte das perguntas respondidas pela análise de dados possuem maior ou menor grau de incerteza e portanto não podem ser respondidas de forma exata. Mas isso não quer dizer que não temos como respondê-las! Ao longo do tempo, os estatísticos desenvolveram uma série de técnicas matemáticas que nos permitem explicar e tirar conclusões de fenômenos aleatórios. Essa incrível área de estudo da estatística é chamada de “Teoria da Probabilidade” e será o tema das nossas próximas aulas. 

### Aula 2.2: Introdução à Probabilidade 

Na última aula falamos sobre como os fenômenos, ou eventos aleatórios estão presentes na análise de dados. Agora vamos entender um pouco melhor sobre o estudo da probabilidade de eventos aleatórios. 

A capacidade de prever a ocorrência de eventos aleatórios1 como os representados por jogos de dados e de moedas sempre foi um tema recorrente na matemática e filosofia. Nos séculos XVII e XVIII, grandes matemáticos como _Jacob Bernouilli_ , _Pascal_ e _Laplace_ criaram os primeiros modelos formais para explicar a ocorrência de eventos aleatórios, dando origem à chamada probabilidade clássica. 

É possível dizer que a probabilidade clássica é uma formalização da intuição: a probabilidade de um evento ocorrer é a frequência que se espera que o evento ocorra em relação a todos os eventos possíveis. Por 

> 1 Também chamados de eventos _estocásticos._ 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

47 

exemplo, ao jogar um dado com 6 lados, a probabilidade de obter um número de 1 a 6 qualquer é simplesmente 1/6. 

Na teoria moderna de probabilidade, também chamada de frequentista ou empírica, as probabilidades são dependentes da realização de experimentos bem-construídos. Para cada experimento (lançar um dado), o conjunto de todos os resultados possíveis é chamado de _espaço amostral_ (por exemplo, os 6 lados de um dado). 

Chamamos de evento um resultado ou combinação de resultados possíveis dentro do espaço amostral. Por exemplo, ao lançar um dado podemos ter o evento de obter o número 3, obter um número ímpar, etc.  A cada experimento, só existem duas possibilidades para cada evento: ele ocorrer ou não. Se repetirmos o experimento  um número suficiente de vezes, a frequência relativa de cada evento representa a medida da probabilidade dele ocorrer. 

A ideia de experimentos une a teoria da probabilidade com a estatística, permitindo usarmos os conceitos de probabilidades para validar hipóteses e responder perguntas de negócio. Também significa que o cálculo de probabilidades não é exato e em geral dependerá da ocorrência de mais e mais experimentos para ser confiável. 

Vamos recapitular: 

- Espaço amostral: conjunto de todos os resultados possíveis 

- Evento: subconjunto do espaço amostral 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

48 

- Probabilidade: frequência relativa de ocorrência de um evento a partir de múltiplas repetições de um experimento. 

### Aula 2.3: Formalização Matemática 

Já tivemos nosso primeiro contato sobre a teoria da probabilidade. A teoria da probabilidade é o ramo da matemática que desenvolve e avalia modelos para descrever fenômenos aleatórios, sendo a base teórica para o desenvolvimento das técnicas estatísticas que aprendemos neste curso. Aprendemos que a probabilidade é medida pela frequência relativa de ocorrência de um evento a partir de múltiplas repetições de um experimento. 

Também definimos o _Espaço Amostral_ como o conjunto de todos os resultados possíveis de um evento aleatório. Formalmente, ele será representado pela letra grega Ω (ômega). Por exemplo, ao lançarmos um dado nosso espaço amostral é composto por todos resultados possíveis 1, 2 … 6. Ou formalmente. Ω = {1,2,3,4,5,6}. Um evento, por sua vez, é definido como um subconjunto do espaço amostral e formalmente é denotado por uma letra maiúscula A, B, C etc. 

A probabilidade de um evento específico ocorrer nada mais é que a frequência relativa deste evento ocorrer na medida que realizamos um número grande de experimentos. Vamos definir o evento A como “obter o número 3 ao jogar um dado” e a probabilidade deste evento ocorrer como P(A). Como calculamos sua probabilidade? Como vimos anteriormente, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

49 

essa probabilidade é calculada através da divisão entre o número de casos favoráveis pelo número de casos totais após a realização de uma série de experimentos. 

No exemplo 5.7 abaixo, podemos simular um jogo de dados com diferentes números de repetições. A probabilidade de obter o número 3 se aproxima rapidamente para o esperado (1/6) conforme aumentamos o número de repetições. Experimente você mesmo alterando o número de repetições. 

#### **Exemplo 5.7: Jogo de Dados** 

O código abaixo simula um jogo de dados utilizando a Linguagem Python, se alterarmos o número de repetições, vemos que a probabilidade do evento “retornar o número 3” vai cada vez mais convergindo para ⅙ . 

Python import random # Jogar dado resultados = [] contagem_3 = 0 repeticoes = 6 for _ in range(repeticoes): resultado = random.randint(1, 6) resultados.append(resultado) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

50 

if resultado == 3: contagem_3 += 1 # Retorna a lista de resultados print(resultados) print("Contagem do evento X=3:", contagem_3) # Calcula a probabilidade do evento 3 print("Probabilidade do evento X=3:", (contagem_3/repeticoes)*100,"%") 

Mas como medimos a probabilidade de mais de um evento ocorrerem de forma simultânea ou mesmo em sequência? Para isso, podemos utilizar nosso conhecimento de ensino médio sobre a teoria dos conjuntos. 

A união de dois eventos A e B, denotada por _A_ U _B_ representa a ocorrência de pelo menos um dos eventos A ou B. Já a ocorrência simultânea de dois eventos é chamada de intersecção e denotada por _A_ ∩ _B2_ (Figura 13). 

2Dizemos que dois eventos são disjuntos ou mutuamente exclusivos quando não têm elementos em comum. Já dois eventos são _complementares_ se sua união é espaço amostral e sua intersecção é vazia. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

51 



Figura 13: Diagrama de Venn. 

O que realmente importa pra nós é como calcular a probabilidade na ocorrência de pelo menos dois eventos ou de dois eventos simultâneos. Para isso, utilizamos a chamada regra de adição de probabilidades: 



Se pensarmos bem, o resultado é bastante intuitivo. Vamos supor que ao realizar uma campanha de marketing no BanVic, nosso público-alvo seja composto de mulheres e por pessoas (de qualquer gênero) entre 40 e 50 anos (Figura 14). Escolhendo uma pessoa ao acaso, qual a probabilidade dela fazer parte do nosso público-alvo? 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

52 



<!-- Start of picture text -->
Espago Amostral = Todas as pessoas<br>P(Mulher) P(40 — 50anos)<br>& & Q a) PA<br>& & P(Mulher Q (40 ~ 50anos) é é<br>g 6 . a<br>& a.ry<br><!-- End of picture text -->

Figura 14: Diagrama de Venn. 

Ora, é fácil perceber que essa probabilidade será a soma da probabilidade de uma pessoa ser mulher com a probabilidade de uma pessoa ter entre 40 e 50 anos. Além disso, para evitar uma dupla contagem, retiramos do cálculo a probabilidade de alguém ser mulher e ter entre 40 e 50 anos. 

Mas na prática, precisamos saber todas essas fórmulas? Em geral, não. Mas a intuição obtida pelo conhecimento de probabilidade é um grande diferencial de um profissional de dados! Até a próxima! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

53 

### Aula 2.4: Probabilidade condicional 

Um dos aspectos mais interessantes da estatística é a capacidade de se obter resultados que muitas vezes fogem ao senso comum. Um dos exemplos mais comuns é quando se analisa o chamado Jogo das três portas3 (Figura 15), comum em programas matinais de Televisão. Neste jogo, o participante tem uma única chance para escolher entre três portas fechadas, sendo que atrás de uma das portas está o grande prêmio, por exemplo, um carro zerinho, e nas outras duas estão dois jumentos. 



<!-- Start of picture text -->
Porta A Porta B Porta C<br><!-- End of picture text -->

Figura 15. O jogo das 3 portas. 

Na 1a etapa do jogo, o participantes escolhe uma das portas, que ainda não é aberta. Em seguida, o apresentador abre uma das portas restantes revelando que o carro não se encontra nesta outra porta. Antes de abrir a 

porta escolhida inicialmente, o apresentador pergunta ao participante se 

> 3 Também chamado de Problema de _Monty Hall_ , em homenagem ao popular apresentador do programa de auditório norte-americano que deu origem a esse problema. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

54 

ele deseja permanecer com a porta escolhida ou trocar para a outra porta que ainda está fechada. E é aí que mora o problema: devemos trocar ou não? 

Vamos supor que quando o jogo se inicia temos que selecionar entre três portas (A, B e C). Utilizando nossos conhecimentos de probabilidade, não é difícil de calcular que temos uma chance de ⅓ de escolher a porta certa e levar o carro pra casa e uma chance de ⅔ de errarmos e voltarmos sem nada. 

Ao abrir uma das portas fechadas, nossa propensão natural é pensar que tanto faz alterar a porta, afinal, se sobraram duas portas para 1 carro, a probabilidade deveria ser de 50% para cada porta. No entanto, essa visão intuitiva está errada. 

Ao abrir a porta B, a probabilidade do carro estar na porta A (inicialmente escolhida por nós) não se altera e permanece em ⅓ . Ou seja, ao decidir trocar nossa escolha e abrir a porta C, nossa chance de acertar e ganhar o carro é de ⅔ e não de ½! 

O motivo principal da confusão ocorre porque a maioria das pessoas não percebe que a escolha da porta a ser aberta pelo apresentador não é aleatória, pois ele obviamente não irá abrir a porta que contém o carro. Na verdade, a decisão do apresentador sobre qual porta abrir depende, ou é _condicional_ , de qual é a porta escolhida pelo participante e em qual porta o carro está. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

55 

Suponha que o participante escolhe a porta A, e esta é a porta certa. Como o apresentador não pode escolher A, ele escolhe abrir as portas B e C com igual probabilidade (½), de modo que a probabilidade das portas B ou C serem abertas _condicional_ ao carro estar em A é de 1/3 (probabilidade do carro estar em A) multiplicado por ½ (probabilidade condicional do apresentador abrir B ou C condicional ao carro estar em A), resultando na probabilidade total de 1/6 de cada uma dessas possibilidade. 

Por outro lado, no caso do carro estar atrás das portas B ou C, só resta ao apresentador escolher uma das portas restantes, de modo que a probabilidade condicional é 1 e a probabilidade total é ⅓ . A figura 16 abaixo apresenta todos estes cenários e probabilidade através de uma árvore de decisão. 



<!-- Start of picture text -->
Carroestaem —Apresentador<br>abre. —-—~Probabilidade total -—~Resultado a0 trocar<br>Perde<br>12 aPortaB 113 x 1/2= 116<br>10 a v2 113 x 112 = 116 Perde<br>PortaA PortaC<br>Participanteescolheici A. 10 —1 113x1= 1/3 Ganha<br>Porta B<br>PortaC<br>18<br>Ganha<br>"|—,  "| 13x 1= 1/3<br>Porta ¢ Porta8<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

56 

Figura 16: Figura com os cenários e as probabilidades correspondentes para a árvore de decisão do exemplo citado. 

Vemos que a partir do momento que o participante escolhe a porta A, o chamado _espaço amostral_ ou conjunto de possibilidades, possui apenas 4 opções: (Carro em) A e B (é aberta), A e C, B e C, C e B. 

Suponha que a porta C é aberta. Nosso objetivo se torna calcular a probabilidade do carro estar em A (nossa escolha) ou B (trocar) condicional à abertura da porta B. Em estatística, essas probabilidades são descritas através da notação 𝑃(𝐴|𝐶) e 𝑃(𝐵|𝐶). Para facilitar o entendimento, vamos recorrer a equação da Probabilidade Condicional: 



Usando os cálculos que fizemos na Figura 16, a equação se torna: 



e: 



Ou seja, a probabilidade de ganhar o carro ao trocar de porta é de ⅔ e não ½ como a intuição levaria a acreditar. 

A teoria de probabilidade é um campo de estudo vasto e com muitas aplicações. Para um profissional de análise de dados, sua principal 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

57 

aplicação é permitir quantificar a incerteza na análise de variáveis quantitativas. Em especial, são conceitos de probabilidade que nos permitem _extrapolar_ resultados obtidos em amostras para um conjunto maior de dados. Mas esse é um tema para uma próxima aula! 

Nesta aula vimos como a teoria da probabilidade pode nos ajudar a resolver problemas do cotidiano utilizando técnicas como a da probabilidade condicional. 

### Aula 2.5: Variáveis Aleatórias 

Em estatística, chamamos de _Variável Aleatória_ uma quantidade X qualquer que assume valores com uma certa probabilidade. Dizemos que uma variável aleatória é _discreta_ quando ela somente pode assumir valores inteiros (por exemplo, o lançamento de um dado). Por outro lado, uma _variável aleatória contínua_ é aquela que pode tomar qualquer valor em um intervalo4. 

Exemplos: 

- **Variáveis Discretas:** lançamento de um dado, número de filhos, ocorrer ou não fraude. 

> 4 Mais formalmente, uma variável aleatória é contínua quando seu conjunto de valores é qualquer intervalo dos números reais. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

58 

- **Variáveis Contínuas:** tempo, valor de uma transação bancária, altura. 

Para poder calcular a probabilidade de um valor específico, usamos uma função de probabilidade. Essa função será diferente no caso da variável discreta ou contínua, por isso a importância de entender essa distinção. A função de probabilidade é geralmente apresentada na seguinte forma5 



Vamos continuar com nosso exemplo do jogo de dados. No exemplo 5.3 mostramos que a probabilidade de obter um número qualquer, digamos o número 3, em um jogo de dados não-viciado é igual a 1/6 e é a mesma para qualquer um dos 6 resultados possíveis. Formalmente, dizemos que a função de probabilidade de um jogo de dados é uniforme e calculada por 



A figura 17 abaixo mostra a probabilidade de cada resultado graficamente: 

> 5 Uma função de probabilidade discreta também satisfaz algumas outras condições matemáticas que não estão expressas aqui. Ver Magalhães e Lima (2023, p.70) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

59 



<!-- Start of picture text -->
Probabilidade de um jogo de Dados<br>0.200<br>0.175<br>’ , , ° ° °<br>0.150) | I 1 i i I<br>1 1 \ \ \ 1<br>v ' 1 ' 1 1 '<br>gots)<br>Fy8 0.1004 1 1 ' ' ' \<br>3&0.075 '11!i 1 1'1' ' ' 1<br>'' ' ' ' '<br>0.0507 4H 1H i'i i 1<br>'t ' ' ' '<br>0.0255 |I 'I {1{ i I<br>tI 1 1 1 t<br>1 1 \ ' 1 1<br>0.000<br>1 2 3 4 5 6<br>Resultado<br><!-- End of picture text -->

Figura 17: Probabilidade de um jogo de dados. 

Existem infinitas funções de probabilidades possíveis, e principalmente no caso de variáveis contínuas, seu cálculo pode ser extremamente complexo. Além da probabilidade de _X_ ter um valor específico, também é útil calcular a soma das probabilidades acumuladas de X, chamada de _função de distribuição acumulada_ : 



Seguindo o exemplo do jogo de dados, é fácil mostrar que a função de distribuição acumulada “dá pulos” de igual tamanho de modo que a probabilidade acumulada segue uma tabela: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

60 

|Resultado|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|P(X=x)|1/6|1/6|1/6|1/6|1/6|1/6|
|P(X<x)|1/6|2/6|3/6|4/6|5/6|6/6=1|



Também é conveniente utilizar um gráfico de barras para apresentar uma distribuição acumulada (Figura 18): 



<!-- Start of picture text -->
Funcao de Distribuigao Probabilidade Acumulada - Jogo de Dados<br>1.0<br>08<br>»<br>& 0.6<br>z<br>rt3<br>s°<br>= 04<br>0.2<br>0.0<br>1 2 3 4 5 6<br>Resultado<br><!-- End of picture text -->

Figura 18 - Função de Distribuição Probabilidade Acumulada - Jogo de Dados. 

Você deve estar se perguntando o porquê de estarmos discutindo fórmulas e conceitos matemáticos em um curso de estatística para análise de dados.  O objetivo aqui é construir a intuição para entendermos os modelos de distribuição de probabilidade, como a tão famosa 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

61 

“distribuição normal”. Como veremos, toda e qualquer distribuição de probabilidade é uma forma particular desta função! 

Vamos recapitular: 

- _Variável Aleatória_ : uma quantidade X qualquer que assume valores com uma certa probabilidade. 

- _Variável aleatória discreta é_ quando ela somente pode assumir valores inteiros, por exemplo, o lançamento de um dado ou o número de filhos de uma família. 

- _Variável aleatória contínua_ é aquela que pode tomar qualquer valor em um intervalo, por exemplo, a renda de uma pessoa em reais ou o peso dela em quilos. 

- Para poder calcular a probabilidade de um valor específico, usamos uma função de probabilidade. 

- Além da probabilidade de _X_ ter um valor específico, também é útil calcular a soma das probabilidades acumuladas de X, chamada de _função de distribuição acumulada._ 

### Aula 2.6: Distribuições de Probabilidade Discretas 

Na grande maioria dos casos práticos, não é necessário estimarmos uma distribuição de probabilidade mas tão somente identificar uma função já calculada que melhor se adequa aos nossos dados. Para realizar essa 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

62 

definição fazemos uso de técnicas visuais, revisão de literatura ou mesmo de testes estatísticos avançados. Além disso, veremos que com um número suficientemente grande de observações algumas distribuições se aproximam da tão popular distribuição normal, ou “curva de sino”. 

Nesta aula falaremos das distribuições mais famosas de variáveis discretas e seus principais usos. Não entraremos em detalhes de cálculos. Para isso, você pode consultar as referências deste módulo ou utilizar as funções disponíveis nos pacotes estatísticos apresentados nos exemplos. 

Já falamos da distribuição uniforme anteriormente. Dizemos que uma variável aleatória segue uma distribuição uniforme se a probabilidade é igual para cada um dos seus valores. Exatamente o caso de um jogo de dados. A figura 19 abaixo apresenta o gráfico da função de probabilidade para uma distribuição uniforme entre 0 e 9. 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

63 



<!-- Start of picture text -->
Distribuigao Uniforme<br>0.14<br>0.12<br>Fol, e@ @© © © © © © © @ @<br>Fad ! t t t ! t t t ' t<br>ri 1 ' 1 1 1 ' 1 1 1 '<br>ee i i I { i i I I i 1<br>2 ee<br>‘30.064 !a 1 1 1 ' 1 1 1 ' 1<br>8\\''1<br>£' ' ' ' ' ' ' 1 ' 1<br>Foooli Fo fob PoE PoE EG<br>0.04 ' ' ' ' i ' ' ' 1 '<br>''''''<br>'t ' 1 ' t ' t ! t<br>1 t t t 1 t ' t 1 t<br>0.02 1 ' i i 1 1 ' 1<br>'tt1it<br>1t t 1 1 t t 1 1 t<br>1 t t 1 1 t t 1 1 t<br>0.00<br>o 1 2 3 4 #5 6 7 8 9<br>Resultado<br><!-- End of picture text -->

Figura 19: Gráfico com as probabilidades da distribuição uniforme. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

64 

#### **Exemplo 5.8: Distribuição Uniforme** 

O código abaixo simula a geração de uma variável aleatória a partir de uma distribuição uniforme com valores entre 0 e 9. Note que conforme aumentamos o tamanho de n, a frequência relativa dos valores se aproxima da distribuição teórica. 

Python import seaborn as sns from scipy.stats import uniform 

# Números aleatórios da distribuição uniforme 

n = 100000 start = 0 width = 10 

data_uniform = uniform.rvs(size=n, loc = start, scale=width) 

ax = sns.displot(data_uniform, 

binwidth=1, kde=True, color='black', stat="density") 

ax.set(xlabel='Valores ', ylabel='Frequência Relativa', title='Distribuição Uniforme n=%d' % n) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

65 



<!-- Start of picture text -->
Distribuigao5 Uniforme n=100<br>ous<br>oso<br>:<br>§ 125<br># 0.100<br>4<br>E cos<br>0050<br>002s<br>000<br>2 4 Valores6 ar)<br><!-- End of picture text -->



<!-- Start of picture text -->
Distribuicaos Uniforme n=1000<br>oa2<br>010<br>§ 008<br>g<br>8 006<br>3<br>£<br>008<br>02<br>0.00<br>° 2 4 Valores 6 ey<br><!-- End of picture text -->



<!-- Start of picture text -->
Distribuicdo Uniforme n=100000<br>010<br>0.08<br>$ oe<br>002<br>0.00<br>° 2 4 6 8 10<br>Valores<br><!-- End of picture text -->

Existem casos em que a variável analisada assume somente dois valores, por exemplo, verdadeiro ou falso, sim ou não, fraude ou não-fraude etc. Neste caso, seria muito conveniente conseguir calcular a probabilidade de obtermos sucesso ou fracasso em cada um desses eventos, a que chamamos de _Ensaios de Bernoulli_ .  Por exemplo, em um jogo de cara ou coroa, ao jogar uma moeda conseguimos imaginar que a probabilidade de obter cara é exatamente 50%. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

66 

Formalmente, dizemos que uma variável aleatória _X_ segue um modelo de _Bernoulli_ se atribui 1 ou 0 à ocorrência de sucesso ou fracasso, respectivamente. Com _p_ representando a probabilidade de sucesso, 0 ≤ _p_ ≤ 1 e sua função de probabilidade representada por: 



Agora imagine que resolvemos jogar uma moeda um número _n_ de vezes, digamos 10 vezes, e contar o número de vezes que obtivemos o resultado “cara”. Qual a probabilidade de obter pelo menos 4 caras? Como respondemos isso? 

Para isso usaremos um novo modelo discreto, chamado de _modelo binominal_ e que tem um papel importantíssimo na estatística. Sua principal propriedade vai ser  a de aproximar a distribuição discreta da distribuição normal. Mas isso é assunto para uma próxima aula! 

Uma variável aleatória Binomial conta o número total de sucessos em _n_ ensaios e tem sua função de probabilidade dada por: 





indicar que a variável aleatória _X_ segue um modelo binomial com parâmetros _n_ e _p_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

67 

#### **Exemplo 5.9:** 

Vamos supor por exemplo que a probabilidade de uma transação financeira do BanVic ser realizada com sucesso é de 90%, sendo que os demais 10% podem incluir falhas na transação, anti-fraude etc. Suponha que nosso time de qualidade resolve obter uma amostra aleatória de 20 transações, qual a probabilidade dele encontrar exatamente 5 transações que falharam (ou de forma equivalente, 15 sucessos)? 

Para resolver esta questão, podemos substituir os parâmetros abaixo na função de probabilidade binomial para P(X=5): 

n = 20 (tamanho do experimento) 

p = 0,9 (probabilidade de sucesso na transação) 

k = 15 ( total de sucessos) 

Que retorna o valor de aproximadamente 3,2%. 



<!-- Start of picture text -->
Python<br>from scipy.stats import binom<br>n = 20<br>p = 0.9<br>k = 15<br>binomial_prob = binom.pmf(k, n, p)<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

68 

print("Probabilidade Binomial:", binomial_prob) 

Agora vamos imaginar um outro cenário. Nosso time de desenvolvimento do BanVic está testando um novo sistema de transações. Para poder torná-lo um novo padrão, foi estabelecida uma meta de que a primeira transação com falha não pode ocorrer antes da 10ª transação realizada. Sabendo que esse sistema novo tem uma probabilidade de uma transação ocorrer com sucesso de 95%, resolvemos calcular a probabilidade do novo sistema atingir a meta. Para isso vamos usar um novo modelo de probabilidade, o modelo geométrico. 

O modelo geométrico pode ser pensado como o número de tentativas de um evento do tipo “sucesso-fracasso” até que ocorra o primeiro sucesso. Seu cálculo é dado pela seguinte fórmula: 



onde k é o número de tentativas e a notação é _X_ ~G _(p)_ . 

Podemos reescrever o evento acima considerando qual a probabilidade de ocorrer uma transação com falha (nosso “sucesso”) até a 10ª tentativa, ou seja, teremos: 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

69 

Realizando alguns cálculos ou utilizando um software estatístico (ver exemplo 5.10) rapidamente obtemos que a probabilidade de se obter uma falha na 10ª tentativa é de aproximadamente 2.43%. 

Será que essa é nossa resposta? Vamos pensar um pouco mais. Se queremos saber a probabilidade de uma falha até a 10ª transação, é evidente que também não podemos ter uma falha com 9 transações, 8 transações e assim sucessivamente. Logo, precisamos calcular a probabilidade _cumulativa_ de falhas até a 10ª transação. Como podemos ver no Exemplo5.10b, essa probabilidade é 53.67%.  No exemplo 5.10c é possível ver como a distribuição se altera com a probabilidade de sucesso. 

#### **Exemplo 5.10a:** 

O código python abaixo calcula a probabilidade geométrica de se obter um sucesso após 10 tentativas em uma variável aleatória _X ~G(0,05)_ : 

Python # Exemplo 5.10a from scipy.stats import geom k=15 p = 0.05 geom_prob = geom.pmf(k,p) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

70 

print(f"Probabilidade Geométrica: {geom_prob:.4%}") 

**Exemplo 5.11b:** O código python abaixo calcula a probabilidade acumulada de se obter um sucesso até 10 tentativas em uma variável aleatória _X ~G(0,05)_ : 

Python # Exemplo 5.10b from scipy.stats import geom k=15 p = 0.05 geom_prob = geom.cdf(k,p) print(f"Probabilidade Acumulada Geométrica: {geom_prob:.4%}") 

#### **Exemplo 5.11c:** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

71 

Alterando a probabilidade _p_ de sucesso, torna-se cada vez mais “fácil” obter o sucesso: 



<!-- Start of picture text -->
Probabilidade Acumulada de obter sucesso até a N-ésima tentativa<br>Funcao de Distribuicao Geométrica com parametros p=0.05,p=0.1, p=0.5<br>10 ponents eA a ee<br>H<br>i ’<br>3sipft<br>2<br>5 0.6 pfPoy<br>< ior<br>3wv podia<br>6 iy<br>z 1<br>2047 : |<br>3 i}<br>a iy<br>° iy<br>a it<br>024 3}<br>HI —<br>i p_005<br>x --> pol<br>0.0 ve p05<br>t) 20 40 60 80 100<br>Tentativas<br><!-- End of picture text -->



<!-- Start of picture text -->
Python<br>from scipy.stats import geom<br>import seaborn as sns<br>import numpy as np<br>import pandas as pd<br>x= np.arange(0, 100, 1)<br>p1 = 0.05<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

72 

y1 = geom.cdf(x, p1) 

p2 = 0.10 y2 = geom.cdf(x, p2) p3 = 0.5 

y3 = geom.cdf(x, p3) 

df = pd.DataFrame(list(zip(y1,y2,y3)), columns = ['p_005','p_01','p_05'], index=x) 

ax = sns.lineplot(data = df) 

ax.set(xlabel='Tentativas ', 

ylabel='Probabilidade Acumulada') 

plt.suptitle("Probabilidade Acumulada de obter sucesso até a N-ésima tentativa",fontweight='bold',size=12, x=0.13, ha='left') 

plt.title("Função de Distribuição Geométrica com parâmetros p=0.05,p=0.1, p=0.5", size=10,x=0.01,loc='left') 

Para finalizar nossa aula sobre distribuições de probabilidade para variáveis discretas, vamos falar de uma distribuição muito importante para modelar a ocorrência em um determinado período de tempo, a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

73 

distribuição de _Poisson_ . Como de costume, vamos começar com um exemplo. 

Voltando ao nosso exemplo do desenvolvimento de um novo sistema de transações, os engenheiros do BanVic estão preocupados com a possibilidade do sistema suportar um pico de transações durante um segundo, que supere a capacidade de 6 transações por segundo do sistema. Utilizando dados históricos, descobrimos que a frequência média de ocorrência, ou _taxa de ocorrência_ , atualmente é de 4,5 transações por segundo. Como podemos calcular a probabilidade de chegarem mais de 6 transações por segundo? Poisson! 

Dizemos que uma variável aleatória _X_ tem uma distribuição de Poisson com parâmetro 𝛌 (lambda) > 0 se sua função de probabilidade é dada por 



com o parâmetro 𝛌 chamado usualmente de _taxa de ocorrência_ . A notação da distribuição Poisson é _X ~Po(_ 𝛌 _)_ 

Agora estamos prontos para resolver nosso problema do BanVic. Como já mencionamos, a taxa de ocorrência é atualmente de 4,5 transações por segundo. A forma mais direta de calcular é utilizar a função de probabilidade da Poisson para os casos onde k=0, 1, …, 6. e subtrair de 1 (a probabilidade total). Da tabela da Poisson obtemos, (ver código no exemplo 5.6): 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

74 

|k (número de<br>transaçõe)|0|1|2|3|4|5|6|k≤6|
|---|---|---|---|---|---|---|---|---|
|Probabilidade<br>(%)|1,11|5,0|11,25|16,87|18,98|17,08|12,81|83,10|



Logo a probabilidade de um pico de transações maior que 6 no sistema do BanVic é 1 - 83,10% = 16,89%. 

#### **Exemplo 5.11a:** 

Para obter valores de probabilidade de uma Poisson com 𝛌 = 4,5 usamos o código abaixo: 

Python from scipy.stats import poisson import numpy as np lmbda=4.5 k = np.arange(0, 7, 1) poisson_prob = poisson.pmf(k, lmbda) print (poisson_prob) print(f"Probabilidade X<=6: {sum(poisson_prob):.4%}") print(f"Probabilidade X>6: {1-sum(poisson_prob):.4%}") 

#### **Exemplo 5.11b:** 

Graficamente temos: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

75 



<!-- Start of picture text -->
Probabilidade de K transacgoes por segundo<br>Fungo de Distribuicao Poisson com parametro lambda=4,5,<br>0.175<br>0.150<br>@ 0-125<br>38<br>2<br>3 0.100<br>@<br>2= 0.075<br>0.050<br>0.025<br>0.000<br>0123 45 67 8 9 10111213 141516171819<br>Transacées<br><!-- End of picture text -->

#### Vamos recapitular: 

- _Distribuição Discreta_ : são distribuições de probabilidades utilizadas para variáveis aleatórias que só tomam valores discretos como número de ocorrências, número de filhos, etc.. 

- _Distribuição Uniforme_ : utilizada quando qualquer resultado tem a mesma probabilidade de ocorrência, como um jogo de dados. 

- _Distribuição de Bernoulli_ : utilizada para descrever o resultado de um único evento do tipo sucesso-fracasso. 

- _Distribuição Binomial_ : é usada para repetições de eventos do tipo sucesso-fracasso. 

- _Distribuição Geométrica_ : usada para calcular o número de tentativas até a 1ª ocorrência de um evento. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

76 

- _Distribuição de Poisson:_ usada para calcular a taxa média de ocorrência de um evento em um intervalo de tempo ou espaço. 

### Aula 2.7: Distribuição Normal 

Nesta aula discutiremos como caracterizar variáveis aleatórias que podem assumir qualquer valor em um intervalo dos números reais, as variáveis contínuas. É seguro afirmar que na grande maioria dos casos de uso da estatística estaremos falando de variáveis contínuas, como renda, _ticket médio_ , tempo de uso de um equipamento, etc. Assim como no caso discreto, para atribuir probabilidade às variáveis contínuas usaremos as distribuições de probabilidade. Em especial, falaremos da distribuição de probabilidade mais popular de todas, a distribuição normal. 

Como em muitos outros casos da estatística, a origem da distribuição normal surgiu há quase 300 anos a partir de um problema de jogos de azar 6 e da nossa já conhecida distribuição binomial. Vamos imaginar um jogo de cara ou coroa, onde a probabilidade de cada resultado é igual a 50%. Ao jogarmos uma moeda 10 vezes, contamos o número de caras. Repetimos esse experimento por 10 vezes e construímos um histograma com as frequências de caras. Em seguida, repetimos o processo com 100, 1000 e 100000 experimentos (Figura 20): 

> 6 A primeira aparição da Distribuição Normal é atribuída a Abraham De Moivre em seu livro _Doctrines of Chance_ de 1733. <u>Fonte</u> 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

77 



<!-- Start of picture text -->
035 DistribuicdoopBinomial n=10,p=0.5<br>030<br>025<br>g<br>$ 020<br>.<br>$ ois<br>o<br>é<br>010<br>0.05.<br>0.00 3 4 5 6 7 8<br>Namero de Caras<br><!-- End of picture text -->



<!-- Start of picture text -->
Distribuicaos Binomial n=100,p=0.5P<br>010<br>0.08<br>&<br>3<br>@ 0.06<br>3<br>g<br>= 0.04<br>0.02<br>0.00 375 40.0 425 45.0 47.5 50.0 525 55.0 575<br>Namero de Caras<br><!-- End of picture text -->



<!-- Start of picture text -->
Distribuicao Binomial n=1000,p=0.5<br>0.030<br>0.025<br>©<br>% 0.020<br>8<br>§<br>© 0015<br>o.o10<br>00s<br>0.000 460-480 =—«500520. SH0<br>Numero de Caras<br><!-- End of picture text -->



<!-- Start of picture text -->
Distribuicéo Binomial n=100000,p=0.5<br>0.0030<br>2.0025<br>‘= 0.0020<br>8<br>3<br>% 9.0015<br>a<br>*<br>0.0010<br>0.0005<br>0.0000 49400 49600 49800 50000 50200 50400 50000 50800<br>Numero de Caras<br><!-- End of picture text -->

Figura 20: Gráfico da distribuição binomial com número de amostras iguais a 10, 100, 1000 e 100000. 

Você deve ter notado que conforme aumentamos o número de experimentos ( _n_ ), nossa curva se aproxima de uma curva em “formato de sino”, uma das características da distribuição normal. Como o cálculo de probabilidades de uma binomial com n grande se torna muito trabalhoso, 

> Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

78 

os estatísticos desenvolveram a distribuição normal utilizando de conceitos de cálculo que permitem calcular a área embaixo da curva, ou seja, a probabilidade, mais facilmente. Na prática, os valores da distribuição normal já estão disponíveis em tabelas e softwares estatísticos e não é necessário mais calculá-los individualmente. De qualquer forma, vamos manter nosso padrão e apresentar a definição da Normal abaixo. 

Dizemos que uma variável aleatória contínua _X_ segue uma distribuição Normal com parâmetros μ (“mi”) e 𝝈² (“sigma”) se sua função densidade é dada por: 



Usamos a notação _X_ ~N( μ , 𝝈²) para indicar que _X_ tem uma distribuição normal com parâmetros μ e 𝝈².  Além disso, é importante falar de algumas propriedades da Normal: 

- 1) A distribuição normal é simétrica em relação à _μ_ 

- 2) A função densidade (𝑓(𝑥)) tende a 0 quando x se aproxima de valores muito pequenos ou muito grandes. Ou seja, a probabilidade de casos extremos é pequena. 

- 3) O valor máximo da função densidade ocorre quando x = _μ_ . Ou seja, a média é a melhor estimativa para a normal. 

Mas o que significam esses parâmetros? De forma resumida, _μ_ é a média e 𝝈² a variância da distribuição. O cálculo da distribuição normal para 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

79 

diferentes valores desses parâmetros é complexo e envolve o conhecimento de cálculo. Ocorre que se realizarmos algumas manipulações matemáticas, que não detalharemos aqui, conseguimos mostrar que se definirmos uma nova variável 𝑍 =<sup>𝑋−</sup> σ<sup><u>µ</u></sup> ~~,~~ ela terá uma distribuição _N_ (0,1). É justamente a Normal com parâmetros μ =0 e 𝝈² = 1 que encontramos nas tabelas estatísticas, a chamada _Normal Padrão._ Como veremos, esse resultado é especialmente importante na área de inferência. 

Vamos mostrar o uso prático da Normal com um exemplo. A área de pessoas do BanVic quer realizar uma campanha interna de divulgação da nova marca do banco através da distribuição de camisetas. Através do cadastro de funcionários, sabemos que a média de altura dos funcionários do banco é de 1,75m e o desvio-padrão é de 10cm. Para que os funcionários “mais altos” não fiquem de fora, queremos calcular qual a probabilidade de um funcionário do BanVic ter entre 1,90m e 2,10m. Sabendo que a altura é uma variável que segue a distribuição normal, como fazemos esse cálculo? 

Começamos definindo nossa variável aleatória _X_ como a _altura de um funcionário_ . Nosso problema pode ser definido como a probabilidade 𝑃(1, 90 ≤𝑋≤2, 10), sendo X~ _N_ ( μ =1,75, 𝝈² = 0,1²). Queremos utilizar a tabela da Normal Padrão, então procedemos da seguinte forma: 

𝑃(𝑎 ≤𝑋≤𝑏) = 𝑃(𝑎 −µ ≤𝑋− µ ≤𝑏 −µ) 

= 𝑃(1, 9 −1, 75 ≤𝑋−µ ≤2, 10 −1, 75) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

80 





Nosso objetivo, portanto, é calcular a área sombreada na figura 21 abaixo. Para nossa sorte, dispomos de uma tabela de valores da distribuição normal já calculada previamente para diferentes valores de Z. Agora precisamos saber como utilizá-la! 



<!-- Start of picture text -->
Probabilidade da Altura entre 1,9 e 2,1m<br>Distribuigao Normal<br>0.5<br>0.4<br>8 03<br>zos<br>ao<br>2<br>&£ 0.2<br>0.1<br>0.0 Zb<br>-4 -3 -2 -1 t) 1 2 3 4<br>Zscore<br><!-- End of picture text -->

Figura 21: Gráfico dos scores da distribuição normal. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

81 

A tabela 08 abaixo tem os valores calculados para a probabilidade de Z<z, onde z é o valor que queremos buscar. Como a distribuição normal é simétrica, os valores partem de 0,507. Como vemos na Figura 21, para calcular a área sombreada precisamos calcular P(Z<3,5) - P(Z<1,5) na tabela (Tabela 08): 

𝑃(1, 5 ≤𝑍≤3, 5) = 𝑃(𝑍≤3, 5) − 𝑃(1, 5 ≤𝑍) = 0, 9998 −0, 9332  = 0, 0666 

Logo, a probabilidade de um colaborador do BanVic medir entre 1,90 e 2,10 é de aproximadamente 6,7%. 

Tabela 08: Tabela da Distribuição normal padrão P(Z<z). 

||**Tabela**|**da Distrib**|**uição norm**|**al padrã**|**o P(Z<z**|**)**|
|---|---|---|---|---|---|---|
|**z**|**0,00**|**0,01**|**0,02**|**0,03**|**(...)**|**0,09**|
|**0,0**|0,50|0,5040|0,5080|0,5120||0,5359|
|**0,1**|0,5398|0,5438|0,5478|0,5517||0,5753|
|**(...)**|||||||
|**1,5**|**0,9332**||||||
|**3,5**|**0,9998**||||||



#### **Exemplo 5.13a: Distribuição Normal Padrão** 

Python # Exemplo 5.9a from scipy.stats import norm 

7 Isso ocorre pois todos os valores de Z negativos somam exatamente 50%. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

82 

norm_prob_1_5 = norm.cdf(1.5) norm_prob_3_5 = norm.cdf(3.5) norm_prob = norm_prob_3_5 - norm_prob_1_5 print(f"Probabilidade Acumulada: {norm_prob:.4%}") 

#### **Exemplo 5.13b: Distribuição Normal Padrão** 

Python #Exemplo 5.9b from scipy.stats import norm import numpy as np import seaborn as sns import matplotlib.pyplot as plt z = np.arange(-4, 4, 0.1) norm_prob = norm.pdf(z) ax = sns.lineplot(x=z, y=norm_prob) y_max=0.5 ax.set_ylim(0,y_max) plt.xlabel('Z-score') plt.ylabel('Probabilidade') 

#Arrumar os eixos ax.axvline(0,ymax=0.4/y_max, color='black', linewidth=0.5) ax.text(0,0.42,'f(x)') 

# Shade the area between Z-scores 2.5 and 3.5 shade = np.linspace(1.5, 3.5, 100) ax.fill_between(shade, 0, norm.pdf(shade), color='gray', alpha=0.9) ax.axvline(1.5,ymin = 0, ymax=norm.pdf(1.5)/y_max) ax.axvline(3.5, ymax=norm.pdf(3.5)/y_max) 

plt.suptitle("Probabilidade da Altura entre 1,9 e 2,1m",fontweight='bold',size=12, x=0.13, ha='left') plt.title("Distribuição Normal", size=10,x=0.01,loc='left') 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

83 

print(norm.pdf(0)) 

Vamos recapitular: 

A distribuição normal é a mais popular das distribuição estatísticas e está presente em muitas disciplinas distintas. Existem muitos fenômenos aleatórios na natureza ou nos negócios em que a maioria dos valores se encontram próximos da média. Além disso, a Normal também nos permite aproximar outras distribuições desconhecidas, um resultado muito importante para a inferência estatística. 

### Aula 2.8: Distribuições não Normais 

Na aula anterior você viu bastante informação e entendeu os principais conceitos sobre a distribuição normal. Agora precisamos entender e saber como tratar os dados que não seguem essa distribuição. 

Você já se perguntou porque a distribuição normal é a mais importante da estatística se raramente temos dados seguindo esse padrão de distribuição? A grande maioria dos fenômenos reais tem características que fazem a nossa tão famosa curva de sino ter um formato bastante “deformado”. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

84 

Mas o que de fato é uma distribuição não normal? Considera-se que a não normalidade acontece quando alguma das variáveis que descreve um fenômeno segue qualquer distribuição que não seja a normal. 

Distribuições não normais são aquelas que não possuem a forma simétrica de sino da distribuição normal. Elas podem ser assimétricas, ter caudas mais longas ou mais curtas, ou mesmo múltiplos picos. Para ficar mais claro, vamos a um exemplo. 

Imagine que você está jogando um dado. A chance de cada face sair é a mesma, e a distribuição dos resultados ao longo de muitas jogadas se aproxima de uma distribuição uniforme com formato de sino. 

Agora, pense em medir a velocidade do vento em diferentes lugares. A distribuição dessas velocidades não será uniforme, mas sim assimétrica, e muito provavelmente terá caldas mais alongadas em algum dos lados, ou até mesmo nos dois lados. Regiões onde há ventanias fortes apresentará uma distribuição com cauda longa à direita, indicando que há uma frequência de ventos intensos. Em contrapartida, nas áreas onde os ventos são mais fracos, a distribuição pode ter uma cauda à esquerda, indicando a ocorrência de ventos fracos. 

Fenômenos não normais são mais corriqueiros e fazem parte do nosso cotidiano muito mais do que fenômenos ditos como normais. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

85 

Existem algumas formas, além das visuais, para identificarmos se uma distribuição é normal ou não. Essas formas são chamadas de momentos e, usualmente, são quatro: 

a) o primeiro momento está relacionado com as **medidas de localização** ou tendência central (média, mediana e moda): Uma distribuição não normal tem média diferente de zero e a média, mediana e moda não coincidem; 

b) o segundo está relacionado com as **medidas de dispersão** (variância, desvio padrão, coeficiente de variação e amplitude): Distribuições com variância muito grande indica que os dados estão amplamente dispersos, enquanto uma variância baixa sugere que os dados estão mais concentrados em torno da média; 

c) o terceiro momento está relacionado às **medidas de assimetria** : Mede a simetria da distribuição dos dados. Uma distribuição assimétrica tem assimetria diferente de zero. Valores positivos indicam cauda à direita, e valores negativos indicam cauda à esquerda; 

d) o quarto momento está relacionado com a **proeminência do pico e da cauda da curva** de distribuição, também chamado de curtose: Curtose zero indica uma distribuição mesocúrtica (semelhante à normal). Curtose positiva indica distribuição leptocúrtica (mais afunilada e com caudas longas). Curtose negativa indica distribuição platicúrtica (mais achatada). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

86 

Pensando nas medidas de localização, uma distribuição é normal quando a sua média é igual a zero. Ela pode ainda ser normal simétrica e então sua média deve ser igual a sua mediana e a sua moda. 

No entanto, quando isso não acontece e temos um alargamento da curva, em especial para um dos lados, dizemos que a distribuição tem “caudas pesadas”. Esse fenômeno está associado aos dois primeiros momentos que falamos anteriormente, aqueles relacionados às medidas de localização e dispersão. 

Diz-se que algumas distribuições possuem caudas pesadas, no sentido de que elas apresentam valores distantes das medidas de localização. Caudas pesadas ocorrem, por exemplo, quando a variância é muito grande, ou até mesmo infinita. Também podem estar associadas à ocorrência de valores discrepantes ou extremos (outliers), entendidos como valores muito distantes dos demais. 

Embora um outlier possa resultar de um erro de medida, ele também pode ser um resultado genuíno, indicando um comportamento extremo, que merece ser estudado, e não apenas removido. 

Caudas pesadas, geralmente, se manifestam com uma proeminência do pico e da cauda da distribuição, podendo ser medida pela curtose. Quando a curtose é igual a zero temos uma distribuição mesocúrtica, e o seu desenho tem um achatamento semelhante ao da distribuição normal. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

87 

Nos casos em que a curtose é positiva a distribuição ganha o nome de leptocúrtica. Isso indica que a distribuição está mais afunilada e com caudas mais alongadas do que as da distribuição normal, no sentido de que se podem obter valores muito distantes da média. 

A curtose negativa, chamada platicúrtica, indica uma distribuição mais achatada do que a distribuição normal. Portanto, curvas mais ou menos achatadas em relação a uma distribuição normal significam não normalidade. A imagem abaixo exemplifica cada uma dessas possibilidades de curtose. 



<!-- Start of picture text -->
0,5<br>04 — Leptocurtica<br>Mesocurtica<br>NY<br>0,3<br>0,2<br>— Platicirtica<br>0,1<br>0,0 —<br>-4 3 2 -l 0 1 2 3 4<br><!-- End of picture text -->

Figura 22: Gráfico com os diferentes tipos de curtose. 

Conforme a média vai se distanciando da mediana começamos a perceber o terceiro momento que falamos antes, a assimetria. Quando a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

88 

assimetria é igual a zero temos uma distribuição simétrica, como a normal. 

Valores positivos para a assimetria indicam que a distribuição possui uma cauda alongada à direita. Nesses casos a Moda é maior que a Mediana que são maiores que a Média (Figura 23). 



<!-- Start of picture text -->
Distribuicdo Assimétrica Positiva<br>i i i <= Média<br>H H H ---+ Mediana<br>06 H H H === Moda<br>04 H H H<br>§ 03 H i H<br>& H H ‘<br>02 | i H<br>oa i i i<br>° H 2 3 4 3<br>Valores<br><!-- End of picture text -->

Figura 22: Gráfico da distribuição assimétrica positiva. 

Quando o valor da assimetria é negativo temos uma cauda alongada para a esquerda. Aqui a Média é maior que a Mediana e que por sua vez são maiores que a Moda (Figura 23). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

89 



<!-- Start of picture text -->
Distribuicao Assimétrica Negativa<br>2.5] ---- Média Ty i<br>---- Mediana 1 an<br>---- Moda Ki}<br>1s od<br>Bro Ho<br>oo a2 os ry os Yo<br>\alores<br><!-- End of picture text -->

Figura 23: Gráfico da distribuição assimétrica negativa. 

As principais distribuições não normais incluem: 

1. **Distribuição exponencial** : frequentemente usada para modelar o tempo entre eventos aleatórios em um processo contínuo e independente (Figura 24). Por exemplo, imagine que você está monitorando o tempo de chegada dos clientes para serem atendidos no BanVic. Se essas chegadas forem aleatórias e independentes é provável que tenhamos um período onde os clientes chegaram em um intervalo menor de tempo, tal como nos períodos de pico. Dessa forma a curva de distribuição desses tempos tende a ter uma cauda alongada à direita. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

90 



<!-- Start of picture text -->
Distribuigao Exponencial<br>05 pot == Média<br>i pot se Mediana<br>i Pp ot —"- Moda<br>oa} | pot<br>i Pot<br>i Pot<br>i pod<br>237 | pot<br>z i pot<br>3 i Kt<br>& i \<br>0.2 i H 4<br>i pot<br>i Pot<br>ory i Pot<br>i pot<br>i Pot<br>i Pot<br>oo} !} pot<br>° 2 4 6 8 10<br>Valores<br><!-- End of picture text -->

Figura 24: Gráfico da distribuição exponencial. 

2. **Distribuição Binomial** : muito utilizada para descrever o número de sucessos em um número fixo de tentativas, onde cada experimento tem dois resultados possíveis: sucesso ou fracasso (Figura 25). Cada tentativa é independente e a probabilidade de sucesso permanece constante. Um exemplo clássico é o lançamento de uma moeda onde iremos modelar o número de “sucessos” nesses lançamentos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

91 



<!-- Start of picture text -->
Distribuicao Binomial<br>030 i === Média<br>i === Mediana<br>me --- Moda<br>025 it<br>i<br>it<br>0.20 it<br>8 it<br>3 it<br>Boas ii<br>2 it<br>8 it<br>I<br>0.10 iit<br>i<br>it<br>i<br>0.05 itit<br>it<br>0.00 it<br>3 2 3 3 3 ry<br>Valores<br><!-- End of picture text -->

Figura 25: Gráfico da distribuição binomial. 

3. **Distribuição Log-normal** : de todas as distribuições é a que mais se aproxima da distribuição normal e tem o resultado similar ao observado no Teorema do Limite Central. É utilizada para modelar variáveis que são o resultado da multiplicação de outras variáveis aleatórias positivas (Figura 26). De forma mais simples, ela é utilizada quando o logaritmo da variável de interesse segue uma distribuição normal. Um exemplo comum é a distribuição de rendas em uma população, que frequentemente tem uma distribuição assimétrica positiva. Quando modelamos com essa distribuição a curva resultante se aproxima de uma normal. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

92 



<!-- Start of picture text -->
Distribuicao Log-normal<br>rot === Média<br>t\ tot == Mediana<br>06 ‘tot => Moda<br>t\ i 4<br>0S 1 1 1<br>t \i ot<br>r \o4<br>04 H H<br>grt\<br>i1 \<br>a<br>00 hot ot<br>° 2 4 6 8 10<br>Valores<br><!-- End of picture text -->

Figura 26: Gráfico da distribuição Log-normal. 

4. **Distribuição Gamma** : É uma distribuição de probabilidade contínua muito utilizada para modelar o tempo até que um determinado número de eventos ocorra em um processo estocástico (processo que evolui de maneira imprevisível, governado por probabilidades). Sua principal característica é a assimetria positiva, mas a forma pode variar dependendo dos parâmetros da curva (Figura 27). Um exemplo de uso poderia ser o número de chamadas recebidas que o call center do BanVic recebeu. Se esperamos que o call center receba 5 chamadas, e o tempo entre as chamadas segue uma distribuição exponencial, então a soma desses tempos pode seguir uma distribuição gamma. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

93 



<!-- Start of picture text -->
Distribuicéo Gamma<br>H Tt === Média<br>0.175 H an "> Mediana<br>H rt =~ Moda<br>0.150 i \t<br>H i\i<br>HH<br>H<br>H tt<br>0.125 H<br>Hl tt<br>¥ o100 poor<br>& 0.075 ' ro<br>H tt<br>0.050 HHi tttthi<br>0.025 H tt<br>0.000 i tt<br>° 2 4 6 8 10 2 4<br>Valores<br><!-- End of picture text -->

Figura 27: Gráfico da distribuição Gamma. 

5. **Distribuição de Poisson** : A distribuição de Poisson é usada para modelar o número de eventos que ocorrem em um intervalo fixo de tempo ou espaço (Figura 28). Por exemplo, considere que estamos fazendo uma ação de marketing para o BanVic e queremos usar essa distribuição para modelar o número de pessoas impactadas pela ação no quarteirão onde o QG foi colocado. Se esses eventos ocorrem com uma taxa constante e independentemente uns dos outros, a distribuição de Poisson pode descrever o número de pessoas por hora, por exemplo. Esta distribuição é assimétrica, com a cauda se estendendo para a direita. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

94 



<!-- Start of picture text -->
Distribuicao de Poisson<br>0.25 \tH ===--- MédiaMediana<br>it<br>0.20 it<br>it<br>it<br>g 015 if<br>8 It<br>010 it<br>it<br>0.05 it<br>it<br>0.00 rt<br>3 2 4 6 3 10 2 1s<br>Valores<br><!-- End of picture text -->

Figura 28: Gráfico da distribuição de Poisson. 

6. **Distribuição Qui-Quadrado** : Amplamente utilizada em estatística descritiva, em especial nos testes de hipóteses e na construção de intervalos de confiança, é particularmente relevante em contextos onde se deseja avaliar a relação entre variáveis categóricas ou a adequação a um modelo estatístico. Essa distribuição é parametrizada pelos graus de liberdade, que estão intimamente relacionados ao número de observações, e assume apenas valores positivos, já que é baseada na soma dos quadrados dos valores observados. Quando temos valores muito pequenos de graus de liberdade essa distribuição tem assimetria positiva (à direita) e à medida que os graus de liberdade aumentam a curva vai se tornando simétrica (Figura 29). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

95 



<!-- Start of picture text -->
Distribuicéo Qui-Quadrado<br>0.175 i\dd 77> Mediana<br>1 \t 7 Meda<br>0.150 Hl \t<br>ozs itt<br>$0100 Pott<br>8 aors ott<br>o.0s0 hort<br>2s hottPott<br>Lott<br>2.000 hott<br>CY SS<br>valores<br><!-- End of picture text -->

Figura 29: Gráfico da distribuição Qui-Quadrado. 

Existem algumas formas de identificarmos a não normalidade de uma curva. Podemos fazer isso com o auxílio de visuais ou com testes estatísticos. 

A forma visual mais fácil e intuitiva de testar a normalidade é através de um gráfico do tipo histograma (Figura 30). Esse tipo de gráfico ajuda a identificar o formato da curva de distribuição dos dados e a identificar características importantes, que falamos anteriormente, como a assimetria, a curtose e a cauda pesada. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

96 



<!-- Start of picture text -->
Histograma da Distribuicéo Exponencial<br>250<br>200<br>$150<br>&<br>100<br>50<br>o<br>° 2 4 6 8 10 2 4 16<br>Valores<br><!-- End of picture text -->

Figura 30: Histograma da distribuição Exponencial. 

Além do histograma, outra forma de identificar a não normalidade é com o auxílio de gráficos do tipo box-plot. Esse gráfico, que tem o nome formal de box-and-whiskers-plot, nada mais é do que um sumário gráfico da curva de distribuição. Isso porque com ele conseguimos identificar a forma da curva, a existência de outliers, a posição da mediana em relação a curva, além dos quartis (Figura 31). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

97 



<!-- Start of picture text -->
Boxplot da Distribuicéo Exponencial<br>°<br>8<br>°<br>8<br>68<br>|2 ° ——<br>Valor<br><!-- End of picture text -->

Figura 31: Boxplot da distribuição Exponencial. 

Uma forma mais robusta de se identificar a não normalidade é através dos gráficos do tipo Q-Q plot. Este gráfico compara os quartis da distribuição dos dados com os quartis da distribuição normal padrão e desenha eles sobre uma linha, similar a um gráfico de dispersão. Desvios dos valores em relação a reta indicam a não normalidade (Figura 32). 



<!-- Start of picture text -->
QQ-Plot da Distribuicéo Normal<br>1<br>3 er ,<br>é<br>2<br>B-1<br>2<br>2 a 3 H 2<br>‘Theoretical Quantiles<br><!-- End of picture text -->



<!-- Start of picture text -->
QQ-Plot da Distribuicéo Exponencial<br>3<br>82<br>an<br>e<br>Boo<br>a<br>2<br>2 a 0 a 3 3 4<br>Theoretical Quantiles<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

98 

Figura 32: Q-Q plot de uma distribuição Normal e de uma distribuição Exponencial. 

Além das formas visuais, é possível que façamos alguns testes estatísticos para testar a normalidade. Os dois testes mais comuns são o de Shapiro-Wilk e o de Kolmogorov-Smirnov. 

O teste de Shapiro-Wilk é baseado na estatística _W_ . Esse parâmetro compara a distribuição dos dados a uma distribuição normal teórica. Quanto mais próximo a 1 for o valor calculado para _W_ , maior a evidência de que os dados estão normalmente distribuídos. No entanto este teste fica limitado ao tamanho da amostra, não sendo o teste mais indicado quando estamos lidando com um conjunto muito pequeno ou muito grande de dados. 

A fórmula básica do teste de Shapiro-Wilk é: 



onde: 

𝑎𝑖 é o coeficiente de Shapiro-Wilk, que dependem do tamanho da amostra, e é tabelado 

é o i-ésimo valor ordenado da amostra 𝑥𝑖 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

99 

#### 𝑥̄ é a média amostral. 

Já o teste de Kolmogorov-Smirnov, quando utilizado para testar a aderência, pode verificar se um conjunto de dados segue uma distribuição específica. Esse teste não é exclusivo da distribuição normal. Podemos utilizá-lo para testar a aderência a qualquer outra distribuição que não seja normal. Ele compara a distribuição dos dados observados com a distribuição teórica esperada. 

Esse teste é baseado na estatística D e ela é calculada como sendo a maior diferença absoluta entre as distribuições empírica (observada) e teórica. Sua fórmula é dada por: 



Onde: 

𝐹𝑛(𝑥) é a função de distribuição acumulada empírica (CDF) dos dados 

observados. 

𝐹𝑥( ) é a CDF da distribuição teórica que estamos testando. 

𝐷 é a maior diferença entre as duas funções. 

Trabalhar com dados não normais tem suas implicações. A grande maioria dos testes estatísticos assume a normalidade como premissa. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

100 

Uma vez que não conseguimos atendê-la podemos afetar significativamente o resultado do teste realizado. 

Em testes de hipóteses e intervalos de confiança, muitas abordagens tradicionais, como o teste t e a análise de variância (ANOVA), assumem que os dados seguem uma distribuição normal. Quando essa suposição não é atendida, os resultados podem ser distorcidos, levando a conclusões erradas, aumentando as chances de termos erros tipo I ou tipo II. Isso ocorre porque esses testes dependem de estimativas precisas da média e da variância, que são bastante sensíveis à forma da distribuição. 

Em modelagem estatística, a não-normalidade pode complicar a construção de alguns modelos, especialmente os de regressão. Modelos lineares e outras técnicas de modelagem, como regressão múltipla, frequentemente assumem que os resíduos do modelo seguem uma distribuição normal. Se os dados ou os resíduos não forem normais, isso pode comprometer a precisão das estimativas dos seus coeficientes. Além disso, a não-normalidade pode afetar a eficiência e a robustez do modelo. 

Uma das formas de se lidar com dados não-normais é por meio de transformações. Transformações como a logarítmica e a Box-Cox podem ser usadas para aproximar os dados da normalidade. A logarítmica é útil quando os dados são assimétricos e têm caudas longas. Já a transformação de Box-Cox permite encontrar a melhor transformação possível para tornar os dados mais simétricos. Esses dois tipos de 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

101 

transformação ajudam a estabilizar a variância e a melhorar a aplicabilidade de métodos estatísticos paramétricos. 

Além disso, existem testes não paramétricos que não assumem uma distribuição específica para os dados. Testes como o de Wilcoxon ou o de Kruskal-Wallis são alternativas poderosas quando a suposição de não normalidade é válida, permitindo comparações robustas entre os grupos sem depender da forma dos dados. 

Recapitulando: 

- ➢ Nesta aula vimos sobre as distribuições não normais. Vimos que a não normalidade ocorre quando as variáveis de um fenômeno não seguem a distribuição normal. Essas distribuições podem ser assimétricas, ter caudas mais longas ou curtas, ou até mesmo apresentar múltiplos picos. 

- ➢ Conhecemos os quatro momentos da distribuição que nos ajudam a identificar se uma distribuição é normal ou não. O primeiro momento está relacionado com as medidas de localização. O segundo momento refere-se à dispersão. O terceiro momento trata da assimetria.  E o quarto momento fala sobre a curtose. 

- ➢ Entre as principais distribuições não normais estão a distribuição exponencial, a distribuição binomial, a log-normal, a gamma, a Poisson e a qui-quadrado. Cada uma delas tem características específicas e é usada em contextos diferentes. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

102 

- ➢ Podemos identificar a não normalidade de forma gráfica com o auxílio de histogramas, boxplots e gráficos do tipo Q-Q plot, mas também conseguimos utilizar testes estatísticos para isso. 

- ➢ A não normalidade pode pôr em cheque os testes estatísticos que assumem a normalidade dos dados como premissa. 

- ➢ Podemos tratar a não normalidade com transformações nos dados para que estes passem a ter uma distribuição normal, ou ainda, podemos aplicar outros testes estatísticos não paramétricos aos dados. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

103 

## Parte 3: Inferência 

### Aula 3.1: Introdução a inferência 

Nas aulas anteriores aprendemos como podemos utilizar medidas como médias e desvios para responder perguntas sobre um problema de negócio qualquer. Por exemplo, podemos calcular a média de altura da população de dois países (ex. Brasil e Holanda) para responder à pergunta de qual país tem uma população mais alta. Um homem brasileiro adulto mede em média 1,75m já o homem holandês adulto tem uma média de 1,84, a maior média de altura do mundo!8 

Em termos práticos, é pouco viável medirmos a altura de cada um dos cerca de 215 milhões de brasileiros ou 17 milhões de holandeses para responder a nossa curiosidade, não é mesmo? Mas se ao invés de um censo populacional demorado e caro, pudéssemos responder a esta mesma pergunta com uma amostra muito menor, digamos de algumas centenas de pessoas? Seria muito mais fácil! 

É justamente este o objetivo da Inferência Estatística, que pode ser definida como o processo de tirar conclusões sobre uma população com 

8 Fonte: 

https://g1.globo.com/ciencia-e-saude/noticia/2021/07/05/por-que-os-holandeses-sao-os-mais-altosdo-mundo.ghtml 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

104 

base em medições ou observações feitas em uma amostra de unidades da população9 (Figura 33). 



<!-- Start of picture text -->
a,<br>»<br>oN & i @ «.<br>r Peg: [ Inferéncia & r \)baa)<br><!-- End of picture text -->

Figura 33. Uma amostra nos permite realizar inferências sobre uma população muito maior. 

Em geral, utilizamos a inferência estatística para: 

   - a) Estimativas pontuais: por exemplo, a partir da média de uma amostra queremos calcular um valor que melhor aproxima o valor real da população. 

   - b) Estimativas de intervalo: um intervalo de valores, também chamado de intervalo de confiança, que deve conter o real valor da população com uma probabilidade _p_ . 

- 9 EVERITT, B. S.; SKRONDAL, A. The Cambridge Dictionary of Statistics. 3a Edição. ed. [S. l.]: Cambridge University Press, 2010. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

105 

Aqui é importante notar que enquanto a análise descritiva busca apenas descrever um fenômeno, ao utilizar a inferência estatística nós fazemos proposições ou afirmações sobre os dados e usamos as técnicas estatísticas para confirmar ou refutar essas proposições. Desta forma, se bem utilizada, a inferência estatística é uma arma poderosa para responder perguntas nas mais diversas áreas do conhecimento. 

### Aula 3.2: Estimação 

Na grande maioria dos casos práticos em estatística precisaremos utilizar quantidades obtidas de amostras para poder obter informações sobre uma população. Nestes casos, há sempre um caráter aleatório e probabilístico em nossas estimativas, de modo que precisamos quantificar a incerteza associada a cada parâmetro que estimamos. 

No exemplo 5.10, calculamos a probabilidade de se obter um número específico de transações com falhas no BanVic, sabendo que a proporção de falhas no sistema era de 10%. A realidade é que na maioria dos casos não sabemos a proporção real de falhas, mas precisamos _estimá-la_ utilizando as técnicas de inferência estatísticas apresentadas aqui. 

Formalmente, denominamos de _parâmetros_ as quantidades da população, em geral desconhecidas, sobre as quais temos interesse. Os 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

106 

parâmetros são geralmente denominados com letras gregas e muitos deles já mencionamos nas aulas de probabilidade como μ (“mi”) para médias e 𝛔 (“sigma”) para o desvio padrão da população. 

Já as quantidades obtidas em amostras e que queremos utilizar para estimar os verdadeiros parâmetros da população são chamadas de _estimadores_ e apresentados através da adição de um acento circunflexo ^ ^ sobre o símbolo do parâmetro, ou seja, usamos  para a média,  para o µ σ ^ desvio padrão,  para proporção etc.  𝑝 

No exemplo citado anteriormente, nosso objetivo é estimar a proporção ^ de transações com falha _p_ a partir da proporção amostral 𝑝. Não apresentaremos os cálculos aqui, mas é possível mostrar que a proporção amostral é de fato o melhor estimador para a proporção populacional. 

A tabela 09 abaixo lista os estimadores mais utilizados para a média, proporção e variância populacional. Note que no caso da variância, o cálculo do estimador _S²_ é diferente da fórmula tradicional da variância para a população. 

Tabela 09: Tabela com os tipos de parâmetros e a fórmula para calcular o estimador. 

|**Parâmetro**|**Estimador**|
|---|---|
|μ(média)|𝑋<br>=<br>𝑋1+ 𝑋2+ 𝑋3+...+𝑋𝑛<br>𝑛|
|p (proporção)|𝑝<br>= <sup>𝑓𝑟𝑒𝑞𝑢ê𝑛𝑐𝑖𝑎 𝑎𝑚𝑜𝑠𝑡𝑟𝑎𝑙 𝑐𝑜𝑚 𝑐𝑎𝑟𝑎𝑐𝑡𝑒𝑟í𝑠𝑡𝑖𝑐𝑎</sup><br>𝑛|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

107 



<!-- Start of picture text -->
𝑛 2<br>𝛔² (variância)  𝑆2 = 𝑛−11 ( ∑(𝑋𝑖2 −𝑛𝑋‾ )<br>𝑖=1<br>𝛔 (desvio padrão)  𝑛 2<br>𝑆= 𝑛−11 ( ∑(𝑋𝑖2 −𝑛𝑋‾ )<br>𝑖=1<br><!-- End of picture text -->

Nesta aula falamos dos estimadores pontuais, isto é, quantidades que podemos calcular a partir de dados amostrais e que segundo a teoria estatística, melhor aproximam os verdadeiros parâmetros da população. Neste momento é importante fazer uma ressalva: estimadores são funções de variáveis aleatórias, e portanto, também são variáveis aleatórias. Logo, quando dizemos que a média amostral é a melhor aproximação da média da população, estamos dizendo que a média amostral é o valor _mais provável_ da verdadeira média. Há sempre uma incerteza nesta afirmação, que precisa ser devidamente considerada e medida. Futuramente, veremos que uma outra forma de realizar a inferência é justamente utilizar intervalos ao invés de estimativas pontuais. 

### Aula 3.3: Distribuição Amostral 

Sempre que utilizamos dados amostrais para fazer afirmações ou hipóteses sobre os verdadeiros valores da população, estamos implicitamente levando em conta a incerteza. Para nossa sorte, os estatísticos chegaram a uma série de resultados que facilitam a quantificação dessa incerteza mesmo com variáveis aleatórias 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

108 

desconhecidas. Nesta aula aprenderemos como calcular a distribuição de probabilidade dos estimadores, também chamada de distribuição amostral. Essas distribuições serão a base do cálculo dos intervalos de confiança, essenciais para a inferência estatística. 

Por ser um curso introdutório, vamos nos concentrar na distribuição da média amostral 𝑋, o mais utilizado em análise de dados. Em primeiro lugar, vamos imaginar o caso de uma variável aleatória que segue a distribuição Normal, por exemplo, a altura. 

Como já mencionado anteriormente, se medíssemos a altura de cada um dos cerca de 215 milhões de brasileiros, poderíamos calcular rapidamente a média populacional e sua variância. Como é pouco viável realizar uma pesquisa desse tamanho, podemos dizer que a altura de um brasileiro é uma variável aleatória 𝑋~𝑁(µ, σ2). Mas e a média amostral? Ora, se medíssemos uma amostra de 10 brasileiros, é evidente que a altura de cada um deles é uma variável aleatória 𝑁(µ, σ2)  e sua média 𝑋1, 𝑋2, ...., 𝑋 10 

amostral é 



Também é possível mostrar que a média amostral segue uma distribuição 2 normal com média  e variância  µ σ𝑛 . Logo, utilizando nosso conhecimento sobre a distribuição Normal, 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

109 

Vamos parar um pouco para interpretar esse resultado. Das aulas sobre medidas de dispersão, sabemos que a variância é uma medida do erro da nossa estimativa, ou seja, do erro da _média amostral_ em relação à verdadeira média da _população_ . Logo, à medida que aumentamos o tamanho da amostra, _n_ , o erro se reduz e a média amostral se aproxima cada vez mais da verdadeira média populacional. Temos assim a primeira ocorrência de um importante resultado da estatística: para uma amostra aleatória, cujos elementos são independentes e seguem a mesma distribuição, quanto maior o tamanho da amostra mais próxima estará a média amostral da média populacional. 

De fato, esse resultado é válido mesmo quando não sabemos a verdadeira distribuição da variável aleatória! Para um _tamanho suficientemente grande da amostra_ , a distribuição de probabilidade da média amostral pode ser aproximada pela distribuição normal. Por isso sua enorme popularidade! 

Este resultado é chamado de Teorema Central do Limite e é um dos teoremas mais importantes da Estatística. 

A medida de variabilidade da amostra é chamada _erro padrão_ e como vimos logo acima seu cálculo é dado por: 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

110 

Você deve ter percebido que conforme o tamanho da amostra cresce, o erro-padrão diminui, de modo que o erro da média amostral se aproxima cada vez mais da média da população. 

Podemos ainda utilizar nosso conhecimento sobre a distribuição normal e descrever com exatidão qual a probabilidade do erro padrão em uma amostra qualquer. Lembra quando calculamos as áreas para descobrir as probabilidades? Aquele aprendizado serve neste contexto na regra 68-95-99. 

Se considerarmos um valor de z = 1, a partir da consulta a tabela sabemos que a área é 0,3413. Decorre daí que a proporção de valores entre z = -1 e z = 1 será 0,3413 + 0,3413 = 0,6826, isto é 68%. Cálculo análogo é feito para z = 2 cujos valores de área serão 0,4772 + 0,4772 = 0,9544 ou 95%. Finalmente para z= 3, a área é a soma de 0,4987 + 0,4987 = 0,9974 ou 99,7%. Portanto, espera-se que 68% de todos os valores estejam a menos de 1 desvio-padrão da média; 95% de todos os valores estejam a menos de 2 desvios-padrão da média e cerca de 99,7% de todos os valores estejam a menos de 3 desvios-padrão da média (Figura 34). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

111 



<!-- Start of picture text -->
w-30 p-2o po B wt+o pt2e pt+3o x<br>H— 68,26%—H<br>-———_ 95% ————4<br>-_—.<br>997% 4,<br><!-- End of picture text -->

Figura 34: Gráfico da distribuição normal com a média e os erros amostrais dos intervalos de confiança. 

### Aula 3.4: Intervalos de confiança 

Já falamos que os estimadores são variáveis aleatórias e portanto possuem uma distribuição de probabilidade. Logo, ao invés de apresentar apenas estimativas _pontuais_ de um parâmetro podemos incluir uma medida de _precisão_ dessa estimativa, o chamado intervalo de confiança. 

Retomamos nosso exemplo anterior utilizando medições da altura em amostras de 10 brasileiros. Como a altura é uma variável aleatória, podemos repetir o experimento com diferentes amostras de 10 pessoas e 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

112 

calcular a média amostral para cada amostra, de modo que passaríamos a ter uma distribuição da _média_ amostral como a tabela abaixo: 

|Amostra|1|2|3|4|5|6|7|8|9|10|Média|
|---|---|---|---|---|---|---|---|---|---|---|---|
|𝑋|1,70|1,75|1,73|1,71|1,71|1,72|1,72|1,71|1,79|1,82|1,73|



A partir de pesquisas científicas, sabemos que o desvio padrão da altura na população é de 10 cm. Logo, usando a fórmula da distribuição amostral temos 



Para poder calcular o intervalo de confiança podemos fazer um processo inverso ao utilizado na aula 2.6 para calcular a probabilidade de se obter um intervalo específico da distribuição normal. Agora, precisamos fixar a probabilidade 𝞪 (“alfa”), ou coeficiente de confiança, e utilizar a tabela da normal padrão para calcular os valores críticos deste intervalo. 



substituindo os valores amostrais obtidos no nosso experimento: 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

113 

Sabemos que 95% das médias amostrais devem estar aproximadamente10 em no máximo 2 desvios padrões da verdadeira média populacional, logo podemos reescrever: 







Assim, podemos escrever o intervalo de confiança para a média de altura da população  com 95%: de intervalo de confiança na seguinte forma: µ 



Ufa! Vamos sair um pouco do “tecniquês” e tentar interpretar o significado do intervalo de confiança que acabamos de construir. Como não sabemos o verdadeiro valor da média da população, nós precisamos definir qual a nossa margem de erro aceitável, que chamamos de grau de confiança e calculamos como 1 - 𝞪 (Figura 35). A interpretação correta do grau de confiança é que se _repetirmos o mesmo experimento com várias amostras do mesmo tamanho, e calcularmos o intervalo de confiança de cada amostra_ , _esperamos que a proporção de intervalos que contenham a média populacional seja igual a 1 -_ 𝞪 _._ Ou seja, se repetirmos nosso experimento da altura dos brasileiros, esperamos que em 95 de cada 100 

> 10 O valor exato é 1,96. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

114 

experimentos, a verdadeira média de altura dos brasileiros estará dentro deste intervalo, ou seja, entre 1,67m e 1,79m. 



<!-- Start of picture text -->
a/2 a/2<br>X_o/2 Xo/2<br><!-- End of picture text -->

Figura 35: Distribuição para representar o intervalo de confiança da distribuição normal. 

Vamos imaginar o que aconteceria se mudássemos nosso grau de confiança. Suponha que 5% de erro seja um valor alto de mais, e que na verdade queremos ter 99% de confiança para o intervalo da média. Ora, a forma mais fácil de garantir isso é simplesmente _aumentar o intervalo,_ ou mais formalmente, aumentar a _amplitude_ do intervalo. Ou seja, quanto menor a precisão do intervalo, maior a chance de que nosso valor verdadeiro esteja dentro nele (se quisermos extrapolar esse raciocínio, provavelmente teríamos 100% de confiança que a média de altura de um 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

115 

brasileiro está entre 0 e 3m!). De fato, retomando os cálculos para o intervalo de confiança com 𝞪 = 0,01, vemos que o intervalo de altura ficaria entre 1,65 e 1,81m. 

#### **Exemplo 5.15: Intervalo de Confiança** 

Para calcular rapidamente o intervalo de confiança, podemos usar o código abaixo: 

Python # Exemplo 5.10b from scipy.stats import norm import numpy as np # Calcular o intervalo de confiança para a normal padrão n = 10 media = 1.73 erro_padrao = 0.10/10**(1/2) print("Intervalo de confiança:", media + np.array(norm.interval(0.95))*erro_padrao) 

Além da média populacional, também é comum estimarmos intervalos de confiança para a proporção _p._ O exemplo mais comum é a estimativa de votos em uma eleição, onde a partir de uma amostra de eleitores queremos determinar a verdadeira proporção de votos na hora da urna. Assim como no caso da média amostral, o teorema central do limite nos garante que para uma amostra grande o suficiente, a proporção amostral ^ 𝑝  será a melhor estimativa para a verdadeira proporção _p_ e poderá ser aproximada por uma distribuição normal. Logo, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

116 



Assim, um intervalo de confiança para a proporção amostral é dado por, 



Como em geral p é desconhecido, uma abordagem é utilizar a proporção observada na amostra para aproximar o erro padrão da proporção. Outra abordagem, chamada de “pessimista”, vem do fato de que como p é um número que varia entre 0 e 1, a expressão p(1-p) tem valor máximo de 0,25 quando p é igual a 0,5. Assim podemos simplesmente substituir esse valor na equação do erro padrão e construir um intervalo de confiança _conservador_ (de fato, essa é a abordagem utilizada pelos institutos de pesquisa eleitorais na construção das “margens de erro” das pesquisas). 

A tabela 10 abaixo resume os intervalos de confiança apresentados: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

117 

Tabela 10: Tabela com os parâmetros e as respectivas fórmulas para calcular o seu estimador. 

|**Parâmetro**|**Estimador**|
|---|---|
|μ,𝛔² (variância) conhecida|[<br>𝑋<sup>‾ </sup>− 𝑧α/2<br>σ<br>𝑛<br>; 𝑋<sup>‾</sup>+ 𝑧α/2<br>σ<br>𝑛<br>~~]~~|
|p (proporção)|]<br>[𝑝<br>^− 𝑧α/2<br>𝑝(1−𝑝)<br>𝑛<br>; 𝑝<br>^+ 𝑧α/2<br>𝑝(1−𝑝)<br>𝑛|
||(otimista)|
|𝛔² (variância)|[𝑝<br>^− 𝑧α/2<br>1<br>4𝑛<br> ; 𝑝<br>^+ 𝑧α/2<br>1<br>4𝑛<br>~~]~~|
||(pessimista)|



Vamos recapitular: 

- os intervalos de confiança permitem calcular a incerteza em uma estimativa; 

- Utilizamos a Normal Padrão para calcular o grau de confiança com uma variância conhecida; 

- Quanto maior o tamanho da amostra, menor o erro padrão e mais próxima nossa amostra estará da população; 

- O tamanho da incerteza “aceita” é dado pelo grau de confiança. Quanto maior o grau de confiança, maior a amplitude do intervalo de confiança. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

118 

### Aula 3.5: Testes de Hipóteses 

Nesta aula falaremos de um dos tópicos mais importantes da inferência estatística: os testes de hipóteses. Mas você já viu isso antes: exames de sangue! Sempre que realizamos um exame laboratorial, os valores encontrados em nosso exame são apresentados em relação a valores de referência (como na Figura 36 abaixo). Mas como esses valores de referência são determinados? Se você pensou em intervalos de confiança, acertou. Veja neste trecho de um portal de saúde a descrição de como são calculados os valores de referência: 

O primeiro passo para determinar um intervalo de referência é definir a população à qual o intervalo será aplicado. Um grande número de indivíduos de um grupo que são pensados para representar uma população "normal", será testado para um teste laboratorial particular. O intervalo de referência é então derivado matematicamente tomando o valor médio para o grupo e permitindo a variação natural em torno desse valor (mais ou menos 2 desvios padrão da média). Dessa forma, as faixas citadas pelos laboratórios representarão os valores encontrados em 95% dos indivíduos do grupo 'referência' escolhido. Em outras palavras, mesmo em uma população "normal", um resultado de teste estará fora da faixa de referência em 5% dos casos (1 em 20). É por isso que o termo "intervalo de referência" é preferido em relação ao "intervalo normal". (Labtestonline, 2023) 

Traduzindo para “estatistiquês”, os valores de referência são calculados como intervalos de confiança com grau de confiança de 95% para cada um dos parâmetros medidos nos exames, assumindo uma população 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

119 

grande e uma distribuição normal. Vamos dar um passo além e tentar interpretar os resultados? 



<!-- Start of picture text -->
Hemograma<br>Material: Sangue total com EDTA (coletado em 27/06/2012)<br>Método: Automacao - Micros 60 / ABX<br>ERITROGRAMA<br>EFitrOCitOS oo enssenenene 5,2 milhdes/imm? 4,5.2.5,9 mihgesimm*<br>Hemoglobina 120% 1200175 9%<br>HematOctito ccc 46% 40.052 %<br>vem 88,46 U 80. 100"<br>[ol 23,08 pg 26.034 pg<br>cHCM 26,09 % 31.036 %<br>ObSErVAaGOES: .nssesnesernrnenee<br>LEUCOGRAMA<br>Leucécitos 8.700 /mm* 4.500 a 11.000 mm?<br>N@UtrOfIOSoo ccentcnntnnennnne 67%<br>Metamiel6citos cece 0% 0/mm* O.a1% Ate 100 /mm*<br>Bastonetes 0% 0 /mm* 0.24% Até.400 mm?<br>Segmentados 67% 5.829 Imm? 36<br>Eosinéfilos 3% 261 Imm? 0. 2  664% %| 1020 0 .4000.0 7500imm*/mm*<br>BaSOMIOS .cccseeennennnes 0% 0 /mm? Oa 1% Ate 100 /mm*<br>Linfécitos 28% 2.436 Imm? 20.240 % 900a 4400 mm?<br>MONOCIOS .oeeorcrcsenrenenee 2% 174 Imm? 28% 200.2800 imm*<br>PlaqUetaS .eceoececennneeee 280.000 Imm? 150.000a 400.000 /uL<br><!-- End of picture text -->

Figura 36: Exemplo do resultado de um hemograma. Fonte: blog-dentalspeed. 

Suponha que a partir de exames em milhares de pessoas _sadias_ , identificamos que a concentração de hemoglobina no sangue varia entre 12,0 a 17,5g% com uma probabilidade de 95%. Chamaremos estes valores de _valores críticos_ . Podemos interpretar nosso exame de rotina da seguinte forma: 

a) O nível de hemoglobina está dentro do intervalo -> resultado normal b) O nível de hemoglobina está fora do intervalo -> resultado anormal. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

120 

Essas duas interpretações, ou _hipóteses_ , podem ser formalizadas através do conceito de _testes de hipóteses_ . Por conveniência, chamamos de hipótese _nula_ a hipótese de que o parâmetro de interesse está dentro de um intervalo esperado. E hipótese alternativa o cenário onde esse parâmetro se encontra fora do intervalo. Uma outra forma de interpretação é dizer que _rejeitamos_ a hipótese nula caso o valor observado do parâmetro se encontre fora do intervalo crítico. É bom reforçar que o teste de hipóteses não _comprova_ uma situação, por exemplo, uma doença, mas apenas informa que existe uma baixa probabilidade de que aquele valor seja observado na população. Mais do que isso, ele nos dá o valor exato dessa probabilidade! 

Vamos evoluir nossa intuição assumindo agora que existem duas populações, os _sadios_ e os _doentes_ . Entre as pessoas sadias, a concentração de uma substância no sangue segue uma distribuição normal com média de 14 unidades/ml e desvio padrão de 6 unidades/ml. Já entre as pessoas doentes, a concentração dessa substância tem uma média de 18 unidades/ml com desvio padrão também de 6 unidades/ml (Figura 37). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

121 



<!-- Start of picture text -->
—— Sadias<br>| —— Doentes<br>|<br>|<br>|<br>||<br>\<br>|<br>16 18<br><!-- End of picture text -->

Figura 37: As Distribuições das populações com ou sem doença se sobrepõem. 

Queremos medir a eficácia de um novo tratamento proposto para combater essa doença. Para isso, selecionamos aleatoriamente uma amostra de 30 pacientes doentes a serem submetidos pelo tratamento e medimos a concentração dessa substância. O primeiro passo, e talvez o mais importante, é definirmos as hipóteses que queremos testar. Por padrão, a primeira hipótese a ser definida é a chamada hipótese nula 𝐻0, de que o tratamento _não tem efeito_ . Em seguida, definimos a hipótese alternativa 𝐻1 de que de fato foi possível reduzir a concentração da substância: 

#### 𝐻0: o tratamento não é eficaz |  = 18 µ 

𝐻1: o tratamento é eficaz |  < 18 µ 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

122 

Para avaliar o tratamento, podemos usar a média amostral  que já vimos 𝑋<sup>‾</sup> ser um bom estimador (consistente e não viesado) para a média da população. Se o valor observado da média amostral for próximo ou superior a 18, não teremos confiança em dizer que o tratamento é eficaz. No entanto, se esse valor for inferior a 18 por uma margem razoável, podemos considerar que o tratamento tem algum efeito positivo. Como  𝑋<sup>‾</sup> é uma variável aleatória, conseguimos atribuir probabilidades do valor observado 𝑥𝑜𝑏𝑠‾ fazer parte de cada uma das populações (sadia ou doente) e utilizar essas probabilidades para responder nosso teste. 

Iniciamos calculando o valor crítico 𝑥𝑐 que nos permitirá aceitar ou rejeitar a hipótese nula. Para obtê-lo, precisamos fixar o chamado nível de α significância . Veremos em breve o que ele significa, mas agora nos basta interpretá-lo como uma medida da qualidade do nosso teste. Em nosso exemplo, podemos usar o valor de α = 5%, comum em estudos parecidos. Nosso objetivo é calcular o valor para a média que, por pura chance, esperaríamos acontecer em no máximo 5% das vezes. 

Para calcular o valor crítico 𝑥𝑐, usaremos um procedimento semelhante o 

que utilizamos para construir os intervalos de confiança: 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

123 

com 𝑍~𝑁(0, 1). Calculamos 𝑥𝑐 da seguinte forma (lembre-se dos intervalos 

de confiança): 



Utilizando a tabela normal (tente você mesmo), verificamos que o valor de 𝑧𝑐para obter uma área de 5%, isto é 𝑃(𝑍 < 𝑧𝑐)é de -1,64.  Substituindo na 

equação acima, 



Logo, para uma amostra de 30 pacientes, se obtivermos uma média amostral (observada) menor que 16,20, podemos rejeitar a hipótese nula de que o tratamento não faz efeito. O intervalo que permite rejeitar a hipótese nula é chamado de Região Crítica ou Região de Rejeição (Figura 38). 



<!-- Start of picture text -->
X. 18<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

124 

Figura 38: Gráfico da distribuição normal com destaque para a área crítica que pontua o valor de corte para rejeitar uma hipótese. 

Aqui é bom reforçar um ponto que é tanto uma arma poderosa quanto uma grande causa de confusão no uso de estatística. A comparação entre duas variáveis aleatórias não depende apenas de seus valores pontuais, mas também de seus intervalos de confiança! Como assim? 

Vamos supor que ao calcularmos a média dos 30 pacientes, a concentração observada da substância de interesse seja de 16,21. Usando apenas técnicas de análise descritiva habituais, poderíamos considerar o tratamento eficiente. Ao utilizar o teste de hipóteses, entretanto, não podemos rejeitar a hipótese nula de que os resultados obtidos pelos pacientes tenham sido apenas uma coincidência. Ou seja, estatisticamente, 16,21 e 18 são “iguais”! Em suma, ao olhar o mundo com as lentes da estatística, não podemos mais responder perguntas sem levar em conta a aleatoriedade à nossa volta. 

O teste realizado no exemplo é também chamado de teste de hipótese unilateral. Outro teste comum é o teste bilateral, onde, supondo que µ𝑜 seja um valor constante conhecido, a hipótese alternativa é expressa como: 





Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

125 

Neste caso, o valor crítico precisa ser calculado considerando as duas áreas de rejeição11 (Figura 39). 



<!-- Start of picture text -->
a/2 a/2<br>X_o/2 L Xa/2<br><!-- End of picture text -->

Figura 39: Gráfico da distribuição normal com destaque para as áreas críticas que pontuam os valores de corte para rejeitar uma hipótese. 

Agora chegou a hora de explicar melhor o significado no nível de α. significância Vamos pensar nos dois tipos de erros que podemos fazer em um teste de hipóteses: 

- I. Rejeitar a hipótese nula, quando ela é verdadeira. Popularmente chamado de “falso positivo” 

- II. Não rejeitar a hipótese nula, quando ela deveria ser rejeitada. Também chamado de “falso negativo”. 

> 11 É comum que tabelas de distribuição normal apresentem os valores críticos de Z considerando uma tabela bilateral. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

126 

α O nível de significância  é a probabilidade de ocorrer um erro do tipo I como acima. Já a probabilidade do erro tipo II, o chamado falso negativo é denotada pela letra  (beta) (Tabela 11).  β 

Tabela 11: Tipos de erros amostrais em testes de hipóteses. 

||Verdadeira<br>𝐻0|Falsa<br>𝐻0|
|---|---|---|
|Rejeitar<br>𝐻0|Erro Tipo I (falso positivo)|Sem erro|
|Não rejeitar<br>𝐻0|Sem erro|Erro Tipo II (falso negativo)|



Idealmente, gostaríamos que tanto o erro do tipo I quando tipo II fossem o mais próximo de zero. Entretanto, à medida que reduzimos um tipo de erro (Figura 40), a tendência é que aumente o outro tipo. Intuitivamente, vamos imaginar que nosso tratamento de exemplo anterior tenha efeitos colaterais muito fortes e queremos evitar ao máximo um falso positivo (erro tipo I), ou seja, um resultado que rejeite a hipótese nula devido ao acaso. Conforme aumentamos nosso rigor neste teste, também corremos o risco de considerar um efeito benéfico real do tratamento como meramente uma coincidência. Ou seja, o risco de um falso negativo (erro tipo II) cresce. Em geral, o erro que queremos minimizar é o erro tipo I. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

127 



<!-- Start of picture text -->
— Sadias<br>| ! —— Doentes<br>I|<br>| |<br>||<br>|<br>°<br>my | Hi<br>| |<br>| |<br>P(erro tipoava na) Plerto|  tipo 11)(8<br>|<br>16 z. 18<br><!-- End of picture text -->

Figura 40: Conforme reduzimos , aumentamos a chance de α um erro Tipo II (β). 

Vamos recapitular: 

- testes de hipóteses são utilizados para realizar inferências sobre variáveis aleatórias. 

- Chamamos de hipótese _nula,_ ou 𝐻𝑜 a hipótese de que o parâmetro 

de interesse está dentro de um intervalo esperado. 

- E hipótese alternativa, ou 𝐻1 o cenário onde esse parâmetro se 

encontra fora do intervalo. 

- Rejeitamos a hipótese nula se o valor observado estiver na região crítica. 

- A probabilidade de rejeitar a hipótese nula quando ela é verdadeira é chamada de Erro tipo I. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

128 

- A probabilidade de aceitar a hipótese nula quando ela deveria ser rejeitada é chamada de Erro tipo II. 

### Aula 3.6: Testes de hipóteses com variância desconhecida 

Na aula anterior explicamos a intuição por trás dos testes de hipóteses. Vimos também como é calculado um teste de hipóteses para a média usando o exemplo de um tratamento de saúde. Mais formalmente, realizamos um teste de hipóteses para a média com variância conhecida, já que sabíamos a variância da população. Nesta aula falaremos sobre outros tipos de testes de hipóteses muito usados na prática. Vamos lá? 

Antes de falarmos de cada caso específico, é bom reforçar que os testes de hipóteses seguem uma série de etapas específicas: 

- 1) Estabelecer as hipóteses nula e alternativa 

- 2) Definir a forma de cálculo da região crítica (ex. unilateral vs bilateral) 

- 3) Identificar a distribuição do estimador e obter sua estimativa (ex. normalidade vs não-normalidade) 

- α α 

- 4) Fixar o  e obter a região crítica (ex.  = 5%) 

- 5) Concluir o teste com base na estimativa e região crítica 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

129 

Em grande parte dos casos práticos não conhecemos a verdadeira variância da população. Como o desvio padrão é desconhecido, precisamos estimá-lo juntamente com a variável aleatória do teste (por exemplo, a média). Mantendo a hipótese de que a variável segue uma distribuição normal, podemos usar a variância amostral ao invés da populacional. A principal diferença é que teremos que usar uma nova distribuição para a variável padronizada T, chamada de _t de student_ : 



com . Onde (n - 1) é o chamado _Grau de Liberdade_ cuja 𝑇 ~ 𝑡 (𝑛−1) explicação pode ser encontrada em materiais mais avançados. Um ponto importante é que quando n é grande, a distribuição t se aproxima da distribuição normal (Figura 41). De fato, a convenção é que para amostras com mais de 30 elementos já é possível usar a distribuição normal padrão _mesmo_ com variância desconhecida. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

130 



<!-- Start of picture text -->
0.407 —— Normal Padréo =<br>Distribuicgéo t (GL=5)<br>0.35 Distribuicdo t (GL=10)<br>—— Distribui¢ao t (GL=30)<br>0.30<br>0.25<br>w<br>3i<br>2 0.20<br>ra<br>a 0.15<br>0.10<br>0.05 \S<br>0.00 — =<br>4 3 -2 -1 te) 1 2 3 4<br>Valores<br><!-- End of picture text -->

Figura 41: Conforme aumentamos o grau de liberdade (GL), a distribuição t se aproxima cada vez mais da normal padrão. 

Vamos novamente usar nossa amostra da altura e peso dos colaboradores de uma agência do BanVic. Anteriormente, dissemos que a variância da população (colaboradores do BanVic) era conhecida. Mas e se quiséssemos utilizar essa amostra para fazer uma inferência sobre outra população, por exemplo, de pessoas adultas no Brasil? Supondo que o peso da população brasileira segue uma distribuição normal com média de 68 Kgs, será que podemos dizer que nossos colaboradores estão “na média” ao nível de 5% de significância? 

Nosso teste de interesse é: 

- 𝐻0: µ𝐵𝑎𝑛𝑉𝑖𝑐 = µ𝐵𝑟𝑎𝑠𝑖𝑙 => Média de peso do BanVic é igual a média brasileira 𝐻1: µ𝐵𝑎𝑛𝑉𝑖𝑐 ≠µ𝐵𝑟𝑎𝑠𝑖𝑙 => Média de peso do BanVic é diferente da média 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

131 

#### brasileira 

Como não sabemos a variância do peso da população brasileira, 𝑛 2 usaremos o estimador 𝑆2 = 𝑛−11 ( ∑(𝑋𝑖2 −𝑛𝑋‾ ) que apresentamos na aula 𝑖=1 

3.2. Supondo 𝐻0 verdadeira, temos que 



Definimos os valores críticos da forma usual, 





Da tabela da distribuição t de Student, obtemos que os valores de t com 9 graus de liberdade correspondente a uma área de 5% são de -2,2622 e 2,2622. Esses serão nossos valores críticos. Agora, substituindo a média da 

amostra ‾ = 77, 3 e a variância amostral ‾ = 209, 35 (tente calcular 𝑥𝑜𝑏𝑠 𝑠𝑜𝑏𝑠² você mesmo), 



E aí? será que podemos dizer que nossos colaboradores estão acima do peso já que a média é acima da média nacional?  Estatisticamente, não! Como o valor crítico superior do nosso teste de hipóteses é de 2,2622, e a estatística t calculada na amostra é de 2,033, não podemos rejeitar a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

132 

hipótese nula de que a média de peso dos nossos colaboradores é igual a média da população brasileira como um todo. Pode parecer pouco intuitivo, mas o teste de hipótese nos permite quantificar e minimizar o risco de tirarmos conclusões equivocadas sobre resultados que podem ter sido gerados apenas pelo acaso! Tente realizar um teste semelhante só que agora considerando a altura dos nossos colaboradores e a média de altura da população brasileira de 1,75m. 

A tabela de referência abaixo apresenta o estimado e estatística teste para os parâmetros mais comuns (Tabela 12): 

Tabela 12: Tabela com os parâmetros, seus estimadores e a estatística de teste correspondente para cada um deles. 

|**Parâmetro**|**Estimador**|**Estatística Teste**|
|---|---|---|
|µ|𝑋<sup>‾</sup>|z (se n > 30)<br>t (se n < 30)|
|𝑝|𝑝<br>^|z|
|σ²|𝑠<br>2|(chi-quadrado)<br>χ<br>2|



Onde o teste para proporções e para a variância será omitido neste curso. Você pode consultar seu cálculo nas referências do curso. 

#### **Exemplo 5.16: Teste hipóteses com variância desconhecida** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

133 

Para calcular a estatística t no python utilizamos a função _t.ppf_ do pacote scipy: 

Python from scipy.stats import t print("Valor de t com p=0.025 e gl=9 é ", round(t.ppf(0.025,9),4)) 

Vamos recapitular: 

- Utilizamos a distribuição normal padrão quando conhecemos a variância da população. 

- Quando a variância é desconhecida, estimamos a estatística T que segue a distribuição _t de student_ com n-1 graus de liberdade. 

- Para amostras com mais de 30 elementos, podemos usar a distribuição normal padrão. 

### Aula 3.7: Amostragem 

O uso de técnicas de amostragem decorre do fato de que nem sempre conseguimos utilizar todo o nosso conjunto de dados disponível para realizar uma análise completa. Isso porque as tabelas podem ser muito grandes ou simplesmente porque não temos como coletar todos os 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

134 

dados disponíveis sobre um determinado assunto. Nesses momentos fazemos uso de uma amostra. 

Para que isso fique ainda mais claro vamos recapitular a definição de população e amostra. 

População é o conjunto completo de indivíduos, objetos, eventos ou medidas que possuem uma ou mais características em comum e que são de interesse para a análise. Em outras palavras, é o grupo **<u>total</u>** de unidades estatísticas que se deseja estudar. A população pode ser finita, quando há um número determinado e limitado de unidades estatísticas, ou infinita, quando o número de unidades é muito grande ou desconhecido. 

Já a Amostra é um subconjunto de indivíduos, objetos, eventos ou medidas selecionado de uma população, para que se possa inferir informações sobre a população como um todo. Se uma amostra for escolhida apropriadamente (de forma aleatória), características de toda a população a partir da qual a amostra é retirada podem ser estimadas para toda a amostra. 

É importante destacar que a análise estatística é realizada a partir de uma amostra representativa da população, pois é inviável ou muito difícil obter informações de todos os elementos da população. A amostra é um subconjunto dos elementos da população, selecionado de forma aleatória e representativa, para que as conclusões obtidas a partir da análise da amostra possam ser generalizadas para toda a população. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

135 

A seleção de uma amostra adequada é fundamental para que as conclusões obtidas a partir da amostra representem e possam ser generalizadas para toda a população. Para isso, é importante utilizar técnicas estatísticas de amostragem, que garantem a aleatoriedade e a representatividade da amostra. 

Vale ressaltar que quanto maior a amostra, maior será a precisão das estimativas e menor será a margem de erro. No entanto, o tamanho da amostra deve ser definido de acordo com o tamanho da população, o nível de confiança e a margem de erro desejados, entre outros fatores. 

Existem várias técnicas amostrais disponíveis, e a escolha da técnica mais adequada depende das características da população e do objetivo da pesquisa. Algumas das principais técnicas amostrais são: 

1. **Amostragem aleatória simples** : é a técnica mais comum e fácil de usar, na qual cada elemento da população tem a mesma probabilidade de ser escolhido para a amostra. Essa técnica é utilizada quando a população é homogênea e não há preocupação com estratificação ou outros fatores. 

2. **Amostragem estratificada** : é uma técnica que divide a população em estratos ou grupos com características similares, e seleciona aleatoriamente uma amostra de cada estrato. Essa técnica é utilizada quando a população é heterogênea e a estratificação permite obter uma amostra mais representativa. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

136 

3. **Amostragem por conglomerados** : é uma técnica que divide a população em conglomerados ou grupos maiores, e seleciona aleatoriamente alguns desses conglomerados para a amostra. Essa técnica é utilizada quando a população é muito grande ou dispersa geograficamente, e os conglomerados podem ser usados para reduzir o custo e o tempo da pesquisa. 

4. **Amostragem sistemática** : é uma técnica que seleciona elementos da população de forma sistemática, com um intervalo pré-determinado. Por exemplo, a cada 10 elementos da população, seleciona-se um para a amostra. Essa técnica é utilizada quando a população é grande e pode ser ordenada em alguma medida. 

5. **Amostragem por quotas** : é uma técnica que seleciona uma amostra com base em cotas pré-estabelecidas, como idade, sexo, classe social, entre outras características. Essa técnica é utilizada quando não é possível usar outras técnicas de amostragem, ou quando se deseja garantir a representatividade de subgrupos específicos da população. 

Uma pergunta comum na hora de construir uma amostra é como definir o tamanho da amostra. E a resposta como sempre é _depende!_ Variáveis como hipóteses sobre a população, escolha da técnica amostral, erro aceitável etc. impactam diretamente no tamanho da amostra ideal. 

Dito isso, falaremos do cálculo mais comum, utilizado em amostragem aleatória simples com população dita “infinita”. Neste caso, é aceitável 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

137 

considerar que as características da população seguem uma distribuição normal de modo que o tamanho da amostra é calculado pela fórmula 



onde: 

n = tamanho da amostra 

𝑍α/2 = valor crítico com grau de confiança desejado 

σ = variância populacional 

𝑒 = margem de erro 

Em geral, os graus de confiança utilizados são os de 90%, 95% e 99% conforme tabela 13 abaixo: 

Tabela 13: Valores críticos para 𝑍α/2 por grau de confiança mais utilizado. 

|**Grau de Confiança**|α|**Valor para**|𝑍α/2|
|---|---|---|---|
|90%|0,10|1,645||
|95%|0,05|1,96||
|99%|0,01|2,575||



Desta forma, sabendo a variância populacional e a margem de erro pretendida, o cálculo do tamanho da amostra é trivial (ver Exemplo). Mas 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

138 

e se a variância populacional é desconhecida? Neste caso, podemos realizar uma amostragem menor (digamos, com 30 indivíduos) e utilizar o estimador da variância S². A estatística tem suas armas! 

#### **Exemplo 5.17: Tamanho da amostra para pesquisas eleitorais** 

Uma das aplicações mais conhecidas da Amostragem é na realização de pesquisas eleitorais. É comum que cada pesquisa divulgue o tamanho da amostra, margem de erro e grau de confiança de cada pesquisa.  Por exemplo, em uma pesquisa eleitoral realizada no Brasil foi informado os seguintes dados: 

“Foram entrevistadas **4.272** pessoas em 236 municípios entre quinta-feira (27) e sábado (29). A **margem de erro é de dois pontos percentuais,** para mais ou para menos, com **índice de confiança de 95%** ” 

Será que o tamanho da amostra nesta pesquisa específica era suficiente? Vamos descobrir! Pesquisas eleitorais são proporções e sabemos da aula 3.4 que a variância máxima ocorre quando p = 50%. Adaptando a fórmula do tamanho da amostra para proporções temos 



Como o índice de confiança é de 95% e a margem de erro é de 2 pontos 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

139 

percentuais, substituímos 



Ou seja, pela fórmula do tamanho da amostra para população infinita precisaríamos de 2400 indivíduos. Será que o instituto de pesquisa cometeu um erro e entrevistou gente demais? Não é bem assim. As preferências políticas variam bastante entre grupos diferentes da população de modo que uma amostragem simples pode esconder vieses na pesquisa. Por isso, é comum que os institutos de pesquisa utilizem técnicas mais avançadas de amostragem que necessitam de ajustes nos cálculos do tamanho da amostra. 

### Aula 3.8: Experimentos 

Talvez o principal uso da estatística na análise de dados é sua capacidade de medir o real impacto de ações realizadas pelas empresas, ou _tratamentos_ . Será que a nova campanha de marketing está com melhor desempenho que a anterior? Mudanças no algoritmo de prevenção de fraude estão de fato reduzindo o impacto financeiro das fraudes? A lista é infinita. 

No entanto, como já mencionamos repetidas vezes durante este curso, as técnicas de inferência estatística raramente comprovam causalidade e mais importante, dependem de uma série de hipóteses sobre a forma 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

140 

com que os dados estão distribuídos. Como diria o ditado popular, “na prática, a teoria é outra”. 

A forma mais simples de utilizarmos com confiança as técnicas estatísticas é através da construção (ou identificação) de experimentos controlados. Um exemplo comum desses experimentos são os chamados Testes A/B. Mas por que é tão importante desenhar bons experimentos? 

Quando analisamos o efeito de uma ação, precisamos compará-la com algo. Como no mundo real existem milhares de fatores ocorrendo simultaneamente, é importante conseguir isolar ao máximo o efeito dos demais fatores em nossa análise. Se aplicarmos um novo modelo de detecção de fraude em todas as transações simultaneamente, como saberemos se as fraudes caíram pelo modelo ou por uma nova campanha antifraude do banco central? 

Uma técnica estabelecida para a construção de experimentos é a construção de dois grupos praticamente idênticos exceto pela aplicação de uma ação específica, também chamada de _tratamento_ . O grupo teste recebe o tratamento, enquanto o grupo controle não o recebe. Assim conseguimos aplicar técnicas como os testes de hipóteses ou análise de regressão considerando o efeito específico do tratamento. 

A maneira mais direta de construir experimentos é construir um grupo de tratamento e um grupo de controle de forma aleatória, chamados de experimentos aleatórios. Infelizmente, fora dos laboratórios não é fácil 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

141 

construir esses grupos, especialmente quando as pessoas estão envolvidas. 

Técnicas para construção de experimentos incluem: 

- disponibilização de websites diferentes para os usuários de forma aleatória; 

- aplicar novas ações de marketing em uma região específica; 

- enviar mensagens em horários diferentes do dia 

- etc 

O importante ao construir um experimento é tentar construir os grupos de forma mais similar entre si, salvo pelo tratamento realizado. Por exemplo, se aplicarmos uma ação de marketing apenas em uma agência do BanVic no Nordeste (nosso grupo de tratamento) e compararmos com uma agência do sul (nosso grupo controle), teríamos que considerar que o comportamento e perfil dos clientes nessas duas regiões são muito diferentes entre si, dificultando a interpretação dos resultados (Figura 42). 



<!-- Start of picture text -->
GC" Homens, 20 a 30 anos Gi! Mutheres, 40 2 50 anos<br>@©  Entretassm ¢ @  Entesassm<br>&q Estudantes q Servidores Publicos<br>Agéncia Sul ‘Agéncia Nordeste<br><!-- End of picture text -->

Figura 42: É difícil isolar o resultado de experimentos não controlados quando os grupos são muito distintos entre si. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

142 

Outra prática importante é evitar muitos tratamentos simultâneos em um experimento. Por exemplo, se queremos realizar testes A/B em nossas campanhas de marketing, podemos começar alterando apenas o texto da campanha, em seguida, somente a imagem etc. Assim é mais fácil isolar o impacto de cada tratamento na variável teste. 

Em muitos casos não é possível realizar experimentos aleatórios controlados. Parece evidente que não seria razoável parar de policiar um bairro apenas para medir o impacto do policiamento na criminalidade. No entanto, com alguma engenhosidade é possível encontrar o que chamamos de “experimentos naturais”. Esses experimentos ocorrem quando circunstâncias aleatórias surgem fazendo com que se aproximem de um experimento aleatório controlado. 

Vamos supor que queremos identificar o impacto da proximidade de uma agência dos Correios na abertura de contas de uma agência bancária. É evidente que não podemos simplesmente abrir uma nova agência dos correios e o custo de abrirmos uma agência do BanVic simplesmente para realizar um experimento não vai ser bem recebido pela diretoria. No entanto, por motivos fora do nosso controle, uma nova agência dos correios foi aberta recentemente ao lado de um agência do BanVic na cidade de São Paulo (onde já temos outras agências, ou seja, temos maior “controle” sobre as demais variáveis). Este é um típico caso de um experimento natural. Ao acompanhar a média de abertura de contas na agência próxima dos correios com as demais agências de São Paulo, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

143 

poderíamos testar a hipótese de que a agência dos correios impacta positivamente na abertura de contas. 

Em muitos casos não conseguiremos construir experimentos controlados nem teremos experimentos naturais à nossa disposição. Ainda assim, pode ser muito útil pensar na construção de experimentos ou pelo menos identificar as limitações de uma análise quando as premissas de aleatoriedade e independência não estiverem presentes. A análise de impacto de uma ação depende da identificação de algo a ser comparado, seja uma região, outro período de tempo, etc. Por fim, técnicas como a análise de regressão nos permitem realizar inferências mesmo quando a construção de experimentos não é possível. 

### Aula 3.9: Regressão 

Vimos que a inferência estatística é uma arma poderosa para responder perguntas sobre uma população utilizando apenas dados amostrais. No entanto, a maior parte dos exemplos e técnicas que mostramos são aplicadas a distribuição de uma _única_ população e nada nos diz sobre as verdadeiras causas daquele processo. Para explicarmos como o valor de uma variável é determinado, precisamos ir além e construir um _modelo estatístico_ . E o mais famoso deles é o modelo de regressão linear. 

Na aula sobre medidas de associação, aprendemos a calcular a associação entre peso e altura dos colaboradores do BanVic. Podemos ir um passo além e construir uma equação que relacione o peso de cada 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

144 

colaborador com a sua altura. Uma forma conveniente de construir essa equação é partir do nosso conhecimento de geometria do ensino médio e utilizar a equação da reta na forma y = a +bx. Onde substituindo x e y para o caso da Altura e Peso, teríamos: 



Chamamos a variável y, que queremos estimar, de variável dependente. E a variável _x_ de variável independente. Desta forma, estamos implicitamente dizendo que a variável x é a causa, ou uma das causas da variável y. Esse ponto é importante e falaremos mais sobre ele em seguida. Antes disso, precisamos de uma forma de calcular o intercepto _a_ e o coeficiente angular _b._ A lógica por trás da regressão linear é imaginar uma série de retas que se aproximem dos pontos em um gráfico de dispersão como na Figura 43 abaixo: 



<!-- Start of picture text -->
125<br>100 *<br>e<br>Ss 75 ae 2. ee —<br>8 e<br>2 50<br>25<br>9<br>150 160 170 180<br>Altura (x)<br><!-- End of picture text -->

Figura 43: Retas de Regressão. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

145 

Não é difícil perceber que a reta que melhor se ajusta aos pontos é a reta que apresenta o menor erro entre o peso observado e o peso previsto pela reta (Figura 44). No entanto, ao invés de minimizar o erro absoluto, minimizamos o _quadrado_ dos erros. Não por acaso, essa técnica é chamada de Mínimos Quadrados Ordinários, ou simplesmente, MQO. 



<!-- Start of picture text -->
125<br>100 ®<br>5 75 ¢ é e ° J +} Erro<br>3 °<br>@ 50<br>25<br>9 SSS<br>150 160 170 180<br>Altura (x)<br><!-- End of picture text -->

Figura 44: Análise de Regressão. 

A análise de regressão linear através do MQO é provavelmente o modelo estatístico mais utilizado no mundo. Está presente em praticamente qualquer estudo científico publicado e na grande maioria das reportagens de jornais que indicam o efeito entre duas variáveis. Quando lemos uma reportagem sobre o efeito de uma taça de vinho sobre a saúde, o aumento do risco de câncer associado ao tabagismo etc, provavelmente estamos lendo o resultado de uma regressão linear. 

Uma das características marcantes da regressão (ou de qualquer modelo estatístico avançado) é sua capacidade de realizar previsões sobre dados 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

146 

“fora da amostra”. No exemplo anterior, utilizando um software estatístico qualquer conseguimos mostrar que a equação da reta de regressão entre Altura e Peso dos colaboradores do BanVic é dada por: 

𝑦^(𝑃𝑒𝑠𝑜 𝐸𝑠𝑡𝑖𝑚𝑎𝑑𝑜) = −91, 56 + 0, 97 * 𝑥(𝐴𝑙𝑡𝑢𝑟𝑎 𝑒𝑚 𝑐𝑚) 

Ou seja, sabendo que a altura de um novo colaborador é de 1,70m (ou 170cm como na equação acima), podemos estimar que seu peso seria de 73,41kg. É claro que precisamos de alguma medida da qualidade da nossa estimativa. A forma mais comum de realizar essa estimativa é através do cálculo do coeficiente R², que determina a qualidade da nossa reta de regressão e tem um valor entre 0 e 1. O cálculo do R² pode ser feito facilmente em qualquer software estatístico ou planilha eletrônica e omitiremos aqui. Tente calcular o R² para nossa reta de regressão (já adianto, ele não é muito bom). 

#### **Exemplo 5.17: Regressão linear em Python** 

É possível construir modelos de regressão linear em Planilhas Eletrônicas, Softwares Estatísticos ou através de pacotes em linguagens como R e Python. No código abaixo mostramos como estimar o modelo de regressão entre altura e peso do BanVic utilizando a linguagem Python: 

##### Python 

import statsmodels.api as sm import pandas as pd 

altura = [188, 180, 168, 150, 179, 178, 169, 172, 179, 177] peso = [95, 90, 77, 55, 70, 103, 68, 75, 70, 70] 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

147 

X = pd.DataFrame(altura) #Adicionar constante X = sm.add_constant(X) modelo = sm.OLS(peso, X ).fit() print(modelo.params) 

Até agora mostramos que a análise de regressão permite quantificar a relação entre uma variável dependente e uma variável independente. Outra vantagem da análise de regressão é a capacidade de quantificarmos a relação entre variáveis específicas enquanto _controlamos_ outros fatores. Em outras palavras, mantidas algumas hipóteses sobre a distribuição de cada variável, ao adicionar novas variáveis em uma regressão estamos medindo o efeito _isolado_ de cada variável independente na variável dependente. Vamos dar um exemplo. 

Em um estudo interno do BanVic, queremos construir um modelo de regressão que relacione o gasto com cartão de crédito dos clientes com uma série de informações que possuímos sobre cada cliente como idade, renda, número de filhos etc. Como estamos lidando com muitas variáveis simultaneamente, não é possível visualizar graficamente. Mas ao rodarmos o modelo de regressão, obtemos o seguinte modelo: 

𝑦^ = 100 + 267 * 𝐹𝑖𝑙ℎ𝑜𝑠 + 0, 05 * 𝑅𝑒𝑛𝑑𝑎 + 80 * 𝐼𝑑𝑎𝑑𝑒 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

148 

A interpretação do modelo é direta. Independente dos demais fatores, cada filho gera um gasto adicional de 267 reais no cartão de crédito. No caso da renda, temos um impacto de 5 centavos de gasto adicional por Real de Renda. A idade por sua vez impacta em 80 reais por ano. Legal não? Esse é o poder da análise de regressão! 

### Aula 3.10: Erros comuns na Regressão 

A análise de regressão é uma das estrelas da análise estatística. Com ela não só conseguimos responder perguntas que envolvem dezenas de variáveis simultaneamente como também realizar previsões sobre dados não observados. Infelizmente, se mal utilizada, a análise de regressão pode causar interpretações equivocadas e gerar mais dano do que benefício (e acredite, isso acontece com frequência). Nesta aula falaremos sobre algumas preocupações no uso da regressão. 

#### **Interpretando o resultado da regressão** 

Ao realizar uma regressão em um software estatístico, você notará uma série de estatísticas com nomes complexos junto com os resultados da regressão. A interpretação da maioria dessas estatísticas foge ao escopo deste curso. No entanto, um coeficiente em particular já é conhecido por nós e tem um papel essencial na interpretação da regressão: o _p-valor_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

149 

O cálculo do _p-valor_ na regressão decorre do fato da regressão ser realizada sobre uma amostra, logo como em qualquer outra inferência estatística, precisamos saber se conseguimos extrapolar os resultados para a população. Para isso, é realizado um teste de hipóteses para cada coeficiente da regressão considerando a hipótese nula de que não há associação entre a variável dependente e a variável independente. Ou de forma equivalente, que o coeficiente é igual a 0. Na figura 45 abaixo os valores são calculados automaticamente. Quanto menor o _p-valor,_ maior a probabilidade de existir uma associação entre as variáveis. No exemplo abaixo, considerando um nível de significância de 5%, aceitaríamos a hipótese nula para a constante e rejeitaríamos para X. 



<!-- Start of picture text -->
OLS Regression Results<br>Dep. Variable: y R-squared: 0.474<br>Model: OLS Adj. R-squared: 8.408<br>Method: Least Squares F-statistic: 7.205<br>Date: Tue, 2@ Jun 2023 Prob (F-statistic): 2.0277<br>Time: 19:16:13  Log-Likelihood: -37.171<br>No. Observations: 1@ AIC: 78.34<br>Df Residuals: 8 BIC: 78.95<br>Df Model: 1<br>Covariance Type: nonrobust<br>coef std err t P>|t| [2.025 8.975]<br>const -91.5608 63.005 1.453 6.184 -236.851 53.729<br>8 2.9785 0.362 2.684 6.028 0.137 1.804<br>Omnibus : 1.808 Durbin-Watson: 2.226<br>Prob(Omnibus): @.485 Jarque-Bera (38): 0.664<br>Skew: @.629 = Prob(JB): 6.718<br>Kurtosis: 2.98@ Cond. No. 3.12e+03<br><!-- End of picture text -->

Figura 45: Resumo da regressão entre Peso e Altura no BanVic. 

#### **Regressão quando a relação é não-linear** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

150 

Outro erro comum na análise de regressão é utilizar essa técnica quando a relação entre as variáveis é não linear. Neste caso, são necessárias técnicas específicas para “linearizar” as variáveis ou mesmo o uso de outras técnicas de modelagem estatística. 

#### **Adicionar variáveis demais** 

Uma propriedade indesejada do R² é a de que conforme aumentamos o número de variáveis no modelo, o R² _sempre aumenta_ mesmo que não exista uma relação verdadeira entre as variáveis. Por isso, é importante tomar cuidado ao interpretar o R² e principalmente ao adicionar variáveis no modelo sem um motivo específico. A recomendação é somente incluir variáveis que o conhecimento de negócio ou científico indiquem a existência de associação. 

#### **Multicolinearidade** 

Quando duas variáveis explicativas são altamente correlacionadas entre si, dizemos que elas sofrem do problema de _multicolinearidade_ . Neste caso, a regressão tem dificuldades de isolar o efeito de cada variável na variável dependente. Por exemplo, se adicionarmos uma variável de escolaridade e renda para determinar o gasto com cartão de crédito, provavelmente teremos dificuldade de isolar o efeito de cada uma já que a renda é altamente correlacionada com a escolaridade. Neste caso, 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

151 

recomenda-se adicionar apenas uma das variáveis no modelo. 

#### **Correlação não é causalidade** 

Já mencionamos esse fenômeno antes, mas vale reforçar. Ainda que a análise de regressão busque mostrar como uma variável _depende_ de outra, a estatística por si só não nos permite provar causalidade. Na verdade, pouco importa para o modelo de regressão qual variável é dependente ou independente, essa decisão tem que ser tomada por nós. Por isso, assim como na escolha de variáveis, a construção do modelo depende de um conhecimento prévio sobre o fenômeno que estamos estudando. 

## Conclusão 

Com isso concluímos o módulo “Estatística aplicada à análise de dados” do Curso de Formação em Análise de Dados. Neste módulo vimos como a Estatística pode ser uma ferramenta poderosíssima para a Análise de Dados, apesar de estar presente há muito mais tempo que tecnologias modernas como Data Warehouses e Ferramentas de Visualização de Dados. 

De fato, a estatística não é só “mais uma ferramenta” mas é parte fundamental de todas as carreiras de dados e das principais tecnologias que utilizamos. Desde os algoritmos utilizados para otimizar consultas nos 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

152 

data warehouses, passando pelas técnicas de visualização de dados até os modelos de aprendizado mais avançados. 

É bem provável que você raramente precise calcular uma distribuição de probabilidade no seu dia-a-dia ou participe da construção de um experimento aleatório controlado. No entanto, é tão importante entender a aplicação da estatística como os problemas e cuidados que devem ser tomados na interpretação dos resultados quando ela não foi explicitamente considerada. 

Espero que após este curso você lembre que quando consideramos a aleatoriedade à nossa volta, a conclusão de uma análise de dados nem sempre é o que parece. 

Obrigada por ter me acompanhado até aqui. 

Nos vemos em outras aulas. Abraço! 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

153 

## Material Complementar 

**Tipo:** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Tabela da Distribuição Normal Padrão 

**Descrição:** Tabela da distribuição normal padrão 

**Link:** https://www.ime.unicamp.br/~cnaber/tabela_normal.pdf 

**Tipo:** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Tabela da Distribuição t de student 

**Descrição:** Tabela da distribuição t de student 

**Link:** http://wiki.icmc.usp.br/images/6/6e/Tabela_t-Student.pdf 

**Tipo:** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Statistical Distributions (em inglês) 

**Descrição:** Neste site você pode simular diferentes distribuições estatísticas de forma interativa. 

**Link:** <u>https://statdist.com/</u> 

**Tipo:** X Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

**Título:** Distribuições de Probabilidade 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

154 

**Descrição:** Nesta aula aberta da UNIVESP você pode complementar seu entendimento sobre distribuições de probabilidade 

**Link:** **<u>Estatística - Aula 09 - Distribuições de probabilidade - YouTube</u>** 

Referências 

EVERITT, B. S.; SKRONDAL, A. **The Cambridge Dictionary of Statistics** . 3a Edição. ed. [S. l.]: Cambridge University Press, 2010. 

MAGALHÃES, Marcos Nascimento; LIMA, Antônio Carlos Pedroso de. **Noções de Probabilidade e Estatística** . 7 ed. ed. São Paulo: EdUsp, 2023. 408 p. v. 1. 

ZAR, Jerrold H. **Biostatistical analysis** . 5. ed. New Jersey: Pearson, 2010. 944 p. ISBN 0132065029. 

BRUCE, Peter; BRUCE, Andrew. **Estatística Prática para Cientistas de Dados: 50 Conceitos Essenciais** . Tradução: Lucianas Ferraz. 1a. ed. Rio de Janeiro: Alta Books, 2019. 320 p. 

WHEELAN, Charles. **Estatística: O que é, para que serve, como funciona** . Tradução: George Schleshinger. 1. ed. Rio de Janeiro: Zahar, 2016. 

EXAME. **Comportamento do preço do bitcoin atinge maior correlação** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

155 

**com o ouro da história** . Exame, [S. l.], p. ND, 4 abr. 2023. Disponível em: https://exame.com/future-of-money/comportamento-preco-bitcoin-mai or-correlacao-ouro/. Acesso em: 19 maio 2023. 

VIGEN, Tyler. **Spurious Correlations** . [S. l.], 4 jul. 2023. Disponível em: https://www.tylervigen.com/spurious-correlations. Acesso em: 20 maio 2023. 

LAB TESTS ONLINE-UK. **Reference Ranges & What They Mean** . [ _S. l._ ], 8 mar. 2021. Disponível em: 

https://labtestsonline.org.uk/articles/laboratory-test-reference-ranges. Acesso em: 31 maio 2023. 

CARVALHO, Sandro Sacchet de. **Retrato dos rendimentos do trabalho – resultados da PNAD contínua do segundo trimestre de 2022** . IPEA CARTA DE CONJUNTURA, [ _s. l._ ], n. 56, 4 jul. 2023. Disponível em: https://www.ipea.gov.br/cartadeconjuntura/wp-content/uploads/2022/09 /220901_cc_56_nota_17_rendimentos_e_horas_trabalhadas.pdf. Acesso em: 12 maio 2023. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

156 

HEMOGRAMA. [ _S. l._ : _s. n._ ], 2023. Disponível em: 

https://blog-dentalspeed-com.s3.amazonaws.com/wp-content/uploads/ 2020/01/Hemograma.jpg. Acesso em: 1 jun. 2023. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

157 

