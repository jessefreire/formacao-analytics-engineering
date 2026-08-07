

BI tools 

**Module 6** - Creating dashboards with Power BI 







Business Intelligence is a set of processes, techniques, and tools that enable the collection, organization, and presentation of data relevant to strategic decision-making in organizations. 

2 



Power BI Components **Module 6** - Creating dashboards with Power BI 





<!-- Start of picture text -->
Components of<br>POWER BI<br>Power Query<br>Linguagem M<br>Semantic model<br>Data flow and published<br>report<br>import import<br>directquery<br>POWER BI SERVICE<br>Data source<br>Semantic  POWER BI DESKTOP<br>model and<br>report<br>DAX<br>4<br><!-- End of picture text -->

# Components of **POWER BI** 





Components of 

# **POWER BI** 

Power BI Desktop 

- free. 

- can be acquired from the Microsoft website or **Microsoft Store.** 

- runs on the Windows operating system. 

- some features only work in this version. 

- we use to create semantic models and develop reports. 



Components of 

# **POWER BI** 

Power BI Service 

- SaaS version, online 

- objective of publishing and sharing reports 

- there are no restrictions regarding the operating system 

- you must have a corporate or student account 

- depending on the license, the features change 



Components of **POWER BI** 

- one tool complements the other 

- while one creates reports, the other distributes them 

- Distribution can be via **reports, dashboards,  applications, and email.** 



Data flow and semantic model 

**Module 6** - Creating dashboards with Power BI 





Data Flow and Semantic Model 

# **POWER BI** 

Data flow 

## **_What is it?_** 

- A tool that allows you to create and manage data flows within the Power BI service. 

## **_What is it for?_** 

- create sets of tables that will be used in future analyses 

- enrich data with logic that can be useful in more than one report 





“Data should be transformed as close to the source as possible and as close to the visualization as necessary.” Matthew Roche 

10 



## Data Flow and Semantic Model 

# **POWER BI** 



<!-- Start of picture text -->
Power Query<br>Linguagem M<br>Fluxo de<br>Data flowdados<br>import<br>POWER BI SERVICE<br>Fonte de<br>Source<br>dados<br><!-- End of picture text -->

## Data flow 

## **_Features_** 

- Less contact with the data source when developers are creating reports. 

- Lower update rate for tables used in more than one report. 

11 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

## Data Flow and Semantic Model 

# **POWER BI** 

Fluxo de dados 

12 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

## Data Flow and Semantic Model 

# **POWER BI** 

Fluxo de dados 



<!-- Start of picture text -->
"7<br>dim_colaboradores<br><!-- End of picture text -->

13 



## Data Flow and Semantic Model 

# **POWER BI** 



<!-- Start of picture text -->
Power Query<br>Linguagem M<br>Fluxo de<br>Data flowdados<br>import<br>POWER BI SERVICE<br>Fonte de<br>Source<br>dados<br><!-- End of picture text -->

## Data flow 

- **_Objectives_** > logical language to natural/business language. 

- delete columns that are not useful. 



<!-- Start of picture text -->
> data consolidation layer<br><!-- End of picture text -->

14 



<!-- Start of picture text -->
Components of<br>POWER BI<br>Power Query<br>Linguagem M<br>Semantic model<br>Semantic model<br>Data flow and published<br>report<br>import import<br>directquery<br>POWER BI SERVICE<br>Data source<br>Semantic  POWER BI DESKTOP<br>model and<br>report<br>DAX<br>15<br><!-- End of picture text -->



<!-- Start of picture text -->
Components of<br>POWER BI<br><!-- End of picture text -->





<!-- Start of picture text -->
Components of<br>POWER BI<br>Semantic model<br>Semantic model<br>and published<br>report<br>import<br>directquery<br>POWER BI SERVICE<br>Data source<br>Semantic  POWER BI DESKTOP<br>import<br>model and<br>report<br>DAX<br>16<br><!-- End of picture text -->

# Components of **POWER BI** 

Semantic model 





<!-- Start of picture text -->
Consists<br><!-- End of picture text -->

Components of 

# **POWER BI** 

Semantic model 

## **_Features_** 

- location of the report where the data is! 

