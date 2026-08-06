Welcome
Module 2 - SQL for data analysis
Hello!
My name is
Henrique.
Team Leader - Data Analytics na Indicium
INDEX
● Overview
● Module objectives
● Expectations at the end of the module
Classroom 01
3
TABLE OF CONTENTS
● Overview
● Module objectives
● Expectations at the end of the module
4
Classroom 1
Overview
● Introduction to databases and SQL
● SQL queries
● Advanced queries in SQL
● Functions in SQL
● Database administration and
optimization
What shall we talk about?TABLE OF CONTENTS
● Overview
● Module objectives
● Expectations at the end of the module
5
Classroom 1
Overview
We will divide each class into the following
```
stages:
```
```
● Theoretical foundations (Slide)
```
```
● Practical classes (SQL)
```
Class structureTABLE OF CONTENTS
● Overview
● Module objectives
● Expectations at the end of the module
6
Classroom 1
Objectives
What is the purpose of the
module?
● Understanding the structure of
relational databases
● Learning to use SQL in a practical way
● Learn how to use functions, clauses,
and operators in SQL
TABLE OF CONTENTS
● Overview
● Module objectives
● Expectations at the end of the module
7
Lesson 1
Expectations
What can you expect from
the module?
● Translate business questions into
queries using SQL
● Master SQL and its functions, as well
as best practices for its use
● Understanding how databases work
What are databases?
Module 2 - SQL for data analysis
INDEX
● What are databases?
● What is a database used for?
● How do databases work?
● Getting to know the BanVic database
Classroom 03
9
WHAT ARE THEY?
DATABASES?
1011
They are organized and structured collections of
data stored in an electronic system.
● Store and manage information
● They commonly have a structure of columns
```
and rows (table).
```
WHAT ARE THEY?
DATABASES?
Definition
WHAT IS THE
PURPOSE OF A
DATABASE?
12
UTILITY
WHAT IS A DATABASE FOR?
Databases serve as accessible and
organized storage and management
for data for a specific purpose. They
can be used, for example, to store
data about customers, processes,
suppliers, and even social networks
within a company.
```
Example:
```
Financial institutions
13
Customers Accounts
Transactions
Database
14
With so much information about customers,
accounts, transactions, and more, it can be
difficult to keep everything organized and well
structured in a logical manner. This is where the
importance of a database comes in, in the
management and organization of information.
Volume of data and information
CHALLENGE
WHAT IS A DATABASE FOR?
HOW THEY WORK
DATABASES?
15
MANAGEMENT
HOW DO DATABASES WORK?
16
DBMSs are used to manipulate, organize,
access, and update data stored in a database.
They are responsible for translating queries into
information.
Some examples of DBMSs: Oracle, PostgreSQL,
Microsoft SQL Server, MySQL, among others.
```
Database Management System (DBMS)
```
OPERATION
HOW DO DATABASES WORK?
17
The operation of the database can be broken down
into three layers:
● Query layer: where the user queries the data.
```
Example: Return data from the customer
```
table.
● Processing layer: is where the DBMS
operates, translating the query into results
for the end user.
● Storage layer: This is where the raw data
that is queried is stored.
The layers of a database
GETTING TO KNOW
THE DATABASE
TO BANVIC
1819
As introduced at the beginning of this training, we
will act as data analysts, performing analyses that
add value to Banco Victoria, using the database
provided by them.
How does it work?
VICTORIA BANK
GETTING TO KNOW THE BANVIC DATABASE
20
What information
shall we analyze?
VICTORIA BANK
GETTING TO KNOW THE BANVIC DATABASE
Main databases
Module 2 - SQL for data analysis
INDEX
● Types of databases
● Relational database
● Non-relational database
● Cloud database
● Object-oriented database
Classroom 04
22
TYPES OF BANKS
DATA?
2324
To best handle data, each organization chooses the
most appropriate structure for storing its
information. Each type has its advantages and
disadvantages, and the choice depends on the type
of need.
Types of databases
DEFINITION
TYPES OF DATABASES
RELATIONAL
DATABASE
25
WHAT IS IT
RELATIONAL DATABASE
The relational database has a more
conventionally known structure for storing data.
It is called relational because of the network of
relationships it establishes between different
tables. In addition, it uses a language known as
```
SQL (Structured Query Language) to query and
```
manage this data/information.
● It is an infrastructure, with table
formats, columns, and rows.
● Each category of information has a
specific table for storage.
● Uses SQL for queries.
● Examples: Oracle, SQL Server, MySQL,
PostgreSQL.
26
Customer Table
name_costumer cpf_costumer email_costumer
João Silva 123.456.789-00 joao.silva20@gmail.com
Júlia Santos 456.123.789-00 julia_santoos@hotmail.com
Pedro Souza 789.456.123-00 souza_pedro@gmail.com
```
Example:
```
ADVANTAGES AND DISADVANTAGES
RELATIONAL DATABASE
```
Advantages:
```
● Well-defined structure
● Data integrity
● Efficient consultations
● Transaction support
27
```
Disadvantages:
```
● Limited scalability
● Limited flexibility
● High cost
NON-RELATIONAL
DATABASE
28
ADVANTAGES AND DISADVANTAGES
NON-RELATIONAL DATABASE
The non-relational database stores data in a
variety of ways, differing from the traditional
structure we have seen in relational databases.
In addition, it performs queries using NoSQL.
● It is an infrastructure without a specific
defined format.
● Stores data in graphs, documents,
columns, or key-value pairs.
```
● It uses NoSQL (Not Only SQL), that is,
```
not only SQL to query information.
● Examples: MongoDB, Cassandra, Redis,
Couchbase.
29
```
Example:
```
Key Values Documents
Graphs
ADVANTAGES AND DISADVANTAGES
NON-RELATIONAL DATABASE
```
Advantages:
```
● Scalability
● Flexibility
● Costs
30
```
Disadvantages:
```
● Difficulty in performing complex queries
● Lack of data integrity
● Scarcity of resourcesCLOUD DATABASE
3132
Cloud databases are databases that run on cloud
infrastructure, where computing, storage, and
networking resources are provided as a service by
the cloud provider.
● They can be relational or non-relational.
● They are fully hosted in the cloud
● Exemplos: Amazon Web Services, Google
Cloud Platform, Microsoft Azure, IBM Cloud,
Oracle Cloud, etc.
WHAT IS IT
CLOUD DATABASE
ADVANTAGES AND DISADVANTAGES
CLOUD DATABASE
```
Advantages:
```
● Scalability
● Availability
● Flexibility
● Reliability
● Safety
● Custo
● Remote access
33
```
Disadvantages:
```
● Supplier dependency
● Safety
● Network latency
● Internet dependency
OBJECT-ORIENTED
DATABASE
3435
```
Object-oriented databases (OODBMS) store and
```
manipulate your data as objects. This means that
instead of being stored as columns and tables, for
example, the data is organized into objects, as are
the methods used. In it, the data is represented as
objects, which can contain both data and behaviors
```
(methods) associated with that data.
```
WHAT IS IT
OBJECT-ORIENTED DATABASE
Contributor
Address
City
Country
Status
36
ADVANTAGES AND DISADVANTAGES
OBJECT-ORIENTED DATABASE
```
Advantages:
```
● More natural data modeling
● Flexibility
● Code reuse
● Performance
```
Disadvantages:
```
● Very steep learning curve
● Limited scalability
● Lack of standards
● Incompatibility with legacy systems
```
OVERVIEW:
```
ADVANTAGES AND
DISADVANTAGES
37
ADVANTAGES AND DISADVANTAGES
DATABASE
38
Advantages Disadvantages
```
Relational database - Well-defined structure;
```
- Data integrity;
- Efficient consultations;
- Transaction support.
- Limited scalability;
- Limited flexibility;
- High cost.
```
Non-relational database - Scalability;
```
- Flexibility;
- Costs.
- Difficulty in performing more complex
```
queries;
```
- Lack of data integrity;
- Scarcity of resources.
```
Cloud database - Scalability;
```
- Availability;
- Flexibility;
- Reliability;
- Safety;
- Cost;
- Remote access.
- Supplier dependency;
- Safety;
- Network latency;
- Internet dependency
```
Object-oriented databases - More natural data modeling;
```
- Flexibility;
- Code reuse;
- Performance.
- Very steep learning curve;
- Limited scalability;
- Lack of standards;
- Incompatibility with legacy systems.
39
IN THE NEXT CLASS
WE WILL TALK ABOUT
Let's talk about the structure best known and most
widely used by companies around the world, going
over some key concepts that will help us better
understand how it works.
Relational databases
Relational database
Module 2 - SQL for data analysis
41
INDEX
● Introduction to relational databases
● Structure
● Relationship between tables
Classroom 04
INTRODUCTION
42
HOW IT BEGAN:
In 1970, Edgar Frank Codd created relational models in
his paper, which later became the basis for relational
databases.
Large volumes of data
1960 Information systems were beginning
to handle large amounts of data.
“A Relational Model of Data for
Large Shared Data Banks”1970
Paper published by Edgar Codd
Relational models as we
know them today
2025
Relational databases
Relational databases
account for 72% of
global popularity.
It is the most widely
used database model in
the world.
44
RELATIONAL
DATABASE
45
REVISITING THE CONCEPT
RELATIONAL DATABASE
46
The relational database has a more conventionally
known structure for storing data. It is called
relational because of the network of relationships it
establishes between different tables. In addition, it
```
uses a language known as SQL (Structured Query
```
```
Language) to query and manage this
```
data/information.
● It is an infrastructure, with table formats,
columns, and rows.
● Each category of information has a specific
table for storage.
● Uses SQL for queries.
● Examples: Oracle, SQL Server, MySQL,
PostgreSQL.
Customer Dimension
name_costumer pk_costumer email_costumer
João Silva 1 joao@gmail.com
Júlia Santos 2 julia@hotmail.com
Pedro Souza 3 pedro@gmail.com
47
Costumers
first_name cod_costumer email cep
João 1 joao@gmail.com 8800000
Júlia 2 julia@hotmail.com 9900000
Pedro 3 pedro@gmail.com 1100000
```
Column: has a single
```
data type
Text - char Number - int
REVISITING THE CONCEPT
RELATIONAL DATABASE
48
REVISITING THE CONCEPT
RELATIONAL DATABASE
```
Registration: storage of
```
information
```
Field: cell
```
Customers
first_name cod_customer email cep
João 1 joao@gmail.com 8800000
Júlia 2 julia@hotmail.com 9900000
Pedro 3 pedro@gmail.com 1100000
49
REVISITING THE CONCEPT
RELATIONAL DATABASE
Primary key:record identifier
undefined
Customers
first_name cod_costumer email cep
João 1 joao@gmail.com 8800000
Júlia 2 julia@hotmail.com 9900000
Pedro 3 pedro@gmail.com 1100000
50
PRIMARY KEY
RELATIONAL DATABASE
Clientes
first_name cod_costum
er
email
João Silva 1 joao@gmail.com
Júlia Santos 2 julia@hotmail.com
Pedro Souza 3 pedro@gmail.com
- They are responsible for identifying a record
in the table.
- They must be unique and not null. They can
```
be a CPF (Individual Taxpayer ID) or a unique
```
registration ID.
```
Concept:
```
51
EXTERNAL KEY
RELATIONAL DATABASE
- They are responsible for assigning an event
to a record in the table.
- They don't have to be unique, since multiple
events can occur for the same key.
```
Concept:Accounts
```
date_opening cod_costu
mer
Total_balance
01/08/2025 1 1000
02/08/2025 2 500
05/10/2025 3 255
52
HOW DOES IT WORK?
RELATIONAL DATABASE
Customers
first_name cod_costu
mer
email
João Silva 1 joao@gmail.com
Júlia Santos 2 julia@hotmail.com
Pedro Souza 3 pedro@gmail.com
Contas
date_opening cod_costu
mer
Total_balance
01/08/2025 1 1000
02/08/2025 2 500
05/10/2025 3 255
Primary key [pk]Foreign key [fk]
- Performance improvement
- Ease of entering and linking data
- Avoid inconsistencies and poor-quality data
Benefits
53
RELATIONSHIPS
RELATIONAL DATABASE
What is SQL?
INDEX
● Introduction to SQL
● Usage
● Structure
Classroom 06
55
Introduction to SQL
Basic concepts
Concepts
```
SQL (Structured Query Language) is a
```
programming language used to manage and
manipulate data in relational databases.It is through SQL that we are able to retrieve
information from the data stored in the
database, using filters and specifying
parameters for the query.
Efficient information retrieval
Used for managing and manipulating data
stored in a relational database.
Management and handling
Use this to view data entered into the
database and update it as needed.
Viewing and updating data
57
Structured
Question
Language
Usage
What is SQL?
58
User
Application
Database
Information
“Select a list of active customers for the year
2025”
Executing the database
query
Feedback to the end user
SQL
Usage
What is SQL?
59
Estrutura
What is SQL?
60
Select * from costumers
Select
something
from
somewhere
Specifies the source
table in the database
Operator
meaning “all
columns”
Source table
customers
first_name cod_costumers email
João 1 joao@gmail.com
Júlia 2 julia@hotmail.com
Pedro 3 pedro@gmail.com
Structure
What is SQL?
61
SELECT first_name,
cod_customer FROM customers
costumer
first_name cod_costumer
João 1
Júlia 2
Pedro 3
Columns we want to
select
Structure
What is SQL?
62
Select * from
dim_costumer
```
Clauses: Clauses are used to modify the query and specify additional conditions. Examples: SELECT, FROM,
```
WHERE, GROUP BY, ORDER BY, HAVING, JOIN…
```
Functions: Functions are used to perform calculations on data, such as counting, summing, finding the
```
maximum or minimum value, and so on. Examples: COUNT, SUM, MAX, MIN, AVG…
```
Transactions: Transactions are used to ensure that database operations are either successfully completed or
```
rolled back if an error or problem occurs. Transactions typically involve multiple database operations, such as
```
inserts (INSERT), updates (UPDATE), and deletes (DELETE or DROP).
```
Structure
What is SQL?
63
Select * from
dim_clientes
Do I need to apply a filter?
Do I need to sort by a specific criterion?
Do I need to group them by some criterion?
WHERE
ORDER BY
GROUP BY
Examples of clauses:
Concepts for the upcoming classes…
Types of SQL statements
Basic concepts
SQL Commands
DML
SELECT
INSERT
UPDATE
DELETE
MERGE
```
Commands:
```
DDL
CREATE
ALTER
DROP
RENAME
TRUNCATED
```
Commands:
```
DCL
GRANT
REVOKE
```
Commands:
```
65
DTL
COMMIT
ROLLBACK
```
Commands:
```
66
Commands for inserting, updating, deleting, or
merging rows and columns of data. DML
commands modify the data, but not its structure or
permissions.
● SELECT: Returns data from one or more
tables.
● INSERT: Inserts new data into a table.
● UPDATE: Modifies existing data in a table.
● DELETE: Removes data from a table.
● MERGE: Combines data from two tables,
inserting, updating, or deleting records
based on the matches.
Data Manipulation Language
DML
SQL Commands
Examples
DML
67
UPDATE clientes SET email = 'joao.silva@novodominio.com'
```
WHERE cod_cliente = 1;
```
```
DELETE FROM clientes WHERE cod_cliente = 1;
```
Update the email field for the customer with
```
customer_id = 1 to the new email address.
```
Delete the records from the table where
```
customer_id = 1.
```
68
Commands for creating, modifying, and deleting
database objects, such as tables. DDL commands
modify the structure, but not the content.
● CREATE: Creates new objects in the
database, such as tables and indexes.
● ALTER: Modifies the structure of existing
objects in the database.
● DROP: Permanently removes objects from
the database, such as tables and indexes.
● RENAME: Renames existing objects in the
database.
● TRUNCATE: Removes all data from a table
without deleting its structure.
Data Definition Language
DDL
SQL Commands
Examples
DDL
69
```
ALTER TABLE customers ADD phone VARCHAR(15);
```
```
DROP CUSTOMERS TABLE;
```
Modify the customers table by adding a "phone"
```
field of type VARCHAR(15).
```
Deletes the customers table from the database.
70
Commands to grant and revoke permissions to view
and edit data objects.
● GRANT: Grants access permissions and
control over database objects to users or
roles.
● REVOKE: Revokes permissions previously
granted to users or roles in the database.
Data Control Language
DCL
SQL Commands
Examples
DCL
71
```
GRANT SELECT, INSERT ON clientes TO usuario_x;
```
```
REVOKE INSERT ON clientes FROM usuario_x;
```
Grant user_x permission to use SELECT and INSERT
on the clients table.
Revoke user_x's permission to use INSERT on the
'clientes' table.
72
Commands for saving or rolling back changes made
in transactions using DML commands.
● COMMIT: Commits the changes made to the
database during a transaction, making them
permanent.
● ROLLBACK: Undoes the changes made to
the database during a transaction, reverting
them to their previous state.
Data Transaction Language
DTL
SQL Commands
Examples
DTL
73
```
COMMIT;
```
```
ROLLBACK;
```
After making several changes, use COMMIT to save
them all.
If an error occurs, you can undo the changes.
SELECT and FROM
Structure
SELECT and FROM
75
SELECT columns FROM customers
Select
something
from
somewhere
Specifies the source
table in the database
The area where we
select the columns we
want to choose
Source table
Structure
SELECT and FROM
76
select * from costumers
```
limit 10;
```
To select all columns,
you can use the *
```
(asterisk)
```
Allows you to limit the
number of rows
returned.
ORDER BY
Structure
ORDER BY
78
select cod_costumer, first_name
from costumers order by
```
cod_costumer;
```
Sort the query results by
the pk_cliente field.
Structure
ORDER BY
79
select cod_costumer, first_name from
```
costumers order by cod_costumer DESC ;
```
It specifies that the sort
order must be
descending. By default,
ORDER BY sorts in
```
ascending order (ASC)
```
Sort the query results by
the pk_cliente field.
Structure
ORDER BY
80
DESCASC
```
(default)
```
cod_costumer first_name
1 João
2 Cléber
3 Júlia
cod_costumer first_name
3 Júlia
2 Cléber
1 João
WHERE
Structure
WHERE
82
select * from costumer where
```
client_type = “PF”
```
Specifies a filter for
the query we are
running.
Filtering by values
WHERE
83
select name, state from agencies
```
where State = ‘SP’;
```
Specifies a value filter for the query we
are running. In this case, only agencies
located in the state of São Paulo.
name State
Ag. Matriz SP
Ag. Tatuapé SP
Ag. Jardins SP
Filtering for null values
WHERE
84
select name, uf from agencies
where state is null
Specifies a filter for null values in the query
we are running. In this case, a list of
agencies where the state field is empty
```
(null).
```
name state
Ag. Digital 1 null
Ag. Digital 2 null
Ag. Digital 3 null
Filtering by logical operators
WHERE
85
select name, state from agencies
where date_opening >= ‘01/01/2020’
Specifies a filter with a logical
operator for the query we are running.
In this case, a list of agencies that
opened after January 1, 2020.
name state
Ag. Criciúma SC
Ag. Matriz SP
Ag. Vitória ES
Filter by comparisons
WHERE
86
select name, state from agencies
where state <> ‘PR’
Specifies a filter for the query we are running. In this
case, agencies where the state is not Paraná.
name state
Ag. Criciúma SC
Ag. Matriz SP
Ag. Pelotas RS
LIKE clause
88
Structure
LIKE clause
select * from costumers where
first_name LIKE ‘João%’
The LIKE clause is used to compare a column
with a text string specified in the clause. In the
example, only customer names that begin with
“João” will be selected.
You can also use NOT LIKE to achieve the same
result, but in an exclusive manner.
Structure
LIKE clause
89
LIKE ‘Jo%’
LIKE ‘%Pedro’
LIKE ‘%Paulo %’
The % operators within the LIKE clause are used to create flexible patterns, meaning they allow for any text to appear
before or after the specified text.
```
Examples:
```
In this case, our search will return only names that begin with “Jo,” such as
Joaquim, João, Jorge, etc.
In this second case, our query will return only names ending in “Pedro,”
such as João Pedro and Pedro.
In this third case, our search will return names that contain the name Paulo
anywhere in the name, such as João Paulo and Paulo Henrique.
Clause IN
Structure
Clause IN
91
SELECT * FROM agencies
```
where state in(‘PA’, ‘PB’, ‘SP’, ‘AC’)
```
The IN clause is used to specify a list of values
```
to be filtered (as in the WHERE clause example).
```
In the example above, only the states of Pará,
Paraíba, São Paulo, and Acre will be selected.
We can also use NOT IN to exclude items from
the list.
BETWEEN clause
Structure
BETWEEN clause
93
select * from agencies where
date_opening between ‘01/01/2024’
and ‘12/31/2024’
The BETWEEN operator is used to select values
within a specific range. It is often used to
retrieve records that fall within a range of values.
You can also use NOT BETWEEN to retrieve
values outside the desired range.
Structure
BETWEEN clause
94
select * from agencies where
date_opening between ‘01/01/2024’
and ‘12/31/2024’
01/01/2024 12/31/2024
Arithmetic Operators
What are they for?
Arithmetic Operators
96
Arithmetic operators in SQL are used to perform mathematical operations on numerical values stored in the database.
Functions such as addition, multiplication, division, subtraction, and other arithmetic operations can be performed in SQL.
```
Examples:
```
```
Addition (+): An arithmetic operator used to add one column to another. Example:
```
```
Subtraction (-): An arithmetic operator used to subtract one column from another. Example:
```
```
Division (/): An arithmetic operator used to divide one column by another. Example:
```
select coluna_1 + coluna_2 from tabela
select coluna_1 - coluna_2 from tabela
select coluna_1 / coluna_2 from tabela
What are they for?
Arithmetic Operators
97
Arithmetic operators in SQL are used to perform mathematical operations on numerical values stored in the database.
Functions such as addition, multiplication, division, subtraction, and other arithmetic operations can be performed in SQL.
```
Examples:
```
```
Multiplication (*): An arithmetic operator that returns the product of one column and another. Example:
```
```
Absolute Value (ABS( )): An arithmetic operator that returns the absolute value of a column. Example:
```
```
Rounded Value (ROUND( )): Arithmetic operator that returns the rounded value of a column. Example:
```
select coluna_1 * coluna_2 from tabela
```
select abs(coluna_1 - coluna_2) from tabela
```
```
select round(coluna_1 / coluna_2, 2) from tabela
```
Logical Operators
What are they for?
Logical Operators
99
Logical operators are used to combine conditions in a query and obtain more precise and specific results. These
operators allow you to specify the relationships between the conditions and filters applied to a query.
Operator AND
This is equivalent to “E” and specifies that only values that meet both specified criteria will be returned.
SELECT name, state FROM agencies
where date_opening >= ‘01/01/2020’ and
```
State= 'PR'
```
What are they for?
Logical Operators
10
0
Operator OR
This is equivalent to “OR” and specifies that only values that meet at least one of the specified criteria will be returned
```
(they may meet both).
```
SELECT name, state FROM agencies
where date_opening >= ‘01/01/2020’ or state
= ‘PR’
What are they for?
Logical Operators
10
1
Operator NOT
This is equivalent to “NO” and specifies that only values that do not meet the specified criteria will be returned.
select name_costumer, state from
dim_costumer where not state = ‘Pará’
Group by
Structure
Group by
10
3
select num_conta,
```
sum( valor_transacao ) from transacoes
```
group by num_conta
The GROUP BY clause is used to group rows
based on common values in one or more
columns. It allows you to perform operations
such as sum, average, maximum, minimum, or
count. The GROUP BY clause is usually used in
conjunction with an aggregate function. We’ll
cover aggregate functions in more detail shortly.
Structure
Group by
10
4
select num_conta ,
```
sum( valor_transacao ) from transacoes
```
group by num_contaIn the specific case described above, the
GROUP BY clause will return the sum of the
transaction values for each account_id, creating
a list of account_ids and their respective total
transaction values.
Having
Structure
Having
10
6
select
number of accounts
```
, sum(transaction_value) < a0> as
```
sum
from transactions
group by num_conta
having soma > 100 The HAVING clause is used to filter a query aftergrouping. In other words, it is always used after
the GROUP BY clause. The GROUP BY clause
groups the rows in the table based on the
selected columns, and the HAVING clause
filters the result of that grouping.
Structure
Having
10
7
select
number of accounts
```
, sum(transaction_value) < a0> as
```
sum
from transactions
group by num_conta
having sum > 100
In this example, our filtered list will only contain
the account_ids whose total transaction amount
is greater than 100.
Case when
Structure
Case when
10
9
select
case
when date_opening < 01/01/2019
then ‘Old Agency’
else ‘New Agency’
end of the classification
from agencies
The CASE WHEN is an operation performed on the values of one or more columns that returns a new column
containing the result of the condition. It allows you to evaluate an expression or condition and return a result based
on that evaluation.
Structure
Case when
11
0
select
case
when date_opening < 01/01/2019
then ‘Old Agency’
else ‘New Agency’
end of the classification
from agencies
The CASE WHEN is an operation performed on the values of one or more columns that returns a new column
containing the result of the condition. It allows you to evaluate an expression or condition and return a result based
on that evaluation.
For the example given, we created a new
column called classification, which specifies
that agencies with an opening date prior to
2019 will be classified as “Old Agencies”,
while those opened after that date will be
classified as “New Agencies”.
Join
As a reminder…
Join
11
2
How can we use data from
more than one table to
perform an analysis?
11
Structure
Join
11
4
A JOIN is an SQL operation that combines data from two or more tables in a single query. JOINs are used to link
```
tables based on common columns (keys) and retrieve data that is not available in a single table. The equality
```
between the columns is specified in the ON clause.
```
Example:
```
customers
cod_cliente
first_name
transactions
cod_cliente
transaction_value
Create a list of customer names and the
total amount of their transactions.
In this scenario, we use a JOIN.
Structure
Join
11
5
select
customers.first_name
, accounts.available_balance
from accounts
JOIN customers ON
accounts.customer_id =
customers.customer_id
The JOIN is performed using a common key between the two
tables. This allows us to link data across the two tables, enabling us
to perform analyses using fields from each.
```
Tipos: INNER JOIN (JOIN)
```
Join
11
6
from accounts
inner join customers on
accounts.customer_id =
customers.customer_id
The JOIN we just learned about is the INNER JOIN. It returns only the
records that exist in both tables. In the Venn diagram shown here, only
the intersection between the two tables would be selected.Table 1 Table 2
```
Types: INNER JOIN (JOIN)
```
Join
11
7
Table 1
A
B
C
Table 2
D
B
E
Results Table
B B
```
Types: LEFT JOIN
```
Join
11
8
from accounts
LEFT JOIN customers ON
accounts.customer_id =
customers.customer_id
```
The LEFT JOIN returns all rows from the left table (the first table
```
```
mentioned in the join) and the matching fields from the right table (the
```
```
second table mentioned). In the example below, our first table would be
```
```
accounts (since it is the first one mentioned in the FROM clause) and
```
```
customers would be our second table (from which only the rows that
```
```
match the first table are selected).
```
Table 1 Table 2
```
Types: LEFT JOIN
```
Join
11
9
Table 1
A
B
C
Table 2
D
B
E
Results Table
A null
B B
C null
```
Types: RIGHT JOIN
```
Join
12
0
from accounts
RIGHT JOIN customers ON
accounts.customer_id =
customers.customer_id
```
The RIGHT JOIN returns all rows from the right table (the second table
```
```
mentioned in the join) and the matching fields from the left table (the first
```
```
table named). In the example below, our first table would be accounts
```
```
(from which only the records in common with the second table are
```
```
selected), and customers would be our first table (from which all records
```
```
are selected).
```
Table 1 Table 2
```
Types: RIGHT JOIN
```
Join
12
1
Table 1
A
B
C
Table 2
D
B
E
Results Table
null D
B B
null E
```
Types: FULL JOIN
```
Join
12
2
from accounts
FULL JOIN customers ON
accounts.customer_id =
customers.customer_id
A FULL JOIN returns all rows from both tables, even those that have no
```
matching entries. For fields where there is no match (customer_id =
```
```
customer_id), it returns blank values for the first (or second) table.Table 1 Table 2
```
```
Types: FULL JOIN
```
Join
12
3
Table 1
A
B
C
Table 2
D
B
E
Table Result
A null
B B
C null
null D
null E
```
Types: CROSS JOIN
```
Join
12
4
from accounts
CROSS JOIN customers
The CROSS JOIN combines each row of one table with each row of
another table. Thus, the result is the Cartesian product of the two tables.
In this type of JOIN, it is not necessary to specify the ON clause, since it
will combine all rows from both tables.
```
Types: CROSS JOIN
```
Join
12
5
Table 1
A
B
C
Table 2
D
B
E
Tabela Result
A D
A B
A E
B D
C D
…
```
Types: SELF JOIN
```
Join
12
6
from accounts
JOIN accounts on t2 where
t2.customer_id
customer_id
A SELF JOIN is a join between a table and itself. This can be useful when
a table contains information that needs to be combined with itself. For
example, it could be used to compare values within the same column
across different rows to identify duplicate data, to obtain hierarchical
information, and so on.
```
Types: SELF JOIN
```
Join
12
7
Table 1
A
B
C
Table 1
A
B
C
Tabela Result
A A
B B
C C
Union
Structure
Union
12
9
The UNION clause combines the results of two or more tables into a single result set, increasing the number of rows.
The final table contains all rows that meet the criteria of the preceding queries, without duplicating any rows.
```
Example:
```
clients_br
customer_cod first_name
1 João
2 Ana
Create a single list of customer names,
combining Brazil and the United States.
In this scenario, we would use UNION.
us_customers
customer_cod first_name
3 John
4 Amanda
Structure
Union
13
0
clients_br
customer_cod first_name
1 João
2 Ana
us_customers
customer_cod first_name
3 John
4 Amanda
select
customer_cod
, first_name
from clients_br
union
select
customer_cod
, first_name
from us_customers
Structure
Union
13
1
clients
customer_cod first_name
1 João
2 Ana
3 John
4 Amanda
select
customer_cod
, first_name
from clients_br
union
select
customer_cod
, first_name
from us_customers
Functions
What are they for?
Functions
13
3
```
Functions in SQL are procedures that accept one or more arguments (inputs) and return a result (output). They can be
```
used in expressions or queries to perform calculations or manipulate data. They are also very useful for simplifying
queries and reducing code redundancy.
We can classify functions into three types, which are:
Aggregation functions:
These are functions used to calculate a value from a set, as we saw in some examples earlier.
```
Examples:
```
- SUM( ): Used to sum values based on the aggregation defined in GROUP BY.
- COUNT( ): Used to count values based on the aggregation defined in GROUP BY.
- AVG( ): Used to calculate the average based on the aggregation defined in GROUP BY.
- MIN( ): Used to calculate the minimum value based on the aggregation defined in GROUP BY.
- MAX( )Used to calculate the maximum value for the aggregation defined in GROUP BY.
What are they for?
Functions
13
4
Scalar Functions:
Scalar functions, on the other hand, are used to manipulate individual data points. They are used to standardize
formatting, remove spaces, concatenate columns, and so on.
```
Examples:
```
- UPPER( ): Converts the values in the selected column to uppercase.
- LOWER( ): Converts the values in the selected column to lowercase.
- TRIM( ): Used to remove whitespace from column values.
- CONCAT( ): Used to concatenate values from one column with another.
- YEAR( ): Used to return the year from a date column.
- MONTH( ): Used to return the month from a date column.
13
5
What are they for?
Functions
```
Analytic Functions (Window Functions):
```
Analytical functions, unlike scalar and aggregation functions, are used to perform advanced calculations on a dataset.
```
Examples:
```
- RANK( ): Assigns a rank to the values based on the defined window.
- FIRST_VALUE( ): Identifies the first value in the column based on the defined window.
- LAST_VALUE( ): Returns the last value in the column based on the defined window.
Special Features
Functions
13
6
Aggregate Functions
What are they for?
Aggregate Functions
13
8
Aggregation functions:
These are functions used to calculate a value from a set, as we saw in some examples earlier.
Examples we will cover:
- SUM( ): Used to sum values based on the aggregation defined in GROUP BY.
- COUNT( ): Used to count values based on the aggregation defined in GROUP BY.
- AVG( ): Used to calculate the average based on the aggregation defined in GROUP BY.
- MIN( ): Used to calculate the minimum value based on the aggregation defined in GROUP BY.
- MAX( )Used to calculate the maximum value for the aggregation defined in GROUP BY.
Scalar Functions
Types
Scalar Functions
14
0
Scalar Functions:
We can divide scalar functions into four groups: text functions, numeric functions, date and time functions, and
conversion functions.
Text functions:
- UPPER( ): Converts the values in the selected column to uppercase.
- LOWER( ): Converts the values in the selected column to lowercase.
- TRIM( ): Used to remove whitespace from column values.
- CONCAT( ): Used to concatenate values from one column with another.
Types
Scalar Functions
14
1
Scalar Functions:
We can divide scalar functions into four groups: text functions, numeric functions, date and time functions, and
conversion functions.
Numerical functions:
- ABS( ): Returns the absolute value of the column, ignoring the negative sign.
- ROUND( ): Rounds the value in the column based on the specified number of decimal places.
- CEIL( ): Returns the largest integer greater than or equal to the value in the column.
- FLOOR( ): Returns the smallest integer less than or equal to the value in the column.
Types
Scalar Functions
14
2
Scalar Functions:
We can divide scalar functions into four groups: text functions, numeric functions, date and time functions, and
conversion functions.
Date and time functions:
- YEAR( ): Used to return the year from a date column.
- MONTH( ): Used to return the month from a date column.
- DAY( ): Used to return the day of the week from a date column.
- NOW( ): Used to return the current date and time.
- DATEADD( ): Used to add days to a date column.
Types
Scalar Functions
14
3
Scalar Functions:
We can divide scalar functions into four groups: text functions, numeric functions, date and time functions, and
conversion functions.
Conversion functions:
- CAST( ): Converts the data type of the values in the selected column to another type.
- CONVERT( ): Converts a value from one data type to another (used in some DBMSs such as SQL Server).
- COALESCE( ): Replaces null values in a column with other specified types of values.
Analytical Functions
What are they for?
Analytical Functions
14
5
Analytical Functions:
Analytical functions are used to perform advanced calculations on a dataset, using aggregation functions to summarize
and categorize data. They allow you to perform aggregate calculations on subsets of data, typically defined by an OVER
clause.
```
Application:
```
Unlike regular aggregation functions, which return a single aggregate value for an entire dataset, analytical functions
return an aggregate value for each row in a dataset, based on user-specified rules.
```
select customer_code, sum( valor_transacao )
```
```
over (partition by client_type )...
```
Types
Analytical Functions
14
6
```
Structure:
```
Analytical functions use the OVER operator in their syntax, as shown below:
```
select cod_cliente, sum( valor_transacao ) over
```
```
(partition by tipo_conta ) as soma_tipo_conta...
```
The OVER PARTITION BY is used to group rows
based on common values in one or more
columns, but without having to restrict the query
to those same columns, as is the case with
```
SUM( ) + GROUP BY.
```
cod_client soma_tipo_con
ta
1 95000
2 200000
PF
PJ
Types
Analytical Functions
14
7
Analytical Functions:
We can divide analytical functions into five groups: window functions, analytical aggregation functions, ratio functions,
shift functions, and statistical aggregation functions.
Window functions:
- RANK( ) OVER (PARTITION BY..): Creates a ranking based on the specified criteria and also generates tie-breaking
values when the chosen criteria are identical.
- ROW_NUMBER( ) OVER (PARTITION BY..): Creates a numerical sort based on the criteria specified for each row,
but does not generate tie-breaking values when the selected criteria are identical.
Types
Analytical Functions
14
8
Analytical Functions:
We can divide analytical functions into five groups: window functions, analytical aggregation functions, ratio functions,
shift functions, and statistical aggregation functions.
Analytical Aggregation Functions:
- SUM( ) OVER (PARTITION BY..): Generates a sum of values according to the aggregation defined by PARTITION
BY.
- COUNT( ) OVER (PARTITION BY..): Generates a count of values according to the aggregation defined by
PARTITION BY.
Types
Analytical Functions
14
9
Analytical Functions:
We can divide analytical functions into five groups: window functions, analytical aggregation functions, ratio functions,
shift functions, and statistical aggregation functions.
Ratio Functions:
- PERCENT_RANK( ) OVER (PARTITION BY..): Returns a percentage value representing a row's rank relative to other
rows, between 0 and 1, based on the specified criteria.
- CUME_DIST( ) OVER (PARTITION BY..): Calculates the cumulative distribution of a row within a window,
representing the percentage of rows whose values are less than or equal to the value of the current row.
Types
Analytical Functions
15
0
Analytical Functions:
We can divide analytical functions into five groups: window functions, analytical aggregation functions, ratio functions,
shift functions, and statistical aggregation functions.
Shift Functions:
- FIRST_VALUE( ) OVER (PARTITION BY..): Identifies the first value in the column based on the defined window.
- LAST_VALUE( ) OVER (PARTITION BY..): Identifies the last value in the column based on the defined window.
Types
Analytical Functions
15
1
Analytical Functions:
We can divide analytical functions into five groups: window functions, analytical aggregation functions, ratio functions,
shift functions, and statistical aggregation functions.
Statistical Aggregation Functions:
- STDEV( ) OVER (PARTITION BY..): Returns the standard deviation based on the criteria specified in the
PARTITION BY clause.
- VAR( ) OVER (PARTITION BY..): Returns the variance according to the criteria specified in PARTITION BY.Text Manipulation Functions
What are they for?
Text manipulation functions
15
3
Some of the most commonly used scalar functions are text functions. There are numerous text formatting functions in
SQL. Some of them are only available in certain versions of SQL.
Text manipulation functions:
- REPLACE( ): Replaces a specified pattern of text with another in a column.
- RIGHT( ): Used to select the characters to the right of the text in a column.
- LEFT( ): Used to select the values to the left of the text in a column.
- SPLIT_PART( ): Used to split the text in a column based on a specified delimiter.
Creating Tables and Views
Managing tables…
Creating Tables and Views
15
5
As we’ve seen, now that we’ve learned about SQL, you might be wondering: How do you manage and create a large
number of highly complex tables?
Understanding CTEs
Creating Tables and Views
15
6
To make it easier to create complex queries—and, consequently, tables and views—we can use what are known as CTEs
```
(Common Table Expressions). CTEs are a way to organize code and save query results for later use within another query.
```
Use of the CTE:
```
with cte_1 as(
```
select
column 1
from 'tabelaX'
```
)
```
```
, cte_2 as(
```
select
columns_1
from cte_1
```
)
```
select * from cte_2
First CTE
Second CTE
Understanding CTEs
Creating Tables and Views
15
7
To make it easier to create complex queries—and, consequently, tables and views—we can use what are known as CTEs
```
(Common Table Expressions). CTEs are a way to organize code and break it down into steps, saving query results for later
```
use within another query.
Use of the CTE:
```
with cte_1 as(
```
select
column 1
from 'tabelaX'
```
)
```
```
, cte_2 as(
```
select
columns_1
from cte_1
```
)
```
select * from cte_2
Level 1
Level 2
Level 3
We reference the first CTE in the
second, and finally select the final
result from that join.
Structure of the CTEs
Creating Tables and Views
15
8
Use of the CTE:
```
with cte_1 as(
```
select
column 1
from 'tabelaX'
```
)
```
select * from cte_1
We start writing CTEs with the
`WITH` keyword, which is responsible
for defining what each CTE is.
Structure of the CTEs
Creating Tables and Views
15
9
Use of the CTE:
```
with cte_1 as(
```
select
column 1
from 'tabelaX'
```
)
```
select * from cte_1
Next, we begin defining the CTE, with the alias
```
(name) set, and the opening parentheses (where
```
```
we will insert the query).
```
Structure of the CTEs
Creating Tables and Views
16
0
Use of the CTE:
```
with cte_1 as(
```
select
column 1
from 'tabelaX'
```
)
```
select * from cte_1
Finally, a final SELECT statement
outside the CTE definition, which will
return its result.
Managing and creating tables
Creating Tables and Views
16
1
With the help of CTEs, we can manage the process of creating complex queries and new tables, since they help us break
the code down into steps.
User Management
Users in the database
User Management
16
3
As we’ve seen, a relational database can contain many tables. But how can we organize user access to them in a
structured way?
Sensitive Information
Administrator
Users in the database
User Management
16
4
As we’ve seen, a relational database can contain many tables. But how can we organize user access to them in a
structured way?
Sensitive Information
Administrator
Analyst
Managing Database Users
User Management
16
5
For efficient user management, some DBMSs feature what are known as “roles,” which are essentially like job titles within
```
the database; they are assigned to a user and grant them permissions. Databases that offer this functionality include
```
PostgreSQL, MySQL, SQL Server, and others.
Administrator
Analyst
Administrative Role
Basic Role
Commands
User Management
16
6
There are commands used to create roles, users, and define access permissions, among other functions, within a
database.
CREATE ROLE: Creates a role to be assigned to a user within a database at a later time. Example: CREATE ROLE
```
MANAGER;
```
ALTER ROLE: Modifies an existing role within a database. Example: ALTER ROLE MANAGER VALID UNTIL
```
'2028-12-31';
```
```
DROP ROLE: Deletes a role that has already been defined in a database. Example: DROP ROLE ANALYST;
```
Commands
User Management
16
7
There are commands used to create roles, users, and define access permissions, among other functions, within a
database.
```
CREATE USER: Creates a user within a database. Example: CREATE USER HENRIQUE WITH PASSWORD password;
```
```
ALTER USER: Modifies a user within a database. Example: ALTER USER HENRIQUE WITH PASSWORD password2;
```
```
DROP USER: Deletes a user from a database. Example: DROP USER HENRIQUE;
```
16
8
Commands
User Management
There are commands used to create roles, users, and define access permissions, among other functions, within a
database.
```
GRANT: Grants permissions to specific users or roles to view, modify, or delete tables within the database. Example:
```
```
GRANT SELECT, INSERT ON CLIENTS TO MANAGER;
```
```
REVOKE: Removes permissions granted to specific users or roles within the database.
```
```
Example: REVOKE INSERT ON CUSTOMERS FOR MANAGER;Performance Improvements
```
Need for Optimization
Performance improvements
17
0
When we’re developing our data model, we can create very complex structures that, over time and as the volume of data
grows, become inefficient.
```
Scenarios:
```
Querying a table whose data volume has
grown from 100,000 rows to 1,000,000,000
rows
Highly complex database query
Measures
Performance improvements
17
1
There are several ways to optimize query performance, thereby avoiding long processing times and potential additional
costs associated with this process.
```
a) Index Creation:
```
Indexes allow the database to quickly find the records that match the query. You can create indexes on the columns that
are used most frequently.
Cássio
João
Beatriz
Ana
```
Ana (1º)
```
```
Beatriz (2º)
```
```
Cássio (3º)
```
```
João (4º)
```
```
Reading: 4 lines Reading: 1 line
```
Measures
Performance improvements
17
2
```
b) Changes to the database schema:
```
The database schema can have a significant impact on query performance. To minimize this impact, tables should ideally
be normalized and optimized to avoid overly complex queries..
Measures
Performance improvements
17
3
```
c) Using WHERE and JOIN:
```
Use WHERE and JOIN clauses effectively to limit the number of records returned by the query. This will reduce the time it
takes to retrieve the results.
Measures
Performance improvements
17
4
```
d) Precautions for large-scale operations:
```
Large-scale operations, such as SELECT * and ORDER BY, can be very time-consuming and consume a lot of server
resources. Try to limit the number of columns selected and avoid sorting large datasets whenever possible.
select * from transactions
select customer_code , transaction
amount
from transactions
Measures
Performance improvements
17
5
```
e) Monitor query performance:
```
Use monitoring tools to identify queries that are taking longer to execute, and then optimize them. Monitoring can also
help you identify broader performance issues on the database server.
A good way to monitor query performance is to use EXPLAIN.
```
Syntax:
```
explain select
costumer_cod
, transaction amount
from transactions
THANK YOU
17