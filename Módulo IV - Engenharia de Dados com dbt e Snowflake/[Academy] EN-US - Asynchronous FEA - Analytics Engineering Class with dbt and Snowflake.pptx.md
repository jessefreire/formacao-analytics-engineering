

Analytics Engineering with DBT 

**Module IV** 





Introduction: Analytics engineering with dbt 





### Hello! 

My name is Rulyan. Data Product Manager & Analytics Engineer @ Indicium Bachelor of Science in Civil Production Engineering (UFSC) 

**https://www.linkedin.com/in/rulyan-fernandes/** 



<!-- Start of picture text -->
'<br>iv.<br>\eu=<br>THE BIGCEsT G<br>MODERN<br>DATA<br>TACK<br><!-- End of picture text -->



Introduction: Analytics engineering with dbt **INTRODUCTION** 

- We learned about the fundamentals of analytics and the role of an analytics engineer. 

- What are databases and their language, SQL? 

- We learned about Data Warehouses (DW) and how to build a fact and dimension architecture. 

- So, how do we get the data into the DW? 

- How to connect different data sources, tools, and processes? 

- How can we ensure that this is done in a way that is organized, easy to monitor, reliable, and repeatable? 

4 



Introduction: Analytics engineering with dbt **MODULE OBJECTIVES** 

- What is the ELT (extract, load, and transform) process? 

- Definition of a data pipeline and its stages. 

- How DataOps is important in building a data project (Data Warehouse). 

- Orchestration of tasks in data pipelines. 

- Hands-on learning of DW development. 

   - How to use dbt as a tool for data transformation. 

   - Star schema modeling. 

   - Application of good software development practices. 

5 





Data pipelines and ETL 



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

Data pipeline and ETL **DATA PIPELINE** 

**OLTP bank** = **API to CRM** = **JSON files** 28= **Business user Spreadsheets** 

7 



#### ETL 

**1** 

EXTRACT 

Retrieve raw data from one or more sources and save them in a single data repository. 

**2** 

TRANSFORM 

Structure, enrich, clean, and convert raw data for a final data model. 

**3** 

LOAD 

Upload the transformed data to a data warehouse or data repository for use in a BI tool. 

8 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

##### Data pipeline and ETL 

## **ETL** 



<!-- Start of picture text -->
PAINEL PRONTO wus<br>BR Fe EBA Fe RRR SB Ra SE<br>= “+ 4 fe ee See . aa]<br>ETL<br>== - f= ;<br>= ESIGN S<br><!-- End of picture text -->

9 

**<mark>ETL ERP SITE</mark>** 

**<mark>ETL ETL CRM MARKETING DATA WAREHOUSE</mark>** 



<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

## Data pipeline and ETL **SUMMARIZING** 

- A data pipeline is the organized flow of activities that moves data from a source to a destination within an organization. All tools, the cloud, the orchestrator, the data extractor, and the data warehouse are part of the pipeline. 

- ELT (extract-load-transform) are the sequential steps in a data pipeline. 

- Every data pipeline must be orchestrated to run in the correct order. 

- Monitoring the execution of a data pipeline is essential to ensure that everything is running correctly. This is critical for company teams to trust the data. 

- Data pipelines are necessary to enrich and centralize data from various sources into a single repository, providing a single source of truth for the company. 

11 





Traditional ETL 



## Traditional ETL **DETAILS** 



<!-- Start of picture text -->
EXTRACT TRANSFORM LOAD<br>Se eo . a ==<br><!-- End of picture text -->

13 



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

## Traditional ETL **DETAILS** 



<!-- Start of picture text -->
Fontes de dados Plataforma de dados Data Products<br>Banco de dados<br>Transformaçã Carregamento<br>: N ii Extração o Dw pi — :<br>H ij i Data Marte i 4 Dashboards :<br>| Planilhasde controle: | | f Po i<br>Área Staging<br>i API do CRM E f i :  Relatérios pontuais H<br><!-- End of picture text -->

