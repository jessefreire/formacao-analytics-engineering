

# Material Teórico 

Curso: Construindo análises com Python 

Autoria 

Prof. MSc. Renata Assunção Prof. MBA Pedro Ferraresi Prof. Damodara Teixeira 

Módulo 

Módulo 8 - Python 

Temas abordados 

- Introdução ao Python e Jupyter Notebooks 

- Manipulando dados com pandas e seaborn 

Objetivos de Aprendizagem 

- Introdução ao Python e Jupyter Notebooks; 

- Manipulação de dados com pandas e seaborn. 

Apresentação do Módulo 

Caro aluno(a), 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

1 

### Seja muito bem vindo a este curso. 

Meu nome é Damodara e vou acompanhar vocês nesse módulo. Mas antes de mais nada gostaria de me apresentar. 

Sou químico de formação e por alguns anos atuei como professor desta disciplina. Porém, desde que comecei a estudar sobre programação, principalmente Python, decidi migrar de carreira e trabalhar com dados. Oportunidades foram surgindo para que eu atuasse como professor em cursos de fundamentos de Python, estatística e Power BI. Hoje sou analista de dados na Indicium e professor do Indicium Academy. 

Neste curso, você aprenderá desde os fundamentos da linguagem Python, como variáveis, estruturas de controle e funções, até técnicas avançadas para manipulação, visualização e modelagem de dados. Vamos explorar bibliotecas essenciais como Pandas, para tratamento de dados, e ferramentas de visualização, que ajudam a interpretar informações de forma clara e intuitiva. 

Além dos conceitos estatísticos básicos, abordaremos também testes de hipóteses para validação de inferências e avançaremos para o universo da análise preditiva, onde aprenderemos a construir modelos capazes de identificar padrões e prever tendências. 

Aproveite as atividades disponibilizadas ao longo do curso para testar seu conhecimento e aprender um pouco mais sobre o assunto. 

Não deixe de conferir também os conteúdos complementares. Eles foram selecionados para reforçar ainda mais a base de conhecimento de vocês sobre os assuntos apresentados e também vão ajudá-los a ter embasamento técnico para resolver alguns desafios do cotidiano. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

2 

## Introdução Etapa de Python 

### **Aula 1: Iniciando o módulo de Python** 

Vamos iniciar os estudos e aprendizados da linguagem Python. 

Durante esta etapa, teremos três ciclos principais: 

1. Ciclo de apresentação do Python: Neste ciclo iremos visitar os principais conceitos da linguagem de programação Python, bem como conhecer o nosso ambiente do Google Colab inteira do Python. 

2. Ciclo de Perguntas de Negócio: Neste ciclo, receberemos uma série de perguntas e desafios para respondermos utilizando o Python. A cada pergunta respondida, iremos adquirir conhecimentos práticos e teóricos sobre esta ferramenta. 

3. Ciclo de análise preditiva: receberemos um novo desafio com novos conjuntos de dados. A ideia é resolver problemas relacionados ao universo da análise preditiva. 

Ao final deste módulo, você terá adquirido uma grande gama de conhecimento sobre Python e seus principais pacotes para análise e manipulação de dados: Pandas e Seaborn. Mas também, conhecimento de estatística com Python. E com isso, terá segurança para fazer análises utilizando essa poderosa ferramenta que é a linguagem de programação Python. 

Sem mais delongas, vamos iniciar nossa jornada de aprendizado com a linguagem de programação Python! 

### **Aulas 2 e 3: Plataforma Google Colab** 

Antes de iniciarmos o nosso conteúdo de fundamentos, vamos primeiro preparar o nosso ambiente de estudos. Para isso, iremos utilizar a 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

3 

plataforma Google Colab. O Colab é uma plataforma de desenvolvimento, estudos e prototipação amplamente utilizada na área de dados. 

Por possuir um repositório próprio e uma ferramenta visual para criação de variáveis de ambiente e instalação de pacotes e bibliotecas, será uma ferramenta essencial para a realização das aulas e atividades práticas. 

Não é necessário instalar o Colab na sua máquina, apenas acessar a plataforma através do seu navegador. 

Já no Colab, selecione o menu "Arquivo". 



<!-- Start of picture text -->
co Damos-Ihe as boas-vindes a0 Colaboratory<br>Ficheiro, Editar Ver Inserir Tempode execucéo Ferramentas Ajuda<br>= indew Ca x. +08009 + Teno | CopirparsoOme<br>rodeo Damos-lhe as boas-vindas; ao Colab!<br>oy 7<br>ee Mrendizagem atomstica (Novo) Experimente a API Gemini<br>ones + Generate a Geri APtey<br>+ jxempos emdestque ++ GeminiTako GeminiAP Quickstart ih the with Spaach-to-Text Python AP<br>— Secqio ++ ComeareGemini APL Gemini code sample with ChatGPr<br>+ More notebooks<br>Se{a conhece Cola, va este video para saber mals sobre as tabelasinerativas a ita de histrico do céigo executado ea paleta de<br>comands.<br><!-- End of picture text -->



<!-- Start of picture text -->
(ae) Damos-lhe as boas-vindas ao Colaboratory<br>Ficheiro. Editar Ver Inserir Tempodeexecucéo Ferramentas Ajuda<br>= | in Novo bloco de notas no Drive xxto. __Copiar para o Drive<br>Abrir bloco de notas Ctri+to.<br>Q 1 Carregar bloco de notas<br>Ihe as boas-vindas ao Colab!<br>{x}<br>Ge |_—_«Guatdar uma eépia no Drive ‘perimente a API Gemini<br>| Guardar uma cépia como um Gist do GitHub<br>o Guardar uma cépia no GitHub teGemini a API key<br>Zemini with the Speech-to-Text API<br>_ Guardar Ctri#S API: Quickstart with Python<br>| ‘API code sample<br>Transferir te Gemini with ChatGPT<br>atebooks<br>Imprimir ctrise<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

4 

Após abrir o menu, podemos criar um novo _notebook_ na opção “Abrir notebook”. 



<!-- Start of picture text -->
co Damos-lhe as boas-vindas ao Colaboratory<br>| Ficheiro | Editar Ver Inserir Tempodeexecugdo Ferramentas Ajuda<br>= iin Novo bloco de notas no Drive ixto Copiar para o Drive<br>Abrir bloco de notas Ctr+o<br>Q 1 Carregar bloco de notas<br>Ihe as boas-vindas ao Colab!<br>{x}!<br>Ge | __ Guardar uma cépia no Drive :perimente a API Gemini<br>| Guardar uma cépia como um Gist do GitHub<br>o Guardar uma cépia no GitHub Geminitea<br>Semini with theAPI key Speech-to-Text<br>Guardar API<br>API code sample<br>( Ctrl#S API: Quickstart with Python<br>»<br>Transferir te Gemini with ChatGPT<br>cise<br>imprimir atebooks<br><!-- End of picture text -->

A partir daí temos o notebook novo para desenvolvermos nosso código. Uma gama das principais bibliotecas já estão disponíveis no Colab sem a necessidade de instalarmos. 



<!-- Start of picture text -->
Oeste© untitedo.ipyndcau er met Tenpodecece Ferment Aut<br>fet Sdgo + Tero<br>—° ————<br>&<br>o<br>o<br><!-- End of picture text -->

Com isso, temos o nosso ambiente pronto para o curso! 

A partir de agora usaremos os _notebooks_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

5 



<!-- Start of picture text -->
co 6 Formagao em Analise de Dados —Indicium, *<br>Ficheiro Editar Ver Inserir Tempodeexecugéo Ferramentas Ajuda Todas as alteracdes foram guardadas.<br><!-- End of picture text -->

Todo arquivo do tipo _notebook_ possui a extensão ".ipynb". Sempre que criarmos um arquivo através do editor, estaremos criando um arquivo _notebook_ . 

Arquivos _notebook_ são excelentes ferramentas para prototipação de códigos Python, pois este tipo de arquivo é dividido em células, o que nos permite rodar vários "snippets" - partes pequenas de códigos - sem termos que rodar uma aplicação Python por completo. 

Além de possibilitar a escrita de códigos Python, arquivos notebook também permitem a escrita de códigos na linguagem R e em linguagem de marcação - <u>Markdown.</u> 

Alguns comandos podem ser executados através da interface gráfica do editor. Para inserir uma nova célula, podemos acessar o menu "Célula de código". 



<!-- Start of picture text -->
co & Formacao em Anilise de Dados - Indicium  ¥¥<br>Ficheiro Editar Ver Inserir Tempodeexecugéo Ferramentas Ajuda Todas as alteracdes foram guardadas.<br>r=~ + Cédigo + Texto Célula de cédigo ctr+MB<br>Célula de texto<br>Q fi) see com] Célula de cabegalho da seccdo<br>{x} warnings. filte Célula de cédigo de rascunho Ctrl+alten<br>o 1 °intint ("F (“Formacé. _ Fragmentosdo cédigo Ctrltalt+P<br>Se Formacio anéli Adicionar<br>~ um campo de formulério<br><!-- End of picture text -->

Por fim, outro comando, ou ação, extremamente importante e que será usada a todo momento durante este módulo é a execução de uma célula. Executar uma célula significa executar o código que há dentro dela. Ou seja, se adicionarmos um código Python dentro de uma célula, e desejamos executar esse código, temos que executar essa célula também. 

Para executarmos a célula atual utilizamos o comando "CTRL + ENTER", ou 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

6 

podemos apertar o botão para execução como é mostrado abaixo: 



<!-- Start of picture text -->
co © Formagao em Analise de Dados - Indicium<br>Ficheiro Editar Ver Inserir Tempode execugéo Ferramentas Ajuda Todas as alteracdes foram quardada:<br>t= + Codigo + Texto<br>Q © import warnings<br>FogI ExecutorA célula nocélulafoi (Crl+Enter)executada nesta sesso<br><!-- End of picture text -->

O atalho do teclado "SHIFT + ENTER" executa a célula e cria uma outra logo abaixo da célula executada. 

Com esses conceitos e comandos básicos, já conseguimos seguir com os conteúdos do curso! 

### **Aulas 4 e 5: Comando print com Python** 

O Python é uma linguagem de programação moderna multiparadigma e multiplataforma, o que a torna uma ferramenta maleável e útil, pois conseguimos utilizar várias técnicas de desenvolvimento, e tudo que construirmos poderá ser executado em qualquer sistema operacional. 

Além disso, ela é uma linguagem de código aberto, o que faz com que ela tenha uma grande comunidade que a mantém atualizada, criando novas funcionalidades e corrigindo bugs, além de criar pacotes, bibliotecas e frameworks, deixando-a cada vez mais pronta para ser utilizada em qualquer frente. 

Fora isso, é uma linguagem que possui uma curva de aprendizado baixa, sendo simples de aprender e de utilizar. 

São esses e outros motivos que fazem com que o Python atualmente seja a linguagem de programação mais utilizada na área de dados, sendo para a realização de análises ou para a criação de Machine Learning. 

Outro ponto importante de conversarmos é sobre como o Python funciona. Observe o Diagrama abaixo: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

7 



<!-- Start of picture text -->
() ‘tla<br>CO CC )<br>o _ || _.| allal<br>Escrevemos e O Computador O Computador<br>executamos os Interpretaos exibe os resultados<br>comandos Comandos e os dos comandos<br>Executa executados<br><!-- End of picture text -->

O diagrama acima representa o processo, embora simplificado, de como um código Python é executado e gera os seus resultados. Entender esse processo é importante para nos ajudar a resolver erros que serão gerados quando desenvolvemos nossos códigos, uma vez que o Python irá executar estritamente o que escrevermos. 

Outros dois tópicos muito importantes para o nosso início são o comando "print( )" e como escrever comentários em Python. 

O comando "print()" é um comando extremamente útil e que usaremos sempre, tanto no curso, quanto profissionalmente. Suas principais funções são: 

- Exibir mensagens em tela 

- Exibir o conteúdo de variáveis 

- Exibir os tipos das variáveis 

- Muito utilizado para debug 

Para exemplificar, vamos utilizar o comando "print()" para exibir uma mensagem qualquer e executar a célula para vermos o resultado: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

8 



<!-- Start of picture text -->
x [1] print("Forma¢ao Andlise de Dados")<br>SY Formacao Analise de Dados<br><!-- End of picture text -->

Ponto importante que devemos aprender neste momento: sempre que executarmos uma célula dentro do Google Colab, será adicionado um número dentro do  "[ ]": 



<!-- Start of picture text -->
¥ [2] print("Médulo 8 - Python")<br>Sy Modulo 8 - Python<br><!-- End of picture text -->

Esse número representa a ordem de execução da célula. Ou seja, o número 2 nos diz que essa célula foi a segunda a ser executada dentro do Colab. Se fosse a terceira, o número seria o 3. Se fosse a quarta, o 4. E assim sucessivamente. 

