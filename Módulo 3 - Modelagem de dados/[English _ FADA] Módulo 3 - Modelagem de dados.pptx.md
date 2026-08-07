

Data analysis Module 3 - Data modeling 





###### Hello! 

My name is Renata. I have been at Indicium for three years, working as an analytics engineer, and I am currently Tech Lead for data analysis. 







<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

###### **WELCOME!** 

3 



## Data modeling **Index** 

- Introduction to analytical databases 

- ETL Concepts 

- Data warehouses vs data lakes vs data lakehouse 



- Data modeling 

- Fact Tables 

- Dimension Tables 

- Bridge Tables 

- Best practices for using analytical databases for data analysts 



4 





###### **INTRODUCTION TO ANALYTICAL DATABASES** 

5 

###### INTRODUCTION TO ANALYTICAL DATABASES 



<!-- Start of picture text -->
:<br>z<br><!-- End of picture text -->

Each database transaction as a document, a contract... 



<!-- Start of picture text -->
[aaa] [Smee] [eames] [eee] [arena]<br>categoryee coegey.romeid  | |reProdame [Ssurpieiaecon.| eesfsemployeename id | ieee[isemployeeid<br>ne quarry pean fo -—_] ares ate ctcouneny |<br>pawn25con ues. stock || |"edEs.regon |Qhireeam”ene dace Va|actenion.ia |<br>a / [se homepage 7 |eearlcountry. -<br>cy me Een<br>set a =<br>[_Sesomers] asemplyee<br>eee estore<br>=<br><!-- End of picture text -->

6 

###### INTRODUCTION TO ANALYTICAL DATABASES 





**System temporarily unavailable** 

7 

###### INTRODUCTION TO ANALYTICAL DATABASES 







<!-- Start of picture text -->
a (a pat Gi et | =a gee ae =<br>E<br>F<br>=ASa7 C D<br>1p a A fe!ae (|WE B gs ate<br><!-- End of picture text -->

8 

###### INTRODUCTION TO ANALYTICAL DATABASES 

**OLTP: On-Line Transactional Processing** 





<!-- Start of picture text -->
7 —-<br>A ee .<br>nS -<br>-— a yr<br>| oo mer.<br><!-- End of picture text -->

9 

##### INTRODUCTION TO ANALYTICAL DATABASES **<mark>PROCESSING</mark>** 

**OLAP: On-Line Analytical Processin g** 





<!-- Start of picture text -->
:<br>A rT ’ wa =<br>> — 9% »<br>ms / ; ——— a =<br>i<br>Ne | maar ) ~<br>H — Ws<br>Wee. ey 7<br><!-- End of picture text -->

10 



<!-- Start of picture text -->
Consivis<br><!-- End of picture text -->

##### INTRODUCTION TO ANALYTICAL DATABASES **<mark>PROCESSING</mark>** 



<!-- Start of picture text -->
g<br>g<br>3<br>2—<br>6<br>is)<br>fo]<br>8&2<br>Fya<br>°<br>3g2ro ( ou rr )<br>—<br>a<br>Ler Escrever<br>Fluxo trabalho<br><!-- End of picture text -->



11 

##### INTRODUCTION TO ANALYTICAL DATABASES **<mark>STORAGE</mark>** 