14 

- Traditional ETL **APPLICATION** ● The concept of ETL is not new. Since 1970, this has been the standard process for extracting and transforming data from numerous sources to a single final destination. 

- ● The emergence of data warehouses in the early 1990s increased their use in corporate data strategies. 

- ● ETL pipelines work very well with structured data and in use cases where the data volume is not large. ● Due to these characteristics, it is common to find companies where each department or professional chose a different tool to perform ETL depending on the source they were working with. 

- ● With the expansion of data volumes across all industries, creating robust ETL systems has become an 15 

- <mark>o</mark> extremely complex undertaking. ~~<mark>e</mark>~~ 





ELT: A new approach 



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

##### ELT: A new approach 

## **DETAILS** 



<!-- Start of picture text -->
Fontes de dados Plataforma de dados Data Products<br>i Banco de dados i i << i<br>i ==) | oe Dashboards i<br>i Planilhas de controle i Lf Dados Transformados i i<br>H i]; Data Lake io ==) H<br>H S fl (opcional) io = i<br>H API do CRM ; H i !  Relatérios pontuais H<br><!-- End of picture text -->

17 



## ELT: A new approach **REMEMBERING...** 

What are the advantages of using a Data Warehouse? 

- Centralization of data from different sources and systems in a single repository, generating a **single source of truth** . 

- Optimization for analytical queries. 

- Data quality. 

- Governance. 

- Storage of data history, which rarely occurs in a transactional system. 

18 





ETL vs ELT 



##### ETL vs ELT 

## **TRADITIONAL ETL** 

   - Responsibility of the IT department. "BI in the bread line." 

   - Far from business analysts. 

- **ERP Bank** ● Not very transparent, no governance. 

- **Software CRM ETL DW** ● Different languages and tools = technical debt. 

- **JSON files** ● Expensive and time-consuming. "Superman"/"Wonder Woman." 

- **Spreadsheets** 

20 



##### ETL vs ELT 

## **ELT NEW APPROACH** 



<!-- Start of picture text -->
Extract & Load Transform Analytics ● Made in a modular way.<br>● Transformation in SQL.<br>ERP Bank<br>DW ● Governance.<br>Software CRM E-L ● Versioning.<br>Raw<br>Data<br>Data<br>●<br>Separation of environments.<br>JSON files<br>● Data testing.<br>dbt<br>Spreadsheets<br>Orchestration & Deployment<br><!-- End of picture text -->



<!-- Start of picture text -->
21<br><!-- End of picture text -->



##### ETL vs ELT 

## **ELT NEW APPROACH** 



<!-- Start of picture text -->
Extract & Load Transform Analytics ● Made in a modular way.<br>● Transformation in SQL.<br>ERP Bank<br>DW ● Governance.<br>Software CRM E-L ● Versioning.<br>Raw<br>Data<br>Data<br>●<br>Separation of environments.<br>JSON files<br>● Data testing.<br>dbt<br>Spreadsheets<br>Orchestration & Deployment<br>What does this mean? -> DataOps<br><!-- End of picture text -->

22 



<!-- Start of picture text -->
‘ACADEMY<br><!-- End of picture text -->

## ETL vs ELT **DATAOPS** 

How to ensure quality in ELT? 

- Data is dynamic, so we need to "take a snapshot" of the data and how it is transformed. You need to test the data, document its attributes, monitor it, and perform these tasks collaboratively. 

- The combination of these practices, tools, and team culture forms the DataOps (Data Operations) process, which is a methodology designed to manage data and data products in a more efficient and scalable manner. 

- DataOps was inspired by the principles of DevOps, which are best practices in software development. 

- DataOps aims to increase the quality of ELT so that the business team can trust the data. 

23 





ELT Steps: Planning 



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

## ELT Steps: Planning **THE FIRST STEP** 