Outro ponto importante é que se desejamos exibir uma mensagem, essa mensagem deve estar entre aspas "duplas" ( " ) ou aspas "simples" ( ' ). Porém, sempre que utilizarmos aspas "duplas", devemos finalizar o texto com aspas "duplas". A mesma coisa vale para aspas ‘simples’. 



<!-- Start of picture text -->
% [3] print('Texto com aspas simples')<br>SY Texto com aspas simples<br><!-- End of picture text -->

Isso indica ao Python que estamos utilizando um texto, dentro do comando "print()", para ser exibido. Por fim, podemos ver que o resultado do comando "print()", ou seja, o texto que pedimos para ser exibido, foi 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

9 

exibido logo abaixo da célula: 



<!-- Start of picture text -->
x [3] print('Texto com aspas simples')<br>Sy Texto _com_aspas simples<br><!-- End of picture text -->

É importante ressaltar que no Colab não é obrigatório o uso da função "print()" para que um valor seja exibido. Caso se escreva uma mensagem na célula e esta for executada, ainda assim ela será exibida. 



<!-- Start of picture text -->
x [4] "Mensagem sem o uso da funcao print()"<br>SY ‘Mensagem sem o uso da fun¢ao print()'<br><!-- End of picture text -->

O mesmo vale para variáveis, assunto que veremos mais para frente. 

Por fim, mas não menos importante, temos os comentários em Python. Comentários são textos que não serão executados pelo Python. Ou seja, o interpretador do Python ignora completamente os comentários que escrevemos e identificamos como comentário. 

Para identificar algo como comentário, basta colocar na frente do texto escrito o caractere, ou símbolo, sustenido ( # ) 



<!-- Start of picture text -->
~ [5] # Isto é um comentdrio<br>print('Indicium Tech’)<br>Sy Indicium Tech<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

10 

Tudo que estiver à frente de um sustenido, o Python irá identificar como comentário e não irá executar esse comando. 

### **Aulas 6 e 7: Tipos primitivos e uso do type** 

Um tópico extremamente importante, para qualquer linguagem de programação, são as variáveis. Variáveis, nada mais são que locais para armazenarmos conteúdos ou resultados. 

Digamos que desejamos criar uma variável para armazenar o resultado da soma entre os números 2 e 3. Em Python, para criarmos essa variável, basta colocar o nome que desejamos dar a ela - vamos utilizar "resultado" - e depois o seu conteúdo. 



<!-- Start of picture text -->
¥ [6] # Criacao de uma variavel<br>resultado = 2 + 3<br><!-- End of picture text -->

Pontos importantes ao observarmos na criação de uma variável: 

- Toda variável precisa ter um nome. Ele deve ser sempre minúsculo, não deve ter espaços e nem acentos ou caracteres especiais, como o cedilha. 

- Python é uma linguagem de programação case sensitive. Ou seja, ele diferencia letras maiúsculas de minúsculas, fazendo com que uma variável chamada “Python” seja diferente de outra variável chamada “python”. 

- Caso a sua variável precise ter um nome composto, ou seja, dois nomes, deve-se utilizar o padrão <u>snake_case.</u> 

- Toda variável deve ser criada recebendo algum valor. Caso você não saiba qual valor colocar, utilize o zero ou algum outro valor que faça sentido para o seu problema. 

- Utilizamos o símbolo de igual ("=") para definirmos que uma variável vai receber um determinado valor. O símbolo de comparação no 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

11 

Python é igual duas vezes  ("==" - conforme veremos mais adiante no módulo). 

- Os símbolos de operações matemáticas no Python são os mesmos que já são utilizados normalmente. 

Além disso, toda variável tem um tipo de dado atrelado a ela. Esse tipo de dado é extremamente importante dentro do Python. Nesta aula iremos aprender sobre os tipos primitivos dentro do Python. 

O tipos primitivos em Python são: 

- Numérico inteiro - tipo "int": É o tipo utilizado para armazenar conteúdos numéricos inteiros, ou naturais. 

- Numérico decimal - tipo "float": É o tipo utilizado para armazenar conteúdos numéricos decimais, ou reais. O separador da casa decimal com o valor inteiro é o **PONTO** ( "." ) e não a vírgula em Python 

- Textual - tipo "str": É o tipo utilizado para armazenar textos ou caracteres únicos. 

- Binários (Verdadeiro ou Falso) - tipo "bool": É utilizada quando desejamos criar uma variável para receber um valor que ou é verdadeiro ("True") ou é falso ("False") 



<!-- Start of picture text -->
x [7] # Uma variadvel para cada tipo de dado<br>inteiro = 108<br>decimal = 1.08<br>texto = 'Analise de Dados'<br>booleano = False<br><!-- End of picture text -->

Para verificarmos qual o tipo da variável, basta utilizar o comando "type()". Por exemplo: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

12 



<!-- Start of picture text -->
x [8] # Verificando o tipo para varidvel "texto"<br>type(texto)<br>=> —<str<br><!-- End of picture text -->

Ao executarmos a célula verificamos que a variável é do tipo _string_ , ou seja, textual. 

Para verificarmos todos os tipos de todas as variáveis que criamos, podemos utilizar o comando "print()" para isso: 



<!-- Start of picture text -->
XY [9] print(f'O tipo da variavel "inteiro" é : {type(inteiro)}')<br>print(f'O tipo da variavel "decimal" é : {type(decimal)}')<br>print(f'O tipo da variavel "texto" é : {type(texto)}')<br>print(f'O tipo da variavel "booleano" é : {type(booleano)}')<br>Sy 0 tipo da varidvel “inteiro” é : <class ‘int'><br>O tipo da variavel "decimal" é : <class 'float'><br>O tipo da variadvel "texto" 6 : <class '‘str'><br>O tipo da variavel "booleano" é : <class 'bool'><br><!-- End of picture text -->

Observe que estamos usando o comando "type()" dentro do comando "print()". Isso é possível em Python utilizando o padrão <u>f-string. Que</u> basicamente consiste em colocarmos um "f" na frente do texto que desejamos exibir, e todas as variáveis ou comandos que desejamos exibir devem ser colocados dentro das chaves ("{ }"). Um ponto de atenção é o uso de aspas duplas e simples nesse contexto. Em Python não podemos utilizar aspas duplas dentro de aspas duplas, assim como não podemos utilizar aspas simples dentro de aspas simples, pois o código retorna o seguinte erro 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

13 



<!-- Start of picture text -->
© oO print(f"O tipo da variavel “inteiro” é : {type(inteiro)}"<br>ya File "<ipython-input-10-e9017ddafe99>", line 1<br>print(f"O tipo da variavel "“inteiro" é& : {type(inteiro)}")<br>a<br>SyntaxError: invalid syntax. Perhaps you forgot a comma?<br><!-- End of picture text -->

### **Aulas 8 e 9: Operadores** 

Operadores são símbolos, ou até mesmo palavras, utilizadas para realizar determinadas operações com variáveis ou valores. Eles normalmente são classificados em 

- Operadores aritméticos; 

- Operadores de atribuição; 

- Operadores de comparação; 

- Operadores lógicos; 

- Operadores de identidade; 

- Operadores de associação. 

Vamos destrinchar melhor cada uma dessas categorias e trazer casos de uso para facilitar o entendimento 

1. Operadores aritméticos: utilizados para realizar operações matemáticas como soma e subtração. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

14 

|**Operador**|**Uso**|**Conceito**|
|---|---|---|
|+ (Adição)|x = 10 + 5|Realiza a soma entre<br>os valores|
|- (Subtração)|x = 8 - 4|Realiza a subtração<br>entre os valores|
|*  (Multiplicação)|x = 2 * 2|Realiza a<br>multiplicação entre os<br>valores|
|/ (Divisão)|x = 20 / 4|Realiza a divisão entre<br>os valores|
|// (Divisão inteira)|x = 100 // 3|Retorna apenas a<br>parte inteira do<br>resultado da divisão|
|% (Resto da divisão)|x = 34 % 2|Retorna o resto da<br>divisão|
|** (Exponenciação)|x = 3 ** 2|Realiza a operação de<br>exponenciação|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

15 



<!-- Start of picture text -->
aa [11] adicao=5+7<br>subtracao = 5 - 8<br>multiplicacao = 2 * 2<br>divisao = 28 / 20<br>divisao_inteira = 10 // 4<br>resto = 10 / 3<br>exponenciacao = 2 ** 3<br>print(f'Resultado da adicao: {adicao}')<br>print(f'Resultado da subtracdo: {subtracao}")<br>print(f'Resultado da multiplicacao: {multiplicacao}’)<br>print(f'Resultado da divisdo: {divisao}")<br>print(f'Resultado da divisdo inteira: {divisao_inteira}')<br>print(f*Resultado do resto da divisdo: {resto}")<br>print(f'Resultado da exponenciacao: {exponenciacao}’)<br>Sy Resultado da adicdo: 12<br>Resultado da subtracao: -3<br>Resultado da multiplicacao: 4<br>Resultado da divisdo: 1.0<br>Resultado da divisdo inteira: 2<br>Resultado do resto da divisdo: 3.3333333333333335<br>Resultado da exponenciacao: 8<br><!-- End of picture text -->

2. Operadores de atribuição: operadores usados para atribuir valores à variáveis. Vários desses operadores serão muito úteis quando formos falar de _loops_ mais pra frente. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

16 

|**Operador**|**Uso**|**Equivalente a**|**Conceito**|
|---|---|---|---|
|=|x = 1|–|Atribui o valor à<br>variável|
|+=|x += 1|x = x + 1|Soma o valor ao<br>valor<br>armazenado na<br>variável|
|-=|x -= 1|x = x - 1|Subtrai o valor<br>ao valor<br>armazenado na<br>variável|
|*=|x *= 1|x = x * 1|Multiplica o<br>valor ao valor<br>armazenado na<br>variável|
|/=|x /= 1|x = x / 1|Divide o valor ao<br>valor<br>armazenado na<br>variável|
|%=|x %= 1|x = x % 1|Calcula o resto<br>da divisão entre<br>o valor atual da<br>variável e o<br>valor ao valor<br>atribuído|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

17 



<!-- Start of picture text -->
¥ [12] x = 2 # varidvel x com valor atribuido<br>X += 8 # nova atribuic&o somando um valor 4 varidvel<br>y = 20 # varidvel y com calor atribuido<br>y -= 45 # nova atribuicdo subtraindo valor<br>print(f'Variadvel x: {x}')<br>print(f'Variavel y: {y}')<br>S¥ Varidvel x: 16<br>Varidvel y: -25<br><!-- End of picture text -->

3. Operadores de comparação: operadores utilizados a fim de comparar valores. 

|**Operador**|**Uso**|**Conceito**|
|---|---|---|
|> (Maior que)|x > 10|Verifica se um valor é<br>maior que outro|
|< (Menor que)|x < 20|Verifica se um valor é<br>menor que outro|
|== (Igual a)|x == 12|Verifica se um valor é<br>igual a outro|
|!= (Diferente de)|x != 3|Verifica se um valor é<br>diferente de outro|
|>= (Maior ou igual)|x >= 15|Verifica se um valor é<br>maior ou igual a outro|
|<= (Menor ou igual)|x <= 30|Verifica se um valor é<br>menor ou igual a outro|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

18 



<!-- Start of picture text -->
% [23] a = 20<br>print(f'A varidvel "a" é igual a 30? R: {a == 30}")<br>Sy A varidvel "a" é igual a 30? R: False<br>¥%v [14] b = 3e<br>print(f'A varidvel "b” 6 diferente de 40? R: {b != 50}')<br>Sy A varidvel “b" é diferente de 4@? R: True<br>¥- [15] ¢d == 9936<br>print(f°A varidvel "c" & maior que "d"? R: {c > d}")<br>Sy A varidvel “c" é maior que “d"? R: True<br>hd O --4<br>f= 54<br>print(f'A varidvel “e" & menor ou igual a "f"? R: {fe <= f}")<br>Sy A varidvel “e" é menor ou igual a "f"? R: True<br><!-- End of picture text -->

4. Operadores lógicos: utilizados para combinar duas ou mais condições. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

19 

|**Operador**|**Uso**|**Conceito**|
|---|---|---|
|and|x > 2 and x < 10|Retorna True se todas<br>as condições forem<br>verdadeiras, caso<br>contrário retorna False|
|or|x == 5 or x != 22|Retorna True se uma<br>das condições for<br>verdadeiras, caso<br>contrário retorna False|
|not|not(x > 1 and x < 5)|Inverte o resultado: se<br>o resultado da<br>expressão for True, o<br>operador retorna false|





<!-- Start of picture text -->
“ [17] x =2<br>x > 1 and x < 18<br>Sy True<br>“ [18] y = 10<br>y == 10 or y == ‘Indicium'<br>Sy True<br>~ [19] z= 55<br>not(z == 98<br>Sy True<br><!-- End of picture text -->

5. Operadores de identidade: verifica se dois objetos ocupam o mesmo lugar na memória, ou seja, se são o mesmo objeto. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

20 

|**Operador**|**Uso**|**Conceito**|
|---|---|---|
|is|name is “Marcos”|Retorna True se as<br>variáveis comparadas<br>forem o mesmo objeto|
|is not|x is not “Python”|Retorna True se as<br>variáveis comparadas<br>não forem o mesmo<br>objeto|





<!-- Start of picture text -->
Y [21] cargo = ‘Professor’<br>cargo is ‘Professor’<br>Sy True<br>x [22] linguagem = ‘Java’<br>linguagem is not ‘Java’<br>Sy False<br><!-- End of picture text -->

6. Operadores de associação: são usados para verificar se um valor ou objeto está presente dentro de uma sequência, como listas, tuplas, strings, etc. 

|**Operador**|**Uso**|**Conceito**|
|---|---|---|
|in|“n” in “North”|Retorna True caso o<br>valor seja encontrado<br>na sequência|
|not in|“n” not in “South”|Retorna True caso o<br>valor não seja<br>encontrado na<br>sequência|



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

21 



<!-- Start of picture text -->
x [23] ‘In’ in ‘Indicium'<br>Sy True<br>¥ [26] ‘Forma’ not in *Indicium’<br>Sy True<br><!-- End of picture text -->

### **Aula 10: Listas** 

Em Python, além dos tipos primitivos, temos também tipos de "coleções". Um desses tipos são as listas. Listas em Python são variáveis que nos permitem armazenar mais de um valor ou até mesmo outras variáveis dentro delas. 

Listas são extremamente úteis e muito utilizadas no dia-a-dia, por serem fáceis de manipular. Para criarmos uma lista podemos utilizar colchetes no lugar do valor da variável, outra forma é definir a variável como "list()": 



<!-- Start of picture text -->
aa [12] # Criacao de uma lista vazia<br>lista = []<br>outra_lista = list()<br># Exibindo o tipo de varidvel<br>print(f'Tipo de variavel de "lista": {type(lista)} \n')<br># Exibindo o conteudo da variavel outra_lista<br>print(f'Conteddo da variavel “outra_lista": {outra_lista}')<br>Sy Tipo de variavel de "lista": <class ‘list'><br>Contetdo da variadvel "“outra_lista": []<br><!-- End of picture text -->

Observe que foram criadas duas variáveis do tipo "list". E nas linhas posteriores, exibimos tanto o seu tipo de dado - "list" - quanto o conteúdo da variável “outra_lista” - "[ ]" - que, no caso, está vazia. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

22 

Ainda na célula da imagem acima usamos os caracteres “\n” é uma instrução para a quebra de linha do texto. Podemos identificar essa ação como o espaço criado entre as duas sentenças exibidas após a execução da célula. 



<!-- Start of picture text -->
4 ie de variavel de "lista": <class ‘list'><br>Contetdo da variavel "“outra_lista": []<br><!-- End of picture text -->

Podemos criar uma lista com conteúdo. Para isso, basta colocar os conteúdos dentro dos colchetes: 



<!-- Start of picture text -->
x [15] # Definindo uma lista com conteudo<br>lista = ['Formacao', 'Analise', 'Dados']<br># Exibi¢cao do tipo de variavel<br>print(f'Tipo da variavel "lista": {type(lista)}')<br># Conteudo da variavel<br>print(f'Conteudo da variavel {lista}')<br>Sy Tipo da varidvel "lista": <class ‘list'><br>Contetido da variavel ['Formacao', 'Analise', 'Dados']<br><!-- End of picture text -->

Observe que agora, a lista possui conteúdo, que são os valores definidos dentro dos colchetes. Podemos colocar qualquer valor dentro de uma lista: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

23 



<!-- Start of picture text -->
os >) # Lista com diversos tipos de dados<br>lista = [1.08, 108, “Indicium", True]<br># Exibindo o conteudo da lista<br>print(f'Conteudo da variadvel: {lista}')<br>ay Conteudo da variavel: [1.08, 108, ‘Indicium', True]<br><!-- End of picture text -->

### **Aulas 11 e 12: Principais funções de listas** 

Os conteúdos de uma lista são armazenados em índices. Ou seja, quando criamos uma lista e adicionamos um novo conteúdo à ela, esse conteúdo será armazenado em um índice. Os índices de uma lista iniciam sempre do zero. 

Por exemplo, se criarmos uma lista com o seguintes conteúdos: 



<!-- Start of picture text -->
x [25] print(f'Conteudo da lista: {lista}')<br><> Conteudo da lista: [1.08, 108, 'Indicium', True]<br>indices da lista: i) 1 2 3<br><!-- End of picture text -->

Os índices de cada conteúdo serão os valores em vermelho, logo abaixo do conteúdo. Portanto, podemos acessar os elementos de uma lista através do seu índice: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

24 



<!-- Start of picture text -->
x [26] # Criando a mesma lista dos exemplos anteriores<br>lista = [1.08, 108, "Indicium", True]<br># Exibindo o conteudo<br>print(f'Conteudo da lista: {lista}')<br># Exibindo elementos especificos da lista<br>print(f'O elemento de indice @ da lista é: {lista[9]}')<br>print(f'O elemento de indice 3 da lista é: {lista[3]}')<br>Sy Contetdo da lista: [1.08, 108, 'Indicium', True]<br>O elemento de indice @ da lista é: 1.08<br>O elemento de indice 3 da lista é: True<br><!-- End of picture text -->

Para adicionar, remover e inserir novos dados na lista há algumas funções nativas do Python. As principais 

- append(x): Adiciona um item ao final da lista. 



<!-- Start of picture text -->
% [22] print(f'Lista antes da adi¢ao: {lista} \n')<br># Adicionando elemento ao final da lista<br>lista. append(2024)<br>print(f'Lista apds adi¢ao: {lista}')<br>Sd Lista antes da adicao: [1.08, 108, 'Indicium', True]<br>Lista apds adi¢ao: [1.08, 108, ‘Indicium', True, 2024]<br><!-- End of picture text -->

- remove(x): Remove a primeira ocorrência do valor especificado. Retorna um erro caso o item que não esteja na lista. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

25 



<!-- Start of picture text -->
xy © # Adicdo de um dado repetido a lista<br>lista.append('Indicium')<br>print(lista, '\n')<br># Remoc&o de item da lista<br>lista.remove('Indicium')<br>print(f'Lista apds remo¢ao do item: {lista}')<br>Sy [1.08, 108, "Indicium', True, 2024, ‘Indicium']<br>Lista apds remocao do item: [1.08, 108, True, 2024, ‘Indicium']<br><!-- End of picture text -->



<!-- Start of picture text -->
© [31] # Caso se tente remover um item que ndo esta na lista<br>lista.remove(False)<br>ValueError Traceback (most recent call last)<br>S<ipython-input-31-81906a8ea520> in <cell line: 3>()<br>1 # Caso se tente remover um item que nao esté na lista<br>2<br>----> 3 lista.remove(False)<br>ValueError: list.remove(x): x not in list<br><!-- End of picture text -->

- insert(i, x): Insere um novo item na posição (índice) especificado. 



<!-- Start of picture text -->
Y% [32] # Insercdo de um item na lista<br>lista.insert(@, 'Posic&o') # indice, item<br>print(f'Lista apés insercao do item: {lista}')<br>Sy Lista apés insercdo do item: ['Posic&o', 1.08, 108, True, 2024, ‘Indicium']<br><!-- End of picture text -->

- pop(i): Remove o item que ocupa a posição do índice passada na função. Se esse não for especificado, remove o último item. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

26 



<!-- Start of picture text -->
% [33] # Remocao do item na posicdo @ da lista<br>lista.pop(@)<br>print(f'Lista apds a remocdo do 12 item: {lista} \n')<br># Remo¢ao de item sem especifica¢ao do indice<br>lista.pop()<br>print(f'Lista apdéds a remocdo sem especificacao do indice: {lista}')<br>Sa Lista apds a remo¢ao do 1° item: [1.08, 108, True, 2024, 'Indicium']<br>Lista apéds a remo¢ao sem especifica¢ao do indice: [1.08, 108, True, 2024]<br><!-- End of picture text -->

- index(x): Retorna o índice da primeira ocorrência do item passado na função. 



<!-- Start of picture text -->
x [77] # Adi¢cao de elemento repetido a lista<br>lista.append(True)<br>print(f'Lista: {lista} \n')<br># Verificacao do indice da 12 ocorréncia<br>print(f'Index: {lista.index(True)}')<br>Dy— Lista:. [1.08, 108, True, 2024, True]<br>Index: 2<br><!-- End of picture text -->

- count(x): Retorna o número de ocorrências do valor passado na função. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

27 



<!-- Start of picture text -->
x [78] # Contagem de item na fun¢ao<br>lista.count(True)<br>Sy 2<br><!-- End of picture text -->

- sort(): Ordena a lista. Aceita um argumento _reverse_ para ordenar a lista de forma decrescente. 



<!-- Start of picture text -->
x [80] # Criac&o de lista numérica<br>numeros = [2, 3, 5, 1, 4]<br># Ordena¢ao crescente<br>numeros.sort()<br>print(f'Lista ordenada de forma crescente: {numeros} \n')<br># Ordenacao decrescente<br>numeros.sort(reverse=True)<br>print(f'Lista ordenada de forma decrescente: {numeros} \n')<br>y Lista ordenada de forma crescente: [1, 2, 3, 4, 5]<br>Lista ordenada de forma decrescente: [5, 4, 3, 2, 1]<br><!-- End of picture text -->

### **Aula 13: Dicionários** 

Outra variável do tipo coleção é o dicionário. O dicionário, ao contrário das listas, possui índices manipuláveis, ou editáveis. Isso significa que podemos criar o índice utilizando qualquer tipo de variável primitiva que quisermos, porém, os tipos mais utilizados são números inteiros - tipo "int" - e textos - tipos "str". 

Para criar um dicionário vazio, utilizamos as chaves: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

28 



<!-- Start of picture text -->
x [81] # Criando uma variavel do tipo dicionario<br>dicionario = {}<br># Exibindo o seu tipo<br>print(f'Tipo da variavel: {type(dicionario)} \n')<br># Exibindo o conteudo da variavel<br>print(f'Contetdo: {dicionario}')<br>Sy Tipo da varidvel: <class ‘dict'><br>Conteudo: {}<br><!-- End of picture text -->

Observe que agora, o tipo da variável é "dict", que representa a palavra dictionary em inglês. Dicionário é outra estrutura muito utilizada na linguagem Python. Caso queiramos criar um dicionário contendo valores, dentro, utilizamos a chaves para delimitar o conteúdo do dicionário e utilizamos o padrão "chave: valor" para criarmos os seus elementos internos: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

29 



<!-- Start of picture text -->
% [82] # Criando variadvel de diciondrio preenchida<br>dicionario = {<br>‘inteiro': 108,<br>‘decimal’: 1.08,<br>"texto': 'Indicium',<br>"bool': True,<br>"lista': [1, 2, 3, 4, 5]<br>}<br># Exibindo o conteudo da variavel<br>dicionario<br>Sy {‘inteiro': 108,<br>‘decimal’: 1.08,<br>"texto': 'Indicium',<br>‘bool’: True,<br>"lista': [1, 2, 3, 4, 5]}<br><!-- End of picture text -->

Observe que a "chave" do conteúdo da lista, diz respeito ao conteúdo do "valor". Ou seja, quando utilizamos a chave "inteiro", iremos acessar o valor "108". Quando utilizamos a chave "texto", iremos acessar o valor "Indicium". Se utilizarmos a chave "lista", acessamos a lista que existe dentro do dicionário: 



<!-- Start of picture text -->
x [83] # Acessando valores de diferentes chaves<br>print(f'Acesso ao valor da chave “inteiro": {dicionario["inteiro"]}')<br>print(f'Acesso ao valor da chave "texto": {dicionario["texto"]}')<br>print(f'Acesso ao valor da chave "lista": {dicionario["lista"]}')<br>S¥ Acesso ao valor da chave “inteiro": 108<br>Acesso ao valor da chave "texto": Indicium<br>Acesso ao valor da chave “lista”: [1, 2, 3, 4, 5]<br><!-- End of picture text -->

Ou seja, se precisamos acessar um valor de um dicionário, utilizamos a chave desse valor. Para criar uma nova chave, basta utilizar o seguinte padrão: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

30 

Python dicionario['nova_chave'] = valor 

Desta forma, iremos criar uma nova chave, contendo um novo valor dentro do dicionário: 



<!-- Start of picture text -->
print(#*chaves antes da insereo: (dicionario.keys()} \n")<br>dicionario[print (F*Contetido‘dict"]do =dicionério:(‘estado': (dicionario}"cearé"} \n")<br>Contetido do dicionsrio: ("inteiro': 108, ‘decimal’: 1.08, ‘texto’: “Indiciun’, "bool": True, ‘Lista’: [1, 2, 3, 4, 5], ‘dict: (‘estado": ‘ceans")}<br>Chaves apés a inserc3o: dict keys({*inteiro', ‘decimal’, ‘texto’, "bool", ‘Lista’, ‘dict*))<br><!-- End of picture text -->

Observe que estamos utilizando uma função que nos devolve somente as chaves da lista. Mas também, estamos criando um novo elemento no dicionário, cuja chave é o texto "dict" e o seu valor é um outro dicionário! 

Porém, os dicionários precisam que suas chaves sejam únicas. Isso significa que não pode haver duas chaves chamadas "texto" dentro do dicionário. Se tentarmos fazer a inserção de um elemento e a sua chave já existir na lista, o valor da chave já existente será atualizado: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

31 



<!-- Start of picture text -->
% [90] # Redefinindo a varidvel diciondrio<br>dicionario = {<br>‘inteiro': 108,<br>“texto': ‘Indicium’<br>}<br># Exibindo valores da variavel<br>print(f'valores da variavel dicionario: {dicionario} \n')<br># Tentativa de inserir novo valor com chave ja existente<br>dicionario['texto'] = ‘Andlise de dados’<br># Nova exibicao da variavel<br>print(f'valores da variavel apés tentativa: {dicionario}')<br>3} valores da variavel diciondrio: {"inteiro': 108, ‘texto’: ‘Indicium'}<br>valores da varidvel apés tentativa: {'inteiro': 108, ‘texto’: ‘Andlise de dados’}<br><!-- End of picture text -->

### **Aulas 14 e 15: Funções de dicionário** 

Além da função key() que vimos anteriormente, também existem outras funções nativas para dicionários no Python. As principais são 

● values(): Retorna aos valores do dicionário. 



<!-- Start of picture text -->
~ [93] # Exibindo apenas valores do dicionario<br>print(f'Valores do dicionario: {dicionario.values()}')<br>3¥ valores do diciondrio: dict_values([108, 'Andlise de dados'])<br><!-- End of picture text -->

- items(): Retorna os pares chave e valor do dicionário. 



<!-- Start of picture text -->
¥, [94] # Exibindo os pares do dicionario<br>print(f"Exibi¢&o dos items do dicionério: {dicionario.items()}")<br>Sy Exibicdo dos items do diciondrio: dict_items([(‘inteiro’, 108), (‘texto’, ‘Andlise de dados')])<br><!-- End of picture text -->

> Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

32 

● pop(): Remoção da chave especificada na função. 



<!-- Start of picture text -->
x [95] # Remocdo de chave especificada<br>dicionario.pop(‘inteiro’ )<br>print(f'Diciondrio com chave "inteiro" removida: {dicionario}')<br>Sy Diciondrio com chave "“inteiro" removida: {'texto': ‘Andlise de dados'}<br><!-- End of picture text -->

### **Aula 16: Estruturas de decisão** 

No nosso código podemos executar comandos diferentes conforme a condição desejada. Isso é possível, em Python, utilizando estruturas de decisão. 

Em Python, utilizamos o comando "if" para criarmos estruturas de decisão. Esse comando permite que façamos testes de verificações e comparações, de forma a tomar ações diferentes conforme o resultado destas verificações/comparações. 

A estrutura do comando "if" é a seguinte: 

Python 

# Verifica se uma determinada condição 

# é verdadeira 

if teste_verificacao: 

# comandos 

Além desta estrutura base, temos ainda uma segunda estrutura, que permite executar um conjunto de comandos caso o teste ou verificação seja verdadeira, e um outro conjunto de comandos caso o teste ou verificação seja falso: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

33 

Python # Verifica se uma determinada condição # é verdadeira if teste_verificacao: # Se sim, executa os comandos # dentro do if else: # Se não, executa os comandos #dentro do else 

E além destas duas estruturas, temos ainda uma terceira, que pode ser encadeada sempre que precisarmos realizar outros testes: 

Python # Verifica se uma determinada condição # é verdadeira if teste_verificacao: # Se sim, executa os comandos # dentro do if elif novo_teste_verificacao: # Se não, realiza o novo teste e/ou # verificação else: # Se nenhuma das verificações ou # testes anteriores forem verdadeiros # executa os comandos dentro do #else 

E esta terceira opção é exatamente a opção que precisamos para resolver o nosso primeiro desafio. 

### **Aula 17: Utilizando a estrutura** **_if_ no Python** 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

34 

Agora que já sabemos como o "if" funciona, vamos utilizá-lo para resolver um desafio. Suponha que cuidamos dos cadastros de novos clientes de uma empresa fictícia e que com a informação da idade se deva classificá-lo em determinada faixa etária: 

- Jovens: indivíduos de até 19 anos; 

- Adultos: indivíduos com idade entre 20 e 59 anos; 

- Idosos: indivíduos com 60 anos ou mais. 

Devemos construir um código que faça essa separação e devolva a faixa etária do novo cliente cadastrado. 

Utilizando o comando "if", podemos verificar em qual faixa etária a idade do cliente está, e verificamos o resultado retornado pelo código. No primeiro exemplo definiremos uma variável “idade” com valor 50. 



<!-- Start of picture text -->
% [39] # Definindo a variavel de idade<br>idade = 50<br>if idade >= 60:<br>print('Cliente na faixa etaria idoso.')<br>elif idade >= 20:<br>print(‘Cliente na faixa etaria adulto.')<br>else:<br>print('Cliente na faixa etaria jovem.')<br>Sy Cliente na faixa etdéria adulto.<br><!-- End of picture text -->

Como 50 anos é menor que 60, mas maior que 20, a condição que é satisfeita é a do “elif” e o comando que se encontra na sua indentação é executado. Uma dúvida que pode surgir é: por que foi usado o “elif” e não o “if” duas vezes? Veremos logo abaixo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

35 



<!-- Start of picture text -->
¥, [45] # Definindo a variadvel de idade<br>idade = 50<br>if idade >= 60:<br>print(‘Cliente nao se enquadra na faixa etdria idoso.')<br>if idade >= 20:<br>print(‘Cliente na faixa etdria adulto.')<br>else:<br>print('Cliente na faixa etaria jovem.')<br>Sy Cliente na faixa etéria adulto.<br><!-- End of picture text -->

Substituindo o “elif” por “if” no segundo comando obtivemos o mesmo resultado, mas uma coisa a se atentar é que um comando “if” sempre é verificado, diferentemente do “elif”! Para isso vamos modificar ligeiramente o código 



<!-- Start of picture text -->
OsY >) # Definindo a variavel de idade<br>idade = 50<br>if idade <= 60:<br>print('Cliente nado se enquadra na faixa etaria idoso.')<br>if idade >= 20:<br>print('Cliente na faixa etdria adulto.')<br>else:<br>print(‘Cliente na faixa etaria jovem.')<br>Sy Cliente nao se enquadra na faixa etéria idoso.<br>Cliente na faixa etaria adulto.<br><!-- End of picture text -->

Podemos perceber que a variável “idade” contém o valor 50 que tanto é menor que 60, como é maior que 20, ou seja, ela satisfaz as duas condições dos “if”, por isso temos dois comandos executados. Se trocarmos o segundo “if” por um “elif” veremos 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

36 



<!-- Start of picture text -->
% [47] # Definindo a variavel de idade<br>idade = 50<br>if idade <= 60:<br>print(‘Cliente nao se enquadra na faixa etdria idoso.')<br>elif idade >= 20:<br>print('Cliente na faixa etdria adulto.')<br>else:<br>print(‘Cliente na faixa etaria jovem.')<br>3y Cliente nao se enquadra na faixa etdéria idoso.<br><!-- End of picture text -->

Que por mais que as duas condições sejam satisfeitas, apenas o “if” é executado. Outro ponto interessante é que essas condições podem se tornar mais complexas com uso de operadores lógicos.  Imagine agora que para ser cadastrado o cliente não deve estar negativado. Vamos desenvolver o código abaixo 



<!-- Start of picture text -->
¥, [52] # Definindo as varidveis idade e negativado<br>idade = 18<br>negativado = False<br>if idade >= 60 and negativado == False:<br>print('Cliente na faixa etdria idoso.')<br>elif idade >= 20 and negativado == False:<br>print('Cliente na faixa etdria adulto.')<br>elif idade < 20 and negativado == False:<br>print('Cliente na faixa etaria jovem.')<br>else:<br>print('Cliente nado satisfaz os critérios de cadastro.')<br>Sy Cliente na faixa etdria jovem.<br><!-- End of picture text -->

Veja que, como estão definidas, as variáveis satisfazem o segundo “elif” e temos o comando executado. Porém, se alterarmos a variável “negativado” para “True” nenhuma das condições é satisfeita e é 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

37 

retornado o comando do “else”. 



<!-- Start of picture text -->
¥, [52] # Definindo as varidveis idade e negativado<br>idade = 18<br>negativado = False<br>if idade >= 60 and negativado == False:<br>print('Cliente na faixa etaria idoso.')<br>elif idade >= 20 and negativado == False:<br>print(‘Cliente na faixa etdria adulto.')<br>elif idade < 2@ and negativado == False:<br>print(‘Cliente na faixa etaria jovem.')<br>else:<br>print('Cliente nao satisfaz os critérios de cadastro.')<br>Sy Cliente na faixa etdria jovem.<br><!-- End of picture text -->

### **Aulas 18 e 19: Estruturas de Repetição em Python: estrutura while** 

Se usarmos o caso de exemplo da aula passada em que uma pessoa deve cadastrar novos clientes, imagine o quão exaustivo seria executar o mesmo código várias vezes! 

Nas linguagens de programação existem estruturas capazes de executar um bloco de código repetidamente mediante determinadas condições. No Python temos as estruturas “for” e “while”. 

Vamos iniciar esse assunto pelo _loop_ “while” e aplicar ao nosso caso. O “while” é uma estrutura utilizada quando deseja-se que determinado bloco de código seja executado **enquanto** uma condição for satisfeita. É escrita conforme o padrão 

Python while condicao: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

38 

# Bloco de código executado 

Vamos para o código usando uma variável que é incrementada a cada _loop_ para entendermos como essa estrutura funciona 



<!-- Start of picture text -->
Y% [55] cliente = 0 # variavel que sera incrementada<br>clientes = [] # lista vazia<br>while len(clientes) < 100:<br>clientes.append(cliente) # adicao do cliente a lista de clientes<br>if len(clientes) > 89: # o comando sé sera mostrado quando tivermos mais de 89 clientes na lista<br>print(f'Ndmero de clientes na lista: {len(clientes)}")<br>cliente += 1 # incremento na variavel<br>Sy Numero de clientes na lista: 90<br>Numero de clientes na lista: 91<br>Nimero de clientes na lista: 92<br>Nimero de clientes na lista: 93<br>Nimero de clientes na lista: 94<br>Nimero de clientes na lista: 95<br>Nimero de clientes na lista: 96<br>Nimero de clientes na lista: 97<br>Nimero de clientes na lista: 98<br>Nimero de clientes na lista: 99<br>Nimero de clientes na lista: 100<br><!-- End of picture text -->

Definimos uma variável “cliente” que será incremental, ou seja, a cada _loop_ o seu valor aumentará, mas também uma variável “clientes” em que serão adicionados os cadastros. Definimos a condição para a nossa estrutura que é a quantidade de elementos na lista, a função “len()” retorna justamente o tamanho de um objeto como listas, dicionários e outros. O cliente é adicionado à lista com o uso da função “append()” e a variável “cliente” é incrementada ao final do loop. O “if” é utilizado a fim de limitar a quantidade de _prints_ retornados, mas é possível observar que o loop é encerrado quando atingimos 100 clientes na lista e a condição é satisfeita. 

Nesse tipo de estrutura é comum utilizarmos alguns auxiliadores, aqui vamos focar no “break”. Esse auxiliador é utilizado quando desejamos encerrar um _loop_ , vamos para o exemplo de seu uso 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

39 



<!-- Start of picture text -->
Y% [58] cliente = @ # variavel que sera incrementada<br>clientes = [] # lista vazia<br>while True:<br>clientes.append(cliente) # adicao do cliente a lista de clientes<br>if len(clientes) > 89: # 0 comando sé sera mostrado quando tivermos mais de 89 clientes na lista<br>print(f*Ndmero de clientes na lista: {len(clientes)}')<br>if len(clientes) == 100:<br>print(‘\n")<br>print('O cédigo se encerral")<br>break<br>cliente += 1 # incremento na variavel<br>Sy Nimero de clientes na lista: 90<br>Ndmero de clientes na lista: 91<br>NGmero de clientes na lista: 92<br>Ndmero de clientes na lista: 93<br>Ndmero de clientes na lista: 94<br>Numero de clientes na lista: 95<br>Ndmero de clientes na lista: 96<br>Ndmero de clientes na lista: 97<br>Ndmero de clientes na lista: 98<br>Ndmero de clientes na lista: 99<br>Ndmero de clientes na lista: 100<br>0 cédigo se encerra!<br><!-- End of picture text -->

Aqui usamos como condição para a estrutura apenas “True”, isso faz com que o loop seja executado indefinidamente, mas não queremos isso! Então, define-se uma condição para que o código seja encerrado quando o tamanho da lista “clientes” for equivalente a 100, com o “break” o bloco de código é encerrado. 

### **Aulas 20 e 21:  Estruturas de Repetição em Python: estrutura for** 

Quando desejamos executar um comando _n_ vezes usamos o "for". O "for" é utilizado quando desejamos executar o mesmo comando n vezes, ou acessar todos os elementos de uma determinada variável do tipo coleção, como listas e dicionários. 

Por exemplo, se desejamos imprimir todos os elementos de uma lista utilizando o comando "for" com o seguinte padrão: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

40 

Python for elemento in lista: print(elemento) 

Se utilizarmos esse padrão para o nosso código, temos: 



<!-- Start of picture text -->
(37] # Amostra de clientes cadastrados na empresa<br>clientes = [<br>{'idcliente': 1, ‘nome’: 'Jodo', 'género': 'H', ‘idade': 20},<br>{‘idcliente': 2, ‘nome’: ‘Maria’, ‘género': 'M', ‘idade': 45},<br>{'idcliente': 3, ‘nome’: ‘Gustavo’, ‘género': 'H', ‘idade': 22},<br>{‘idcliente’: 4, ‘nome’: ‘Gabriel’, ‘género': 'H', ‘idade': 33},<br>{‘idcliente’: 5, ‘nome’: ‘Juliana’, ‘género': 'M', ‘idade': 19},<br>{'idcliente': 6, ‘nome’: ‘Cristina’, ‘género': 'M', ‘idade': 27},<br>{‘idcliente': 7, ‘nome’: ‘Cristiano’, ‘género': 'H', ‘idade': 50},<br>{‘idcliente’: 8, ‘nome’: ‘Ronaldo’, ‘género’: ‘H', ‘idade': 62},<br>{‘idcliente’: 9, ‘nome’: ‘Daiane’, ‘género': ‘M', ‘idade’: 23},<br>{‘idcliente’: 10, ‘nome’: ‘Francisco’, ‘género': ‘H', ‘idade': 25},<br>]<br><!-- End of picture text -->

Ou seja, uma lista de dicionários, sendo que cada dicionário representa os dados de um dos 10 clientes que foram selecionados. O seu chefe deseja que seja calculada a média de idade destes clientes. 

Como já sabemos como percorrer uma lista de elementos, elemento a elemento, como feito abaixo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

41 



<!-- Start of picture text -->
% [38] # Percorrendo os diciondrios da lista<br>for cliente in clientes:<br>print(cliente)<br>Sy {‘idcliente': 1, ‘nome’: "Jodo", ‘género': 'H', ‘idade': 20}<br>{‘idcliente’: 2, ‘nome’: ‘Maria’, ‘género': 'M', ‘idade': 45}<br>{‘idcliente’: 3, ‘nome’: ‘Gustavo’, ‘género': 'H', ‘idade': 22}<br>{‘idcliente’: 4, ‘nome’: ‘Gabriel’, ‘género': 'H', ‘idade': 33}<br>{'idcliente’: 5, ‘nome’: ‘Juliana’, ‘género': 'M', ‘idade': 19}<br>{‘idcliente’: 6, ‘nome’: ‘Cristina’, ‘género': 'M', ‘idade': 27}<br>{‘idcliente’: 7, ‘nome’: ‘Cristiano’, ‘género': 'H', ‘idade': 50}<br>{‘idcliente’: 8, ‘nome’: ‘Ronaldo’, ‘género': 'H', ‘idade': 62}<br>{'idcliente': 9, 'nome': ‘Daiane'’, ‘género': 'M', ‘idade': 23}<br>{'idcliente’: 10, ‘nome’: ‘Francisco’, ‘género': 'H', ‘idade': 25}<br><!-- End of picture text -->

Podemos usar esse tipo de estrutura para realizar algumas operações como, por exemplo, calcular a média de idade da amostra dos clientes 



<!-- Start of picture text -->
% [39] soma = © # variadvel para acumular a idade<br>for cliente in clientes:<br>soma += Cliente['idade'] # acumula as idades a cada loop<br># Calculo da média da idade dos clientes<br>media = soma / len(clientes)<br>print(f'A média de idade dos clientes é: {media} anos’)<br>Sy A média de idade dos clientes é: 32.6 anos<br><!-- End of picture text -->

É possível segmentar o número de clientes por gênero, dessa vez adicionaremos uma estrutura de decisão a fim de fazer a contabilização 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

42 



<!-- Start of picture text -->
[41] homens = @ # varidvel incremental que retornara a quantidade de clientes homens<br>mulheres = @ # varidvel incremental que retornara a quantidade de clientes mulheres<br>for cliente in clientes:<br>if cliente['genero'] == 'M': # verifica o valor para chave género<br>mulheres += 1<br>else:<br>homens += 1<br>print(#'Clientes do género feminino: {mulheres}')<br>print(f*Clientes do género masculino: {homens}")<br>3} Clientes do género feminino: 4<br>Clientes do género masculino: 6<br><!-- End of picture text -->

Uma função bem interessante e útil para ser usada em _loops_ "for" em é a função “enumerate()”. Essa função é utilizada em iteráveis e retorna tanto o índice como o próprio item. 



<!-- Start of picture text -->
x [42] for index, value in enumerate(clientes):<br>print(index, value)<br>Sa @ {‘idcliente': 1, ‘nome’: ‘Jodo’, ‘genero': 'H', ‘idade': 20}<br>1 {‘idcliente’: 2, ‘nome’: ‘Maria’, ‘genero': 'M', ‘idade': 45}<br>2 {‘idcliente’: 3, ‘nome’: ‘Gustavo’, ‘genero': 'H', ‘idade': 22}<br>3 {'idcliente’: 4, ‘nome’: ‘Gabriel’, ‘genero': ‘H', ‘idade’: 33}<br>4 {‘idcliente': 5, ‘nome’: ‘Juliana’, ‘genero': ‘mM’, ‘idade': 19}<br>5 {'idcliente’: 6, ‘nome’: ‘Cristina’, ‘genero': 'M', ‘idade': 27}<br>6 {‘idcliente’: 7, ‘nome’: ‘Cristiano’, ‘genero': ‘H', ‘idade’: 50}<br>7 {‘idcliente’: 8, ‘nome’: ‘Ronaldo’, ‘genero': 'H', ‘idade': 62}<br>8 {'idcliente': 9, ‘nome’: 'Daiane', ‘genero': 'M', ‘idade': 23}<br>9 {‘idcliente’: 10, ‘nome’: ‘Francisco’, ‘genero': ‘H', ‘idade': 25}<br><!-- End of picture text -->

### **Aula 22: Estrutura de uma função em Python** 

Uma das técnicas mais importantes da linguagem de programação Python é a possibilidade da criação e uso de funções. O Python por si só já possui um conjunto muito bom de <u>funções built-in, que são funções</u> próprias do Python. 

Mas e se desejarmos criar as nossas próprias funções? É sobre isso que será esta aula. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

43 

Funções nada mais são que blocos de código que possuem um propósito específico. Esse propósito pode ser o cálculo de um valor, o processamento de dados, como endereços e documentos de clientes, pode ser o desenho de um gráfico e etc. A criação de funções também é bastante recomendada quando sabemos que executaremos uma ação repetidas vezes. A funcionalidade de uma função está limitada apenas ao poder criativo da pessoa que a cria! 

Porém, antes de iniciarmos a criação das nossas próprias funções, vamos entender melhor a sua estrutura. Toda função deve possuir um  nome. Além disso, ela pode ou não possuir o que chamamos de parâmetros. Podemos utilizar o seguinte padrão para a criação de uma função: 

Python 

def nome_funcao(parametros): # comandos 

return retorno 

Ou seja, o "nome_funcao" é o que define o nome da função. E é através desse nome que utilizamos as funções. O "parametros" é onde definimos os parâmetros que iremos receber para utilizar na função, ou seja, são os valores que iremos utilizar dentro da função. Por fim, o "retorno" é o valor que iremos retornar como resultado. Caso a nossa função não precise retornar nenhum tipo de parâmetro, basta colocar a palavra reservada "None" para indicar ao Python que não há retorno algum. 

#### Python 

# Exemplo de função com retorno def func_com_retorno(): 

# comandos 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

44 

return retorno # Exemplo de função sem retorno def func_sem_retorno(): print("Texto representativo") 

### **Aula 23: Construindo e utilizando funções em Python** 

Agora que entendemos o que são funções e como é a sua estrutura, vamos criar botar a mão na massa e criar e usar algumas funções. 

Vamos primeiro criar uma função que faz o cálculo do da média das idades dos clientes. Ou seja, vamos transformar o nosso código anterior em função. 

Vamos reutilizar a mesma estrutura de clientes de antes: 



<!-- Start of picture text -->
(37] # Amostra de clientes cadastrados na empresa<br>clientes = [<br>{'idcliente': 1, ‘nome’: 'Jodo', 'género': 'H', ‘idade': 20},<br>{‘idcliente': 2, ‘nome’: ‘Maria’, ‘género': 'M', ‘idade': 45},<br>{'idcliente': 3, ‘nome’: ‘Gustavo’, ‘género': 'H', ‘idade': 22},<br>{‘idcliente’: 4, ‘nome’: ‘Gabriel’, ‘género': 'H', ‘idade': 33},<br>{‘idcliente’: 5, ‘nome’: ‘Juliana’, ‘género': 'M', ‘idade': 19},<br>{'idcliente': 6, ‘nome’: ‘Cristina’, ‘género': 'M', ‘idade': 27},<br>{‘idcliente': 7, ‘nome’: ‘Cristiano’, ‘género': 'H', ‘idade': 50},<br>{‘idcliente’: 8, ‘nome’: ‘Ronaldo’, ‘género’: ‘H', ‘idade': 62},<br>{‘idcliente’: 9, ‘nome’: ‘Daiane’, ‘género': ‘M', ‘idade’: 23},<br>{‘idcliente’: 10, ‘nome’: ‘Francisco’, ‘género': ‘H', ‘idade': 25},<br>]<br><!-- End of picture text -->

Nós vamos também utilizar os códigos que construímos para calcular a média das idades dos clientes e adaptar ao bloco de função. 

Com isso em mãos, vamos definir a nossa primeira função. O nome da 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

45 

nossa função será "calculo_media_idades". Ela deverá receber a lista de clientes como parâmetro e o seu retorno será a média das idades. Dessa forma, temos o seguinte resultado: 



<!-- Start of picture text -->
aa [42] # Definicao da funcao de cdlculo das médias<br>def calculo_media_idades(lista_clientes):<br>soma = @ # varidvel que acumulara as idades a cada loop<br># Percorre-se os elementos da lista<br>for cliente in lista_clientes:<br>soma += Cliente[‘idade’]<br>media = soma / len(lista_clientes) # cdlculo da média das idades<br># Retorna a média calculada<br>return media<br><!-- End of picture text -->

Observe que  agora, todos os códigos que utilizamos anteriormente estão "dentro" da função. Ou seja, todos eles estão com indentação, informando ao Python que eles pertencem à função "calculo_media_idades". 

Além disso, podemos ver que percorremos a lista de clientes - "lista_clientes" - com o comando "for" dentro da função. Por fim, após o cálculo da média, retornamos o resultado com o comando "return". 

Com a função criada e definida, para utilizarmos basta chamar o nome da função e passar a lista de cliente como argumento. Além disso, temos que receber o retorno da função em uma variável: 



<!-- Start of picture text -->
x [43] # Uso da funcdo na criac&o da varidvel de média de idades<br>media_idades = calculo_media_idades(clientes) # parametro -> clientes<br># Exibindo o valor calculado<br>print(f'A média de idade dos clientes é: {media_idades} anos’)<br>Sy A média de idade dos clientes é: 32.6 anos<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

46 

Observe que "chamamos" a função utilizando o seu nome e passamos como argumento (dentro dos parênteses) a lista de clientes, e salvamos o resultado da função na variável "media_idades". 

Caso desejássemos que a função exibisse o resultado ao invés de devolvê-lo, basta ajustarmos a função e adicionar um comando "print()" dentro dela. Vamos criar uma nova função para fazer essas modificações: 



<!-- Start of picture text -->
%, [44] def exibe_media_idades(lista_clientes):<br>soma = @ # varidvel que acumulara as idades a cada loop<br># Percorre-se os elementos da lista<br>for cliente in lista_clientes:<br>soma += cliente[‘idade']<br>media = soma / len(lista_clientes) # c4lculo da média das idades<br># Exibe a média das idades<br>print(f'A média de idade dos clientes é: {media} anos’)<br>return None # essa linha é opcional<br><!-- End of picture text -->

Observe que agora, além do nome ser diferente, "exibe_media_idade", exibimos diretamente o resultado da média com o comando "print()", e o retorno da função é "None", uma vez que já exibimos a média das idades. 

O uso da função também será diferente. Agora, basta "chamá-la" e passar a lista de clientes como argumento. 



<!-- Start of picture text -->
x [45] # Executando a func4o para exibicdo das médias<br>exibe_media_idades(clientes)<br>Sy A média de idade dos clientes é: 32.6 anos<br><!-- End of picture text -->

Como o retorno é "None", não precisamos mais salvar ele em uma variável como fizemos anteriormente. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

47 

### **Aula 24: Módulos vs Pacotes vs Bibliotecas** 

Antes de iniciarmos um novo ciclo nesta etapa, vamos entender melhor a diferença entre módulos, pacotes e bibliotecas. 

Módulos nada mais são que arquivos Python executáveis. Geralmente são compostos de um único arquivo com funções dentro dele. Geralmente estão incorporados junto do Python, não sendo necessário a sua instalação. Por exemplo: Podemos utilizar o módulo "sqlite3", que é um módulo built-in do Python para nos conectarmos com banco de dados. 

Pacotes são um conjunto de módulos, geralmente organizados dentro de um diretório (pasta). Possui bem mais funcionalidades se comparado aos módulos do Python. Geralmente precisam ser instalados utilizando um gerenciador de pacotes. Geralmente possuem um conjunto de funcionalidades bem específico Exemplo: Iremos utilizar o pacote pandas para realizar a leitura dos dados e para manipular os dados. 

Bibliotecas são conjuntos de pacotes, de forma que uma biblioteca é uma ferramenta muito mais robusta e com muito mais funcionalidades do que um pacote. Assim como os pacotes, as bibliotecas precisam ser instaladas utilizando um gerenciador de pacotes. A biblioteca de visualização de dados que iremos utilizar no módulo, a seaborn. 

### **Aula 25: Ciclo 2 - O problema de negócio** 

Agora que finalizamos o nosso ciclo de fundamentos do Python, iremos iniciar um novo ciclo. Neste novo ciclo, iremos receber um problema de negócio para nos nortear, e a cada pergunta respondida, iremos aprender técnicas novas, utilizando o pacote Pandas e a biblioteca Seaborn. 

O novo problema de negócio é: Fomos transferidos para um novo time dentro do BanVic, e nosso novo time utiliza majoritariamente o Python para realizar análises e responder perguntas de negócios feitas pelos gerentes do banco. O gerente do time nos entregou uma base de dados 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

48 

que contém um sample das transações efetuadas nas agências pertencentes ao banco. 

Com esses dados em mãos, o gerente do time fez as seguintes perguntas: 

1. Existem quantas transações dentro da base de dados? 

2. Quantos tipos de transação existem dentro da base de dados e quais são suas proporções? 

3. Qual a conta com maior valor médio de transação? 

4. Qual o tipo de transação teve maior montante transacionado? 

5. Há correlação entre o valor do financiamento e o valor de entrada? Se sim, de qual tipo? 

Utilizando os conhecimentos já adquiridos no ciclo anterior, iremos aprender novas técnicas e responder estas perguntas! 

### **Aula 26: Pandas** 

O <u>Pandas é uma biblioteca open-source que é muito utilizada dentro do</u> mercado de trabalho para manipulação de dados. Um dos principais motivos se deve ao fato do Pandas ser utilizado para manipulação de dados muito utilizado, é a sua facilidade em trabalharmos com dados nulos, possuir funções de leitura para múltiplas fontes, desde arquivos _.csv_ a bancos de dados, e sua baixa curva de aprendizado. 

Quando importamos dados de uma fonte de dados utilizando o Pandas, ele cria uma estrutura de dados chamada de _Dataframe_ , que organiza os dados em linhas e colunas, da mesma forma que o MS Excel faz. Isso facilita a manipulação dos dados, tornando o trabalho mais ágil. 

O _Dataframe_ é uma das principais estruturas de dados do Pandas. Cada linhas e cada coluna são organizadas por índices, e é através destes índices que manipulamos as informações que estão contidas dentro das linhas, colunas e/ou células. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

49 



<!-- Start of picture text -->
DataFrame<br>mz<br>a<br>a<br>row<br>i<br>a<br>column<br><!-- End of picture text -->

Fonte: <u>What kind of data does pandas handle?</u> 

Na imagem acima, podemos observar que há uma linha e uma coluna mais escura que as outras. Essa camada mais escura são os índices do _Dataframe_ . Ao longo deste ciclo, iremos trabalhar cada vez mais com essas informações e esse conceito ficará cada vez mais claro, à medida que formos respondendo às nossas perguntas de negócio. 

Antes de iniciarmos a leitura dos dados e a responder às perguntas de negócio, vamos entender primeiro como o Pandas organiza os seus tipos de dados. 

Como já sabemos, o Pandas organiza os seus dados em linhas e colunas. As colunas representam as características de um dado, enquanto a linha representa a combinação destas características, da mesma forma que vimos na etapa de SQL. 

Dessa forma, o Pandas atribui um dos seus tipos de dados para cada uma das colunas. Ou seja, se temos uma coluna que contém texto, como um endereço, o Pandas irá atribuir um tipo de dado para essa coluna. Se temos uma coluna que contém números inteiros, como códigos identificadores (ID), o Pandas irá atribuir um tipo de dados para essa coluna, e assim por diante, atribuindo um tipo de dado para cada uma das colunas. 

Basicamente, temos 4 tipos de dados principais: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

50 

- Valores numéricos inteiros - tipo "int64": Esse tipo de dado é atribuído para colunas que possuam dados numéricos inteiros. Caso uma das linhas desta coluna contenha dados faltantes, ela será lida como "float64" 

- Valores numéricos decimais - tipo "float64": Esse tipo de dado é atribuído para colunas que possuam dados numéricos decimais. 

- Valores textuais - tipo "object": Esse tipo de dados é atribuído para colunas que possuam dados textuais, como endereços ou nomes. 

- Data - tipo "datetime[ns]": Esse tipo de dado é atribuído quando colunas que contenham datas. Porém, nem sempre o Pandas consegue entender o padrão das datas na leitura dos dados, o que faz com que tenhamos que converter estas colunas manualmente. 

É importante que entendamos esse conceito pois, caso o Pandas leia os dados e não atribua corretamente os tipos de dados para as colunas, teremos que fazer esses ajustes manualmente, uma vez que se as colunas não estiverem com os seus tipos de dados corretos, a manipulação dos dados será algo complicado de ser feito. 

### **Aulas 26, 27 e 28: Principais funções e atributos do Pandas** 

Agora que temos uma base sobre o pacote Pandas, podemos começar a responder as perguntas de negócio feitas pelo nosso gerente. 

A primeira pergunta é: 

"Existem quantas transações dentro da base de dados?" 

Para responder esta e as outras perguntas, vamos criar um novo _notebook_ no Google Colab. Podemos organizar como feito abaixo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

51 



<!-- Start of picture text -->
¥ 1. Problema de negocio<br>Fomos transferidos para um novo time dentro do BanVic, e nosso novo time utiliza majoritariamente o Python para realizar andlises e<br>responder perguntas de negocios feitas pelos gerentes do banco. O gerente do time nos entregou uma base de dados que contém um sample<br>das transacées efetuadas nas agéncias pertencentes ao banco.<br>Com esses dados em mos, o gerente do time fez as seguintes perguntas:<br>1. Existem quantas transagdes dentro da base de dados?<br>2. Quantos tipos de transagao existem dentro da base de dados e quais sao suas proporcdes?<br>3. Quantas agéncias existem dentro de cada estado?<br>4. Qual a agéncia teve a maior quantidade de transacées do tipo Compra Crédito?<br>5. Qual a varia¢ao do volume monetario de saida e entrada no ano de 2022?<br>v 2. Imports<br>y 2.1. Leitura de dados<br>v 3. Fungées auxiliares<br><!-- End of picture text -->

A primeira coisa que temos que fazer, antes de pensarmos em como responder a nossa pergunta é fazer a importação do pacote Pandas e carregar os dados. 

Para isso, vamos na seção "2. Imports" e vamos realizar o importação do pandas. Para isso, vamos digitar o comando: 

Python import pandas as pd 

Com esse comando, estamos importando o pacote pandas para o nosso arquivo _notebook_ , e dando um nome de "pd" para ele. Ou seja, a partir de agora, para acessar as funcionalidades do Pandas, vamos utilizar o padrão "pd.funcionalidade". 

Execute a célula, para que o Python faça a importação do pacote. Na 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

52 

seção "2.1. Leitura dos Dados", iremos realizar a leitura dos dados transacionais. Se você ainda não baixou este arquivo da plataforma, baixe-o agora e coloque-o dentro da pasta do módulo, junto dos arquivos notebook. É o arquivo com o nome "transacoes.csv". E para usar o arquivo no Google Colab basta seguir os passos abaixo 

1. Clicar no ícone de pasta denominado “Ficheiros” 

2. Clicar na opção de carregar para o armazenamento da sessão 



<!-- Start of picture text -->
© —_ Fomos transferidos para um novo time dentro do BanVic, e nosso novo time utiliza majoritariamente o Python para realizar andlises e<br>responder perguntas de negocios feitas pelos gerentes do banco. 0 gerente do time nos entregou uma base de dados que contém um sample<br>das transagées efetuadas nas agéncias pertencentes ao banco.<br>Com esses dados em maos, o gerente do time fez as sequintes perguntas:<br>1. Existem quantas transagées dentro da base de dados?<br>2. Quantos tipos de transacao existem dentro da base de dados e quais sao suas proporgdes?<br>3. Quantas agéncias existem dentro de cada estado?<br>4. Qual a agéncia teve a maior quantidade de transagées do tipo Compra Crédito?<br>5. Qual a variagao do volume monetario de saida e entrada no ano de 2022?<br><!-- End of picture text -->

Ao realizar o passo anterior uma janela será aberta para selecionar um arquivo do seu computador. Após a seleção do arquivo “transacoes.csv” veremos o arquivo agora carregado na aba. 



<!-- Start of picture text -->
© Problema de negécioipynb<br>= vinous Cy x) +060. + Tero<br>abecner Fomostransferdosresponder  para um novo tine dentro do BanVic,e nosso novo time liza majrtariamenteo Python paa realizar andlises ©<br>ow perguntas de negécios felts pelos gerentes do banco. 0 gerente do time nos enegou uma base de dados que contém um sample<br>oe das transagées efetuadas.  nas agéncis pertencentes a0 banco<br>> In sample cata ‘Com esses dados em més, o gerente do time fer as seguintes pergutas:<br>2B5 _—transacoes csv 2.1. QuantostposExistem quantastransagGes de transagdo existe dentro da base de dados?dentro da base de dados<br>2. Quantas agéncia exstem dentro de cada estado? e quale so suas proporgSes?<br>4.5. QualQual aagénciatevevariagdo do volumea maior monetrio quantidade de de sala transag6ese entradado no tipo anode Compra 2022? Crésto?<br><!-- End of picture text -->

Com o arquivo no local correto, vamos realizar a leitura dele. O Pandas possui várias funções de leitura prontas. Como desejamos ler um arquivo _.csv_ , iremos utilizar a função "read_csv()". 

Para que o Pandas leia corretamente o arquivo devemos passar como 

_____________________________________________________________________________________________________________________________________ Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

53 

parâmetro o caminho do arquivo. Esse pode ser obtido clicando no botão com três pontos ao lado do arquivo como mostrado abaixo 



<!-- Start of picture text -->
co & Problema de negocio.ipynb **<br>Ficheiro Editar Ver Inserir Tempodee:<br>i= Ficheiros Gx<br>qa A CBR<br>{x} =.<br>> [BB sample_data<br>Ce BB transacoes.csv ®<br>=)<br><!-- End of picture text -->

Selecionando a opção “Copiar caminho” já obtemos a informação necessária para que o Pandas leia o arquivo. 



<!-- Start of picture text -->
co & Problema de negocio.ipynb  ¥*r<br>Ficheiro Editar Ver Inserir Tempode exec<br>—t= Ficheirospy, Gx 4<br>qa AC BR<br>{x} =.<br>> [BB sample_data<br>oe Transferir<br>| a) Mudar o nome do ficheiro<br>Eliminar ficheiro<br>Copiar caminho<br>Atualizar<br><!-- End of picture text -->

Desta forma, nosso arquivo _notebook_ deverá ficar da seguinte forma: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

54 



<!-- Start of picture text -->
v 2. Imports<br>[1] # Import do pacote Pandas<br>import pandas as pd<br>v 2.1. Leitura de dados<br>y, [2] # Leitura dos dados e definicdo de uma varidvel com o dataframe<br>df = pd.read_csv('/content/transacoes.csv')<br>df.head() # A func&o head() mostra as primeiras linhas do dataframe<br>a COD_TRANSACAO NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO =<br>o 1 1 2016-03-15 18:09:56.704 Z Depédsito em espécie 130.1 oO<br>1 2 2 2021-02-03 02:56:28.418 Z_Depdsito em espécie 270.1<br>2 3 3 2017-01-18 22:55:42.504 Z TED - Recebido 1205.0<br>3 4 4 2019-06-26 21:38:39.164 Z Depdsito em espécie 166.5<br>4 5 5 2015-09-28 05:58:31.182 Z Depdsito em espécie 491.5<br><!-- End of picture text -->

Com o arquivo de dados lido, vamos usar algumas das principais funções do Pandas e aproveitar para já responder algumas perguntas de negócio. Vamos dividir as funções em categorias 

- Resumo dos dados 

1. .head(): Como vimos anteriormente, retorna as primeiras linhas do _Dataframe_ , caso nenhum parâmetro seja passado retorna as 5 primeiras linhas, porém há a possibilidade de definir um valor personalizado. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

55 



<!-- Start of picture text -->
v 3.1. Resumo<br>aa [3] # Mostrar as 10 primeiras linhas do dataframe<br>df .head(10)<br>oe COD_TRANSACAO NUM_CONTA DATA_TRANSACAO ——-NOME_TRANSACAO VALOR_TRANSACAO — f]<br>C) 1 1 2016-03-15 18:09:56.704 Z Depésito em espécie 1301<br>1 2 2 2021-02-03 02:56:28.418 Z_Depésito em espécie 270.1<br>2 3 3 2017-01-18 22:55:42.504 Z TED - Recebido 1205.0<br>3 4 4 2019-06-26 21:38:39.164 Z Depésito em espécie 166.5<br>4 5 5 2015-09-28 05:58:31.182 Z_Depésito em espécie 491.5<br>5 6 6 2017-11-21 03:38:45.347 Z_Depésito em espécie 398.0<br>6 7 7 2022-04-08 06:18:27.941 Z Depésito em espécie 25.2<br>7 8 8 2017-10-21 00:38:39.755 Z TED - Recebido 1883.0<br>8 9 9 2021-01-14 18:55:55.062 Z Depdsito em espécie 64.1<br>9 10 10 2015-07-24 13:49:52.225 Z TED - Recebido 9648.0<br><!-- End of picture text -->

2. .tail(): Retorna as últimas linhas do Dataframe. De forma similar à função .head(), caso nenhum valor seja passado teremos as 5 últimas linhas, mas também pode mostrar um número personalizado de linhas. 



<!-- Start of picture text -->
Y% [4] # Mostrar as 8 Gltimas linhas do dataframe<br>df.tail(s)<br>a COD_TRANSACAO NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO fF]<br>10991 10992 922 2018-04-27 19:42:58.534Z — Compra Crédito 616<br>10992 10993 26 2021-10-22 06:51:01.985Z — Pix- Recebido 368.80<br>10993 10994 481 2022-09-25 04:04:08.278Z Pix - Realizado -99.90<br>10994 10995 5 2015-10-07 12:03:06.543Z — Compra Crédito -22.03<br>10995 10996 643 2020-04-05 10:05:02.717Z Compra Débito ~18.95<br>10996 10997 545 2020-04-13 09:40:10.888 Z Compra Débito -8.58<br>10997 10998 517 2022-07-14 04:28:18.245Z — Compra Débito -93.88<br>10998 10999 885 2019-12-16 02:25:51.858 Z Compra Crédito -450.40<br><!-- End of picture text -->

3. .dtypes: Retorna o tipo de dados das colunas do _Dataframe_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

56 



<!-- Start of picture text -->
x [5] # Retorna os tipos dos dados<br>df.dtypes<br>= 3<br>COD_TRANSACAO int64<br>NUM_CONTA int64<br>DATA_TRANSACAO object<br>NOME_TRANSACAO object<br>VALOR_TRANSACAO float64<br>dtype: object<br><!-- End of picture text -->

4. .info(): Retorna algumas informações como o número de linhas, o nome das colunas, a quantidade de valores não nulos das colunas e os respectivos tipos de dados. 



<!-- Start of picture text -->
~ [6] # Uso da funcdo info()<br>df.info()<br>Sy<br><classRangeIndex:‘pandas.core.frame.DataFrame'16999 entries, ® to 10998><br>Data columns (total 5 columns):<br># = Column Non-Null Count Dtype<br>e COD_TRANSACAO 10999 non-null inté64<br>1 = NUM_CONTA 10999 non-null int64<br>2  DATA_TRANSACAO 10999 non-null object<br>3. NOME_TRANSACAO 18999 non-null object<br>4 VALOR_TRANSACAO 10999 non-null float64<br>dtypes: float64(1), int64(2), object(2)<br>memory usage: 429.8+ KB<br><!-- End of picture text -->

Com essa função **respondemos a 1ª pergunta de negócios** “Existem 

quantas transações dentro da base de dados?”. Como cada registro corresponde a uma transação, se temos 10999 linhas, temos 10999 transações. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

57 

Um forma ainda mais simples seria usando 

5. .shape: Retorna uma tupla com o número de linhas e colunas do _Dataframe_ . 



<!-- Start of picture text -->
vy 4.1. Existem quantas transacées dentro da base de dados?<br>¥~ [7] # Retorna uma tupla com a quantidade de linhas e colunas do dataframe<br>d¥.shape<br>Sy (1e999, 5)<br>Y [8] print(#'Temos {df.shape[@]} transacdes no banco de dados.")<br>Sy} Temos 10999 transacdes no banco de dados.<br><!-- End of picture text -->

Perceba que no “print()” selecionamos apenas o elemento que ocupa o 1º índice para retornar apenas o número de linhas. 

- Seleção/filtragem de dados 

1. .iloc: Seleção de linhas a partir de índices. Pode ser usada a fim de selecionar apenas um índice, mas também podem ser selecionados mais de uma linha definindo um intervalo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

58 



<!-- Start of picture text -->
v 3.1. Selegao/filtragem de dados<br>[8] # Selecdo de linhas por indice<br>df.iloc[1@:20] # Intervalo da linha com indice 10 até o indice 19<br>= COD_TRANSACAO =NUM_CONTA DATA_TRANSACAO: NOME_TRANSACAO VALOR_TRANSACAO fa<br>10 ai 11 2021-10-04 23:30:41.005 Z Depdsito em espécie 104.2 B<br>" 12 12 2013-03-29 19:10:36.160 Z TED - Recebido 858.0<br>12 13 13 2020-01-12 06:10:48.684 Z Depdsito em espécie 32.0<br>13 14 14 2021-12-04 10:42:34.663 Z Depdsito em espécie 301.4<br>14 15 15 2019-02-13 13:11:40.865 Z Depdsito em espécie 296.3<br>15 16 16 2021-04-23 00:51:30.839 Z TED - Recebido 7131.0<br>16 7 17 2020-08-17 19:45:02.974 Z Depdsito em espécie 718.5,<br>17 18 18 2011-06-24 14:21:00.175 Z TED - Recebido 262.0<br>18 19 19 2016-09-06 09:08:49.525 Z Depdsito em espécie 1063.7<br>19 20 20 2019-05-26 23:19:52.375Z Depdsito em espécie 301.8<br><!-- End of picture text -->

2. .loc: Seleciona linhas e colunas de um _DataFrame_ com base em rótulos, mas também pode ser feita a seleção com base em uma condição como vemos adiante 



<!-- Start of picture text -->
x [10] # Vamos selecionar transacdes com valor maior que R$ 100 mil<br>d¥.loc[df[‘VALOR_TRANSACAO’] > 100000]<br>wa COD_TRANSACAO NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO fF<br>1111 1112 275 2015-03-07 03:34:15.723Z TED -Recebido 138445.0 oO<br>1609 1610 502 2012-05-12 22:10:29.910Z DOC - Recebido 166090.0<br>2238 2239 219 2019-12-21 15:38:29.381Z TED -Recebido 221390.0<br>4158 4159 110 2013-10-19 22:44:08.942Z TED - Recebido 101815.0<br>6119 6120 372 2019-10-30 18:13:14.328Z DOC - Recebido 106155.0<br>8837 8838 660 2015-01-14 06:08:19.952 Z TED - Recebido 127945.0<br>9395 9396 91 2020-02-01 12:16:30.840Z DOC - Recebido 160560.0<br><!-- End of picture text -->

Perceba que entre os colchetes foi passada uma expressão _booleana._ Veja que nessa expressão selecionamos especificamente a coluna “VALOR_TRANSACAO”, sempre que desejarmos fazer isso deveremos usar o seguinte formato 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

59 

#### Python 

dataframe['coluna'] 

3. .query(): Seleciona os dados conforme o que for passado como argumento para função. Vamos realizar o mesmo filtro usado no exemplo da função anterior, dessa vez com a função .query(). 



<!-- Start of picture text -->
¥, [11] # Selecdo dos valores com a funcdo query<br>d¥.query('VALOR_TRANSACAO > 160@0@" )<br>ra COD_TRANSACAO =NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO fa<br>1111 1112 275 2015-03-07 03:34:15.723Z TED - Recebido 138445.0 oO<br>1609 1610 502 2012-05-12 22:10:29.910Z DOC - Recebido 166090.0<br>2238 2239 219 2019-12-21 15:38:29.381Z TED -Recebido 221390.0<br>4158 4159 110 2013-10-19 22:44:08.942Z TED - Recebido 101815.0<br>6119 6120 372 2019-10-30 18:13:14.328 Z DOC - Recebido 106155.0<br>8837 8838 660 2015-01-14 06:08:19.952Z TED -Recebido 127945.0<br>9395 9396 91 2020-02-01 12:16:30.840Z DOC - Recebido 160560.0<br><!-- End of picture text -->

- Operações e agregação 

1. .sum(): Retorna a soma dos valores numéricos do campo especificado. 



<!-- Start of picture text -->
v 3.3. Operagdes e agregacao<br>x [13] # Soma dos valores de transacao de todo dataframe<br>df["VALOR_TRANSACAO" ]. sum()<br>Sy 8785102.93865779<br><!-- End of picture text -->

2. .mean(): Retorna a média dos valores numéricos do campo 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

60 

especificado. 



<!-- Start of picture text -->
aa [14] # Média dos valores de transacao<br>df["VALOR_TRANSACAO" ].mean()<br>Sy 798.7183324536586<br><!-- End of picture text -->

3. .median(): Retorna a mediana dos valores numéricos do campo especificado. 



<!-- Start of picture text -->
x oO # Mediana dos valores de transacéo<br>d¥[‘VALOR_TRANSACAO* ] .median()<br>By -23.19<br><!-- End of picture text -->

4. .var(): Retorna a variância dos valores numéricos do campo especificado. 



<!-- Start of picture text -->
x [15] # Variancia dos valores de transacao<br>df["VALOR_TRANSACAO" ].var()<br>Sy 46181441.922160044<br><!-- End of picture text -->

5. .std(): Retorna o desvio padrão dos valores numéricos do campo especificado. 



<!-- Start of picture text -->
x [16] # Desvio padrao dos valores de transacao<br>d¥[‘VALOR_TRANSACAO" }.std()<br>S¥ 6795.692894926907<br><!-- End of picture text -->

6. .value_counts(): Retorna a contagem de valores, tanto de valores numéricos como categóricos. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

61 

Com essa função somos capazes de **responder a 2ª pergunta!** Ao utilizar a coluna “NOME_TRANSACAO” a função retornará a contagem de valores para cada tipo de transação como vemos abaixo 



<!-- Start of picture text -->
x [17] # Contagem de categorias<br>df["NOME_TRANSACAO' ].value_counts()<br>rg count<br>NOME_TRANSACAO<br>Compra Crédito 4072<br>Compra Débito 2770<br>Depésito em espécie 1770<br>Pix - Realizado 733<br>Pix - Recebido 527<br>TED - Recebido 384<br>Saque 366<br>DOC - Recebido 95<br><!-- End of picture text -->

E se quisermos analisar o valor relativo para cada tipo de transação basta utilizar o parâmetro _normalize_ como “True”. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

62 



<!-- Start of picture text -->
x [18] # Frequéncia relativa com o uso do parametro normalize<br>d#["NOME_TRANSACAO' ].value_counts(normalize=True)<br>32> proportion<br>NOME_TRANSACAO<br>Compra Crédito 0.370215<br>Compra Débito 0.251841<br>Depésito em espécie 0.160924<br>Pix - Realizado 0.066642<br>Pix - Recebido 0.047913<br>TED - Recebido 0.034912<br>Saque 0.033276<br>DOC - Recebido 0.008637<br>Transferéncia entre CC - Crédito 0.008546<br><!-- End of picture text -->

7. .groupby(): Agrupa dados por valores e permite realizar operações como as vistas anteriormente. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

63 



<!-- Start of picture text -->
hd oO # 0 valor médio das transacoes por tipo<br>df .groupby( ‘NOME_TRANSACAO" )[ ‘VALOR_TRANSACAO" ] .mean()<br>2 VALOR_TRANSACAO<br>NOME_TRANSACAO<br>Compra Crédito -45.734000<br>Compra Débito -49.085487<br>DOC - Realizado -17651.666667<br>DOC - Recebido 33479.263158<br>Depdsito em espécie 140.165288<br>Estorno de Debito 57.740741<br>Pagamento de boleto -937.722449<br>Pix - Realizado -401.547749<br>Pix - Recebido 673.747249<br>Pix Saque -220.346461<br><!-- End of picture text -->

- Manipulação de dados 

1. .drop(): Remove colunas ou linhas. 

Normalmente removemos colunas do _DataFrame_ , e para isso devemos passar para função o parâmetro _axis_ com valor 1. Caso deseje-se manter a remoção da coluna, a variável do _DataFrame_ pode ser sobrescrita ou com o uso do parâmetro _inplace_ com valor “True”. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

64 



<!-- Start of picture text -->
v 3.4. Manipulagdo de dados<br>X% © # Se desejarmos eliminar a coluna do cédigo da transacdo<br>df .drop('COD_TRANSACAO', axis=1)<br>s¢ NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO fF]<br>o 1 2016-03-15 18:09:56.704 Z Depdsito em espécie 130.10 Oo<br>1 2 2021-02-03 02:56:28.418 Z Depdsito em espécie 270.10<br>2 3 2017-01-18 22:55:42.504Z TED - Recebido 1205.00<br>3 4 2019-06-26 21:38:39.164Z Depdsito em espécie 166.50<br>4 5 2015-09-28 05:58:31.182 Z Depdsito em espécie 491.50<br>10994 5 2015-10-07 12:03:06.543 Z Compra Crédito -22.03<br>10995 643 2020-04-05 10:05:02.717 Z Compra Débito -18.95<br>10996 545 2020-04-13 09:40:10.888 Z Compra Débito 8.58<br>10997 517 2022-07-14 04:28:18.245Z Compra Débito -93.88<br>10998 885 2019-12-16 02:25:51.858 Z ‘Compra Crédito -450.40<br>10999 rows x 4 columns<br>[ ] # Caso seja necessério que o drop seja definitivo, temos as opcées<br># df = df.drop(‘COD_TRANSACAO", axis=1)<br># df.drop("COD_TRANSACAO’, inplace=True)<br><!-- End of picture text -->

### 2. .rename(): Renomeia colunas. 

Caso seja necessário renomear definitivamente a coluna, assim como para a função _.drop()_ , podemos sobrescrever a variável ou utilizar o parâmetro _inplace_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

65 



<!-- Start of picture text -->
Y% [28] # Vamos renomear a coluna NUM_CONTA para COD_CONTA<br>df.rename({‘NUM_CONTA’: ‘COD_CONTA'}, axis=1)<br>= COD_TRANSACAO COD_CONTA DATA_TRANSACAO —-NOME_TRANSACAO VALOR_TRANSACAO — []<br>C) 1 1 2016-03-15 18:09:56.704 Z Depésito em espécie 130.10 Ay<br>1 2 2 2021-02-03 02:56:28.418 Z _Depésito em espécie 270.10<br>2 3 3 2017-01-18 22:55:42.504Z TED - Recebido 1205.00<br>3 4 4 2019-06-26 21:38:39.164 Z Depdsito em espécie 166.50<br>4 5 5 2015-09-28 05:58:31.182 Z_ Depésito em espécie 491.50<br>10994 10995 5 2015-10-07 12:03:06.543Z Compra Crédito -22.03<br>10995 10996 643 2020-04-05 10:05:02.717 Z Compra Débito 18.95<br>10996 10997 545 2020-04-13 09:40:10.888 Z Compra Débito 8.58<br>10997 10998 517 2022-07-14 04:28:18.245 Z Compra Débito -93.88<br>10998 10999 885 2019-12-16 02:25:51.858 Z Compra Crédito -450.40<br>10999 rows x 5 columns<br><!-- End of picture text -->

3. .sort_values(): Ordena o _DataFrame_ com base em valores de uma ou mais colunas. 

Para uma ordenação em ordem decrescente, deve-se utilizar o parâmetro _ascending_ como “False”. 

**A 3ª pergunta pode ser respondida com essa função** , basta agruparmos pelo campo de conta e calcular a média e usar a função _sort_values_ para vermos na ordem desejada. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

66 



<!-- Start of picture text -->
x [31] # Resposta da 32 pergunta<br>df. groupby(‘NUM_CONTA")[ ‘VALOR_TRANSACAO' ].mean().sort_values(ascending=False)<br>roe VALOR_TRANSACAO<br>NUM_CONTA<br>219 15778.211754<br>502 15136.357273<br>275 13787.365328<br>91 12350.819231<br>660 11618.981515<br>781 0.131111<br>507 0.080000<br>197 0.078615<br>975 0.065909<br>580 0.010769<br>999 rows x 1 columns<br>dtype: floaté4<br><!-- End of picture text -->

A tabela é truncada visto que temos uma quantidade considerável de valores, no entanto, vemos que a conta **219** é aquela com maior valor médio das transações. 

4. .reset_index(): Redefine o índice do _DataFrame_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

67 



<!-- Start of picture text -->
xy [32] # Redefinindo o index do dataframe<br>df.reset_index()<br>oe index COD_TRANSACAO NUM_CONTA DATA_TRANSACAO —-NOME_TRANSACAO VALOR_TRANSACAO fF]<br>° C) 1 1 2016-03-15 18:09:56.704Z Depésitoem espécie 130.10 Ay<br>1 1 2 2 2021-02-03 02:56:28.418 Z Depésito em espécie 270.10<br>2 2 3 3 2017-01-18 22:55:42,504 Z TED - Recebido 1205.00<br>3 3 4 4 2019-06-26 21:38:39.164Z Depésito em espécie 166.50<br>4 4 5 5 2015-09-28 05:58:31.182Z Depésito em espécie 491.50<br>10994 10994 10995 5 2015-10-07 12:03:06.543Z Compra Crédito -22.03<br>10995 10995 10996 643 2020-04-05 10:05:02.717 Z Compra Débito 18.95<br>10996 10996 10997 545 2020-04-13 09:40:10.888 Z Compra Débito 8.58<br>10897 10997 10998 517 2022-07-14 04:28:18.245Z Compra Débito 93.88<br>10998 10998 10999 885 2019-12-16 02:25:51.858 Z Compra Crédito -450.40<br>10999 rows x 6 columns<br><!-- End of picture text -->

- Operações com _strings_ 

1. .str.lower(): Converte todos os caracteres para letras minúsculas. 

Aqui iremos sobrescrever o DataFrame retornando os nomes das colunas com caracteres minúsculos. 



<!-- Start of picture text -->
¥, [34] # Passando os nomes das colunas para caracteres minisculos<br>df.columns = df.columns.str.lower()<br>df.head()<br>rag cod_transacao num_conta data_transacao nome_transacao valor_transacao [fH<br>oO 1 1 2016-03-15 18:09:56.704 Z Depésito em espécie 130.1 Bo<br>1 2 2 2021-02-03 02:56:28.418 Z_Depésito em espécie 270.1<br>2 3 3 2017-01-18 22:55:42.504 Z TED - Recebido 1205.0<br>3 4 4 2019-06-26 21:38:39.164 Z Depdsito em espécie 166.5<br>4 5 5 2015-09-28 05:58:31.182 Z Depdsito em espécie 491.5<br><!-- End of picture text -->

2. .str.upper(): Converte todos os caracteres para letras maiúsculas. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

68 



<!-- Start of picture text -->
% [35] # Retornando os nomes das colunas para forma original<br>df.columns = df.columns.str.upper()<br>df.head()<br>og COD_TRANSACAO NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO ff]<br>o 1 1 2016-03-15 18:09:56.704 Z Depdsito em espécie 130.1 it<br>1 2 2 2021-02-03 02:56:28.418 Z Depésito em espécie 270.1<br>2 3 3 2017-01-18 22:55:42.504 Z TED - Recebido 1205.0<br>3 4 4 2019-06-26 21:38:39.164 Z Depésito em espécie 166.5<br>4 5 5 2015-09-28 05:58:31.182 Z Depdsito em espécie 491.5<br><!-- End of picture text -->

### 3. .str.contains(): Verifica se uma _substring_ está presente. 

Vamos buscar no campo “NOME_TRANSACAO” valores que contenham a _substring_ “Pix”. 



<!-- Start of picture text -->
[37] # Buscando por Pix no campo “NOME_TRANSACAO™<br>d¥.1oc[df[ 'NOME_TRANSACAO" ].str.contains(’Pix’)]<br>oe COD_TRANSACAO NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO — [Fz]<br>1007 1008 42 2021-08-20 05:10:10.185 Z Pix - Realizado -525.0 Oo<br>1017 1018 95 2022-09-07 17:47:45.388 Z Pix - Realizado 132.4<br>1019 1020 495 2022-07-08 13:58:24.388 Z Pix - Recebido 482.8<br>1036 1037 546 2020-12-11 20:51:32.663 Z Pix - Recebido 840.5<br>1076 1077 768 2022-02-05 03:57:44.675 Z Pix - Recebido 238.0<br>10982 10983 762 2022-07-01 16:52:06.427 Z Pix - Realizado 471<br>10983 10984 256 2022-03-08 15:03:10.626 Z Pix - Recebido 182.2<br>10989 10990 702 2022-08-03 08:14:30.095 Z Pix - Realizado -402.3<br>10992 10993 26 2021-10-22 06:51:01.985 Z Pix - Recebido 368.8<br>10993, 10994 481 2022-09-25 04:04:08.278 Z Pix - Realizado -99.9<br>1264 rows x 5 columns<br><!-- End of picture text -->

- Exportação dos dados 

1. .to_csv(): Exporta o _DataFrame_ para um arquivo do tipo _.csv_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

69 

Quando fazemos alguma alteração nos dados, podemos querer exportar os dados como um arquivo _.csv_ , para isso usamos a função. 



<!-- Start of picture text -->
Ficheiros To x. + Cédigo + Testo<br>== 5 ‘5 2015-09126 05'58'91 1627 Deptaito<br>acne em espece 4315<br>ow Passos seguintes: | Gerar cédigo com df | @ Vergrificos recomendados New interactivesheet<br>> [BB sample_data ¥, [37] # Buscando por Pix no campo “NOME_TRANSACAO”<br>BB tansacao_tatado.csy °<br>Be onsacoescsv 4f Loc F[NOME_TRANSACAO" ].str-contains("Pix")]<br>= COD_TRANSACAO NUM_CONTA DATA_TRANSACAO NOME_TRANSACAO VALOR_TRANSACAO ff]<br>1007 1008 42 2021-08-20 05:10:10.1852  Px-Realizado 250<br>1017 1018 95. 2022.09.07 17:47:45.386Z _ Pix- Realizado “1924<br>1019 1020 495 2022-07-08 19:58:24,882 PIx-Recedido 4028<br>1098 1037 546 2020-12-11 20'51:92.6532 _Pix- Recebido e405<br>1078 1077 768 2022-02-05 03:57:44,675 2 _Pix- Recebido 2380<br>1098210983 10983 762 2022.07-01 1652.06.272 Pix- Realzado 474<br>10969 10984 286 2022-03-08 15:03:10.6262 _Pix- Recebido 1022<br>10993 26 2021-10-2205:51:01.9852  PIx-Recebido 368.8<br>10992 10990 702 2022-08-03 06:14:30,095 2 Pix- Realizado 402.3<br>10993 10994 481. 2022.09.25 04:04:08.2782 _Pix- Realizado 299<br>1264 rows 5 columns<br>oa © + Exporter o arquivo<br>éf to_csv("“transacao_tratado.csv")<br><!-- End of picture text -->

O arquivo aparece na aba de arquivos e pode ser baixado. 

### **Aula 28: Introdução à visualização de dados** 

Para plotar gráficos no Python vamos trabalhar com as bibliotecas Matplotlib e Seaborn, e para isso devemos importá-las em uma célula do Python como vemos abaixo. 



<!-- Start of picture text -->
x [39] # Import das bibliotecas de visualizacao de dados<br>import matplotlib.pyplot as plt<br>import seaborn as sns<br><!-- End of picture text -->

A biblioteca Seaborn é construída tendo como base a Matplotlib, a Seaborn é capaz de plotar gráficos mais estéticos, mas utilizaremos um 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

70 

misto das duas bibliotecas. 

### **Aulas 29, 30 e 31: Principais gráficos** 

Vamos iniciar pelo simples, porém muito útil e utilizado gráfico de barras. Para isso, vamos somar os valores das transações por tipo de transação. 



<!-- Start of picture text -->
oa [44] # Soma dos valores transacionados por tipo de transacao<br>dados_agrupados = df.groupby(‘NOME_TRANSACAO" )[ "VALOR_TRANSACAO" ].sum().reset_index()<br># Resultado<br>dados_agrupados<br>= NOME_TRANSACAO VALOR_TRANSACAO fF]<br>o Compra Crédito -1.862289e+05 Bo<br>1 Compra Débito -1.359668e+05 Y<br>2 DOC - Realizado -1.059100e+05<br>3 DOC - Recebido 3.180530e€+06<br>4 Depésito em espécie 2.480926e+05<br>5 Estorno de Debito 4.677000e+03<br>6 Pagamento de boleto -4.594840e+04<br>7 Pix - Realizado -2.943345e+05<br>8 Pix - Recebido 3.550648e+05<br>9 Pix Saque ~8.813858e+02<br>10 Saque -8.298999e+04<br>11 TED - Realizado -1.148500e+05<br>12 TED - Recebido 5.929251e+06<br>13 Transferéncia entre CC - Crédito 5.751830e+04<br>14 Transferéncia entre CC - Débito -2.292080e+04<br><!-- End of picture text -->

### ● Gráfico de barras 

Um gráfico de barras é uma forma de representar visualmente dados categóricos usando barras retangulares. O comprimento de cada barra é proporcional ao valor que ela representa. Para plotarmos um gráfico de barras devemos utilizar a função .barplot(), veremos que as funções da 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

71 

biblioteca Seaborn são bastante parecidas e os parâmetros passados devem ser _data_ , _x_ e _y_ . 



<!-- Start of picture text -->
¥ [45] # Plot de um grafico<br>ax = sns.barplot(data=dados_agrupados, x="NOME_TRANSACAO", y="VALOR_TRANSACAO’)<br>2 1e6<br>6<br>5<br>o4<br><g<<br>Gvg3<br>i<br>y<br>a<br>G2<br>s<br>1<br>0<br>Com/Srantpeninaritey Gette bined aiiebdiad mae sid Gilt renentivtinetetinechCe CEdibebito<br>NOME_TRANSACAO<br><!-- End of picture text -->

A visualização foi plotada, porém há pontos de melhoria para melhorar a sua apresentação como: adicionar um título, alterar os rótulos dos eixos e ajustar os valores das categorias no eixo x. Vamos adicionar mais linhas ao código para personalizar a nossa visualização e ver o resultado. 



<!-- Start of picture text -->
¥ © # Plot de um grafico<br>ax = sns.barplot(data=dados_agrupados, x="NOME_TRANSACAO’, y="VALOR_TRANSACAO')<br>ax.set_title(‘Total dos valores de transacao por tipo’) # titulo do grafico<br>ax.set_ylabel('Total’) # rétulo do eixo y<br>ax.set_xlabel('Tipo de transac3o') # rétulo do eixo x<br>plt.xticks(rotation=90) # altera a orientacao das categorias no eixo x<br>plt.show()<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

72 



<!-- Start of picture text -->
1e6 Total dos valores de transacao por tipo<br>6<br>5<br>4<br>33<br>Ke)<br>ec<br>2<br>1<br>0<br>ee£23sesee28o> 2 8 5o OG 2o °9o= 888B [o]BF S$F $zeszezeesFTF B&G FEF DVD 2°o<br>Ss @ Foose gs kos KF RD YW vw<br>i) A = vb © OA 2 = Bo HW => o § a<br>so & sc&Y ¢&g o © $vw ?6 X $a°o fy<br>SaeF etyxs g8eEexéFo 5 fe fe es98.0?9 8<br>6°48 % 2 eg FF ££ @<br>aa 0 oY<br>a) as 3so&8<br>c @<br>o ©<br>2<br>a5 26<br>ge<br>Tipo de transacgao<br><!-- End of picture text -->

Perceba que, na célula com o código, utilizamos tanto funções da biblioteca Seaborn como Matplotlib. 

Ainda assim, para tornar a visualização mais legível, podemos plotar o gráfico com as barras orientadas de forma horizontal, para isso basta inverter os campos passados para os parâmetros _x_ e _y_ . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

73 



<!-- Start of picture text -->
© # Plot de um grafico<br>ax = sns.barplot(data=dados_agrupados, y="NOME_TRANSACAO’, x="VALOR_TRANSACAO')<br>ax.set_title('Total dos valores de transacdo por tipo’) # titulo do grafico<br>ax.set_ylabel(‘Total') # rdétulo do eixo y<br>ax.set_xlabel('Tipo de transacéo') # rdétulo do eixo x<br>plt.show()<br><!-- End of picture text -->



<!-- Start of picture text -->
Total dos valores de transacao por tipo<br>Compra Crédito<br>Compra Débito<br>DOC - Realizado<br>DOC - Recebido<br>Depdsito em espécie<br>Estorno de Debito<br>_g PagamentoPix - Realizadode boleto<br>Pix - Recebido<br>Pix Saque<br>Saque<br>TED - Realizado<br>TED - Recebido<br>Transferéncia entre CC - Crédito<br>Transferéncia entre CC - Débito<br>0 1 2 3 4 5 6<br>Tipo de transacao le6<br><!-- End of picture text -->

Aqui respondemos a **4ª pergunta: “Qual o tipo de transação teve maior montante transacionado?”** . A percepção é bem intuitiva, pois a maior barra é a de “TED - Recebido”. 

Existe um outro tipo de gráfico gráfico de barras no Seaborn que é o _countplot._ Este é utilizado quando queremos contar, ou seja, determinar a frequência de diferentes categorias nos dados. 



<!-- Start of picture text -->
aa [43] ax = sns.countplot(data=df, y="NOME_TRANSACAO" )<br>ax.set_title('Frequéncia das categorias no conjunto de dados') # titulo<br>ax.set_ylabel('Frequéncia’) # rdétulo do eixo y<br>ax.set_xlabel('Tipo de transacdo’) # rétulo do eixo x<br>plt.show()<br><!-- End of picture text -->

> Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

74 



<!-- Start of picture text -->
Frequéncia das categorias no conjunto de dados<br>Depésito em espécie<br>TED - Recebido<br>Compra Crédito<br>Compra Débito<br>Pix - Realizado<br>Pix - Recebido<br>‘§ Transferéncia entre CC - Débito<br>cy Saque<br>z Pagamento de boleto<br>Transferéncia entre CC - Crédito<br>DOC - Recebido<br>Estorno de Debito<br>Pix Saque<br>DOC - Realizado<br>TED - Realizado<br>oO 500 1000 1500 2000 2500 3000 3500 4000<br>Tipo de transacao<br><!-- End of picture text -->

● Histograma 

Para quem nunca utilizou um histograma em suas análises, pode parecer apenas mais um gráfico de barras/colunas, no entanto, é utilizado quando queremos entender a distribuição dos dados. Cada coluna corresponde a um intervalo de valores e a sua altura denota a frequência dos dados dentro do intervalo no conjunto de dados. 



<!-- Start of picture text -->
&, [45] ax = sns.histplot(data=df, x="VALOR_TRANSACAO" )<br>ax.set_title(‘Distribuicao dos valores de transa¢aéo') # titulo<br>ax.set_ylabel('Frequéncia’) # rétulo do eixo y<br>ax.set_xlabel('Valor da transacao') # rdétulo do eixo x<br>plt.show()<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

75 



<!-- Start of picture text -->
Distribuicao dos valores de transacao<br>1000<br>800<br>6<br>% 600<br>©<br>oO3<br>a<br>r<br>400<br>200<br>0<br>(e) 50000 100000 150000 200000<br>Valor da transacao<br><!-- End of picture text -->

Como temos dados bastante dispersos e certamente _outliers_ , o histograma plotado é de difícil leitura. Porém, podemos selecionar apenas os dados de transações com valores mais baixos. Aqui vamos filtrar os dados com valores menores ou iguais a R$ 1000,00 e maiores que R$ -1000,00. Vamos considerar que uma transação negativa indica uma saída da conta, enquanto uma positiva indica uma entrada do valor na conta. 



<!-- Start of picture text -->
[51] ax = sns.histplot(<br>data=df.query(‘VALOR_TRANSACAO <= 16@@ and VALOR_TRANSACAO >= -1080")<br>» X="VALOR_TRANSACAO*<br>) # histograma com os dados filtrados<br>ax.set_title('Distribuicao dos valores de transac4o com dados filtrados’) # titulo<br>ax.set_ylabel('Frequéncia’) # rétulo do eixo y<br>ax.set_xlabel('Valor da transacao') # rétulo do eixo x<br>plt.show()<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

76 



<!-- Start of picture text -->
Distribuigao dos valores de transacao com dados filtrados<br>700<br>600<br>500<br>sg<br>3G<br>& 400<br>Ss<br>o<br>© 300<br>200<br>100<br>0<br>-1000 -750 -500 -250 0 250 500 750 1000<br>Valor da transacao<br><!-- End of picture text -->

Percebemos, a partir do histograma, que a maior parte das transações no _DataFrame_ filtrado são de valores em torno de zero. 

Em histogramas podemos plotar também a curva de densidade de probabilidade adicionando parâmetro _kde_ . Além disso, podemos alterar a cor do gráfico definindo o parâmetro _color_ , este é o mesmo para os demais gráficos do Seaborn. 



<!-- Start of picture text -->
[52] ax = sns.histplot(<br>data=df.query(‘VALOR_TRANSACAO <= 1@0@ and VALOR_TRANSACAO >= -1008") # histograma com os dados filtrados<br>2 X="VALOR_TRANSACAO*<br>, color="red’ # alterando a cor do grafico<br>» kde=True<br>)<br>ax.set_title("Distribuicdo dos valores de transacao com dados filtrados’) # titulo<br>ax.set_ylabel(‘Frequéncia’) # rétulo do eixo y<br>ax.set_xlabel(‘Valor da transaco') # rétulo do eixo x<br>plt.show()<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

77 



<!-- Start of picture text -->
Distribuigao dos valores de transacao com dados filtrados<br>700<br>600<br>500<br>a<br>&FS 400<br>Ss<br>o<br>= 300<br>!<br>200 |<br>100 |<br>y »<br>0 a =<br>-1000 -750 -500 -250 (o} 250 500 750 1000<br>Valor da transacao<br><!-- End of picture text -->

### ● Boxplot 

O boxplot é bastante interessante, pois indica, de maneira visual, os valores de diferentes medidas estatísticas como podemos ver abaixo. 



<!-- Start of picture text -->
Interquartile Range<br>Outliers I(IQR) Outliers<br>"Minimum"; | | "Maximum"I<br>(Q1 - 1.5*IQR) Ql Median Q3 (Q3 + 1.5*IQR)<br>(25th Percentile) (75th Percentile)<br>-4 3 -2 -1 0 1 2 3 4<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

78 

Os valores que se encontram além dos limites máximo e mínimo são marcados como pontos individuais e são os _outliers_ do conjunto. Para o conjunto de dados teremos o seguinte boxplot. 



<!-- Start of picture text -->
aa [53] ax = sns.boxplot(data=df, y="VALOR_TRANSACAO")<br>ax.set_title(‘Boxplot dos valores de transac4o') # titulo<br>ax.set_ylabel('Valor da transacao') # rétulo do eixo y<br>plt.show()<br><!-- End of picture text -->



<!-- Start of picture text -->
Boxplot dos valores de transagao<br>fe)<br>200000<br>150000<br>S °<br>S °<br>id<br>u<br>Cc<br>© 100000<br>5<br>oO<br>nol<br>re<br>2<br>$ 50000<br>0<br><!-- End of picture text -->

Analisando o gráfico percebemos que temos muitos outliers no conjunto de dados de transações, o que distorce bastante o gráfico. Portanto, vamos realizar a mesma abordagem do histograma, ou seja, vamos filtrar os valores de transação, mas dessa vez entre um intervalo de valores maiores ou iguais a zero e menores ou iguais a R$ 500,00. 



<!-- Start of picture text -->
x7 [56] axax.set_title(‘Boxplot= sns.boxplot (data=df.query(‘VALOR_TRANSACAOdos valores de transacdo com<= dados5@@ andfiltrados')VALOR_TRANSACAO# titulo>= @'), y="VALOR_TRANSACAO")<br>ax.set_ylabel(‘Valor da transa¢do’) # rétulo do eixo y<br>plt.show()<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

79 



<!-- Start of picture text -->
Boxplot dos valores de transagao com dados filtrados<br>500<br>400<br>°<br>oO<br>ye<br>$ 300<br>Cc<br>oO£<br>5<br>oO<br>mol<br>5 200<br>>&<br>100<br>t)<br><!-- End of picture text -->

O diagrama de caixa é muito bom para comparar a distribuição dos valores entre categorias. Podemos fazer isso com o campo com tipo de transação. 



<!-- Start of picture text -->
%. © ax = sns.boxplot(data=dF.query(“VALOR_TRANSACAO <= 5@@ and VALOR_TRANSACAO >= @"), x="VALOR_TRANSACAO", y="NOME_TRANSACAO")<br>ax.set_title(‘Boxplot dos valores de transacdo com dados filtrados’) # titulo<br>ax.set_ylabel("") # sem rétulo do eixo y<br>plt.show()<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

80 



<!-- Start of picture text -->
Boxplot dos valores de transacao com dados filtrados<br>Depésito em espécie yo —-<br>men feceoee le<br>Transferéncia entre CC - Crédito fy.<br>Estorno de Debito i—- o Oo ©<br>t) 100 200 300 400 500<br>Valor da transacao<br><!-- End of picture text -->

● Gráfico de dispersão e mapa de calor 

O gráfico de dispersão é muito útil quando desejamos representar qual a relação entre duas variáveis numéricas. Ele é constituído por pontos distribuídos em um plano cartesiano, cada ponto representa uma observação com posições correspondentes às posições nos eixos _x_ e _y_ baseadas no valor das variáveis. 

No conjunto de dados de transações temos apenas uma variável que exprime valor, por isso vamos importar o conjunto de propostas de crédito para realizar a análise com esse tipo de gráfico. 



<!-- Start of picture text -->
rn Oop ESC<br>& a cow.cseme co cousonook 0814 8TROK PEPOSTA. THAR PESAL_VAIORPEPOSTA VALOR FEMACIIENTO VALOR ENTRAON VALOR PESTAAO.QUNTIORE PAKCELAS CARENTA SATS. ROOSTA.<br>1 1s a7 mone n24sease coro: exsterrser fives sostesaira——spneose mo ete<br>: or re mzzasa4ssz212088 cores ssrorerast sonst wrisersa sera 6 eta<br><!-- End of picture text -->

Vamos observar o tipo de relação entre as variáveis “VALOR_FINANCIAMENTO” e “VALOR_ENTRADA” plotando o gráfico. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

81 



<!-- Start of picture text -->
Y% © # Plot do grafico de dispersdo<br>ax = sns.scatterplot(data=credito, x="VALOR_FINANCIAMENTO", y="VALOR_ENTRADA*)<br>ax.set_title(‘Relacdo entre o valor do financiamento e o valor da entrada’) # titulo<br>ax.set_ylabel( ‘valor da entrada’) # rétulo do eixo y<br>ax.set_xlabel('Valor do financiamento')<br>plt.show()<br><!-- End of picture text -->



<!-- Start of picture text -->
Relacao entre o valor do financiamento e o valor da entrada<br>120000 Z<br>100000 ges<br>peter<br>3: 80000 ce Pete aese<br>ro - saree Gees<br>o &s*s,2) 2, oS?<br>3 60000 rgrotesPeat© Sian é ogonteeee eats<br>5 ae fo ¥ % %<br>8 spore ro easese @ en an<br>40000 paced, 2°00 9288 % 9h, *aut?<br>is eaaeat TAO te) oer we<br>ee Sele wal ercace! Bo Ses<br>a6)08%>wieaeea tas Gocigete rele<br>20000 0) She18 eore8 8 ceive’<br>Keres<br>orca! eriteneyg 27.18 seine) e)<br>seeeMeanaie<br>oF 4 Sigpene) =<br>0 50000 100000 150000 200000 250000<br>Valor do financiamento<br><!-- End of picture text -->