- location where calculated columns and DAX measures are created. 

- place where relationships between tables are created. 



<!-- Start of picture text -->
Snowflake Banvic :<br>i. . Banvic oe<br><!-- End of picture text -->

17 



Storage modes **Module 6** - Creating dashboards with Power BI 





# Storage modes **POWER BI** 



<!-- Start of picture text -->
queries and data stored in the model or cache<br>IMPORT<br>queries performed directly on the data source<br>DIRECTQUERY<br>DUAL<br>the two formats happening together<br><!-- End of picture text -->

19 



## Storage modes 

# **POWER BI** 

**IMPORT** 





- We want Power BI to copy the data from the tables and columns into the model. 

- Optimized transfer, compressing data in the model by up to 10x. 

- Every time the data is updated, a "select *" query is performed in the DW. 

- Better dashboard performance because the data is stored in the model. 

- All features in DAX and M are supported. 

- Lower data transfer volume, because updates are scheduled. 

20 



## Storage modes 

# **POWER BI** 

**DIRECTQUERY** 





- We want Power BI to connect directly to the data source. 

- The model only contains metadata, and all data is stored in the DW. 

- For this reason, there are no issues regarding the amount of data in the report. 

- A good option when security policies prohibit importing local copies of data. 

- Data is updated with DW in real time. 

21 



Storage modes 

# **POWER BI** 

**DUAL** 





- We only want a few tables via DirectQuery and the rest via Import. 

- More flexible model. 

22 





<!-- Start of picture text -->
Storage modes<br>POWER BI<br>Do I need to have specific data  Yes<br>sources available?<br>No<br>Yes<br>Do I need all DAX functions, M<br>functions, and calculated tables?<br>No<br>Yes<br>DirectQuery Do I need real-time data updates? Import<br>No<br>Yes Do I need space for large volumes  No<br>Duplo<br>of data?<br>23<br><!-- End of picture text -->



Table structure 

**Module 6** - Creating dashboards with Power BI 





<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

## Table structure 

# **POWER BI** 

Star Schema example 



<!-- Start of picture text -->
O< colaborador_fk<br>data_fk we<br>colaborador_sk<br><!-- End of picture text -->

25 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

Table structure **POWER BI** 

Example of relations 



<!-- Start of picture text -->
O< colaborador_fk<br>data_tk bo<br>colaborador_sk<br><!-- End of picture text -->

26 



Table structure 

# **POWER BI** 

Relation 1:many (1:*) 

> most common and recommended 

> linking one key in the dimension table and one or more in the fact table 

fact_transacao 

dim_dates 

Data Data 2025-03-01 2025-03-01 2025-03-01 



<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

## Table structure 

# **POWER BI** 

1:1 relationship 

> unique values between the two tables 

> redundant information storage 

dim_dates 

Data 2025-03-01 

fact_transacao 

Data 2025-03-01 



Table structure 

# **POWER BI** 

Relationship many:many 

> there are no unique values in either table 

> may generate ambiguity in the model 

> incorrect results and loss of performance 

fact_transacao 

dim_dates 

Data Data 2025-03-01 2025-03-01 2025-03-01 2025-03-01 



<!-- Start of picture text -->
ConsistsQD osc<br><!-- End of picture text -->

Table structure 

# **POWER BI** 

Dimension with multiple functions 

> More than one column can be a key to another table. 

dim_dates fact_proposta Data ~~—>~~ Data entrada Data efetivada 2025-03-01 2025-02-27 2025-03-01 2025-03-01 2025-03-03 



<!-- Start of picture text -->
ConsistsQD osc<br><!-- End of picture text -->

Table structure 

# **POWER BI** 

Dimension with multiple functions 

> More than one column can be a key to another table. 

fact_proposta 

dim_dates fact_proposta Data ~~—>~~ Data entrada Data efetivada 2025-03-01 2025-02-27 2025-03-01 2025-03-01 2025-03-03 Function DAX USERELATIONSHIP 



Power Query and M language **Module 6** - Creating dashboards with Power BI 



<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

Power Query and M language **POWER BI** 

Power Query 

## **_What is it?_** 

- initially an Excel add-in, which is capable of performing data transformation within the tool. 