<!-- Start of picture text -->
Ingestao (E-L)<br>Transformagao<br>(7)<br>Entrega<br>(deploy)<br><!-- End of picture text -->

The planning steps are: 

- Understanding the business problem and its requirements. 

- Data mapping. 

- Development of the conceptual model of the DW. 

25 





Stage: Ingestion 



## Stage: Ingestion **KEY POINTS** 

- **Map data for extraction:** which data sources and tables/datasets are needed for this stage of the project. 

- **Define the type of processing required:** what type of processing is required in production. At this stage, we need to predict whether the data can be updated in daily batches, hourly batches, or even in real time. 

- **Analyze data volume:** how much data is stored and how fast is it growing. 

- **Check security policy and sensitive data:** when the project involves sensitive data, extra care is needed in terms of access and processing. 

- **Define infrastructure type:** the ETL infrastructure will be cloud-based, on-premises, or hybrid. 

- **● Map data consumption patterns:** map how data will be consumed at the end point, such as reports, BI tools, APIs, etc. 

27 



Lesson 4.8 - Intake - Types of processing 





## Ingestion - Types of processing **EXAMPLE** 



<!-- Start of picture text -->
Once a day<br>Source<br>    Extract-LoadIntake<br>DW<br>Data<br><!-- End of picture text -->

29 



##### Ingestion - Types of processing 

## **LOAD FULL-REFRESH** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 3 lines|
|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00||
|3<br>Day 2|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00||
|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 5 lines|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|**Ld**|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|**oa**<br>**Full**|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00||



30 



##### Ingestion - Types of processing 

## **LOAD FULL-REFRESH** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 3 lines|
|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00||
|3<br>Day 2|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00||
|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 5 lines|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|**Ld**|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|**oa**<br>**Full**|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00||



31 



##### Ingestion - Types of processing 

## **INCREMENTAL LOAD** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 3 lines|
|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00||



###### Day 2 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|
|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|



32 



##### Ingestion - Types of processing 

## **INCREMENTAL LOAD** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 3 lines|
|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00||



###### Day 2 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|
|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|



33 



##### Ingestion - Types of processing 

## **INCREMENTAL LOAD** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 3 lines|
|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00||



###### Day 2 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|
|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|



34 



##### Ingestion - Types of processing 

## **INCREMENTAL LOAD** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 3 lines|
|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00||
|3<br>Day 2|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00||
|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|Processed: 2 lines|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|**Incremental**|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|<br>**Load**|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00||



35 



##### Ingestion - Types of processing 

## **INCREMENTAL LOAD** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|Processed: 3 lines|
|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Pendant||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant||
|**Order ID**<br>Day 2|**Date**|**Customer**|**Product**|**Total Value**|**Status**|Processed: 2 lines|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Cancelled|**Itl**|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|**ncremena**<br>**Load**|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|Finished||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|Pendant||



36 



##### Ingestion - Types of processing 

## **INCREMENTAL LOAD** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|Processed: 3 lines|
|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Pendant||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant||



###### Day 2 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|Processed: 2 lines|
|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Cancelled|**Il**|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|**ncrementa**<br>**Load**|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|Finished||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|Pendant||



37 



##### Ingestion - Types of processing 

## **TYPES OF PROCESSING** 

###### Dia 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|Processed: 3 lines|
|---|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Pendant|10/01/2015||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015||



38 



##### Ingestion - Types of processing 

## **TYPES OF PROCESSING** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|Processed: 3 lines|
|---|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Pendant|10/01/2015||
|Day 2<br>3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015||
|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|Processed: 3 lines|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Cancelled|11/01/20215||
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|Finished|11/01/2015||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|Pendant|11/01/2015||



39 



##### Ingestion - Types of processing 

## **TYPES OF PROCESSING** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|Processed: 3 lines|
|---|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Pendant|10/01/2015||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015||



Dia 2 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|Processed: 3 lines|
|---|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Cancelled|11/01/20215||
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|Finished|11/01/2015||
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|Pendant|11/01/2015||