O gráfico responde a **5ª pergunta: “Há correlação entre o valor do financiamento e o valor de entrada? Se sim, de qual tipo?”** . Há uma tendência de aumento nos valores de entrada com o aumento do valor do financiamento. Nesse caso dizemos que as duas variáveis possuem uma correlação positiva, pois enquanto o valor do financiamento, o valor da entrada também aumenta em algum grau. 

Existe uma função no Pandas que retorna os valores de correlação e aí temos um valor que exprime quantitativamente a correlação, seu uso é demonstrado abaixo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

82 



<!-- Start of picture text -->
oa [44] credito[["VALOR_FINANCIAMENTO’, ‘VALOR_ENTRADA‘]].corr(numeric_only=True)<br>2 VALOR_FINANCIAMENTO VALOR_ENTRADA [FH]<br>VALOR_FINANCIAMENTO 1.00000 0.84333 A<br>VALOR_ENTRADA 0.84333 1.00000<br><!-- End of picture text -->

Nesse caso, analisamos apenas a correlação entre as duas variáveis, porém podemos querer ter a visão da correlação entre todas as variáveis numéricas e de forma gráfica, para isso existe o mapa de calor. 



<!-- Start of picture text -->
¥% © # Grafico mapa de calor<br>ax = sns.heatmap(data=credito.corr(numeric_only=True), cbar=False, annot=True, cmap='coolwarm'))<br>ax.set_title(‘Mapa de calor da correlacao entre as varidveis’)<br>plt.show()<br><!-- End of picture text -->



<!-- Start of picture text -->
Mapa de calor da correlagao entre as variaveis<br>COD_PROPOSTA iam 0.043<br>COD_CLIENTE 1<br>COD_COLABORADOR 1<br>TAXA_JUROS_MENSAL =)9 = 1<br>VALOR_PROPOSTA 1 0.96<br>VALOR_FINANCIAMENTO 0.96 1 | 0.84<br>VALOR_ENTRADA 084 1<br>VALOR_PRESTACAO 025 023 015 | 1 0.35<br>QUANTIDADE_PARCELAS 0.35 1<br>CARENCIA 1<br><coowBE «§ 2§ &§ € <8 8 3 <<br>g | F G 2 = —E = g w<br>ec ce) fo} =, fe) = 2 ny =<br>a t a 1 a yn 1 eca raf1} w 1 rda Eg 5<br>a g fo} i 2 ing a wl!<br>fe}9 §8 S$ ce5 «6 £€ 52 x d @Q<br>1 oO 2g & gs g fa]<br>fay Ss gy =<br>8 & 8 s 8<<br>3$ 3<br><!-- End of picture text -->

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