<!-- Start of picture text -->
L 1234 Margarida de Jesus margarida65@mail.com PF 01/05/2015 10/08/1984, Sdo Paulo SP J<br>1235 Joanada Siva —=Ssjslva@malicom=—=SSPF~OC*«*«tROSIBON«=SC*C«NANGOG~—=Loncrina’  ==<br>1236 Gabriela Oliveira gabi_oliveira@mail.com Pr 02/05/2015, 31/01/2000 Piracicaba sP<br>1237 Roberto Garcia garcia_bbto@mail.com PF 03/05/2015, 04/10/1978 Sao Paulo SP<br>1238 Felipe Novalis {felipe novais@mail.com PF 03/05/2015 22/06/1998 Rio de Janeiro RJ<br><!-- End of picture text -->



<!-- Start of picture text -->
<=<br><!-- End of picture text -->

[‘1234’,’Margarida de Jesus’, ‘margarida65@mail.com’,’PF’, ‘01/05/2015’,’10/08/1984’,’São Paulo’,’SP’], 

[‘1235’,’Joana da Silva’, ‘j.silva@mail.com’,’PF’, ‘02/05/2015,’25/11/1995’,’Londrina,’PR’] 

Velocity 

Integrity 

12 



<!-- Start of picture text -->
INTRODUCTION TO ANALYTICAL DATABASES<br>STORAGE<br>select<br>    count (“Data Inclusão”)<br>    , extract(month from  “Data Inclusão”)  as month<br>from clientes<br>where  estado =  ‘PR’<br>group by extract(month from “Data Inclusão”)<br>[‘1238’,’Felipe Novais’, ‘felipe.novais@mail.com’,’PF’, ‘03/05/2015’,’22/06/1998’,’Rio de Janeiro’,’RJ’],<br>[‘1239’,’Joaquim Pereira, ‘Joaquim@email.com’,’PF’, ‘03/05/2015,’12/04/1979’,’Campinas,’SP’]<br>[‘1234’,’Margarida de Jesus’, ‘margarida65@mail.com’,’PF’, ‘01/05/2015’,’10/08/1984’,’São Paulo’,’SP’],<br>[‘1235’,’Joana da Silva’, ‘j.silva@mail.com’,’PF’, ‘02/05/2015’,’25/11/1995’,’Londrina’,’PR’]<br>Useless<br>information<br>13<br><!-- End of picture text -->



<!-- Start of picture text -->
(Cae<br>INTRODUCTION TO ANALYTICAL DATABASES<br>STORAGE<br>i Tipo Cliente | Data inclusio | Data Nascimento | Cidade Estado<br>1234 Margarida de Jesus _margarida65@mail. com Pr | 01/05/2015 | 1010811984 So Paulo | se |<br>1236 Joana da Silva jsiiva@mail.com pr | o5/2015 25/11/1995 —_Londrina | pe<br>1236 Gabriela Oliveira <gabi_oliveira@mall.com pr — | camsr2015 | 31/01/2000 —_—Pracicaba | se<br>1237 Roberto Garcia garcia_bbto@mail.com pe | osiosr2015 | 04/10/1978 So Paulo | se<br>1238 Felipe Novais felipe novais@mail.com Pen poansanis | ee key |<br>1239 Joaquim Pereira Joaquim@email com = —ae 1210811979 Cary =z —|<br>Nome<br>Data Inclusão<br>Email _ = [‘01/05/2015’,’02/05/2015’, ’02/05/2015’,<br>‘03/05/2015’,‘03/05/2015’,‘03/05/2015’,...]<br>SenenSEE88 feesSeee8<br>SEne8 seee8<br>S088 Seeee . Estado<br>Tipo Cliente =eeen, 2o00<br>tere} ar<br>[‘SP’,’RJ’, ’PR’,’SC’,...]<br><!-- End of picture text -->

14 



<!-- Start of picture text -->
Consist<br>INTRODUCTION TO ANALYTICAL DATABASES<br>STORAGE<br>select<br>    count( “Data Inclusão”)<br>    , extract(month from  “Data Inclusão”)  as month<br>from clientes |}, ee<br>where  estado =  ‘PR’<br>LC] eee<br>group by extract(month from “Data Inclusão”)<br>[‘01/05/2015’,’02/05/2015’, ’02/05/2015’, ‘03/05/2015’,‘03/05/2015’,‘03/05/2015’,...]<br>[‘SP’, ’PR’, ‘SP’, ‘SP’, ’RJ’, ‘SP’,...]<br><!-- End of picture text -->

15 