40 



##### Ingestion - Types of processing 

## **TYPES OF PROCESSING** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|Processed: 3 lines|
|---|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015||
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015||
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Cancelled|11/01/20215|**Incremental load**<br>|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|Finished|11/01/2015|**Insert Overwrite**|
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|Pendant|11/01/2015||



41 



##### Ingestion - Types of processing 

## **TYPES OF PROCESSING** 

###### Day 1 

|**Order ID**|**Date**|**Customer**|**Product**|**Total Value**|**Status**|**Update Date**|
|---|---|---|---|---|---|---|
|1|10/01/2015|João da Silva|Flying Bicycle|R$ 150,00|Finished|10/01/2015|
|3|10/01/2015|Tony Stark|4-Wheel Bicycle|R$ 180,00|Pendant|10/01/2015|
|2|10/01/2015|Joana D’arc|Water Bike|R$ 200,00|Cancelled|11/01/20215|
|4|11/01/2015|Carlos Santos|Flying Bicycle|R$ 150,00|Finished|11/01/2015|
|5|11/01/2015|Edson Arantes|4-Wheel Bicycle|R$ 180,00|Pendant|11/01/2015|



###### Or you can use the database log itself: 

**This method is called CDC (change data capture) and is not simple to implement.** 

42 



Ingestion - Types of processing **SUMMARIZING** 

- Data source type: SQL, NoSQL, API, text, etc. 

- Access type: bank mirror, API, report, etc. 

- Environment: cloud, on-premises, or hybrid. 

- Frequency: weekly, daily, hourly, minute-by-minute, near real-time, or real-time. 

- Data volume in each pipeline run. 

- The type of processing: full, incremental, incremental + overwrite. 

43 



Lesson 4.9 - Stage: Transformation 





##### Stage: Transformation 

## **KEY POINTS** 

- Select the relevant business fields. 

- Filter out incorrect or incomplete data. 

- De-duplicate data. 

- Combine data from different data sources and/or tables. 

- Rename columns. 

- Create new fields and calculated metrics. 

- Sort data by one or more fields. 

- Remodel the data into a model of facts and dimensions. 

- Transpose or pivot tables. 

- Aggregate or disaggregate tables. 

45 



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

## Stage: Transformation **TRANSFORMATION LAYERS** 