83 

Voltando ao gráfico de dispersão, é possível realizar uma análise partindo de categorias utilizando o parâmetro _hue_ . 



<!-- Start of picture text -->
YX [47] # Plot do grafico de dispersao<br>ax = sns.scatterplot(data=credito, x="VALOR_FINANCIAMENTO', y="VALOR_ENTRADA', hue="STATUS_PROPOSTA')<br>ax.set_title(‘Relacdo entre o valor do financiamento e o valor da entrada’) # titulo<br>ax.set_ylabel(‘Valor da entrada’) # rétulo do eixo y<br>ax.set_xlabel(‘Valor do financiamento’)<br>plt.show()<br><!-- End of picture text -->



<!-- Start of picture text -->
Relacao entre o valor do financiamento e o valor da entrada<br>120000 STATUS_PROPOSTA °<br>e Validagao documentos oh<br>100000 e Enviada ee es<br>e Aprovada ad ook<br>e Em anilise goo.<br>80000 abiss’sensosm e eaex)<br>g 9 canee<br>g 60000 He Sa 0 Sore ere, we<br>5 yom mee oe eon e% o> ‘. : Ki<br>8g 068 Sedan Mine? S288 % 2%, *Seet®<br>40000 ag e,es* Soha es 53) ieee. O°.<br>o BESS ED os rere o'er78 SI<br>oeenl oneness Pawn e<br>20000 treesae eee<br>o, #<br>0 50000 100000 150000 200000 250000<br>Valor do financiamento<br><!-- End of picture text -->