<!-- Start of picture text -->
INTRODUCTION TO ANALYTICAL DATABASES<br>Tipo de tabela Particionada<br>PARTITIONING<br>Particionada por DAY<br>Particionada no campo -PARTITIONTIME @<br>Expiragdo da particgo. As partigdes no expiram<br>|<br>Filtro de particao Nao obrigatério<br>Data Inclusão<br>Estado<br>[‘01/05/2015’] [‘SP’]<br>Data Inclusão<br>[‘01/05/2015’,’02/05/2015’,  [’02/05/2015’, ’02/05/2015’] [’PR’, ’SP’]<br>’02/05/2015’,‘03/05/2015’,<br>‘03/05/2015’,‘03/05/2015’,<br>‘03/05/2015’,‘04/05/2015’,  [‘03/05/2015’,‘03/05/2015’,<br>[‘SP, ‘RJ’, ’SP’, ‘PR’]<br>‘04/05/2015’,‘04/05/2015’,  ’03/05/2015’,‘03/05/2015’]<br>‘04/05/2015’,‘04/05/2015’,...]<br>[‘04/05/2015’,‘04/05/2015’,<br>‘04/05/2015’,‘04/05/2015’,  [‘SP’, ‘AM’, ’RJ’, ‘SP’, ‘SP’,...]<br>‘04/05/2015’,...]<br>16<br><!-- End of picture text -->



<!-- Start of picture text -->
INTRODUCTION TO ANALYTICAL DATABASES<br>PARTITIONING select     count(“Data Inclusão”)<br>    , estado<br>from clientes<br>where “Data Inclusão” = ‘02/05/2015’<br>group by estado<br>Data Inclusão Estado<br>[‘01/05/2015’] [‘SP’]<br>Data Inclusão<br>[‘01/05/2015’,’02/05/2015’,  [’02/05/2015’, ’02/05/2015’] [’PR’, ’SP’]<br>’02/05/2015’,‘03/05/2015’,<br>‘03/05/2015’,‘03/05/2015’,<br>‘03/05/2015’,‘04/05/2015’,  [‘03/05/2015’,‘03/05/2015’,<br>[‘SP, ‘RJ’, ’SP’, ‘PR’]<br>‘04/05/2015’,‘04/05/2015’,  ’03/05/2015’,‘03/05/2015’]<br>‘04/05/2015’,‘04/05/2015’,...]<br>[‘04/05/2015’,‘04/05/2015’,<br>‘04/05/2015’,‘04/05/2015’,  [‘SP’, ‘AM’, ’RJ’, ‘SP’, ‘SP’,...]<br>‘04/05/2015’,...]<br>17<br><!-- End of picture text -->

##### INTRODUCTION TO ANALYTICAL DATABASES **<mark>CARDINALITY</mark>** 



<!-- Start of picture text -->
1:N - one to many<br>N:1 - many for one<br>>—— | =<br>N:N - many to many<br>1:1 - one to one<br><!-- End of picture text -->



18 



<!-- Start of picture text -->
Conse<br>‘So Paulo SP<br>Londrina PR<br>Piracicaba SP<br>‘So Paulo SP<br>Rio de Janeiro RJ<br><!-- End of picture text -->

##### INTRODUCTION TO ANALYTICAL DATABASES **<mark>PARTITIONING</mark>** 



<!-- Start of picture text -->
Estado<br>Data Nascimento<br>ID Cliente<br>Nome Sacee/soeee<br>Tipo ClienteEmail SHEEsites S2itz Data InclusãoCidade<br><!-- End of picture text -->



19 



<!-- Start of picture text -->
INTRODUCTION TO ANALYTICAL DATABASES<br>SS) & @ °<br>Purpose Structure Users Content<br><!-- End of picture text -->

###### INTRODUCTION TO ANALYTICAL DATABASES 



20 

#### INTRODUCTION TO ANALYTICAL DATABASES **<mark>PURPOSE</mark>** 

###### Transactional database 

- Daily operations of the organization. 

- E.g.: processing sales transactions, managing inventory, making reservations, etc. 

- Data analysis. 

- Decision-making. 

- Allows you to consult large amounts of historical data. 



21 

#### INTRODUCTION TO ANALYTICAL DATABASES **<mark>STRUCTURE</mark>** 

###### Transactional database 

- Structured in normalized tables with many relationships. 

- Uses an optimized dimensional structure for data analysis. 



22 

#### INTRODUCTION TO ANALYTICAL DATABASES **<mark>CONTENTS</mark>** 

Transactional database 

   - Historical and consolidated data. 

- Contains current and updated operational data. 

- Multiple data sources. 



