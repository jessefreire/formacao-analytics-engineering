


## Material Teórico
Curso: SQL para Análise de Dados

## Autoria
Prof. MSc. Renata Assunção
## Prof. Henrique Macedo Coelho


## Módulo
Módulo 2 - Consultando dados com SQL



Temas abordados


● Bancos de dados relacionais
● Aprenda a usar uma linguagem SQL através de consultas reais em um
banco de dados
● Principais cláusulas e operadores de SQL
● Principais funções agregadas, escalares e analíticas de SQL
● Boas práticas em SQL

Objetivos de Aprendizagem

● Ter noções básicas sobre bancos de dados e relacionamentos entre
tabelas
● Familiarizar-se com a linguagem SQL, sua aplicação e conceitos
fundamentais
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 1


● Conhecer e saber aplicar as principais funções para manipulação de
dados em SQL
● Aprender a manusear linguagem SQL para responder perguntas
usando consultas reais em um banco de dados

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 2


Apresentação do Módulo


Caro(a) aluno(a),

Seja bem vindo ao módulo de SQL para análise de dados.

Me chamo Henrique e vou acompanhar você durante esta jornada!

Sou formado em Administração Empresarial e entrei no mundo dos dados
há quatro anos. Meu primeiro contato com a análise de dados foi em
matérias da faculdade, mas, aos poucos, fui me interessando e
ingressando cada vez mais nesse mercado. Já atuei como Analytics
Engineer e, atualmente, sou analista de dados e team lead de uma equipe
de analistas.

Durante este módulo, entenderemos mais sobre bancos de dados e a
importância do SQL e suas funções para a carreira do analista de dados,
de forma teórica e prática. Você atuará como analista de dados de uma
empresa fictícia, o Banvic, traduzindo as necessidades do negócio em
análises valiosas ao aplicar os conceitos que aprenderemos em conjunto.

Ao final deste módulo, você será capaz de usar o SQL e suas funções, bem
como de compreender os principais conceitos sobre bancos de dados.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 3


Módulo 2 - Consultando dados com SQL

Aula 03: O que são bancos de dados

No módulo anterior, você teve uma introdução à análise de dados,
explorando seus conceitos e princípios. Agora, você talvez esteja se
perguntando algo que ouviu falar bastante: "Afinal, o que são bancos de
dados?".
De forma simples, um banco de dados é uma coleção organizada e
estruturada de informações, geralmente armazenada em formato
eletrônico. Pense nele como um grande arquivo digital, guardado em um
servidor e projetado para registrar, proteger e permitir o acesso a um
volume imenso de dados sobre qualquer assunto.
Para gerenciar tudo isso, os bancos de dados são controlados por um
Sistema de Gerenciamento de Banco de Dados (SGBD). Ele atua como
uma interface entre nós e os dados, sendo o responsável por traduzir uma
consulta (feita em uma linguagem específica, como o SQL), localizar a
informação e nos devolver a resposta de forma simplificada.
No modelo mais comum de banco de dados, as informações são
estruturadas em tabelas, compostas por linhas e colunas. Esse formato
torna o armazenamento e a consulta de dados extremamente eficientes.
A aplicação dos bancos de dados é vasta: eles são usados para
armazenar desde informações de clientes e fornecedores até dados de
redes sociais e processos internos de uma empresa. Justamente por
terem tantos usos, existem diferentes tipos e estruturas, que variam
conforme o modelo de dados mais adequado para cada situação.
Na próxima aula, vamos conhecer os principais tipos de bancos de dados
e as características de cada um deles.


_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 4



Figura: Sistema Gerenciador de Banco de Dados
Fonte: adaptada de Mattoso.



Aula 04: Quais os principais bancos de dados

Na aula anterior, você entendeu o que são bancos de dados, conhecendo
sua estrutura e a forma como são gerenciados. Agora, vamos dar o
próximo passo e explorar os principais tipos que existem e suas
características.
Afinal, como escolher a opção mais adequada para cada projeto? A
resposta para essa pergunta começa com o entendimento das diferenças
entre os principais modelos disponíveis.
Com a evolução da tecnologia, os bancos de dados também se
diversificaram para atender a novas demandas. Hoje, cada tipo é
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 5


projetado com características específicas para diferentes necessidades e
formatos de dados. Vamos conhecer os principais:

Banco de dados relacional: Este é o modelo mais tradicional, no qual os
dados são organizados em tabelas compostas por linhas e colunas, de
forma semelhante a uma planilha. Sua principal característica é a
capacidade de criar relacionamentos entre as tabelas, conectando
diferentes categorias de informação. Para consultar e manipular esses
dados, utiliza-se a linguagem SQL (Structured Query Language).
● Exemplos: Oracle, SQL Server, MySQL, PostgreSQL.
Banco de dados não relacional: Em contraste com o modelo relacional,
aqui os dados não exigem uma estrutura fixa. Eles podem ser
armazenados em diversos formatos flexíveis, como documentos, grafos,
ou pares de chave-valor. Conhecida como NoSQL (Not Only SQL), essa
abordagem é ideal para esquemas dinâmicos, permitindo que novas
propriedades sejam adicionadas facilmente sem impactar os dados já
existentes.
● Exemplos: MongoDB, Cassandra, Redis, Couchbase.
Banco de dados em nuvem: Mais do que um tipo de estrutura, este é um
modelo de implementação. Um banco de dados em nuvem, seja ele
relacional ou não relacional, é hospedado e operado por um provedor de
serviços (cloud provider). Nesse modelo, toda a infraestrutura é oferecida
como um serviço (DBaaS - Database as a Service), eliminando a
necessidade de a empresa gerenciar o hardware físico.
● Exemplos: Amazon Web Services (AWS), Google Cloud Platform
(GCP), Microsoft Azure.
Banco de dados orientado a objetos: Este modelo armazena informações
na forma de "objetos", de maneira similar à programação orientada a
objetos. Cada objeto pode conter tanto os dados (atributos) quanto os
procedimentos ou "métodos" que podem ser aplicados a esses dados.
Essa abordagem permite uma representação mais direta e fiel de
elementos complexos do mundo real dentro do sistema.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 6


● Exemplos: ObjectDB, db4o, Versant, GemStone/S.
Banco de dados distribuído: É composto por múltiplos bancos de dados
interligados por uma rede, que podem estar em diferentes computadores
ou locais geográficos. Do ponto de vista do usuário, o sistema funciona
como uma base de dados única e coesa. Cada parte do sistema é
chamada de "nó", e essa arquitetura garante benefícios como alta
escalabilidade e tolerância a falhas.
● Exemplos: Apache Cassandra, Amazon DynamoDB, Google Bigtable.


Agora que conhecemos os principais tipos de bancos de dados, vamos
nos aprofundar no modelo relacional, o mais comum no mercado. Mas
isso fica para próxima aula. Até lá!

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 7



## Vantagens Desvantagens
Banco de dados
relacional
- Estrutura bem definida;
- Integridade dos dados;
- Consultas eficientes;
- Suporte a transações.
## - Escalabilidade
limitada;
- Flexibilidade limitada;
- Custo elevado.
Banco de dados não
relacional
## - Escalabilidade;
## - Flexibilidade;
## - Custos.
- Dificuldade na
realização de
consultas mais
complexas;
- Falta de integridade
dos dados;
- Escassez de recursos.
Banco de dados em
nuvem
## - Escalabilidade;
## - Disponibilidade;
## - Flexibilidade;
## - Confiabilidade;
## - Segurança;
## - Custo;
- Acesso remoto.
- Dependência do
fornecedor;
## - Segurança;
- Latência de rede;
- Dependência de
internet
## - Custos
- Limitações de recursos
Bancos de dados
orientados a objetos
- Modelagem de dados
mais natural;
## - Flexibilidade;
- Reutilização de
códigos;
## - Performance.
- Curva de aprendizado
muito íngreme;
## - Escalabilidade
limitada;
- Falta de padrões;
## - Incompatibilidade
com sistemas legados.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 8