**Aulas 32 a 36: Testes de hipóteses** 

O Python é uma importante ferramenta, isso já sabemos, porém a linguagem também é muito útil quando desejamos realizar análises estatísticas. Bibliotecas como Pandas, Numpy já contêm funções que calculam medidas estatísticas, mas caso seja necessário trabalhar com testes de hipóteses, temos que partir para o uso de bibliotecas como SciPy e Statsmodels. 

Teste de hipótese é um procedimento estatístico realizado quando desejamos avaliar uma afirmação sobre uma população com base em 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

84 

dados amostrais. Recomendo fortemente uma revisão rápida no módulo anterior do curso, o módulo de Estatística. 

Existem diferentes tipos de teste de hipóteses, nesse módulo falaremos em três deles 

1. Teste de normalidade; 

2. Teste de média com uma amostra; 

3. Teste de média com duas amostras independentes. 

- Teste de normalidade 

A normalidade dos dados é uma condição importante para realização de muitas inferências a respeito da população. Testes de normalidade testam se uma amostra é proveniente de uma distribuição normal. 

Existem diferentes funções para realização de teste de normalidade, aqui vamos utilizar a função “normaltest” que é baseada no teste Kolmogorov-Smirnov. Para a sua realização criaremos uma amostra pseudo aleatória com “np.random.normal()”. 