<!-- Start of picture text -->
a<br>(tmy\<br>vge<br><!-- End of picture text -->

23 

#### INTRODUCTION TO ANALYTICAL DATABASES **<mark>USERS</mark>** 

Transactional database 

- Employees who perform daily operational tasks. 

- Analysts, managers, and executives who need information for decision-making. 



24 



#### INTRODUCTION TO ANALYTICAL DATABASES **<mark>USERS</mark>** 



<!-- Start of picture text -->
Transactional<br>database<br>J DW<br><!-- End of picture text -->



25 

> <sup>(DN</sup> 26 





<!-- Start of picture text -->
=J-J-<br>\ ap"<br>=<br><!-- End of picture text -->

###### **ETL CONCEPTS** 

27 

###### ETL CONCEPTS 

# **<mark>E</mark>** 

# **<mark>T</mark>** 

# **L** 

(Extraction) (Transformation) (Loading) 

- Collect the necessary data. 

- Transform to integrate diverse data sources. 

- Load the data into DW. 



**28** 

###### ETL CONCEPTS 



Files 

<mark>=</mark> Some sy <mark>a—</mark> e1,<sup>c</sup> ETL .—>3«bet ! Database Comme! I Data Warehouse 



<!-- Start of picture text -->
A<br>myn<br><!-- End of picture text -->



Spreadsheets 

**29** 

###### ETL CONCEPTS 





<!-- Start of picture text -->
EXTRACT TRANSFORM LOAD<br>———=> al Q - Boe = : ios<br><!-- End of picture text -->

**30** 

###### CONCEITOS DE ETL 

**E E T L L T** 



**31** 



<!-- Start of picture text -->
Ceasitits<br>ETL CONCEPTS<br>Files<br>FI<br>mae<br>i<br>EL T<br>Database<br>~ toad<br>i Raw data layer Data<br>A 1 Warehouse<br>Spreadsheets<br><!-- End of picture text -->



<!-- Start of picture text -->
ETL CONCEPTS<br><!-- End of picture text -->



**32** 

###### ETL CONCEPTS 



<!-- Start of picture text -->
DATA INGESTION DATA TRANSFORMATION [ anatyrics<br>ERP no : sik ‘ :<br>AWS A wicorottAawe Google Cloud GERBER 3 :<br>DATABASE - ERP ny<br>S<br>4— cf & Diey MACHINE LEARNING<br>RTABASE- CRM [>= (sau) =4<br>N = Mdbt =<br>TAPS RAW DATA TRANSFORMED DATA oul[|<br>Loss BUSINESS INTELLIGENCE<br>N<br>pret SCHEDULER & DEPLOY Riitiow Wroocker<br><!-- End of picture text -->



**33** 

#### ETL CONCEPTS **<mark>Modern ETL</mark>** 

**<mark>The main advantages of modern ELT are:</mark>** 

- Modularity 

- Simplicity 

- Governance 

- Versioning 

- Separation of environments 

- Tests 





**34** 

#### ETL CONCEPTS **<mark>MODULARITY</mark>** 







<!-- Start of picture text -->
2<br>——<br><!-- End of picture text -->



<!-- Start of picture text -->
aaa<br>See<br><!-- End of picture text -->



<!-- Start of picture text -->
oO<br><!-- End of picture text -->

**<mark>1. Orchestration</mark>** 

**<mark>2. MLOps</mark>** 

**<mark>3. Extraction</mark>** 

**<mark>4. Transformation</mark>** 





<!-- Start of picture text -->
—<br><!-- End of picture text -->



<!-- Start of picture text -->
©<br><!-- End of picture text -->

**<mark>5. Data catalog</mark>** 

**<mark>6. BI tool</mark>** 

**7. Advanced Analytics Tool** 

**35** 

#### ETL CONCEPTS **<mark>SIMPLICITY</mark>** 



<!-- Start of picture text -->
G5<br><<<br>java<br><!-- End of picture text -->



<!-- Start of picture text -->
soeiae<br>Pam.<br><!-- End of picture text -->



<!-- Start of picture text -->
e<br>python<br><!-- End of picture text -->



<!-- Start of picture text -->
Scala<br><!-- End of picture text -->







**36** 

#### ETL CONCEPTS **<mark>GOVERNANCE</mark>** 



<!-- Start of picture text -->
°<br>G80)<br><!-- End of picture text -->

###### **<mark>Management</mark>** 

<mark>Ease of managing a single platform.</mark> 

###### **<mark>Documentation</mark>** 



<!-- Start of picture text -->
eH<br><!-- End of picture text -->

Documentation of data as part of the work in the transformation stage, by people close to the business. 







<!-- Start of picture text -->
Ceasitits<br><!-- End of picture text -->

**37** 

#### ETL CONCEPTS **<mark>VERSIONING</mark>** 





<!-- Start of picture text -->
-<br>-<br>eee tee wee<br><!-- End of picture text -->

**38** 

#### ETL CONCEPTS **<mark>SEPARATION OF ENVIRONMENTS</mark>** 



<!-- Start of picture text -->
<=<br>aw<br>Raw data layer Data<br>Warehouse<br>SANDBOX<br>Work environment  Work environment  Work environment<br>Employee 1 Employee 2 Employee 3<br>39<br><!-- End of picture text -->

#### ETL CONCEPTS **<mark>TESTS</mark>** 





<!-- Start of picture text -->
7<br><!-- End of picture text -->

Raw data layer 



<!-- Start of picture text -->
=o<br><!-- End of picture text -->

Tests 

<mark>_ &</mark> Data warehouse Transformation 

Tests 

**40** 

#### ETL CONCEPTS **<mark>SUMMARIZING</mark>** 

- Extract data from multiple sources 

- Efficient charging 

- Transform as needed 





<!-- Start of picture text -->
Ceasitits<br>“| BM @<br><!-- End of picture text -->

**41** 

> <sup>(DN</sup> 42 





###### **DATA WAREHOUSES X DATA LAKES X** 

**DATA LAKEHOUSE** 

43 

DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE **<mark>DATA WAREHOUSE</mark>** 

- Data structured according to business needs with observed analytical value 

- Concern about data standardization, quality, and consistency 

- Does not support unstructured data 

- Columnar databases optimized for aggregations, best for use with BI tools 

- Scalable 

- Greater performance for big data processing 

- Optimized for querying 

- Reduced storage and processing costs 





44 



DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE **<mark>DATA WAREHOUSE</mark>** 



<!-- Start of picture text -->
Presentation<br>BI Reports<br>Storage and<br>metadata<br>Data mart<br>Extraction<br>and ingestion<br>Fonte<br>Dados externos Dados operação<br><!-- End of picture text -->



45 

DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE **<mark>DATA LAKE</mark>** 

- Data storage flexibility. 

- No need to worry about data duplication. 

- More likely to have data inconsistencies. 

- No concern for business use cases. 

- Greater performance for big data processing. 

- More flexible for use in ML models. 

- Not optimized for queries. 

- Reduced storage and processing costs. 





46 

#### DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE **<mark>DATA LAKE</mark>** 





<!-- Start of picture text -->
As its data lakes slowly turned into a<br>data swamp, it regretted not having a<br>invested more in data quality. =<br>0,00 0.00<br>OM HS<br>we Wa, WSS<br><—e “<“eE2<br><!-- End of picture text -->

47 



<!-- Start of picture text -->
DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE<br>DATA LAKE<br>Presentation<br>Machine  Data  Real-time  and analysis<br>Learning Science Database BI Reports<br>Storage and<br>metadata<br>Data prep e  Data mart<br>visualização<br>Extraction,<br>intake, and<br>Data Lake processing<br>Source<br>Estruturado, semi e não estruturado<br><!-- End of picture text -->

#### DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE **<mark>DATA LAKE</mark>** 



48 

DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE **<mark>DATA LAKEHOUSE</mark>** 

- Combines the flexibility and low costs of a data lake with the query efficiency of a data warehouse. 

- Enables data governance. 





<!-- Start of picture text -->
Data  Streaming<br>Science analytics<br>Machine<br>Learning BI<br><!-- End of picture text -->



<!-- Start of picture text -->
Data Lake<br>Estruturado, semi e não estruturado<br><!-- End of picture text -->

49 



<!-- Start of picture text -->
DATA WAREHOUSES vs DATA LAKES vs DATA LAKEHOUSE<br>BI Reports LearningMachine  ScienceData  Real-time Database BI Reports ScienceData  Streaming analytics<br>Machine<br>Learning BI<br>Data mart<br>Data prep e  Data mart<br>visualização<br>Data Lake<br>Data Lake<br>Dados externos Dados operação Estruturado, semi e não estruturado Estruturado, semi e não estruturado<br>50<br><!-- End of picture text -->

> <sup>(DN</sup> 51 





<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

###### **DATA MODELING** 

52 

###### DATA MODELING 



<!-- Start of picture text -->
< ><br><!-- End of picture text -->





<!-- Start of picture text -->
ConsisivQD osc<br>nome TEXT,<br>cidade TEXT,<br>uf TEXT,<br>cod_agencia<br>ep<br>cod_cliente ;<br>primeiro_nome TEXT,<br>enail<br>tipo_cliente TEXT,<br>cpfcnpj 5<br>data_nascinent ;<br>oe<br>cod_cliente<br><!-- End of picture text -->



<!-- Start of picture text -->
tem 4 iia<br>tem 12 tem 2.4<br>tem 13 item22<br>><br>item4<br>item 2<br>item 3<br>a Htem 4<br>tem 3.1 item 44<br>tem 32 item 42<br><!-- End of picture text -->

53 



<!-- Start of picture text -->
=<br>a<br>_~<br>7<br><!-- End of picture text -->

#### DATA MODELING **<mark>CONCEPTUAL MODEL</mark>** 



<!-- Start of picture text -->
[ = | [|<br>Credit Proposals<br><!-- End of picture text -->



54 

#### DATA MODELING **<mark>LOGICAL MODEL</mark>** 





<!-- Start of picture text -->
| <<br>~<br><!-- End of picture text -->

55 

#### DATA MODELING **<mark>PHYSICAL MODEL</mark>** 



<!-- Start of picture text -->
1 |<br>T agencias (<br>cod_agencia INTEGER NOT NULL,<br>nome 5<br>endereco TEXT,<br>cidade :<br>uf TEXT,<br>data_abertura DATE,<br>tipo_agencia TEXT,<br>cod_agencia<br>clientes (<br>cod_cliente INTEG LL,<br>primeiro_nome 5<br>ultimo_nome TEXT,<br>email TEXT,<br>tipo_cliente TEXT,<br>data_inclusao ¢<br>cpfcnpj TEXT,<br>data_nascimento DATE,<br>endereco TEXT,<br>cep TEXT,<br>cod_cliente<br><!-- End of picture text -->





<!-- Start of picture text -->
ACADEMY<br><!-- End of picture text -->

56 

#### DATA MODELING **<mark>BENEFITS</mark>** 

- Clarity and Consistency 

- ● Efficiency 

- ● Flexibility 

- Data Quality 





<!-- Start of picture text -->
ia<br><!-- End of picture text -->

57 



<!-- Start of picture text -->
DATA MODELING<br>DIMENSIONAL<br>Mart 1 Mart 2<br>Dimension Dimension Dimension Dimension<br>FATO FATO<br>Dimension Dimension Dimension Dimension<br>58<br><!-- End of picture text -->

#### DATA MODELING **<mark>STAR SCHEMA</mark>** 

**Dimension** 

- Fact table 

**Dimension** 

**Dimension** 

**FATO** YA **Dimension Dimension** 



- Dimension tables 

- Foreign key 

- Primary key 

59 

DATA MODELING **<mark>SNOWFLAKE</mark> Dim Dim Dim** ~N , **Dim Dim Dim Dim** \ **<mark>Advantages:</mark> Dim Dim Dim** ae lea **Dim** ● Redundancy Reduction **FACT** ● Flexibility and Maintenance ● **Dim Dim** Query Optimization =z ~~ **Dim Dim Dim Dim** | | ~ **Dim Dim Dim Dim Dim** v\* **Dim** 60 

> <sup>(DN</sup> 61 





<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

###### **FACT TABLES** 

62 



<!-- Start of picture text -->
FACT TABLES<br>Dimension<br>J \<br>Dimension Dimension<br>FACT<br>Yr<br>Dimension Dimension<br>63<br><!-- End of picture text -->

###### FACT TABLES 



<!-- Start of picture text -->
Fato Transacgées<br>Chave de Data (FK)<br>Chave Cliente (FK)<br>Chave Estabelecimento (FK)<br>Se traduz em: Numero da Transagao<br>Valor em Total Reais<br>Cashback Recebido em Reais<br><!-- End of picture text -->



64 

#### FACT TABLES **<mark>FEATURES</mark>** 

- ➢ Measures generated from a measurable real-world event. 

- ➢ Foreign keys (FKs) for each associated dimension. 

- ❏ At the lowest granularity, a row in the fact table corresponds to the event. 





<!-- Start of picture text -->
4<br>ACADEMY<br>Perform a transaction<br><!-- End of picture text -->

65 

###### FACT TABLES 

#### **<mark>TYPES</mark>** 

###### **Transactional** 

- A line corresponds to an event in time and space. 

- This type of table provides more flexibility in data exploration. 

- However, they can be very dense or sparse, since the fact is only recorded when a new event occurs. 

###### **Aggregates** 

- These are tables that aim to improve query performance in the BI tool. 

- Since transactional data can result in very large tables, it is common to aggregate the information by periods and dimensions that make sense for business analysis. 



66 

> <sup>(DN</sup> 67 





<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

###### **DIMENSION TABLES** 

68 

###### DIMENSION TABLES 

- ✓ The dimensions provide the context of the business event: When, Who, What, Where, Why, and How. 

- ✓ Contains the descriptive attributes used by BI applications to filter and group facts. 

- ✓ We should spend more time focusing on governance and dimension development, as these are the driving forces behind the DW/BI experience. 





<!-- Start of picture text -->
ACADEMY<br>Perform a<br>transaction<br>ty,<br>a<br>Credit<br>>”<br><!-- End of picture text -->

69 

###### TABELAS DIMENSÃO 

- ✓ **Unique key** for identifying the row, which will be included as FK in the fact table. 

- ✓ Information about the context of the dimension. 

- ✓ **Hierarchies** 

- ❖ The dimension must have only one possible connection for each row in the fact, otherwise it will duplicate the same row. 





<!-- Start of picture text -->
Pe<br>ACADEMY<br>Dimension<br>Establishment<br>_<br>K Establishment<br>Establishment Code<br>CNAE<br>City<br><!-- End of picture text -->

70 



<!-- Start of picture text -->
‘<br> Type4<br>(nistory<br>New<br><!-- End of picture text -->

###### DIMENSION TABLES 

#### **<mark>SLOW CHANGE DIMENSION</mark>** 



71 

#### DIMENSION TABLES **<mark>TYPE 1 SCD</mark>** 

###### Table then 



<!-- Start of picture text -->
oe Data Cidade<br>Contratacéo ___Residéncia uy ueuetio<br><!-- End of picture text -->



João moves to São Paulo 





###### Table now 



<!-- Start of picture text -->
ote Data Cidade 3<br>Contratacao Residéncia us Usuario<br><!-- End of picture text -->

72 

###### DIMENSION TABLES 

#### **<mark>TYPE 2 SCD</mark>** 

###### Table then 



<!-- Start of picture text -->
a Data Cidade<br>Aauisicaéo Residéncia<br><!-- End of picture text -->



João moves to São Paulo 

###### Table now 





<!-- Start of picture text -->
Nome dois eos Valido De Valido Até<br>Aauisicao Residéncia<br>01/01/2015 |Manaus| 01/01/2015 05/10/2020<br>2001/2015 |__Manaus__|[ 20/01/2015 | __nut_|<br><!-- End of picture text -->

73 

#### DIMENSION TABLES **<mark>KEYS</mark>** 

###### Natural operational key of the system 



<!-- Start of picture text -->
ID Cliente Nome pea cae Valido De Valido Até<br>Aauisicdo Residéncia<br>José Oliveira | 01/01/2015 01/01/2015 05/10/2020<br><!-- End of picture text -->

Unique key 



74 

#### DIMENSION TABLES **<mark>Degenerate Dimension</mark>** 



Address dimension Customer Dimension Fact Transactions —_ Status dimension 

75 

#### DIMENSION TABLES **<mark>DEGENERATE DIMENSION</mark>** 



<!-- Start of picture text -->
Address dimension<br>Customer Dimension<br>Fact Transactions<br>Status dimension<br><!-- End of picture text -->



76 

> <sup>(DN</sup> 77 





<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

###### **BRIDGE TABLES** 

78 



<!-- Start of picture text -->
Gos<br>DIMENSION<br><!-- End of picture text -->



<!-- Start of picture text -->
BRIDGE TABLES<br><!-- End of picture text -->





<!-- Start of picture text -->
FATO<br><!-- End of picture text -->



79 

###### BRIDGE TABLES 



<!-- Start of picture text -->
— {ne rato | | |<br><!-- End of picture text -->

80 



<!-- Start of picture text -->
ID_Data Nome_Colaborator<br>20250101 01/01/2025<br>20250102 02/01/2025<br>20250103 03/01/2025<br>20250104 04/01/2025<br><!-- End of picture text -->

###### BRIDGE TABLES 



<!-- Start of picture text -->
ID_Client Name_Client ID_Colaborator Nome_Colaborator 20250101<br>1 João da Silva 101 Carlos Andrade 20250102<br>2 Maria Oliveira 102 Ana Souza 20250103<br>20250104<br>ID_Cliente ID_Colaborator ID_Data<br>1 101 20250101<br>1 102 20250102<br>2 101 20250103<br>2 102 20250104<br>81<br><!-- End of picture text -->

###### BRIDGE TABLES 



###### **Useful when:** 

- Many-to-many relationship; 

- Connect tables with different granularities; 

- Many possible combinations between the data. 

###### **Requirements:** 

- Ensure the existence of primary keys 

- Identify many-to-many relationships 

82 

##### BRIDGE TABLES **<mark>BENEFITS</mark>** 

- Simplicity in joins 

- Scalability 

- Flexibility 

- Analysis Enhancement 





<!-- Start of picture text -->
». a Le<br><!-- End of picture text -->

83 

###### BRIDGE TABLES 

##### **POINTS OF ATTENTION** 



- A. Performance 

- B. Maintenance 

- C. Additional Complexity 





<!-- Start of picture text -->
‘el % = Y; ‘<br>re<br>ingggiuer® Y aly | cin )<br>it<br><!-- End of picture text -->

84 

> <sup>(DN</sup> 85 





<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

###### **GOOD PRACTICES** 

86 

### **BEST PRACTICES** 





ACID Transactions Atomicity Consistency Isolation Durability 



Access control Encryption and security 



87 

### **BEST PRACTICES** 



<!-- Start of picture text -->
:<br><!-- End of picture text -->



<!-- Start of picture text -->
=)<br><!-- End of picture text -->

Optimize Z-Ordering Auto-optimize 



<!-- Start of picture text -->
.<br><!-- End of picture text -->



<!-- Start of picture text -->
fe)<br><!-- End of picture text -->





<!-- Start of picture text -->
@<br><!-- End of picture text -->

Partitioning Delta cache Cost-based optimizer 



88 

### **BEST PRACTICES** 



<!-- Start of picture text -->
ra<br><!-- End of picture text -->

Serverless Architecture 



<!-- Start of picture text -->
)<br><!-- End of picture text -->

Automatic cluster suspension 





<!-- Start of picture text -->
(cal<br><!-- End of picture text -->

Workload monitoring Cost management 



89 

> <sup>(DN</sup> 90 

### **BOAS PRÁTICAS** 



Otimização de consultas Warehouses virtualizados ©© H Clustering para melhorar o desempenho Suspensão e retomada de warehouses 





Minimizar joins complexos Materialized views 



<!-- Start of picture text -->
val<br><!-- End of picture text -->



<!-- Start of picture text -->
res<br><!-- End of picture text -->

Cargas de trabalho Gerenciamento de custos e créditos 

91 

### **BOAS PRÁTICAS** 



Multi-cluster warehouses Controle de acesso Criptografia Gerenciamento de dados sensíveis 



<!-- Start of picture text -->
Q<br><!-- End of picture text -->



<!-- Start of picture text -->
ea<br><!-- End of picture text -->



<!-- Start of picture text -->
&<br><!-- End of picture text -->



Micro-partitioning Time travel Uso de data sharing 



<!-- Start of picture text -->
&<br><!-- End of picture text -->



92 



**JOIN OUR COMMUNITY** CT 