Aula 05: Banco de dados relacional

Agora que já conhecemos os principais tipos de bancos de dados, vamos
nos aprofundar na estrela entre eles: o banco de dados relacional. Este
modelo, proposto por Edgar Codd em 1970, não apenas armazena, mas
também gerencia com eficiência grandes volumes de informação em um
formato estruturado. Sua popularidade é imensa; segundo a plataforma
Statista, os bancos de dados relacionais são os mais difundidos no
mundo, sendo responsáveis por guardar a maior parte dos dados
coletados atualmente.
A estrutura organizada do modelo relacional é o segredo de sua eficiência
e flexibilidade. Tudo se baseia em um componente central: a tabela. Cada
tabela armazena informações sobre uma categoria específica, como
"Clientes" ou "Produtos", e é composta por colunas e linhas.
● As colunas (ou campos) representam os atributos de um registro,
como o nome de um cliente ou o saldo de uma conta. Todos os
dados em uma mesma coluna devem ser do mesmo tipo (texto,
número, data, etc.).
● As linhas (ou registros) representam uma única entrada dentro da
tabela. Cada linha possui a mesma estrutura de colunas, embora
alguns campos possam ter valores nulos (não preenchidos).
● A intersecção de uma linha e uma coluna forma um campo, a
menor unidade de informação do banco de dados, análoga a uma
célula em uma planilha.
O que torna este modelo verdadeiramente poderoso, no entanto, é a
capacidade de criar relacionamentos entre as tabelas. Essa conexão é
estabelecida por meio de "chaves".
● A Chave Primária (Primary Key ou PK) é um ou mais atributos que
identificam cada registro de forma única dentro de uma tabela. Um
CPF, por exemplo, é uma excelente chave primária para uma tabela
de clientes, pois garante que não haverá duas pessoas com o
mesmo número. Se houver uma tentativa de inserir um cliente com
um CPF já existente, o banco de dados rejeitará a operação.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 9


● A Chave Estrangeira (Foreign Key ou FK) é a chave primária de uma
tabela que é inserida em outra para conectar os dados. Por
exemplo, a tabela "Pedidos" pode ter uma chave estrangeira com o
CPF do cliente, vinculando cada pedido ao cliente que o realizou.
Esse mecanismo de chaves permite garantir a integridade dos dados.
Uma das principais garantias é a integridade referencial, que impede, por
exemplo, a exclusão de um cliente que possua pedidos vinculados a ele.
Isso torna o modelo relacional a escolha ideal para aplicações que
exigem dados confiáveis e consistentes.
Para interagir com essa estrutura, utiliza-se uma linguagem padrão: o SQL
(Structured Query Language). Suas definições se baseiam na teoria dos
conjuntos, e a linguagem é dividida em sublinguagens que representam
as diferentes operações possíveis (consultar, inserir, atualizar, etc.).
Embora cada sistema de banco de dados possua seu próprio "dialeto" de
SQL, os conceitos e comandos principais são, em grande parte, os
mesmos.


Aula 06: SQL: O que é

Agora que você já conhece os bancos de dados relacionais, chegou a
hora de aprender a interagir com eles. A ferramenta para essa
comunicação é a linguagem SQL. Vamos explorar suas principais
características e seu funcionamento?
A Structured Query Language, ou SQL, é a linguagem de programação
padrão para gerenciar e manipular dados em bancos de dados
relacionais. Desenvolvida na década de 1970, sua robustez e eficiência a
tornaram uma ferramenta indispensável e amplamente utilizada por
empresas no mundo todo.
A interação com o banco de dados é feita por meio de consultas
(queries). Embora a sintaxe — a forma como escrevemos os comandos —
possa variar sutilmente entre os diferentes sistemas, a estrutura
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 10


fundamental para visualizar informações geralmente envolve as cláusulas
## SELECT
e
## FROM
## .
Consultas mais complexas podem ser enriquecidas com outras cláusulas,
que devem, obrigatoriamente, ser escritas na seguinte ordem:
## SELECT
## ,
## FROM
## ,
## WHERE
## ,
## GROUP BY
## ,
## HAVING
## ,
## ORDER BY
e
## LIMIT
## .
A linguagem SQL é composta por alguns elementos principais:
● Cláusulas: São os comandos que definem a estrutura da consulta,
especificando a ação a ser realizada. As mais comuns são
## SELECT

(seleciona as colunas),
## FROM
(indica a tabela de origem),
## WHERE

(filtra os registros),
## GROUP BY
(agrupa os dados) e
## ORDER BY
## (ordena
o resultado).
● Funções: São operações utilizadas para realizar cálculos sobre os
dados, como contar registros (
## COUNT()
), somar valores (
## SUM()
) ou
encontrar o maior (
## MAX()
) e o menor (
## MIN()
) valor de um conjunto.
● Transações: Além de consultar, o SQL permite a manipulação de
dados através de três operações básicas: inserção (
## INSERT
## ),
atualização (
## UPDATE
) e exclusão (
## DELETE
) de registros. A execução
segura de um conjunto dessas operações é chamada de
transação, garantindo a consistência dos dados.
Agora que você tem uma visão geral sobre o SQL, que tal colocá-lo em
prática? Na próxima aula, vamos começar a escrever nossos primeiros
comandos.


AULA 07: Tipos de comandos SQL

Após a introdução ao SQL na aula anterior, o próximo passo é entender
como os diferentes comandos da linguagem são classificados.
Esses comandos são agrupados em quatro categorias principais, de
acordo com a sua função:


_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 11




No dia a dia de uma análise de dados, você usará os comandos de forma
direta, e essa classificação teórica não costuma ser mencionada.
Contudo, compreendê-la é fundamental, pois estes termos são
frequentemente encontrados em documentações técnicas e no
vocabulário de profissionais da área.
Os comandos de SQL são agrupados em cinco sublinguagens principais,
cada uma com uma finalidade específica:
DQL (Data Query Language / Linguagem de Consulta de Dados) É
composta essencialmente pelo comando
## SELECT
e suas cláusulas (
## WHERE
## ,
## GROUP BY
, etc.). Sua única finalidade é consultar (ler) os dados, sem
realizar qualquer modificação. Para analistas de dados, esta é, de longe, a
sublinguagem mais utilizada.
● Principal comando:
## SELECT
## .
DML (Data Manipulation Language / Linguagem de Manipulação de
Dados) Comandos utilizados para manipular os dados, ou seja, para
inserir, atualizar ou excluir registros. Diferente da DQL, a DML efetivamente
modifica o conteúdo das tabelas.
● Principais comandos:
## INSERT
## ,
## UPDATE
## ,
## DELETE
## .
DDL (Data Definition Language / Linguagem de Definição de Dados)
Comandos que definem a estrutura dos objetos do banco de dados. São
usados para criar, alterar ou excluir tabelas, índices e outros componentes.
A DDL modifica o "esqueleto" do banco, não os dados contidos nele.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 12


● Principais comandos:
## CREATE
## ,
## ALTER
## ,
## DROP
## .
DCL (Data Control Language / Linguagem de Controle de Dados)
Comandos que gerenciam o acesso e as permissões dos usuários aos
dados, garantindo a segurança do banco.
● Principais comandos:
## GRANT
## (conceder),
## REVOKE
## (revogar).
TCL (Transaction Control Language / Linguagem de Controle de
Transação) Comandos que gerenciam as transações para garantir a
consistência das operações. Eles confirmam (
## COMMIT
) ou desfazem
## (
## ROLLBACK
) um bloco de alterações realizadas pela DML.
● Principais comandos:
## COMMIT
## ,
## ROLLBACK
## .
É comum encontrar materiais, principalmente os mais antigos, que
agrupam a DQL (o
## SELECT
) dentro da DML. A razão para a separação
adotada aqui, que é mais moderna, é a clareza: a DQL apenas lê os dados,
enquanto a DML os modifica.
Na prática, para analistas e engenheiros de dados, os comandos de DQL
(SELECT) são, de longe, os mais utilizados no dia a dia, seguidos pelos de
## DML.