<!-- Start of picture text -->
~ [6] # Criac&o de uma amostra<br>np.random.seed(42<br>amostra = np.random.normal(loc=1, scale=0.4, size=100@)<br><!-- End of picture text -->

Os parâmetros passados “loc”, “scale” e “size” definem, respectivamente, os valores da média, desvio padrão e tamanho da amostra. 

Com a realização do teste teremos as hipóteses 

𝐻0: a amostra é oriunda de uma distribuição normal 

𝐻1: a amostra não é oriunda de uma distribuição normal 

Devemos considerar um valor de nível de significância (𝝰), no nosso caso podemos trabalhar com 5%. Essa informação é importante para rejeitar ou 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

85 

não a hipótese nula após a realização do teste. A função é importada e o conjunto amostral é utilizado. 



<!-- Start of picture text -->
x [7] from scipy.stats import normaltest # import da funcao<br>x [10] test, pvalue = normaltest(amostra) # teste de Kolmogorov-Smirnov<br>print(f"Estatistica de teste: {test}")<br>print(#"P-valor: {pvalue}")<br>Sy Estatistica de teste: @.5750300947846562<br>P-valor: @.7501252792566859<br><!-- End of picture text -->

A função retorna a estatística de teste e o p-valor. Ambas informações podem ser utilizadas para avaliar as hipóteses. O critério que vamos utilizar é: caso p-valor for menor que o nível de significância, a hipótese nula deve ser rejeitada. 



<!-- Start of picture text -->
x [11] if pvalue > @.@5:<br>print("A amostra segue uma distribuicdo normal.")<br>else:<br>print("A amostra nao segue uma distribui¢ao normal.")<br>Sy A amostra segue uma distribuicdo normal.<br><!-- End of picture text -->

- Teste de média com uma amostra 