<!-- Start of picture text -->
Data Warehouse<br>—_ ><br>                  Transform<br>Raw data Data Marts<br>i [|<br>46<br><!-- End of picture text -->



<!-- Start of picture text -->
Coasts<br><!-- End of picture text -->

## Stage: Transformation **TRANSFORMATION LAYERS** 



<!-- Start of picture text -->
Data Warehouse<br>Layer Intermediate<br>Raw data Staging Layer Data Marts<br>                  Transform<br><!-- End of picture text -->

47 



<!-- Start of picture text -->
Stage: Transformation<br>TRANSFORMATION LAYERS<br>Layer Layer Intermediate<br>Layer<br>Raw Staging Layer<br>Marts<br>4<br><!-- End of picture text -->

48 



<!-- Start of picture text -->
Stage: Transformation<br>TRANSFORMATION LAYERS<br>Layer Layer Intermediate<br>Layer<br>Raw Staging Layer<br>Marts<br>Anat<br><!-- End of picture text -->

49 



<!-- Start of picture text -->
Stage: Transformation<br>TRANSFORMATION LAYERS<br>Layer Layer Intermediate<br>Layer<br>Raw Staging Layer<br>Marts<br>FFED<br><!-- End of picture text -->

50 



## Stage: Transformation **TRANSFORMATION LAYERS** 



<!-- Start of picture text -->
Layer Layer Intermediate<br>Layer<br>Raw Staging Layer<br>Marts<br>DIM DIM<br>FCT<br>DIM DIM<br>51<br><!-- End of picture text -->



Lesson 4.10 - Transformation - DataOps 





## Transformation - DataOps **DATAOPS PILLARS** 

- Automation. 

- Collaboration. 

- Continuous integration and continuous delivery (CI/CD). 

- Analytics as a code. 

- Data quality and governance. 

- Monitoring and observability. 

- Agility and flexibility. 

53 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

## Transformation - DataOps **EXAMPLE** 



<!-- Start of picture text -->
Data Warehouse<br>Once a day<br>Dice<br>    Extract-Load<br>Raw data Final data<br>                  Transform<br>Models in SQL<br><!-- End of picture text -->

54 



## Transformation - DataOps **WHAT IS DBT?** 



<!-- Start of picture text -->
 dbt<br><!-- End of picture text -->

“dbt™ is a SQL transformation workflow that enables teams to deploy analytical code quickly and collaboratively while following software engineering best practices such as modularity, portability, CI/CD, and documentation. Now, anyone on the data team can confidently contribute to production-grade data pipelines.” 

55 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

##### Transformation - DataOps 

## **SEPARATION OF ENVIRONMENTS** 

##### **Data Warehouse** 



<!-- Start of picture text -->
Production<br>i S S Once a day marts C f 4 fonte_erp Cc) 4 schema 1 {<br>H; Bando de dados     Extract-Load intermediate DW Raw data Bando de dados Transform(branch main) fonte_crm MarchDW  Bando de dados schema 2 ::<br>: Produgao Dados Brutos Desenvolvimento Dashboard H<br>H staging fonte_planilhas schema 3 d<br>production.marts.dim_customers<br><!-- End of picture text -->

56 



<!-- Start of picture text -->
Corsi<br>Transformation - DataOps<br>SEPARATION OF ENVIRONMENTS<br>Production<br>Once a day<br>    Extract-Load DW Raw  Transform DW<br>data (branch main) March<br>at)<br>57<br><!-- End of picture text -->



<!-- Start of picture text -->
Corsi<br>Transformation - DataOps<br>SEPARATION OF ENVIRONMENTS<br>Carla (Eng. de analytics)<br>I'm sorry,<br>but I can't<br>Personal branch<br>help with<br>4 S<br>that.<br>Production<br>Once a day<br>    Extract-Load DW Raw  Transform DW<br>data (branch main) March<br>at<br><!-- End of picture text -->

58 



## Transformation - DataOps **SEPARATION OF ENVIRONMENTS** 



<!-- Start of picture text -->
Carla (Eng. de analytics)<br>I'm sorry,<br>but I can't<br>Personal branch<br>help with<br>that.<br>Production<br>Once a day<br>    Extract-Load DW Raw  Transform DW<br>data (branch main) March<br>Personal branch<br>DWJoão<br>João (Analytics Engineer)<br><!-- End of picture text -->

59 



## Transformation - DataOps **SEPARATION OF ENVIRONMENTS** 



<!-- Start of picture text -->
Carla (Eng. de analytics)<br>I'm sorry,<br>but I can't<br>Personal branch<br>help with<br>that.<br>Production<br>Once a day<br>    Extract-Load DW Raw  Transform DW<br>data (branch main) March<br>Personal branch<br>DWJoão<br>João (Analytics Engineer)<br><!-- End of picture text -->

60 



## Transformation - DataOps **SEPARATION OF ENVIRONMENTS** 



<!-- Start of picture text -->
Carla (Eng. de analytics)<br>I'm sorry,<br>but I can't<br>Personal branch<br>help with<br>that.<br>Production<br>Once a day<br>    Extract-Load DW Raw  Transform DW<br>data (branch main) March<br>Personal branch<br>DWJoão<br>João (Analytics Engineer)<br><!-- End of picture text -->

61 



Lesson 4.11 - DataOps - Code Versioning 





<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

## Transformation - DataOps **WHAT ARE BRANCHES?** 