Aula 08: Select e From

Vamos ver como o SQL se comporta na prática.

SELECT e FROM:

Toda consulta para extrair dados em SQL começa, invariavelmente, com a
cláusula
## SELECT
. Ela é usada para especificar quais colunas você deseja
que sejam retornadas. Essa cláusula é sempre acompanhada da
## FROM
## ,
que indica de qual tabela os dados devem ser extraídos.
A sintaxe básica é a seguinte:
## SQL
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 13

## None
## None
## None

SELECT nome_da_coluna_1, nome_da_coluna_2
FROM nome_da_tabela;
## ●
## SELECT
: Define as colunas a serem exibidas no resultado.
## ●
## FROM
: Especifica a tabela que serve como fonte dos dados.
Caso seu objetivo seja visualizar todas as colunas da tabela, sem
exceção, você pode usar o caractere curinga
## *
## (asterisco).
## SQL
## SELECT *
FROM nome_da_tabela;
## LIMIT
Ao trabalhar com tabelas que contêm milhares ou milhões de linhas,
geralmente é útil visualizar apenas uma pequena amostra dos dados
para entender sua estrutura. Para isso, usamos a cláusula
## LIMIT
, que
restringe a quantidade de linhas que a consulta irá retornar.
A sintaxe fica assim:
## SQL
## SELECT *
FROM nome_da_tabela
## LIMIT 10;
Neste exemplo, a consulta retornará apenas as 10 primeiras linhas da
tabela.




_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 14

## None
## None

Aula 09: Order by

Agora que você sabe como selecionar colunas de uma tabela, o próximo
passo é aprender a ordenar os resultados. Em muitas análises, exibir os
dados em uma sequência lógica, seja ela crescente ou decrescente, é um
requisito fundamental. Para isso, utilizamos a cláusula
## ORDER BY.
## Ordem Crescente (
## ASC)
Por padrão, a cláusula
## ORDER BY
classifica os resultados em ordem
crescente (de A a Z para textos, ou do menor para o maior para números).
Se desejado, podemos tornar essa instrução explícita usando a
palavra-chave
## ASC
## (ascending).
A sintaxe é a seguinte:
## SQL
SELECT nome_da_coluna_1, nome_da_coluna_2
FROM nome_da_tabela
ORDER BY nome_da_coluna_1 ASC; -- O "ASC" é opcional, pois é o
padrão.
## Ordem Decrescente (
## DESC
## )

Para inverter a ordem e apresentar os resultados de forma decrescente
(de Z a A, ou do maior para o menor), é necessário adicionar a
palavra-chave

## DESC
(descending) ao final da cláusula.

## SQL
SELECT nome_da_coluna_1, nome_da_coluna_2
FROM nome_da_tabela
ORDER BY nome_da_coluna_1 DESC;
## Combinando Cláusulas
As cláusulas SQL são combinadas em uma ordem específica. O

## ORDER BY

é
executado antes do

## LIMIT
. Isso permite, por exemplo, encontrar "os 10
maiores valores" de uma tabela.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 15

## None
## None

Veja o exemplo abaixo, que retorna os 5 produtos mais caros:

## SQL
SELECT nome_do_produto, preco
FROM tabela_de_produtos
ORDER BY preco DESC
## LIMIT 5;
Ordenando por Múltiplas Colunas
É possível ordenar o resultado por mais de uma coluna. Basta separá-las
por vírgula. O SQL irá ordenar primeiro pela primeira coluna e, em caso de
empate, usará a segunda coluna como critério de desempate, e assim por
diante.

## SQL
SELECT nome_do_cliente, estado, cidade
FROM tabela_de_clientes
ORDER BY estado ASC, cidade ASC;
Neste caso, a lista de clientes será ordenada primeiro por estado e, dentro
de cada estado, por cidade.



## Aula 10: Where

Nas aulas anteriores, você aprendeu a selecionar colunas, ordenar
resultados e limitar o número de linhas. Mas como fazer para visualizar
apenas os registros que atendem a uma condição específica?
É aqui que entra a cláusula
## WHERE
. Sua função é filtrar os dados de uma
consulta, de modo que apenas as linhas que atendem a uma ou mais
condições especificadas sejam retornadas.
Vamos conhecer os principais tipos de filtros:
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 16

## None
## None
## None