Quando queremos determinar se a média de uma amostra é significativamente diferente da média populacional, devemos realizar esse tipo de teste. Vamos partir de uma situação problema. 

Uma empresa deseja avaliar se o tempo médio de atendimento ao cliente, registrado por uma nova equipe de suporte, é significativamente diferente do padrão de 15 minutos, que é a média histórica da empresa. Sabe-se que a população segue uma distribuição normal. A equipe coletou uma amostra aleatória de tempos de atendimento para 25 chamadas recentes. Os tempos registrados (em minutos) foram: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

86 



<!-- Start of picture text -->
¥ [11] # Amostra coletada<br>amostra_coletada = [14.8, 15.2, 15.1, 16.0, 14.9, 15.3, 14.7, 15.4, 15.5, 14.6,<br>15.2, 15.0, 15.6, 15.8, 14.8, 14.9, 15.0, 15.1, 15.7, 14.9,<br>15.3, 15.6, 15.4, 15.5, 14.8]<br><!-- End of picture text -->

Como temos uma amostra de tamanho menor que 30 e não sabemos o desvio padrão populacional, nesse caso devemos utilizar o teste _t de Student_ . Dado o enunciado, o teste possui duas hipóteses 



Nesse caso, o teste que vamos realizar deve ser do tipo bicaudal, e essa informação deverá ser passada na função. 



<!-- Start of picture text -->
t 0 t<br><!-- End of picture text -->

Definimos as variáveis e executamos as células para realização do teste. Assim como, o valor de nível de significância de 5%. A função para realização do teste é a “ttest_1samp”. Passamos “two-sided” para o parâmetro “alternative”. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

87 



<!-- Start of picture text -->
X% [22] media = 15 # valor da média histérica<br>alpha = @.05 # nivel de significancia<br>X% [23] from scipy.stats import ttest_1samp<br>aa [24] # Teste t para uma amostra<br>stat, pvalue = ttest_1samp(amostra_coletada, media, alternative="two-sided")<br>print(f"Estatistica de teste: {stat}")<br>print(#"P-valor: {pvalue}")<br>Sy Estatistica de teste: 2.746743077618503<br>P-valor: @.011231923627007468<br><!-- End of picture text -->

A função retorna a estatística de teste e p-valor, e o último é utilizado para rejeitarmos ou não a hipótese nula. Utilizando o critério do p-valor, o bloco de código retorna a decisão. 



<!-- Start of picture text -->
x [26] if pvalue < alpha:<br>print("A hipdtese nula é rejeitada.")<br>else:<br>print("Nao ha evidéncia suficiente para rejeitar a hipdtese nula.")<br>S¥ A hipétese nula é rejeitada.<br><!-- End of picture text -->

Rejeitamos a hipótese nula, a média dos dados é diferente da média histórica. 

- Teste de média com duas amostras independentes 

Esse teste é utilizado quando desejamos comparar a média de dois grupos independentes, ou seja, dois grupos que são constituídos por indivíduos experimentais diferentes. Vamos partir da situação problema. 

Uma empresa de varejo implementou dois métodos diferentes de treinamento para suas equipes de vendas, com o objetivo de aumentar o número médio de vendas realizadas por dia. Após o treinamento, os números de vendas diárias foram registrados para dois grupos de 20 vendedores cada (um para cada método). Sabe-se que os dados seguem uma distribuição. A empresa deseja verificar, com um nível de 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

88 

significância de 5%, se há uma diferença significativa entre as médias de vendas diárias dos dois grupos. 



<!-- Start of picture text -->
y, [40] # Dados das duas amostras<br>grupo_a = [15, 17, 16, 14, 18, 19, 13, 20, 18, 14, 16, 17, 15, 19, 18, 14, 17, 16, 15, 19]<br>grupo_b = [16, 19, 18, 17, 21, 20, 15, 22, 21, 19, 17, 18, 20, 22, 21, 18, 2, 19, 17, 22]<br><!-- End of picture text -->

Como temos uma amostra de tamanho menor que 30 e não sabemos o desvio padrão populacional, nesse caso devemos utilizar o teste _t de Student_ . Dado o enunciado, o teste possui duas hipóteses 





Dado as hipóteses também deveremos realizar um teste bicaudal. Definimos as variáveis, teste de significância de 5%. A função para realização do teste é a “ttest_ind”. Passamos “two-sided” para o parâmetro “alternative”. 



<!-- Start of picture text -->
x [41] alpha = 0.05 # nivel de significancia<br>x [42] from scipy.stats import ttest_ind<br>aa [43] # Teste t para duas amostras independentes<br>stat, pvalue = ttest_ind(grupo_a, grupo_b, alternative="two-sided")<br>print(f"Estatistica de teste: {stat}")<br>print(f"P-valor: {pvalue}")<br>Sy Estatistica de teste: -4.021979912696735<br>P-valor: @.0@02645468562017813<br><!-- End of picture text -->

A função retorna a estatística de teste e p-valor, e o último é utilizado para rejeitarmos ou não a hipótese nula. Utilizando o critério do p-valor, o bloco 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

89 

de código retorna a decisão. 



<!-- Start of picture text -->
~ [45] if pvalue < alpha:<br>print("A hipétese nula é rejeitada.")<br>else:<br>print("Naéo ha evidéncia suficiente para rejeitar a hipdtese nula.")<br>Sy A hipdtese nula é rejeitada.<br><!-- End of picture text -->

Rejeitamos a hipótese nula, há uma diferença entre as médias de vendas diárias entre os métodos de treinamento. 

### **Aulas 37 e 38: Análise preditiva e modelos de** **_machine learning_** 

No BanVic os analistas sempre se deparam com alguns novos desafios. Há três situações distintas, com três diferentes bancos de dados: 

- O BanVic busca aprimorar sua análise de crédito imobiliário utilizando inteligência artificial, especificamente modelos de regressão para prever os preços dos imóveis e oferecer condições mais justas e competitivas para seus clientes. Com uma base de dados detalhada sobre características de imóveis e seus respectivos preços, o banco deseja criar um modelo preditivo que ajude na tomada de decisão para concessão de financiamentos. A base de dados histórica para o problema é a “house_prices.csv”; 

- Um outro problema que a mesma instituição está enfrentando: a evasão de clientes. Nos últimos meses, um número significativo de clientes tem encerrado suas contas, impactando diretamente a rentabilidade e a reputação da instituição no mercado. Para combater esse problema, o banco decidiu utilizar análise preditiva e machine learning para prever quais clientes têm maior probabilidade de sair e agir proativamente para retê-los. O conjunto utilizado para o desafio é “Customer-Churn-Records.csv”; 

- O BanVic busca aprimorar sua estratégia de retenção e fidelização 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

90 

de clientes ao compreender melhor os diferentes perfis de usuários dos seus cartões de crédito. Atualmente, o banco enfrenta desafios na personalização de ofertas e na identificação de clientes que podem abandonar seus serviços. Para resolver esse problema, a instituição decidiu utilizar análise preditiva para segmentar os clientes de forma precisa e automatizada. O conjunto de dados utilizado para resolver este problema é “CC GENERAL.csv”. 

Podemos dividir a análise de dados em 4 diferentes tipos, como mostrado a seguir. 

Um resumo breve da definição de cada tipo de análise. 

- Descritiva: feita para entender e descrever fatos, resultados obtidos. 

- Diagnóstica: busca pela identificação de causas e relações entre variáveis. 

- Preditiva: utiliza dados a fim de prever tendências e resultados futuros. 

- Prescritiva:  baseado nos dados, busca fornecer recomendações para tomada de ações. 

Quando trabalhamos com análise preditiva temos bastante contato com algoritmos de _machine learning_ e/ou modelos estatísticos. Neste módulo trabalharemos, de maneira introdutória, com algoritmos de duas grandes áreas do aprendizado de máquina: o aprendizado supervisionado e o não supervisionado. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

91 



<!-- Start of picture text -->
Meaningful ‘Structur fr<br>Compression Discovery chs Customer Retention<br>ae Unsupervised Supervised Padvardsing Populariy<br>Learning Learning WeatherForecasting<br>Targetted Clustering M h . Popul: Regression<br>Customer : Prediction Esimating<br>Segmentation earnl ng life expectancy<br>Real-time decisions GameAl<br>Reinforcement<br>Learning<br>Robot Navigation Skill Acquisition<br>Learning Tasks<br><!-- End of picture text -->

Na área do aprendizado supervisionado temos modelos que trabalham com um conjunto de dados já rotulados, em que cada entrada (também chamada de _feature_ ) está associada a uma saída (ou _target_ ) conhecida. 



<!-- Start of picture text -->
Feature Target<br>_—$——— TT<br>[Tamanho| |Borda| | Marca/estilo|| Escalal | | Cor | |<br>[| 1] |Médio| |fistradf [| [x | || 5 [| Vermelho | |<br>| 5[eo6 _|| Grande]Grande] || PontilhadaPontihaga || [|[|Xo |{||| 16 {||] Vermetho[Azul] || ||<br>L7a| Enormel! | Normal’ [ | xy soy Aza<br>t a | | a a<br>Index<br><!-- End of picture text -->

Ou seja, no aprendizado supervisionado temos modelos que mapeiam as _features_ e, com base no aprendizado dos padrões desse conjunto de dados, fazem a previsão dos valores do _target_ . As suas principais 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

92 

aplicações são nos modelos de 

● Regressão: quando busca-se estimar valores numéricos contínuos. Exemplo: a partir das características de um carro, como ano de fabricação, quantidade de portas, quilometragem, cor, busca-se prever o seu preço de venda. 

● Classificação: quando busca-se prever categorias ou classes. 

Exemplo: a partir das características de uma pessoa, como massa corporal, idade, altura, presença de comorbidades, busca-se prever se a pessoa desenvolverá ou não diabetes no futuro. 

Outra grande área no universo de machine learning é o aprendizado não supervisionado. Nesse caso, o modelo trabalha com dados não rotulados, ou seja, o _target_ não é conhecido. 

Uma aplicação bastante conhecida é a clusterização. Nela busca-se agrupar dados semelhantes. 



<!-- Start of picture text -->
Clustering<br>fe) 4 Clustert<br>fe) fo) @®%6 fe) e.. @ O%e6<br>fe) So0%0 Go fe©..€_4%%© ge<br>0 80 © 0.0ne) c> o% .@..~ @606<br>ews ete ee<br>oo ome) Go. of<br>0 O S00 @ O Ago CLluster3<br>e2Qo_0 “@e@ 9<br>Cluster2<br>Oo ® @® ig o) ® oe<br><!-- End of picture text -->

Na clusterização podemos agrupar, por exemplo, clientes de uma rede de lojas. Nesse tipo de modelo, padrões são identificados e utilizados para formação dos grupos. Perceba que não teríamos, previamente, os dados de saída, mas os grupos seriam retornados pelo modelo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

93 

Quando utilizamos algoritmos de _machine learning_ , é fundamental separar o conjunto de dados em dois subconjuntos principais: dados de treino e dados de teste. 

- Os dados de treino são usados para construir o modelo, ou seja, é com eles que o algoritmo aprende os padrões dos dados. 

- Já os dados de teste são usados para avaliar o desempenho do modelo em dados que ele ainda não viu. 



<!-- Start of picture text -->
<——__———_ Dataset _____—_iy¥s?<br>Training Set Test Set<br><!-- End of picture text -->

Essa separação é importante porque garante que a avaliação do modelo seja mais fiel à realidade, permitindo entender se ele realmente generaliza bem para novos dados. Sem essa separação, corremos o risco de avaliar o modelo com os mesmos dados que ele usou para aprender, o que pode mascarar falhas e dar uma falsa impressão de qualidade. 

Durante o desenvolvimento de modelos de _machine learning_ , também é comum nos depararmos com dois problemas: o overfitting e o underfitting. 

- Overfitting (ou sobreajuste): acontece quando o modelo aprende os dados de treino _bem demais_ , incluindo ruídos ou padrões específicos que não se repetem nos dados reais. Como resultado, ele tem um ótimo desempenho nos dados de treino, mas um desempenho ruim em novos dados. 

- Underfitting (ou subajuste): ocorre quando o modelo é _simples demais_ e não consegue capturar os padrões presentes nem nos dados de treino. Isso leva a um baixo desempenho tanto no treino 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

94 

quanto no teste. 



<!-- Start of picture text -->
Underfit Good Fit Overfit<br><!-- End of picture text -->

A busca por um bom modelo envolve encontrar o equilíbrio certo, onde o modelo aprende bem os dados de treino, mas ainda consegue generalizar para novos exemplos com precisão. 

### **Aulas 39 e 40: Regressão com o modelo de regressão linear** 

Há diferentes modelos de regressão, neste módulo vamos explorar a regressão linear. Este tipo de modelo é relativamente simples, pois parte de uma técnica estatística estabelecida e largamente aplicável. 

O modelo de regressão linear busca estabelecer uma relação linear entre as variáveis de entrada e o _target_ , ou seja, encontrar a equação que melhor representa essa relação. De forma genérica teremos a fórmula 

𝑌 = β0 + β1𝑋1 + β2𝑋2 + β3𝑋3 + ... + β𝑛𝑋𝑛 + ε 

Em que 

- Y é a variável _target_ , a qual deseja-se prever o valor; 

- 𝑋1, 𝑋2, 𝑋3 … 𝑋𝑛 são as variáveis de entrada do modelo; 

- β0 é o intercepto, valor que a variável Y assume quando as demais variáveis de entrada são zero; 

- β1, β2, β3 … β𝑛 são os coeficientes, representam a influência de cada 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

95 

### variável de entrada sobre o _target_ ; 

- ε é o erro residual. 

Este tipo de modelo busca traçar a reta que melhor se ajusta aos dados, portanto, os coeficientes encontrados devem minimizar o somatório dos erros quadráticos (OLS). Analisando visualmente temos 



<!-- Start of picture text -->
60<br>°<br>55 fe}<br>50 ae<br>oO<br>4s Oo U7 a<br>a Negative<br>° ° o? 2? Residual<br>40 Positive eo- °<br>Residual,- a °<br>35 fo}<br>30<br>5 10 1s 20 2s 30 35<br><!-- End of picture text -->

Portanto, o OLS busca diminuir a soma do erro quadrático que é representada abaixo 



Em que 

- é o valor real da variável de saída; 

- 𝑦𝑖 

- 𝑦𝑖 é o valor estimado pelo modelo da variável de saída. 

Agora que demos um overview em como o modelo de regressão linear funciona, temos que organizar o nosso conjunto de dados para treinar o modelo. 

Em _machine learning_ é necessário dividir o conjunto de dados em dois 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

96 

subconjuntos: dados de treino e dados de teste. 

- Dados de treino: como o próprio nome diz, é o conjunto de dados utilizado para treinar o modelo. Este se ajusta a esse conjunto de forma ter seus parâmetros que melhor se adequam aos dados; 

- Dados de teste: conjunto de dados que não foi utilizado no modelo a fim de avaliá-lo. A avaliação do modelo com base no conjunto de teste garante a capacidade de generalização a partir de novos dados, ou seja, como ele se comporta com dados não antes vistos. 

A avaliação do modelo com base nos dados de teste, além de garantir uma avaliação da sua capacidade de generalização, também evita o _overfitting_ : um modelo extremamente ajustado aos dados de treino, mas que não é capaz de generalizar, isso levaria a uma ótima avaliação neste conjunto, mas um péssimo desempenho em dados novos. 

Existem diferentes técnicas utilizadas para separar o conjunto de dados nos dois subconjuntos, a mais simples e que utilizaremos aqui é a _Holdout_ . A imagem a seguir ilustra como a técnica é aplicada 



<!-- Start of picture text -->
DATASET<br>Training Dataset Testing Dataset<br>TRAIN<br>Train Model Evaluate Model<br><!-- End of picture text -->

Para aplicar a técnica no Python podemos importar a função “train_test_split” da biblioteca Scikit-learn, como é mostrado abaixo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

97 

Python 

# Import da função train_test_split 

from sklearn.model_selection import train_test_split 

É uma convenção na comunidade de machine learning, definir as variáveis de entrada como “X” e a variável de saída como “y”como. A partir dessa definição, é usada a função para definir em conjuntos de treino e teste. A nomenclatura mais comum é “X_train”, “X_test”, “y_train”, “y_test”. Ao trabalhar com a função “train_test_split” é necessário explicitar qual a proporção dos dados vai ser reservada no conjunto de testes, sendo as proporções mais comuns entre treino e teste, respectivamente, 70%/30% ou 75%/25% ou 80%/20%. A proporção é definida pelo parâmetro “test_size” e o parâmetro “random_state” permite a reprodução da exata mesma separação dos dados. 

#### Python 

# Separando em variáveis de entrada e saída 

X = df[['variavel_um', 'variavel_dois']] y = df['target'] 

# Definindo os conjuntos de treino e teste 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

O algoritmo da regressão linear também pode ser importado a partir da Scikit-learn, como mostrado abaixo 

#### Python 

# Import do algoritmo LinearRegression 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

98 

from sklearn.linear_model import LinearRegression 

model = LinearRegression() 

Após utilizar “train_test_split” é preciso treinar o modelo, para isso usa-se a função “fit()”, ou seja, o modelo é ajustado, e nesse caso **SEMPRE** com base no conjunto de treino. 

Python 

# Ajuste do modelo com base nos dados de treino 

model.fit(X_train) 

As estimativas são feitas usando a função “predict()”, dessa vez com o conjunto reservado para teste. 

Python 

# As estimativas são geradas e armazenadas na variável 

y_pred = model.predict(X_test) 

Por fim, o modelo é avaliado confrontando os valores preditos aos valores reais do conjunto reservado de teste. Os principais métodos de avaliação em problemas de regressão são 

- R²: contabiliza a proporção da variabilidade da variável de saída explicada pelo modelo. 



Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

99 

- Mean Absolute Error (MAE): é a média do valor absoluto de todos os erros. 



- Mean Squared Error (MSE): é a média dos erros quadrados. 



- Root Mean Squared Error (RMSE): é a raiz quadrada da média dos erros quadrados. 

𝑛1 Σ𝑖=1𝑛 (𝑦𝑖 − 𝑦𝑖)² 

As funções podem ser importadas, o código abaixo também mostra o seu uso. Perceba que o RMSE não possui própria, mas é calculado com a raiz quadrada do MSE. 

Python # Import das funções para avaliar o modelo 

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error # Coeficiente de determinação (R²) R2 = r2_score(y_test, y_pred) # Mean absolute error (MAE) 

MAE = mean_absolute_error(y_test, y_pred) 

# Mean squared error (MSE) 

MSE = mean_squared_error(y_test, y_pred) 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

100 

# Root mean squared error (RMSE) RMSE = np.sqrt(MSE) 

### **Aulas 41 e 42: Classificação com o modelo de regressão logística** 

Para problemas de classificação também há diferentes algoritmos que podem ser utilizados, no entanto, para resolução do nosso problema utilizaremos um modelo de regressão logística. 

O objetivo da regressão logística é modelar problemas de classificação binários, ou seja, em que a resposta é “sim” ou “não”, “sucesso” ou “fracasso”. 

Com este algoritmo o que ocorre é a modelagem da probabilidade de dada observação, com seus valores nas variáveis de entrada, pertencer a classe 1 (sendo esta a classe de interesse). 



Na regressão logística existe uma adaptação da função de regressão linear para outra função que retorna valores entre 0 e 1. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

101 



<!-- Start of picture text -->
y Y =bo +b,X 4 Linear Model<br>12<br>p Logistic Model<br>4 1<br>A PT Hebets)<br>0)<br>x<br><!-- End of picture text -->

Como o output que esperamos é binário, 0 ou 1, uma vez que a probabilidade é modelada entre 0 e 1, é necessário realizar uma espécie de decisão de corte, normalmente denominada de _cutoff_ da seguinte maneira 

● 𝑃(𝑥⃗) ≥ 0, 5: x pertence à classe 1; 

● 𝑃(𝑥⃗) < 0, 5: x pertence à classe 0. 

Aqui no problema de classificação repetiremos a aplicação da técnica de Holdout, assim como também teremos que ter os mesmos cuidados com o overfitting, treinar o modelo apenas com o conjunto de treino e avaliá-lo com o conjunto de teste. Portanto, os próximos passos são bem próximos ao que vimos no treinamento do modelo de regressão linear, diferenciando-se no _import_ do modelo e nas técnicas que vamos avaliá-lo. 

Python 

# Import da função train_test_split 

from sklearn.model_selection import train_test_split 

# Separando em variáveis de entrada e saída 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

102 

X = df[['variavel_um', 'variavel_dois']] y = df['target'] 

# Definindo os conjuntos de treino e teste 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Import do algoritmo LogisticRegression 

from sklearn.linear_model import LogisticRegression 

model = LogisticRegression() 

# Ajuste do modelo com base nos dados de treino 

model.fit(X_train) 

# As estimativas são geradas e armazenadas na variável 