- later added to Power BI as well 

- In MDS, we use it to rename columns and tables, change text to numerals, remove lines, etc. 



DAX language **Module 6** - Creating dashboards with Power BI 





<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

DAX language **POWER BI** 

## **_What is it?_** 

- DAX: Data Analysis Expressions. 

- Solution initially designed for Excel but widely used in other services, such as Power BI. 

- Over 200 functions available. 



<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

DAX language **POWER BI** 

**_What is it used for?_** 

- Measures 

- Calculated columns 

- Calculated tables 

- Row Level Security (RLS) 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

# DAX language **POWER BI** 

## Expression 

## **_Measures_** 

- ➔ Dynamic calculations with filter context: they only gain context when inserted into a visual. 

Field in the visual Data segmenter Report/page filter Filtro Drill-Through Filter other views 

_Filter_ ➔ They do not take up physical _context_ space in the model. 

Result displayed in the visual 



# DAX language **POWER BI** 

## **_Calculated columns and tables_** 

➔ They are static and calculated at the line level. 

- ➔ They are stored in the template and weighed in the final file. 









Line context Line context Line context Line context Line context Line context 



<!-- Start of picture text -->
Consists<br><!-- End of picture text -->

# DAX language **POWER BI** 

## **_Implicit measures_** 



<!-- Start of picture text -->
on<br>pecsenssscccececceccece Dados x<br>—Nomeda Agé.. X | >  a :<br>—sume<br>+Adicionar dados<br>No resumir<br>Soma<br>Maia<br>aaa<br>Contagem (Dist)<br>-<br>Contagem<br>Desvopsarte<br>aaa<br>Mediana<br><!-- End of picture text -->

## **_Explicit measures_** 



<!-- Start of picture text -->
1 Transacoes_Digital =<br>3<br>43 VAR Transacoes_ALL =<br>4% SUM(fact_transacoes[valor_transacao])<br>6 VAR Transacoes_Digital =<br>7<br>CALCULATE(<br>8 SUM(fact_transacoes[valor_transacao])<br>9 » dim_agencias[Nome da Agéncia] = “Agéncia Digital"<br>1<br>12 RETURN<br>ES a<br>14 Transacoes Digital<br>15 » Transacoes_ALL<br>16 )<br><!-- End of picture text -->



## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
CALCULATE ( <Expression> [, <Filter> [, <Filter> [, ~. ] ] ] )<br><!-- End of picture text -->

- Creates new contexts for a measure/calculation based on filters selected for it. 



<!-- Start of picture text -->
FILTER ( <Table>, <FilterExpression> )<br><!-- End of picture text -->

- Creates a new table, filtered based on the specified conditions. 

- For scenarios that are minimally more complex than Calculate. 



# DAX language **POWER BI** 



<!-- Start of picture text -->
DIVIDE ( <Numerator>, <Denominator> [, <AlternateResult>] )<br><!-- End of picture text -->

> Safer than using the "/" operator. 



<!-- Start of picture text -->
ACADEMY<br><!-- End of picture text -->

## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
VAR <name> = <expression><br>VAR <name2> = <expression2> [...]]<br>RETURN <result_expression><br><!-- End of picture text -->

- fundamental for developing organized and complex measures in Power BI. 

- improves file performance 

- improves code readability 

- simplifies debugging 