- Filtro por Valor Exato (
## =
## )
É a forma mais comum, usada quando sabemos exatamente o valor que
procuramos. Para valores de texto, é fundamental que eles estejam entre
aspas simples (
## ' '
## ).
## SQL
## SELECT *
FROM tabela_de_clientes
WHERE cidade = 'São Paulo';
- Filtro com Outros Operadores de Comparação
Podemos usar diversos operadores para comparar valores:
## ●
## <>
ou
## !=
(diferente de)
## ●
## >
(maior que)
## ●
## <
(menor que)
## ●
## >=
(maior ou igual a)
## ●
## <=
(menor ou igual a)

## SELECT *
FROM tabela_de_produtos
WHERE preco >= 100.00;
- Filtro com Operadores Lógicos (
## AND
## /
## OR
## )
É possível combinar múltiplas condições em um mesmo filtro:
## ●
## AND
: Exige que todas as condições sejam verdadeiras.
## ●
## OR
: Exige que pelo menos uma das condições seja verdadeira.

## SELECT *
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 17

## None
## None

FROM tabela_de_produtos
WHERE categoria = 'Eletrônicos' AND preco > 500.00;
- Filtro por Lista de Valores (
## IN
## )
O operador
## IN
é usado para verificar se um valor corresponde a qualquer
um dos valores em uma lista.

## SELECT *
FROM tabela_de_clientes
WHERE estado IN ('SP', 'RJ', 'MG');
- Filtro de Valores Nulos (
## IS NULL
## )
Para encontrar linhas em que uma coluna não tenha nenhum valor
preenchido (ou seja, um valor nulo), usamos a expressão
## IS NULL
## . Para
checar o oposto, usamos
## IS NOT NULL
## .

## SELECT *
FROM tabela_de_pedidos
WHERE data_de_envio IS NULL;



Aula 11: A cláusula Like

Até o momento, você aprendeu a filtrar textos por meio de
correspondências exatas. Contudo, existem formas mais flexíveis de
realizar essa busca, como veremos a seguir.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 18

## None
## None
## None

O operador
## LIKE
é utilizado na cláusula
## WHERE
para buscar um padrão
específico em uma coluna de texto. Ele opera em conjunto com
caracteres curinga (wildcards), que são símbolos especiais para
representar partes desconhecidas de um texto.
Os dois caracteres curinga mais importantes são:
## ●
## %
(Porcentagem): Representa qualquer sequência de caracteres,
incluindo nenhum.
## ●
## _
(Sublinhado): Representa um, e somente um, caractere qualquer.
## SQL
## SELECT *
FROM 'tabelaX'
WHERE 'colunaA' LIKE 'Ca%'
## SQL
## SELECT *
FROM 'tabelaX'
WHERE 'colunaA' LIKE '%ar%'
## SQL
## SELECT
'colunaA'
, 'colunaB' LIKE '%ar%'
, 'colunaC'
, 'colunaD' LIKE 'Ca%'
FROM 'tabelaX'



Aula 12: A cláusula IN


_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 19

## None
## None
## None

Na aula anterior, você aprendeu a filtrar dados por um valor específico (ex:
WHERE categoria = 'Eletrônicos'
). Mas e se precisarmos buscar
produtos de várias categorias ao mesmo tempo? Como podemos fazer
isso de forma eficiente?
Para resolver esse problema, utilizamos o operador
## IN
na cláusula
## WHERE
## .
Ele permite especificar uma lista de valores e retorna todas as linhas em
que uma coluna corresponde a qualquer um dos itens dessa lista. Para o
efeito contrário (buscar por valores que não estão na lista usamos o
## NOT
## IN
## .
O operador
## IN
é uma alternativa mais eficiente e legível do que o uso de
múltiplos operadores
## OR
. Por exemplo, a consulta abaixo:
WHERE estado IN ('SP', 'RJ', 'MG')
É equivalente a
WHERE estado = 'SP' OR estado = 'RJ' OR estado =
## 'MG'
, porém muito mais limpa e performática.
## SQL
## SELECT *
FROM 'tabelaX'
WHERE 'colunaA' IN ('categoria1', 'categoria2')
## SQL
## SELECT
'colunaA'
, 'colunaB'
, 'colunaC' IN ('categoria1', 'categoria2')
, 'colunaD'
FROM 'tabelaX'
## SQL
## SELECT *
FROM 'tabelaX'
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 20

## None
## None

WHERE 'colunaA' NOT IN ('categoria1', 'categoria2')
## SQL
## SELECT
'colunaA'
, 'colunaB'
, 'colunaC' NOT IN ('categoria1', 'categoria2')
, 'colunaD'
FROM 'tabelaX'

## Aula 13: Between


Até agora, aprendemos a filtrar dados por valores específicos (usando
operadores como
## IN
e
## =
). Mas e se quisermos selecionar registros dentro
de um intervalo, como produtos em uma determinada faixa de preço?
Para essa finalidade, utilizamos o operador
## BETWEEN
. Ele seleciona linhas
em que o valor de uma coluna está dentro de um intervalo especificado,
incluindo os valores de início e fim. Seu uso é muito comum para filtrar
faixas de valores numéricos (como preços e quantidades) ou intervalos
de datas.
Para selecionar valores que estão fora de um intervalo, utiliza-se a forma
negativa do operador:
## NOT BETWEEN
## .
A sintaxe básica para filtrar dentro de um intervalo é:
## SQL
SELECT 'colunas'
FROM 'tabelaX'
WHERE 'colunaA' BETWEEN 'min' AND 'max'
## SQL
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 21

## None
## None
## None

## SELECT
'colunaA'
, 'colunaB'
, 'colunaC' BETWEEN 'min' AND 'max'
, 'colunaD'
FROM 'tabelaX'
A sintaxe para filtrar fora de um intervalo é:
## SQL
SELECT 'colunas'
FROM 'tabelaX'
WHERE 'colunaA' NOT BETWEEN 'min' AND 'max'
## SQL
## SELECT
'colunaA'
, 'colunaB'
, 'colunaC' NOT BETWEEN 'min' AND 'max'
, 'colunaD'
FROM 'tabelaX'

## Aula 14: Operadores Aritméticos


Com a base de consultas e filtros já estabelecida, o próximo passo é
aprender a realizar operações matemáticas diretamente sobre os dados.
Os operadores aritméticos do SQL permitem executar cálculos sobre
valores numéricos. Eles podem ser utilizados tanto na cláusula
## SELECT
## ,
para criar colunas calculadas, quanto na cláusula
## WHERE
, para filtrar
dados com base em um resultado.
Os operadores mais comuns são:
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 22




## Símbolo Operação Observação
+ Adição Adiciona valores
- Subtração Subtrai valores
- Multiplicação Multiplica valores
/ Divisão Divide valores
% Módulo Retorna o resto da divisão inteira de um
valor por outro
ABS Valor absoluto Retorna o valor absoluto de um número
ROUND Arredondamento Arredonda um valor para o número de
casas decimais especificado

Retomaremos este assunto mais adiante, quando falarmos sobre funções
nas próximas aulas.

## Aula 15: Operadores Lógicos


Além dos operadores aritméticos, o SQL também possui os operadores
lógicos. Nós já os utilizamos brevemente na cláusula WHERE em aulas
anteriores, mas agora vamos entender em detalhes como eles funcionam.

Os operadores lógicos são usados para combinar múltiplas condições de
filtro, permitindo criar regras mais precisas e específicas para as suas
consultas. Os três operadores lógicos fundamentais em SQL são: AND, OR e
## NOT.

Eles funcionam em conjunto com os operadores de comparação que já
conhecemos (=, >, <, <>), conectando as diferentes partes de um filtro.

O operador AND exige que todas as condições conectadas por ele sejam
verdadeiras para que uma linha seja retornada no resultado.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 23

## None
## None
## None


SELECT 'colunas'
FROM 'tabelaX'
WHERE 'colunaA' = 10 AND 'colunaB' LIKE 'Florian%'

O operador OR é usado para combinar duas ou mais condições, mas,
diferente do AND, ele é mais flexível. Ele retorna um registro se pelo menos
uma das condições especificadas for verdadeira.

SELECT 'colunas'
FROM 'tabelaX'
WHERE 'colunaA' = 5 OR 'colunaA' <> 10

O NOT é usado para negar/inverter uma condição, selecionando todas as
linhas que não atendem ao critério especificado.

SELECT 'colunas'
FROM 'tabelaX'
WHERE NOT 'colunaA' = 'São Paulo'

Aula 16: Group by


A cláusula GROUP BY é uma das ferramentas mais poderosas do SQL. Sua
função é agrupar linhas que têm os mesmos valores em uma ou mais
colunas, transformando-as em uma única linha de resumo.

Ela é usada em conjunto com funções de agregação (como SUM(),
COUNT(), AVG()) para realizar cálculos sobre cada um desses grupos.
Basicamente, você define as categorias pelas quais quer agrupar, e a
função de agregação calcula um valor para cada uma dessas categorias.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 24

## None



## SELECT
'colunaA'
, 'colunaB'
, SUM('colunaC') as soma
FROM 'tabelaX'
GROUP BY 'colunaA'
, 'colunaB'

É fundamental entender a regra principal desta cláusula: toda coluna
listada no SELECT que não está dentro de uma função de agregação (SUM,
COUNT, etc.) obrigatoriamente precisa estar listada na cláusula GROUP BY.


## Aula 17: Having


Nas aulas anteriores, vimos como usar o GROUP BY para criar grupos e o
WHERE para filtrar linhas individuais. Mas surge uma nova pergunta: como
podemos filtrar os próprios grupos depois que os cálculos de agregação
(como SUM ou COUNT) foram feitos?

Para isso, usamos a cláusula HAVING.

O HAVING foi criado especificamente para filtrar os resultados de um
GROUP BY, aplicando condições sobre os valores agregados. Ele é sempre
usado após a cláusula GROUP BY.

A diferença fundamental entre WHERE e HAVING está na ordem de
execução da consulta. O WHERE funciona como o primeiro filtro,
selecionando as linhas individuais da tabela antes que qualquer
agrupamento seja feito. Em seguida, a cláusula GROUP BY pega as linhas
que passaram por esse filtro e as organiza em grupos. Por último, o
HAVING atua como um segundo filtro, mas desta vez sobre os grupos já
formados, permitindo aplicar condições com base nos resultados de
funções de agregação.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 25

## None
## None


## SELECT
'colunaA'
, 'colunaB'
, SUM('colunaC') as soma
FROM 'tabelaX'
GROUP BY 'colunaA'
, 'colunaB'
HAVING soma > 10


## Aula 18: Case When

Até agora, selecionamos e calculamos dados existentes. Mas e se
quiséssemos criar uma nova classificação para eles diretamente na
consulta? Por exemplo, como poderíamos rotular clientes como 'VIP' ou
'Regular' com base em seus gastos?

Para isso, usamos a estrutura CASE WHEN. Ela funciona de forma muito
parecida com a função SE() (ou IF()) do Excel, permitindo aplicar uma
lógica condicional para criar uma nova coluna com resultados
personalizados.

A estrutura CASE WHEN avalia uma lista de condições em sequência e
retorna um valor assim que a primeira condição verdadeira é encontrada.

## SELECT
'colunaA'
, 'colunaB'
## , CASE
WHEN 'condição1' THEN 'resultado1'
WHEN 'condição2' THEN 'resultado2'
ELSE 'resultado3'
END AS 'colunaC'
FROM 'tabelaX'
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 26




## Aula 19: Join


Até agora, todas as nossas consultas, filtros e categorizações foram
aplicados a uma única tabela por vez. Mas e se quisermos, por exemplo,
ver o nome do cliente (que está na tabela clientes) junto com os produtos
que ele comprou (que estão na tabela pedidos)? Para isso, usamos uma
operação do SQL relacional chamada: JOIN.

A cláusula JOIN combina linhas de duas ou mais tabelas com base em
uma coluna de relacionamento em comum, conhecida como chave (por
exemplo, id_cliente). É por meio dessa chave que o SQL sabe quais linhas
de uma tabela correspondem às da outra. A condição que estabelece
essa ligação é especificada na cláusula ON.

Para entender visualmente os diferentes tipos de JOIN e como eles
funcionam, a melhor ferramenta é o Diagrama de Venn, que vem da
Teoria dos Conjuntos.

Figura: Diagrama de Veen.
Fonte: adaptada por Indicium Academy.


A sintaxe básica para realizar um join é:

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 27

## None
## None
## None

## SELECT
## 'tabela1'.'colunas'
## , 'tabela2'.'colunas'
FROM 'tabela1'
JOIN 'tabela2' ON 'tabela1'.'colunaX' = 'tabela2'.'coluna X'

Existem diferentes tipos de JOIN, e a escolha depende do resultado que
queremos obter. Vamos conhecer os principais:

## ●
(INNER) JOIN: Retorna apenas os registros que possuem
correspondência em ambas as tabelas. Pense na interseção dos
dois círculos do Diagrama de Venn.

## SELECT
## 'tabela1'.'colunas'
## , 'tabela2'.'colunas'
FROM 'tabela1'
INNER JOIN 'tabela2' ON 'tabela1'.'colunaX' = 'tabela2'.'colunaX'

## ●
LEFT (OUTER) JOIN: Retorna todos os registros da tabela da esquerda
(a primeira mencionada, FROM) e os registros correspondentes da
tabela da direita. Se não houver correspondência na direita, os
campos virão como nulos.

## SELECT
## 'tabela1'.'colunas'
## , 'tabela2'.'colunas'
FROM 'tabela1'
LEFT JOIN 'tabela2' ON 'tabela1'.'colunaX' = 'tabela2'.'colunaX'

## ●
RIGHT (OUTER) JOIN: É o oposto do LEFT JOIN. Retorna todos os
registros da tabela da direita (a segunda mencionada, JOIN) e os
correspondentes da tabela da esquerda.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 28

## None
## None
## None


## SELECT
## 'tabela1'.'colunas'
## , 'tabela2'.'colunas'
FROM 'tabela1'
RIGHT JOIN 'tabela2' ON 'tabela1'.'colunaX' = 'tabela2'.'colunaX'

## ●
FULL (OUTER) JOIN: Retorna todos os registros de ambas as tabelas.
Se houver correspondência, as informações são combinadas. Se
não, as colunas da tabela sem correspondência ficam nulas.

## SELECT
## 'tabela1'.'colunas'
## , 'tabela2'.'colunas'
FROM 'tabela1'
FULL OUTER JOIN 'tabela2' ON 'tabela.'colunaX' = 'tabela2'.'colunaX'

Além dos mais comuns, existem outros tipos para casos de uso
específicos:

## CROSS JOIN

Combina cada linha da primeira tabela com cada linha da segunda,
criando um produto cartesiano. Se a Tabela A tem 10 linhas e a Tabela B
tem 5, o resultado terá 50 linhas. Não se utiliza a cláusula ON.

## SELECT
## 'tabela1'.'colunas'
## , 'tabela2'.'colunas'
FROM 'tabela1'
CROSS JOIN 'tabela2'

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 29

## None

O CROSS JOIN pode ser útil em muitos casos, mas use com cuidado! Este
JOIN pode gerar um volume de dados imenso, impactando
negativamente o desempenho da consulta.

## SELF JOIN

Já o SELF JOIN é a combinação da tabela com ela mesma. Essa
abordagem é útil quando uma única tabela contém registros que se
relacionam entre si, como uma hierarquia de funcionários e seus
respectivos gestores. Na prática, o SELF JOIN é usado para extrair essas
informações hierárquicas, comparar valores entre diferentes linhas,
identificar dados duplicados, entre outras análises.

## SELECT
'tabela1'.'colunaA'
, 't2'.'colunaA'
, 'tabela1'.'colunaB'
FROM 'tabela1'
JOIN 'tabela1' as 't2' ON 'tabela1'.'colunaX' = 'tabela2'.'colunaX'

Assim como o CROSS JOIN, o SELF JOIN deve ser utilizado com cautela, pois
uma lógica de ligação incorreta pode gerar duplicações e resultados
inesperados.

## Aula 20: Union

Nas aulas anteriores, vimos como o JOIN combina tabelas, adicionando
novas colunas para criar uma visão de dados mais larga, de forma
horizontal.

Mas e se o nosso objetivo for diferente? E se, em vez de adicionar colunas,
quisermos empilhar os resultados de duas ou mais consultas, uma sobre
a outra, para criar uma lista única e mais longa, de forma vertical?

Para resolver esse problema, usamos o operador UNION.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 30

## None

A cláusula UNION combina o resultado de duas ou mais consultas SELECT
em um único conjunto de resultados. Pense nela como uma forma de
"anexar" uma tabela ao final da outra, aumentando o número de linhas.

Mas para que isso seja possível é necessário que as tabelas tenham
exatamente as mesmas colunas. A sintaxe do UNION é apresentada
abaixo:

## SELECT
## 'colunas'
FROM 'tabela1'
## UNION
## SELECT
## 'colunas'
FROM 'tabela2'

É importante ressaltar que o UNION pode ser muito custoso em termos de
desempenho, especialmente se estivermos falando de tabelas muito
grandes. Por isso devemos ser cautelosos ao utilizar o UNION.

## Aula 21: Funções


Certo! Agora já sabemos consultar dados, filtrar, misturar e juntar tabelas.
Mas e se nós quiséssemos realizar cálculos entre as colunas?
E se precisássemos limpar a base de dados para excluir outliers ou dados
inseridos de forma errada?
Como será que poderíamos fazer?
Para isso poderíamos utilizar as diferentes funções disponíveis em SQL.


As funções dentro da linguagem SQL são procedimentos que aceitam um
ou mais argumentos (inputs, valores de entrada) e retornam um resultado
(output, valor de saída). Elas podem ser utilizadas em expressões ou
consultas para executar cálculos ou manipular dados. Além de serem
bastante úteis para simplificar as consultas e reduzir a redundância no
código.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 31


Existem três tipos básicos de funções:

- Funções de Agregação: Já falamos sobre elas anteriormente, mas
vamos explicar melhor. Uma função desse tipo é utilizada para
calcular um valor a partir de um conjunto. As Funções de Agregação
mais comuns são: contagem (COUNT), soma (SUM), média (AVG),
mínimo (MIN) e máximo (MAX).

- Funções Escalares: As funções escalares, por sua vez, são utilizadas
para manipular dados individualmente. Elas servem para padronizar
tipo de escrita, para remover espaço, para concatenar colunas, etc.
Assim sendo, as funções mais comuns são: UPPER, LOWER, TRIM ,
CONCAT, etc.

- Funções Analíticas: essas funções são usadas para realizar cálculos
avançados em um conjunto de dados. Os exemplos de funções
analíticas incluem funções de janela, como RANK, DENSE_RANK, LAG,
LEAD, além de outras funções como FIRST_VALUE, LAST_VALUE,
STDDEV, VAR, COVAR, PERCENT_RANK, CUME_DIST, etc.

Vale lembrar que cada banco de dados pode ter um conjunto específico
de funções. Além disso, também podemos desenvolver as nossas próprias
funções, personalizando o nosso código para atender a demandas mais
específicas.

Nós vamos ver em maior detalhe cada tipo de função nas próximas aulas.
Não perca!

Aula 22: Funções agregadas

As funções agregadas são essenciais para quem é data analyst. Elas
permitem reduzir ou agregar uma série de campos para um único valor
ou alguns poucos valores.

Embora seu funcionamento seja muito simples, quando analisadas
individualmente, a sua combinação com os demais comandos do SQL
permite realizar consultas extremamente poderosas em grandes volumes
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 32


de dados.

A maioria dos bancos de dados relacionais suportam essas funções de
agregação, e elas são amplamente utilizadas em consultas SQL. É
importante notar que essas funções podem ser usadas em colunas
numéricas ou de texto, desde que não contenham valores nulos. Além
disso, é possível usar a cláusula GROUP BY para agrupar os resultados de
uma consulta com base em uma ou mais colunas.

As principais funções de agregação em SQL incluem:

- SUM: calcula a soma dos valores em uma coluna numérica.
- AVG: calcula a média dos valores em uma coluna numérica.
- COUNT: conta o número de linhas em uma tabela ou grupo de
tabelas.
- MAX: retorna o valor máximo em uma coluna.
- MIN: retorna o valor mínimo em uma coluna.
## .

Aula 23: Funções escalares

Na aula anterior vimos quais são as principais funções de agregação e
como utilizá-las. Nesta aula veremos o segundo tipo, as funções escalares.

As funções escalares são aquelas utilizadas para manipular valores
individuais de uma coluna ou expressão.

Aqui estão alguns dos principais tipos de funções escalares:

- Funções de texto: são usadas para manipular strings. Exemplo:
UPPER, LOWER, SUBSTRING, TRIM e etc.

- Funções numéricas: são usadas para manipular valores numéricos.
Exemplo: ROUND, ABS, CEILING, FLOOR e etc.

- Funções de data e hora: são usadas para manipular valores de data
e hora. Exemplo: NOW, DATEADD, DATEPART, CONVERT e etc.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 33



- Funções de conversão: são usadas para converter um tipo de dados
em outro. Exemplo: CAST, COALESCE, NULLIF e etc.

Vale lembrar que cada banco de dados pode ter sua própria lista de
funções escalares disponíveis. É importante consultar a documentação do
banco de dados utilizado para consultar se existe a função e qual a sua
sintaxe.


Aula 24: funções analíticas

Nas aulas anteriores vimos dois tipos de função: as funções de agregação
e as funções escalares. Nesta aula vamos conhecer quais são as funções
analíticas e como elas são utilizadas.

As funções analíticas são usadas para realizar cálculos avançados em um
conjunto de dados, usando funções de agregação para resumir e
classificar dados. Elas permitem que você execute cálculos agregados em
subconjuntos de dados, geralmente definidos por uma cláusula OVER.

Ao contrário das funções de agregação regulares, que retornam um único
valor agregado para um conjunto de dados inteiro, as funções analíticas
retornam um valor agregado para cada linha em um conjunto de dados,
com base nas regras especificadas pelo usuário.

As funções analíticas SQL são usadas com mais frequência em consultas
para elaboração de relatórios, análises de dados e consultas de BI.

Os principais tipos de funções analíticas são:

- Funções de janela (Window functions): as funções de janela
permitem executar cálculos agregados definidos por uma cláusula
OVER. Algumas funções de janela comuns incluem RANK,
DENSE_RANK, ROW_NUMBER, LAG e LEAD.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 34


- Funções de agregação analítica (Analytic aggregate functions):
essas funções são semelhantes às funções de agregação comuns,
como SUM, AVG, COUNT, MAX e MIN, mas são usadas com a cláusula
OVER para calcular valores agregados nos subconjuntos de dados.

- Funções de deslocamento (Offset functions): as funções de
deslocamento permitem que você acesse linhas específicas de uma
tabela com base em um deslocamento a partir da posição atual. As
funções mais comuns são FIRST_VALUE e LAST_VALUE.

- Funções de proporção (Ratio functions): as funções de proporção
permitem que você calcule proporções entre valores em um
subconjunto de dados, sendo que as funções mais comuns incluem
PERCENT_RANK e CUME_DIST.

- Funções de agregação estatística (Statistical aggregate functions):
essas funções são usadas para realizar cálculos estatísticos como
desvio padrão (STDDEV), variância (VAR) e covariância (COVAR).

Lembrando que diferentes bancos de dados podem ter funções diferentes
disponíveis. As funções analíticas são frequentemente usadas em
consultas complexas e com cálculos mais sofisticados, possibilitando
obter insights mais profundos sobre os dados.

Dentre as funções analíticas a mais utilizada é a função de janela
(Window function).

Estas funções possibilitam que cálculos sejam feitos a um conjunto
específico de linhas (o que seria a “janela”) que são definidas por uma
cláusula OVER, podendo ser dividida em partições com a cláusula
PARTITION BY, e apresentadas de forma ordenada com um ORDER BY.

## Simplificando:
- O OVER vai determinar a janela de dados sobre a qual a função vai ser
aplicada.
- O PARTITION BY vai dividir essa janela em subconjuntos.
- O ORDER BY vai ordenar as linhas dentro dos subconjuntos criados
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 35

## None


## SELECT
'colunaA'
, 'colunaB'
, AVG('colunaC') OVER (PARTITION BY 'colunaB' ORDER BY 'colunaA') as media
FROM 'tabelaX'

As funções de janela são usadas para calcular totais cumulativos,
classificações, médias móveis e outras operações analíticas em um
conjunto de dados. Elas são úteis para calcular valores agregados em um
subconjunto de linhas em uma consulta, sem a necessidade de usar uma
subconsulta ou uma junção.

Algumas das funções de janela mais comuns incluem:
- ROW_NUMBER(): atribui um número sequencial a cada linha de uma
consulta.
- RANK(): atribui um número de classificação a cada linha de uma
consulta com base no valor da coluna especificada.
- DENSE_RANK(): atribui um número de classificação a cada linha de
uma consulta com base no valor da coluna especificada, mas as
classificações podem ser "compactadas" se houver valores
duplicados.
- LAG(): retorna o valor da coluna da linha anterior no conjunto de
resultados.
- LEAD(): retorna o valor da coluna da próxima linha no conjunto de
resultados.
- SUM(), AVG(), MAX(), MIN(): calcula um valor agregado em um
conjunto de linhas definido pela cláusula OVER.


Aula 25: funções de manipulação textual

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 36

## None
## None

Algumas das mais usadas funções escalares são as funções de texto.
Existem inúmeras funções de formatação de texto em SQL. Algumas delas
só estão disponíveis em certos tipos de SQL.

Veremos a seguir as principais manipulações de texto que você irá
precisar.

Use UPPER() para deixar todo o texto em caixa alta e LOWER() para
deixá-lo em caixa baixa.

## SELECT
UPPER(col_A)
,LOWER(col_B)
FROM tabela_X

Para deixar apenas a primeira letra maiúscula, use INITCAP(). Contudo,
essa função não está disponível em certos sistemas. Se esse for o caso,
uma outra forma de realizar isso é combinar as funções UPPER() e LOWER()
com a função SUBSTR(text, início, tamanho), uma função versátil que
retorna uma parte específica de um texto.

● SUBSTR(col_A, 2, 1) retorna apenas o 2º caractere.
● SUBSTR(col_A, 2) retorna todo o texto a partir do segundo caractere.


## SELECT
UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2))
FROM tabela_X

A função SUBSTR() também é uma boa alternativa às funções LEFT() e
RIGHT(). Essas funções retornam o número de caracteres especificados,
mas elas também não estão presentes em todos os sistemas.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 37

## None
## None
## None

## Exemplo:

SELECT RIGHT(‘Dados são o novo petróleo’, 8)
>> ‘Petróleo’

Outra manipulação útil é a substituição de textos de uma coluna
utilizando a função REPLACE(), que busca por uma sequência de
caracteres específica e a substitui por outra. Se o texto a ser buscado no
segundo argumento for uma parte do texto, a função irá substituir
somente esta parte. Desse modo, é possível substituir, ‘Vendas Executive’,
por ‘Sales Executive”.

A função REPLACE() é útil para remover partes de um texto. Por exemplo,
pegar apenas o usuário de endereços de email.

SELECT REPLACE(col_A, '@company.com', '')
FROM TabelaX

Em um cenário mais avançado, é possível aninhar as funções para definir
mais de uma condição. No exemplo abaixo,  buscamos por dois textos da
col_A e os substituímos por textos que atendem um padrão.

SELECT REPLACE(REPLACE(col_A, 'txto_erad948', 'Texto_Correto_948')
,'txt_err974', 'Texto_Correto_974'
## )
FROM TabelaX

Para remover apenas caracteres indesejados do início e fim dos textos, a
função TRIM() é bastante útil. As keywords ‘leading’ e ‘trailing’ especificam,
respectivamente, início e fim do texto.

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 38

## None
## None
## None

## SELECT
TRIM(‘#’ from col_A)
TRIM(leading '#' from col_B) -- remove apenas no início
FROM TabelaX


Uma função bastante popular em manipulações de texto com SQL que
envolvem separar quebrar ou separar partes de um texto é a split_part().
A função usa um delimitador para separar o texto em n partes. A
quantidade de partes depende da quantidade de delimitadores.

Fica fácil entender o seu uso ao usar uma coluna de email. Ao usarmos ‘.’
como separador, obtemos 4 partes, uma vez que o padrão do email é
‘Claudio.Santos@empresa.com.br’. Contudo, se usarmos ‘@’ como
separador, será retornado apenas 2 partes


## SELECT
split_part(email, '.', 2)
FROM TabelaX
>> .Santos@empresa
>> .Munhoz@empresa
>> .Ferreira@empresa



## SELECT
split_part(email, '.', 4)
FROM TabelaX
>> br
>> br
>> br
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 39

## None



Assim, é possível obter o nome do usuário de email, utilizando o código:


## SELECT
split_part(email, '@', 1)
FROM TabelaX
>> Claudio.Santos
>> Davi.Munhoz
>> Eliza.Ferreira


Aula 26: Criação e manutenção das Tabelas e Views



Nas aulas anteriores nós vimos conceitos importantes sobre bancos de
dados e conhecemos os principais tipos existentes.

Vimos também como funciona a linguagem SQL, suas funções e tivemos
alguns exemplos da sua utilização. Mas uma coisa é fato. Precisamos
manter a ordem para facilitar nosso entendimento e manutenções no
futuro.

Conforme vamos evoluindo nas nossas análises vamos percebendo a
necessidade de manter os códigos organizados, fáceis de ler e entender. A
criação e manutenção de tabelas e views são tarefas importantes.

Para facilitar a criação de consultas complexas, e consequentemente de
tabelas e views, podemos utilizar as chamadas CTEs (Common Table
Expressions). As CTEs são uma forma de organizar o código e salvar os
resultados de consultas para serem usados posteriormente dentro de
outra consulta.

A estrutura básica de uma CTE é:

_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 40

## None
## None
## None

WITH nome_da_cte AS (
## SELECT
## 'colunas'
FROM 'tabelaX'
## )

Para executar a CTE criada basta chamá-la em um novo SELECT ao final
do código.

WITH nome_da_cte AS (
## SELECT
## 'colunas'
FROM 'tabelaX'
## )
## SELECT *
FROM nome_da_cte

Também é possível criar diversas CTEs em sequência. Note que uma CTE
pode ser usada tanto como parte de outra (FROM) quanto como na
consulta final.

WITH cte1 AS (
## SELECT
## 'colunas'
FROM 'tabelaX'
## )
, cte2 AS (
## SELECT
## 'colunas'
FROM 'tabelaY'
## )
cte3 AS (
## SELECT
cte1.'colunas'
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 41


, cte2.'colunas'
FROM cte1
JOIN cte2 ON cte1.colunaA = cte2.colunaA
## )
## SELECT *
FROM cte3

O conhecimento sobre CTEs dá a capacidade de criar consultas
complexas em SQL e gerar análises avançadas para a tomada de decisão
ou transformação de dados com maior robustez.

As CTEs são uma excelente solução quando se trabalha em equipe e de
forma colaborativa em um código. Isso porque torna mais compreensível,
e muitas vezes legível, o código que está sendo desenvolvido.

Para os fins de análise de dados, o custo em horas de trabalho para
entender uma consulta complexa feita por outra pessoa é, na grande
maioria dos casos, maior que a perda de alguns segundos ou minutos
para rodar uma consulta ineficiente.

A finalidade de dividir a criação da tabela em diferentes CTEs é para
facilitar a manutenção do código. Dessa forma é mais simples de
buscarmos por possíveis inconsistências ou problemas na execução dos
comandos.

Uma dica bastante eficiente: comente o que cada CTE vai executar, em
especial naquelas que envolvem cálculos mais específicos, regras de
negócio, etc. Quando você, ou outra pessoa, precisar revisitar o código
encontrará uma breve descrição do que é feito em cada uma das etapas.


Aula 27: Gestão de usuários


Nem sempre queremos que todos os usuários tenham acesso irrestrito às
tabelas do banco de dados ou que possam executar qualquer tipo de
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 42


operação. Para resolver esse problema, existem mecanismos para
gerenciar os usuários que acessam o banco.
Esse gerenciamento envolve a criação, a configuração e a administração
de contas de usuário. Tais contas são utilizadas para controlar o acesso
aos dados armazenados, bem como para permitir que os usuários
executem tarefas específicas, como criação, alteração e consulta de
dados, entre outras.
Para implementar a gestão de usuários, algumas etapas são necessárias,
começando pela criação das contas. Cada conta é utilizada para
autenticar e autorizar o acesso ao banco de dados, sendo identificada por
um nome de usuário exclusivo e associada a um conjunto de permissões
e privilégios.
Alguns sistemas de gerenciamento de banco de dados (SGBDs) utilizam a
figura dos papéis (roles). Os papéis são conjuntos de privilégios que
podem ser concedidos a um ou mais usuários, o que simplifica e facilita a
administração dessas permissões.
Uma vez definidos os usuários ou papéis, o próximo passo é atribuir os
privilégios. Os privilégios são permissões concedidas a uma conta de
usuário ou a um papel para executar tarefas específicas em um banco de
dados, como, por exemplo, criar ou excluir tabelas ou apenas realizar
consultas.
Os comandos mais comuns para essa gestão incluem
## CREATE USER
## ,
## ALTER USER
e
## DROP USER
, para criar, modificar e excluir contas,
respectivamente. Os comandos
## GRANT
e
## REVOKE
são usados para
conceder e revogar privilégios, enquanto
## CREATE ROLE
## ,
## ALTER ROLE
e
## DROP
## ROLE
gerenciam os papéis.
Desta forma, é possível controlar o acesso aos dados de forma granular,
garantindo que apenas usuários autorizados possam interagir com
informações específicas.




_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 43


Aula 28: Conceitos de melhoria de desempenho


Quando estamos desenvolvendo nosso modelo de dados podemos criar
coisas muito complexas e que com o passar do tempo, e com o volume
de dados crescendo, vão se tornando ineficientes. A partir disso é
necessário que façamos melhorias no código para otimizar as nossas
consultas. Existem diversas maneiras de fazermos isso e algumas delas
incluem:

Criar índices: Os índices permitem que o banco de dados encontre
rapidamente os registros que correspondem à consulta. Você pode criar
índices nas colunas usadas com mais frequência.

Ajustar o esquema do banco de dados: O esquema do banco de dados
pode ter um impacto significativo no desempenho das consultas. Para
diminuir esses impactos o ideal é que as tabelas estejam normalizadas e
otimizadas para evitar consultas excessivamente complexas.

Uso do WHERE e JOIN: Use as cláusulas WHERE e JOIN de forma eficiente
para limitar o número de registros retornados pela consulta. Isso reduzirá
o tempo necessário para recuperar os resultados.

Evitar operações em larga escala: Operações em larga escala, como
SELECT * e ORDER BY, podem ser muito demoradas e consumir muitos
recursos do servidor. Tente limitar o número de colunas selecionadas e
evite ordenar grandes conjuntos de dados sempre que possível. Ao utilizar
as CTEs você pode trazer para a consulta apenas as colunas que são
realmente necessárias, evitando processamento desnecessário.

Monitorar o desempenho da consulta: Use ferramentas de monitoramento
para identificar consultas que estão demorando mais tempo para serem
executadas e, em seguida, otimize-as. O monitoramento também pode
ajudar você a identificar problemas de desempenho mais amplos no
servidor de banco de dados.

Uma boa forma de monitorar o desempenho das consultas é utilizando o
EXPLAIN. Este comando serve para visualizar o plano de execução de uma
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 44

## None

consulta. O seu resultado inclui informações sobre a estratégia de acesso
aos dados usada pelo banco de dados para gerar a consulta, incluindo o
tipo de acesso a índice, o método de junção e a ordem de classificação. O
resultado também inclui informações sobre o custo estimado da consulta
em termos de recursos de hardware, como CPU e memória.

O comando EXPLAIN é útil nesse processo de melhoria de desempenho,
pois permite visualizar como o banco de dados planeja executar uma
consulta e identificar pontos de melhoria de desempenho. Ao examinar o
plano de execução, você pode identificar as etapas que estão
consumindo mais recursos e determinar se a consulta está usando
índices de maneira eficaz.

Em resumo, o EXPLAIN é uma ferramenta útil para analisar e otimizar o
desempenho de consultas, fornecendo informações detalhadas sobre a
estratégia de acesso aos dados e o custo estimado para tal.

A sintaxe básica do EXPLAIN é a seguinte:

EXPLAIN SELECT 'colunas'
FROM 'tabelaX'
WHERE 'condicoes'

Utilizar o cache de consultas: Muitos bancos de dados possuem sistemas
de cache de consultas que armazenam resultados de consultas
frequentes em memória. Isso pode melhorar significativamente o
desempenho de consultas repetidas.

Otimizar consultas com funções agregadas: Se você estiver usando
funções agregadas como SUM, AVG ou COUNT em suas consultas, tente
usar índices para melhorar o desempenho.

No entanto, cada caso é único e pode exigir abordagens diferentes. É
importante estar sempre atento ao desempenho do banco de dados e
realizar ajustes de acordo com as necessidades.
_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 45



_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 46


## Material Complementar


## Tipo: ☐ Site  [x] Livro   ☐ Vídeo   ☐ Leitura   ☐ Filme   ☐ Visite
Título:   Learning SQL de Alan Beaulieu
Descrição: Este livro é um guia prático para aprender SQL, com exemplos práticos
que ajudam a entender como usar a linguagem para recuperar, atualizar e
gerenciar dados em bancos de dados relacionais.
## Link:
https://pt.slideshare.net/slideshow/learning-sql-by-alan-beaulieupdf-fade/2629
## 81856


## Tipo: [x] Site   ☐ Livro   ☐ Vídeo   ☐ Leitura   ☐ Filme   ☐ Visite
Título:  GitHub: sql_book
Descrição: Repositório com vários códigos do livro “SQL para Análise de Dados”.
Link: https://github.com/cathytanimura/sql_book


## Tipo: [x] Site   ☐ Livro   ☐ Vídeo   ☐ Leitura   ☐ Filme   ☐ Visite
Título:  SQL Cheat Sheet
Descrição: Artigo e Infográfico com as principais funções em SQL básicas e
intermediárias com exemplos de aplicações
Link: https://www.geeksforgeeks.org/sql-cheat-sheet/


## Tipo: ☐ Site   ☐ Livro   ☐ Vídeo   [x] Leitura   ☐ Filme   ☐ Visite
Título:  WINDOWS FUNCTIONS: Desvendando o Poder das Funções de Janela no
## SQL.
Descrição: Artigo sobre uma das técnicas avançadas mais úteis para análise de
dados com SQL;
## Link:
https://medium.com/comunidadeds/windows-functions-desvendando-o-poder
-das-fun%C3%A7%C3%B5es-de-janela-no-sql-805cf12bfff2



_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 47



## Referências
AMAZON WEB SERVICES. What is a database? [online] Disponível em:
https://aws.amazon.com/pt/what-is/database/. Acesso em: 21 jun. 2023.

KONDADO. Banco de dados: o que é e quais são os principais tipos?
[online] Disponível em:
https://kondado.com.br/blog/blog/2022/09/13/banco-de-dados-o-que-e
-e-quais-sao-os-principais-tipos/. Acesso em: 21 jun. 2023.

ORACLE. O que é banco de dados? [online] Disponível em:
https://www.oracle.com/br/database/what-is-database/. Acesso em: 21
jun. 2023.

ROCKCONTENT.COM. Banco de dados: o que é, tipos e importância dele no
site da sua empresa. [online] Disponível em:
<https://rockcontent.com/br/blog/banco-de-dados/>. Acesso em: 21 jun.
## 2023.

TANIMURA, Cathy. SQL para Análise de Dados. São Paulo: Ed. Novatec, 2022.





_____________________________________________________________________________________________________________________________________

Este documento é de uso exclusivo dos clientes e parceiros da Indicium Tecnologia de Dados LTDA
e não deve ser reproduzido ou compartilhado sem autorização expressa da Indicium.
## 48