<!-- Start of picture text -->
“Customer dimension created”<br>Branch feature/clientes<br>a y oN [> \ rN [>> ranch mat<br>— ) ; ——<— ) ranch main<br>ww wy yy ~ yy<br>“Merged branch<br>feature/customers”<br>- —_<br>———_—_————_:ss sks :sSMs<br>Commit history<br><!-- End of picture text -->

63 



<!-- Start of picture text -->
Consists<br><!-- End of picture text -->

## Transformation - DataOps **CODE VERSIONING** 



<!-- Start of picture text -->
Branch main | ( vos \ nl v0.2 v0.3LS vo. ) i: | Schemadeprodugaodbt_carla_aimeida | H<br>Development<br>branch<br>ee : dbt_joao_silva H<br>: \i<br><!-- End of picture text -->

64 



<!-- Start of picture text -->
ConsistsQD osc<br><!-- End of picture text -->

## Transformation - DataOps **CODE VERSIONING** 



<!-- Start of picture text -->
Branch main vot vo } { v0.3LS vos : Schema deprodugao H<br>— Ee) H dbt_carla_almeida H<br>Development<br>branch<br>—$—$—$— i dbt_joao_silva H<br>: Ji<br><!-- End of picture text -->

65 



## Transformation - DataOps **CODE VERSIONING** 



<!-- Start of picture text -->
Project<br>Launched Production Bench<br>Development bank<br><!-- End of picture text -->

66 



## Transformation - DataOps **CODE VERSIONING** 



<!-- Start of picture text -->
Project<br>Launched Production Bench<br>Development bank<br><!-- End of picture text -->

67 



## Transformation - DataOps **CODE VERSIONING** 



<!-- Start of picture text -->
Project  Production Bench<br>Launched<br>Development bank<br><!-- End of picture text -->

68 



Lesson 4.12 - DataOps - Test data and documentation 





## Transformation - DataOps **TESTING DATA WITH DBT** 

###### **Generic tests** 

- unique 

   - Checks if each value is unique. 

- not_null 

   - Checks whether each value is not null. 

- accepted_values 

   - Tests whether each value belongs to a defined list. 

- relationship 

   - Test whether each value has a relationship with a column in another table. 

70 



<!-- Start of picture text -->
ACADEMY<br><!-- End of picture text -->

## Transformation - DataOps **TESTING DATA WITH DBT** 

###### **Single tests** 

71 



<!-- Start of picture text -->
PD 0x<br>ACADEMY<br><!-- End of picture text -->

##### Transformation - DataOps 

## **DOCUMENTATION WITH DBT DOCS** 



<!-- Start of picture text -->
version<br>models:<br>name: events<br>description: This table contains clickstream events from the marketing website<br>columns:<br>- name: event_id<br>description: This is a unique identifier for the event<br>tests:<br>— unique<br>- not_null<br>- name: user-id<br>quote:<br>description: The user who performed the event<br>tests:<br>- not_null<br><!-- End of picture text -->

72 



## Transformation - DataOps **REMEMBERING...** 



<!-- Start of picture text -->
Extract & Load Transform Analytics ● Made in a modular way.<br>● Transformation in SQL.<br>ERP Bank<br>DW ● Governance.<br>Software CRM E-L ● Versioning.<br>Raw<br>Data<br>Data<br>●<br>Separation of environments.<br>JSON files<br>● Data testing.<br>dbt<br>Spreadsheets<br>Orchestration & Deployment<br>What does this mean? -> DataOps<br><!-- End of picture text -->

73 



Lesson 4.13 - Step: Pipeline orchestration 





Step - Pipeline orchestration **KEY POINTS** 

- Schedule data pipeline tasks. 

- Monitor the execution of tasks. 

- Notify users in case of failures. 

- Facilitate the management and visualization of stages from the data pipeline. 

- Ensure tasks are executed in the defined order (DAGs). 

75 





## Step - Pipeline orchestration **WHAT IS A DAG?** 