<!-- Start of picture text -->
(Cac<br><!-- End of picture text -->

## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
SUM oax Function (Aggregation)<br>‘Adds all the numbers in a column.<br>Syntax<br>SUM ( <ColumnName> )<br>PARAMETER ATTRIBUTES DESCRIPTION<br>ColumnNName The column that contains the numbers to sum.<br>Return values<br>Asinglevalue of any type.<br>Result of the sum.<br><!-- End of picture text -->

## **_Aggregation Functions:_** 

> These are the basic functions, ranging from implicit measurements to the most complex ones. > count, sum, average, minimum, or maximum for all rows in a column or table, as defined by the expression. 

Source: DAX Guide 



<!-- Start of picture text -->
Consists<br><!-- End of picture text -->

## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
CALENDAR ax Function (oate and Time)<br>Returns a table with one column of all dates between StartDate and EndDate.<br>‘Syntax<br>CALENDAR ( <StartDate>, <EndDate> )<br>StartDate The start date in datetime format<br>EndDate The end date in datetime format<br>Return values<br>table with a single column,<br>dates. The<br>Retums a table witha single column named "Date" containing @ contiguous set of<br>range of dates is from the specified start date tothe specified end date inclusive of those two<br>dates<br><!-- End of picture text -->

## **_Date and Time Functions:_** 

- manipulate and calculate dates and times 

- These functions assist in creating columns such as day, difference between days, months, years, hours, etc. 

Source: DAX Guide 



<!-- Start of picture text -->
(Cac<br><!-- End of picture text -->

## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
DAX Function (Time Intelligence)<br>Returns a set of dates in the current selection from the previous year.<br>syntax<br>SAMEPERIODLASTYEAR ( <Dates> )<br>PARAMETER ATTRIBUTES DESCRIPTION<br>Dates The name of a column containing dates or a one column table<br>containing dates,<br>Return values<br>Atable with a single column.<br>The corresponding dates in the previous year.<br><!-- End of picture text -->

**_Temporal data intelligence functions:_** 

> used to manipulate data, create and compare temporal calculations. 

> Specialized functions for time analysis calculations: firstdate, previousyear, sameperiodolastyear, etc. 

Source: DAX Guide 



<!-- Start of picture text -->
Consists<br><!-- End of picture text -->

## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
SWITCH oaxrunction (Logical<br>Returns different results depending on the value of an expression<br><!-- End of picture text -->



<!-- Start of picture text -->
‘Syntax<br>SMITH ( <Expression>, <value>, <Result> [, <Value>, <Result> [,<br>~ 11 L elses )<br>Expression The expression tobe evaluated<br>Value __~epssable_f expression has this valu the corresponding esut wil be<br>retumed<br>Result _Pepeiale The result be returned it Expression has corresponding<br>value<br>kise oftens! there are no matching values the Ee value is etumed.<br>Return values<br>A single value of any type<br>A scalar value coming from one ofthe Result expressions if there was a match with Value, or<br>from the Else expression if there was no match with any Value<br><!-- End of picture text -->

## **_Logical Functions:_** 

- return information about values based on a condition. 

- The main ones are IF and SWITCH statements. 

Source: DAX Guide 



<!-- Start of picture text -->
(Cac<br><!-- End of picture text -->

## DAX language 

# **POWER BI** 



<!-- Start of picture text -->
DAX Function (Relationships management)<br>Specifies an existing relationship to be used in the evaluation of a DAX expression.<br>The relationship is defined by naming, as arguments, the two columns that serve as<br>endpoints.<br>syntax<br>USERELATIONSHIP ( <ColumnName1>, <ColumnName2> )<br>ColumnNamet Foreign (or primary) key ofthe relationship<br>ColumnNName2 Primary (or foreign) key of the relationship.<br>Return values<br>The function retums no value; the function only enables the indicated relationship for the<br>duration of the calculation<br><!-- End of picture text -->

## **_Relationship Functions:_** 

- manage the relationship between tables, beyond the relationship established at the semantic layer level. 

> The main functions are USERELATIONSHIP and CROSSFILTER. 

Source: DAX Guide 



<!-- Start of picture text -->
Coit<br><!-- End of picture text -->

# DAX language **POWER BI** 



<!-- Start of picture text -->
MAXX ax Function (agaregation)<br>Returns the largest value that results from evaluating an expression for each row<br>of a table. Strings are compared according to alphabetical order.<br>syntax<br>wx ( <table>, <Expression> [, <ariant>] )<br>table,<br>Return values<br>A single value of any type<br><!-- End of picture text -->

## **_Iterator Functions:_** 

- measurements behave like conventional columns. 

> SUMX, MINX, MAXX, AVERAGEX, COUNTX, RANKX. 

Source: DAX Guide 





Optimizing data models **Module 6** - Creating dashboards with Power BI 



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

Optimizing data models 

# **POWER BI** 

Fundamental assumptions 

**_Use of the Star Schema_** > in Power BI is the most optimized structure to use 

> highly relevant to the development of the model 

> favor tables with cardinality 1:many 



<!-- Start of picture text -->
BB mension table<br>1<br>f<br>* a tableFact Ws<br>1Va x 1<br>BB Dimension table {EB Dimension table<br><!-- End of picture text -->

Source: Microsoft 



<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

Optimizing data models 

# **POWER BI** 

Fundamental assumptions 

**_Analyze measurements and visuals_** 

- maintain simple and optimized semantic models. 

- Use the tool's Performance Analyzer to validate that visuals and formulas are up to date and optimized. 

- propose improvements in visuals and queries, reducing volume and complexity. 



<!-- Start of picture text -->
(Cac<br><!-- End of picture text -->

Optimizing data models 

# **POWER BI** 

Fundamental assumptions 

**_Remove automatic date and time feature_** 

> This feature automatically creates hidden calculated tables that weigh into the final model. 



<!-- Start of picture text -->
Opgées<br>GtoBaL er Quen Es jadasimutaneamente, em por =o a<br>Sequence Inteligéncia de dados temporais<br>ssusizagee ‘Opces de Gerenciamento de Cache de Dados<br>Rae LUmpar cache<br>ie aaaiiaenl a Opcéesde Cache de PeR<br>ARQUIVO ATUL sate TE<br>Configuacsesdomessiosemin~ S06 do Cache de Artefatos Particionados<br>configuagiesdo retro sper Cotte v<br><!-- End of picture text -->



Optimizing data models **POWER BI** 

Fundamental assumptions 

## **_Reduce tables and calculated columns_** 

- Creating tables and columns should be part of the data transformation stage. 

- Calculated tables and columns take up space in the pbix file memory and affect its performance. 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

Optimizing data models **POWER BI** 

Strategies for reducing data and optimizing 

**_Vertical filtration_** 

> removal of unnecessary columns from the template. 



<!-- Start of picture text -->
68451979 lcbefacSdfOF30a826d6c0a 6 Agéncia Rio de Janeiro | R. Sen. Dantas, 15 - Centro, Rio de Janeiro - Rl, 20031-202 Rio de Janeiro RJ 2031-202 _quarto-feira, 1 de abrilde 2015 Fisica<br>4765283854e658addc8c5893 18637146 9 Agéncia Floriandpolis | Av. Jom, Rubénsde Arruda Ramos, 1280 - Centro, Floriandpolis -SC, €8015-700 Florianépolis SC | 88015-700 quarta-feira, 9 de outubrode 2019 Fisica<br><!-- End of picture text -->



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

Optimizing data models **POWER BI** 

Strategies for reducing data and optimizing 

**_Horizontal filtration_** > removal of unnecessary lines from the template. 



<!-- Start of picture text -->
68451979 lcbefacSdfOF30a826d6c0a 6 Agéncia Rio de Janeiro R. Sen. Dantas, 15 - Centro, Rio de Janeiro - Rl, 20031-202 Riode Janeiro RI 20031-202—_quarta-feira, 1 de abrilde 2015 Fisica<br>4745283854e65Badde8c589318b37 146 9 Agéncia Florianépolis Av. Jorn. Rubénsde Arruda Ramos, 1280 - Centro, Florianépolis - SC, 88015-700 Floriandpolis SC  88015-700 _quarta-feira, 9 de outubrode 2019 Fisica<br><!-- End of picture text -->



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

Optimizing data models **POWER BI** 

Strategies for reducing data and optimizing 

**_Group and summarize_** > removal of unnecessary rows and columns from the template, grouping information, and changing the granularity of the table. 



<!-- Start of picture text -->
tnoacerca Rises 5<br>Fisica SP 3<br>ae = :<br>Fisica sc 1<br>Fisica PE 1<br>Fisica RS 1<br>Fisica RU 1<br><!-- End of picture text -->



<!-- Start of picture text -->
Coss<br><!-- End of picture text -->

Optimizing data models **POWER BI** 

Strategies for reducing data and optimizing 

## **_DirectQuery_** 

- removal of data from the model, retaining only metadata. 





> Data remains in the data warehouse, and each interaction generates a new query to the database. 



<!-- Start of picture text -->
(MN<br><!-- End of picture text -->

**THANK YOU** 