y_pred = model.predict(X_test) 

Com o modelo de regressão logística treinado, devemos avaliá-lo levando em conta os valores estimados a partir do conjunto de teste, assim como fizemos com o modelo de regressão linear. No entanto, as métricas utilizadas em modelos de classificação são diferentes das utilizadas em modelos de regressão. 

Em classificação as métricas são derivadas de um conceito importante denominado **matriz de confusão** . 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

103 



<!-- Start of picture text -->
0 TN FP<br>1 FN TP<br><!-- End of picture text -->

Neste método, leva-se em consideração as classes preditas e as classes verdadeiras da base de teste, e contabiliza a performance do modelo. Para entendermos a matriz de correlação, vamos utilizar o exemplo de testes de COVID-19. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

104 



<!-- Start of picture text -->
coviD 2<br>rs)®<br>a<br>®<br>no<br>8ao<br>cS)<br>NORMAL — 1<br>1<br>covip NORMAL<br>Classe prevista<br><!-- End of picture text -->

Durante a pandemia de COVID-19 era muito comum ouvir sobre resultados de testes falsos positivos ou falsos negativos. Isso ocorre, pois nem sempre o resultado do teste reflete o estado de saúde real da pessoa. Ou seja, uma pessoa infectada com o vírus pode ter resultado negativo para o teste, mas uma pessoa sem infecção pode ter resultado positivo, nestes casos teríamos, respectivamente, um **falso negativo** e um **falso positivo** . Um teste eficaz, portanto, reflete majoritariamente resultados que coincidem com o estado de saúde real das pessoas. Em resumo 

- Verdadeiros positivos (VP): classificação correta da classe positivo; 

- ● Verdadeiros negativos (VN): classificação correta da classe negativo; 

- Falsos positivos (FP): classe correta negativo, classe prevista positivo; 

- Falsos negativos (FN): classe correta positivo, classe prevista negativo. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

105 

As métricas derivadas da matriz de confusão e que serão utilizadas são 

- Acurácia: proporção entre as previsões corretas e o total de amostras. 

𝑇𝑃 + 𝑇𝑁 𝐴𝑐𝑢𝑟á𝑐𝑖𝑎 = 𝑇𝑃 + 𝑇𝑁 + 𝐹𝑃 + 𝐹𝑁 

- Precisão (precision): mede a taxa de acerto entre as previsões positivas, em outras palavras, mede a qualidade das previsões positivas. 

𝑇𝑃 𝑃𝑟𝑒𝑐𝑖𝑠ã𝑜 = 𝑇𝑃 + 𝐹𝑃 

- Revocação (recall): mede a capacidade do modelo em identificar corretamente todas as ocorrências da classe positiva. 

𝑇𝑃 

𝑅𝑒𝑣𝑜𝑐𝑎çã𝑜 = 𝑇𝑃 + 𝐹𝑁 

- F1-Score: média harmônica entre precisão e revocação, equilibra as duas métricas. 

𝐹1 = 2 ×<sup>𝑃𝑟𝑒𝑐𝑖𝑠ã𝑜 × 𝑅𝑒𝑣𝑜𝑐𝑎çã𝑜</sup> 𝑃𝑟𝑒𝑐𝑖𝑠ã𝑜 + 𝑅𝑒𝑣𝑜𝑐𝑎çã𝑜 

A biblioteca Scikit-learn contém funções que retornam o resultado das métricas, para realizar o _import_ temos 

Python 

# Import das funções para avaliar o modelo 

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score 

# Matriz de confusão 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

106 

print(confusion_matrix(y_test, y_pred)) # Acurácia print(accuracy_score(y_test, y_pred)) # Precisão print(precision_score(y_test, y_pred)) # Revocação print(recall_score(y_test, y_pred)) # F1-Score print(f1_score(y_test, y_pred)) 

### **Aulas 43 e 44: Clusterização com o modelo K-Means** 

O último caso de estudo é um pouco diferente, como vimos anteriormente, devemos trabalhar com uma técnica que permita que rótulos sejam destinados para cada observação. Para alcançarmos este objetivo, vamos trabalhar com o algoritmo K-Means. 

Este algoritmo, de aprendizado não supervisionado, é utilizado a fim de clusterizar dados, ou seja, quando deseja-se agrupar observações similares. Funciona de forma a dividi-los em um número K de grupos distintos. Para definição de qual cluster a observação faz parte, é necessário a de um ponto médio representativo do agrupamento, os centróides. 

O processo se dá seguinte forma: 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

107 

1. Escolha do número de agrupamentos (K): uma das técnicas mais utilizadas para determinar o número adequado de _clusters_ é a técnica _elbow;_ 

2. Inicialização dos centróides: a quantidade K de pontos é posicionada de forma aleatória no espaço dos dados; 

3. Atribuição das observações aos _clusters_ : cada observação é atribuída ao centróide mais próximo, com base em métricas de distância, normalmente a distância euclidiana; 

4. Novo cálculo dos centróides: o K-Means é iterativo, portanto, novos centróides são calculados a partir da média da distância entre as observações do agrupamento. Com o reposicionamento do centróide, as observações são atribuídas aos seus pontos centrais mais próximos; 

5. Convergência: as etapas 3 e 4 são repetidas até que os pontos centrais não mudem mais. 



<!-- Start of picture text -->
. : f<br>we we a |<br>(a) (b) ()<br>* © =<br>e e »<br>° Mod . ’ Md od . * ee<br>. : :<br>oe wm ee |<br>(d) (e) ()<br><!-- End of picture text -->

É comum, ao trabalhar com K-Means, que deseje-se analisar os _clusters_ após a sua definição bidimensionalmente em um gráfico de dispersão. No entanto, tal visualização não é possível se o conjunto de dados possuir mais de duas variáveis. Para contornar essa situação é possível utilizar a técnica _Principal Component Analysis_ (PCA). 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

108 

A PCA transforma um conjunto de variáveis em um novo conjunto conhecido como componentes principais, isto é, uma combinação das variáveis originais que preserve a máxima variância possível dos dados originais. 

Python 

# Import do PCA from sklearn.decomposition import PCA # Instancia-se o PCA pca = PCA(n_components=2) 

Perceba que definimos o número de componentes que desejamos obter ao aplicar a técnica no parâmetro do PCA. Após isso, fazemos o ajuste e transformação dos dados conforme mostrado abaixo 

Python # Ajuste e transformação com PCA df_pca = pca.fit_transform(df) 

Para definir o número ideal de _clusters, algumas_ técnicas podem ser usadas como o método _Elbow_ e _Silhouette_ . O mais comum é o primeiro. No método _Elbow_ plota-se um gráfico com o número de _clusters_ no eixo _x_ e no eixo _y_ uma métrica de distorção que é a soma das distâncias quadradas entre os pontos dos dados e seus respectivos centróides. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

109 

A quantidade adequada de _clusters_ é determinada pela visualização gráfica, sendo esse o ponto de inflexão do gráfico, ou seja, "o cotovelo", parte do corpo ao qual o nome do método se refere. 

Aqui é necessário importar o algoritmo K-Means, além disso, existe uma função que facilita a conclusão do número ideal de agrupamentos a partir do método _elbow_ 

Python 

# Import do algoritmo K-Means 

from sklearn.cluster import KMeans 

# Import do KElbowVisualizer 

from yellowbrick.cluster import KElbowVisualizer 

O algoritmo é passado na função KElbowVisualizer de forma a fim de que seja possível retornar a visualização com a análise do número ideal de _clusters_ 

Python 

# Objeto KMeans com os parâmetros kmeans = KMeans(init='k-means++', n_init='auto', random_state=42) 

# Instancia-se o objeto da função KElbowVisualizer 

elbow = KElbowVisualizer(kmeans, k=10) 

# Ajuste do Elbow passando o conjunto de dados 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

110 

elbow.fit(df_pca) # Visualização do resultado elbow.show() 

O resultado obtido por KElbowVisualizer pode ser visualizado a partir do exemplo abaixo, perceba que a visualização já traz o indicativo do número K ideal de centróides 



<!-- Start of picture text -->
Distortion Score Elbow for KMeans Clustering<br>I<br>250 H --- elbow at k=4, score = 122.909<br>'<br>'<br>i<br>i<br>i<br>i<br>200 I!<br>'<br>'<br>2!<br>°1<br>&1<br>& 150 I1<br>=]oi'<br>2<br>iy<br>5<br>'<br>i<br>100 1<br>I<br>!<br>'<br>'<br>'<br>!<br>50 1<br>I<br>2 3 4 5 6 7 8 9 10<br>k<br><!-- End of picture text -->

Os parâmetros utilizados ao definir o objeto K-Means, em resumo: “init” com argumento “k-means++”  melhora a escolha inicial dos centróides, “n_init” com argumento “auto”  define o número de inicializações de centróides, que será 1 devido ao uso do “k-means++”, o “random_state” garante a reprodutibilidade. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

111 

Com o número de clusters definidos, pode-se partir para o ajuste do modelo. É importante destacar que o número K de agrupamentos foi definido com base em valores definidos de parâmetros, portanto, devemos mantê-los ao treinar o algoritmo. 

Python 

# Definição do KMeans 

kmeans = KMeans(n_clusters=4, init='k-means++', n_init='auto', random_state=42) 

# É feito o ajuste e previsão dos clusters 

clusters = kmeans.fit_predict(df_pca) 

O código abaixo retorna os valores das coordenadas para os centróides e um _array_ com os valores previstos para os _clusters_ para cada observação. 

Python 

# Valores dos centróides 

centroides = kmeans.cluster_centers_ 

# Array com rótulos 

labels = kmeans.labels_ 

É possível  adicionar os rótulos referentes a cada observação, dessa forma é possível analisar de perto cada agrupamento. 

Python 

# Adição dos rótulos ao dataframe 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

112 

df['clusters'] = kmeans.labels_ 

## Conclusão 

Ao longo deste curso, exploramos os principais conceitos e ferramentas do Python para análise de dados, desde a base da linguagem até técnicas mais avançadas. Começamos com a introdução ao Python, compreendendo sua sintaxe e versatilidade. Em seguida, avançamos para variáveis, estruturas de decisão e estruturas de repetição, fundamentais para manipulação de dados e automação de processos. 

Aprofundamos nosso conhecimento com estruturas de funções, permitindo a criação de códigos mais modulares e reutilizáveis. Também exploramos módulos, pacotes e bibliotecas, facilitando o uso de recursos externos para otimizar análises e processamento de dados. 

O Pacote Pandas foi um dos destaques do curso, sendo uma ferramenta essencial para manipulação e transformação de dados. Além disso, aprendemos a gerar visualizações de dados, fundamentais para interpretar e comunicar insights de forma clara e eficaz. 

Por fim, entramos no universo da estatística e aprendizado de máquina, abordando testes de hipóteses para validação estatística e análise preditiva para modelagem de tendências e previsões. 

Com esse conhecimento, você agora possui uma base sólida para trabalhar com Python em análise de dados. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

113 

## Material Complementar 

**Tipo:** ☐ Site  [x] Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Learning SQL de Alan Beaulieu **Descrição:** Este livro é um guia prático para aprender SQL, com exemplos práticos que ajudam a entender como usar a linguagem para recuperar, atualizar e gerenciar dados em bancos de dados relacionais. **Link:** https://www.r-5.org/files/books/computers/languages/sql/mysql/Alan_Bea ulieu-Learning_SQL-EN.pdf 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** SQL for Data Analysis **Descrição:** Neste blog são apresentados conceitos básicos sobre SQL. **Link:** https://medium.com/blog-do-zouza/sql-for-data-analysis-e8d0356ecd3c 

## PYTHON 

**Tipo:** ☐ Site   [x] Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python Para Análise de Dados: Tratamento de Dados com Pandas, NumPy e IPython - Wes McKinney 

**Descrição:** Este é um dos melhores livros para aprender como manipular dados com Pandas. 

**Link:** 

https://www.amazon.com.br/Python-Para-An%C3%A1lise-Dados-Tratamento/dp/ 8575226479 

**Tipo:** ☐ Site   [x] Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python Fluente: Programação Clara, Concisa e Eficaz **Descrição:** Este é um excelente livro para aprender técnicas de escrita avançadas utilizando a linguagem Python 

**Link:** https://www.amazon.com.br/Python-Fluente-Programa%C3%A7%C3%A3o-C oncisa-Eficaz/dp/857522462X/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5% BD%C3%95%C3%91&crid=37WZTQZKYDHW&keywords=python+fluente&qid=16853 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

114 

64888&s=books&sprefix=python+fluent%2Cstripbooks%2C283&sr=1-1&ufe=app_ do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d 

**Tipo:** ☐ Site   [x] Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Pense em Python: Pense Como um Cientista da Computação **Descrição:** Este é um excelente livro introdutório sobre a linguagem de programação Python 

**Link:** https://www.amazon.com.br/Pense-Python-Como-Cientista-Computa%C3% A7%C3%A3o/dp/8575225081/ref=pd_bxgy_img_sccl_1/141-6529160-4900556?pd _rd_w=210au&content-id=amzn1.sym.758f3509-df88-4265-806c-565a738dc05d &pf_rd_p=758f3509-df88-4265-806c-565a738dc05d&pf_rd_r=VZ8HX4Z7EGXVM MB747V2&pd_rd_wg=VofwL&pd_rd_r=69e696a3-b7d9-4aa0-8807-6be8f0ec3d 02&pd_rd_i=8575225081&psc=1 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Como Alterar O Diretório De Trabalho Do Jupyter E Jupyter Lab No Ambiente Windows 

**Descrição:** Neste post você verá como trocar o diretório padrão de trabalho do Jupyter Notebbok, de forma a atender melhor as suas necessidades. **Link:** https://wpraiz.com.br/como-alterar-o-diretorio-de-trabalho-do-jupyter-e-j upyter-lab-no-ambiente-windows/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python uma linguagem de tipagem dinâmica e forte **Descrição:** Neste post você aprenderá mais sobre como funciona a tipagem de dados no Python. 

**Link:** http://blog.abraseucodigo.com.br/python-uma-linguagem-de-tipagem-di namica-e-forte.html 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Snake Case VS Camel Case VS Pascal Case VS Kebab Case – What's the Difference Between Casings? 

**Descrição:** Neste post você aprenderá mais sobre os padrões de uso de "cases" (tamanho de texto) em programação. Nele você terá um entendimento complementar a respeito do padrão "snake_case", que é o padrão utilizado pelo Python. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

115 

**Link:** https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pasc al-case-vs-kebab-case-whats-the-difference/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python 3's f-Strings: An Improved String Formatting Syntax (Guide) **Descrição:** Neste post você aprenderá mais sobre o funcionamento e o uso do padrão "f-string" do Python. 

**Link:** https://realpython.com/python-f-strings/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python Functions **Descrição:** Neste post você aprenderá mais sobre funções em Python. **Link:** https://www.geeksforgeeks.org/python-functions/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python Functions **Descrição:** Neste post você aprenderá mais sobre funções em Python. **Link:** https://www.w3schools.com/python/python_functions.asp 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python Functions **Descrição:** Neste post você aprenderá mais sobre funções em Python. **Link:** https://www.programiz.com/python-programming/function 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** How to Use Conditional Statements in Python – Examples of if, else, and elif **Descrição:** Neste post você aprenderá mais sobre o uso de estruturas condicionais - if - em Python. 

**Link:** https://www.freecodecamp.org/news/how-to-use-conditional-statements-i f-else-elif-in-python/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Glossário Python, biblioteca é sinônimo de pacote? Modulo é sinônimo de classe? 

**Descrição:** Neste post você aprenderá mais sobre o que são classes, módulos, pacotes e bibliotecas em Python 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

116 

**Link:** https://pt.stackoverflow.com/questions/377213/gloss%C3%A1rio-python-bibli oteca-%C3%A9-sin%C3%B4nimo-de-pacote-modulo-%C3%A9-sin%C3%B4nimode-classe 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Glossário Python, biblioteca é sinônimo de pacote? Modulo é sinônimo de classe? 

**Descrição:** Neste post você aprenderá mais sobre o que são classes, módulos, pacotes e bibliotecas em Python 

**Link:** https://pt.stackoverflow.com/questions/377213/gloss%C3%A1rio-python-bibli oteca-%C3%A9-sin%C3%B4nimo-de-pacote-modulo-%C3%A9-sin%C3%B4nimode-classe 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** 10 minutes to pandas 

**Descrição:** Neste post você aprenderá mais sobre o pacote Pandas do Python. **Link:** https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-panda s 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Package overview 

**Descrição:** Neste post você aprenderá mais sobre o pacote Pandas do Python. **Link:** https://pandas.pydata.org/docs/getting_started/overview.html 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Python Strings **Descrição:** Neste post você aprenderá mais sobre o strings em Python. **Link:** https://www.w3schools.com/python/python_strings.asp 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Pandas Tutor visualizes how Python code transforms dataframes **Descrição:** Neste post você aprenderá mais sobre como funcionam as agregações do pacote pandas do Python **Link:** https://pandastutor.com/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

117 

**Título:** Join tables using a common identifier **Descrição:** Neste post você aprenderá mais sobre como funcionam os agrupamentos no pacote Pandas em Python **Link:** https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combin e_dataframes.html#join-tables-using-a-common-identifier 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Join tables using a common identifier **Descrição:** Neste post você aprenderá mais sobre como funcionam os agrupamentos no pacote Pandas em Python 

**Link:** https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combin e_dataframes.html#join-tables-using-a-common-identifier 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** 5 Examples to Learn Date and Time Manipulation with Python Pandas **Descrição:** Neste post você aprenderá mais sobre como manipular datas utilizando o pacote padas do Python 

**Link:** https://towardsdatascience.com/5-examples-to-learn-date-and-time-ma nipulation-with-python-pandas-9ab9cdeb032e 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Pandas Dtype-Specific Operations: Accessors **Descrição:** Neste post você aprenderá mais sobre como utilizar assessores para manipular colunas do tipo "datetime" utilizando o pacote pandas do Python **Link:** https://towardsdatascience.com/pandas-dtype-specific-operations-acces sors-c749bafb30a4 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Apply and Lambda usage in pandas **Descrição:** Neste post você aprenderá mais sobre como utilizar a função apply e a utilizar "lambdas" em Python 

**Link:** https://towardsdatascience.com/apply-and-lambda-usage-in-pandas-b13 a1ea037f7 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Applying Lambda functions to Pandas Dataframe 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

118 

**Descrição:** Neste post você aprenderá mais sobre como utilizar a função apply e a utilizar "lambdas" em Python **Link:** https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dat aframe/ 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Pandas: combinando data frames com merge() e concat() **Descrição:** Neste post você aprenderá mais sobre como combinar DataFrames utilizando o pacote pandas do Python 

**Link:** https://medium.com/data-hackers/pandas-combinando-data-frames-co m-merge-e-concat-10e7d07ca5ec 

**Tipo:** [x] Site ☐ Livro ☐ Vídeo ☐ Leitura ☐ Filme ☐ Visite **Título:** Combining Data in pandas With merge(), .join(), and concat() **Descrição:** Neste post você aprenderá mais sobre como combinar DataFrames utilizando o pacote pandas do Python 

**Link:** https://realpython.com/pandas-merge-join-and-concat/ 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

119 

## Referências 

ORACLE. **O que é banco de dados?** [online] Disponível em: 

https://www.oracle.com/br/database/what-is-database/. Acesso em: 21 jun. 2023. 

KONDADO. **Banco de dados: o que é e quais são os principais tipos?** [online] Disponível em: 

https://kondado.com.br/blog/blog/2022/09/13/banco-de-dados-o-que-e -e-quais-sao-os-principais-tipos/. Acesso em: 21 jun. 2023. 

AMAZON WEB SERVICES. **What is a database?** [online] Disponível em: https://aws.amazon.com/pt/what-is/database/. Acesso em: 21 jun. 2023. 

ROCKCONTENT.COM. **Banco de dados: o que é, tipos e importância dele no site da sua empresa** . [online] Disponível em: 

<https://rockcontent.com/br/blog/banco-de-dados/>. Acesso em: 21 jun. 2023. 

ANACONDA. **Plataforma Anaconda.** [online] Disponível em: <https://www.anaconda.com/>. Acesso em: 21 jun. 2023. 

PROJECT JUPYTER. **Jupyter Notebook.** [online] Disponível em: <https://jupyter.org/>. Acesso em: 21 jun. 2023. 

GUARDIANS OF THE GALAXY. **Guia de Markdown.** [online] Disponível em: <https://www.markdownguide.org/>. Acesso em: 21 jun. 2023. 

PYTHON. **Documentação Python 3.9** . [online] Disponível em: <https://docs.python.org/pt-br/3.9/>. Acesso em: 21 jun. 2023. 

PANDAS. **Documentação Pandas.** [online] Disponível em: <https://pandas.pydata.org/docs/getting_started/index.html>. Acesso em: 21 jun. 2023. 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

120 

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA 

e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium. 

121 