<!-- Start of picture text -->
2 4 7<br>1 5 6<br>3 8<br><!-- End of picture text -->

76 



## Step - Pipeline orchestration **EXAMPLE OF A DAG** 



<!-- Start of picture text -->
ERP extraction Loading Source test: ERP<br>dbt build commercial<br>Spreadsheet  Source test:<br>Loading<br>extraction spreadsheets<br>dbt build marketing<br>CRM extraction Loading Source test: CRM<br><!-- End of picture text -->

77 



## Step - Pipeline orchestration **EXAMPLE OF A DAG** 



<!-- Start of picture text -->
ERP extraction Loading Source test: ERP<br>dbt build commercial<br>Spreadsheet  Source test:<br>Loading<br>extraction spreadsheets<br>dbt build marketing<br>CRM extraction Loading Source test: CRM<br>Falha<br>Failure notification email: Impact<br>on marketing data<br><!-- End of picture text -->

78 



<!-- Start of picture text -->
ConsistsYD sca<br><!-- End of picture text -->

## Step - Pipeline orchestration **PIPELINE MONITORING** 



<!-- Start of picture text -->
Péaitiow acs bata Proing- —Browse~ Admin~ —Docs~ About<br>fon f] example_dag<br>BRCCUINGAE $7ceView<br>dtTask Duration WW Task'Tries © A.Landing Times Gai Betas 4 Code GRettesh Oekete<br>EMME Base date: 2019-10-22 12060 Numberofruns: 5  ¥ Run:  scheduled_2019-10-22T12:06:00+0000  |Layout:| Let->Right || Go<br>konProprarOperate)<br>F<br>collect_data_trom_database_1 | =<br>collect_data_trom_database_2 | aggregate_cotected_data_t | _| buil_a_report_using_transtormed_data<br>collectdata_from_extemal_api_1 }~=a transform _aggregated_dataee |—4 store_transformed_data_in_warenouse<br>TA =<br>collect_data_from_intemat_api_1 |— A —4 post_transformed_data_to_intemal_api<br>aggregate _colected_data 2 }~<br>collect_data_from_extemal_api_2 }- carry_out_alerting_using_transformed_data<br><!-- End of picture text -->

79 



<!-- Start of picture text -->
Corsi<br><!-- End of picture text -->

## Step - Pipeline orchestration **PIPELINE MONITORING** 



<!-- Start of picture text -->
PLAirFlow DAGs Toolsy Browsexy Adminy  Docs~<br>DAG: example2<br>E ZCISWRMCWME Run: 2015-01-07T00:00:00 anding Times = Gantt % Code<br>Started: 2015-02-01T20:22:22<br>Ended: 2015-02-01T20:22:22<br>Duration: 0<br>Quun_this_tast Beem 00000000o0000000000<br>run this SEBe@eeOOO000ooooooooo00000<br>Orunme_o SEBBB8—@80000000ooo0oo0o00000<br>Orunme_t SEBBB8—8800000000oo0oo000000<br>Orunme_2 SEBeB8—@800000000oo0oo0o00000<br>JOrunme_3 SEBB88—@800000000o0oo000000<br>Ornme4 SEBBBE—@800000000oo0oooo00000<br>Orunme_s SEEBBE—@80000000ooooooOo000<br>Onnme_6 SEBeB8—@800000000oo0ooooO0000<br>Onnme_7 SEBBBEE@—8O0C000oooooooOoo0o00<br>Ornmes SEBBB8—@8O00000oooooooo000<br>Onunme_9 SEBB88—@—800CO00oooooooOoo0o00<br>Oaiso_run_this SEBe@eCOOOO0ooooooooooo000<br>@rnnthis SEBe@@eOOOOCOoooooooooooo00<br><!-- End of picture text -->

80 



<!-- Start of picture text -->
(MN<br><!-- End of picture text -->

# **THANK YOU** 

81 

