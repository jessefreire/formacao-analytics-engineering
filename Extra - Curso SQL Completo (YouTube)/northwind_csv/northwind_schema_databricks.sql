-- Northwind para Databricks (Delta). Gerado automaticamente.
-- 1) Crie o schema:  CREATE SCHEMA IF NOT EXISTS northwind;
-- 2) Ajuste o caminho /Volumes/... no COPY INTO e rode num SQL warehouse.

CREATE SCHEMA IF NOT EXISTS northwind;

DROP TABLE IF EXISTS northwind.categories;
CREATE TABLE northwind.categories (
    category_id INT,
    category_name STRING,
    description STRING,
    picture STRING
) USING DELTA;
COPY INTO northwind.categories FROM '/Volumes/main/datalake/raw/northwind/categories.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.customers;
CREATE TABLE northwind.customers (
    customer_id STRING,
    company_name STRING,
    contact_name STRING,
    contact_title STRING,
    address STRING,
    city STRING,
    region STRING,
    postal_code STRING,
    country STRING,
    phone STRING,
    fax STRING
) USING DELTA;
COPY INTO northwind.customers FROM '/Volumes/main/datalake/raw/northwind/customers.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.employee_territories;
CREATE TABLE northwind.employee_territories (
    employee_id INT,
    territory_id STRING
) USING DELTA;
COPY INTO northwind.employee_territories FROM '/Volumes/main/datalake/raw/northwind/employee_territories.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.employees;
CREATE TABLE northwind.employees (
    employee_id INT,
    last_name STRING,
    first_name STRING,
    title STRING,
    title_of_courtesy STRING,
    birth_date TIMESTAMP,
    hire_date TIMESTAMP,
    address STRING,
    city STRING,
    region STRING,
    postal_code STRING,
    country STRING,
    home_phone STRING,
    extension STRING,
    photo STRING,
    notes STRING,
    reports_to INT,
    photo_path STRING
) USING DELTA;
COPY INTO northwind.employees FROM '/Volumes/main/datalake/raw/northwind/employees.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.order_details;
CREATE TABLE northwind.order_details (
    order_id INT,
    product_id INT,
    unit_price DECIMAL(19,4),
    quantity SMALLINT,
    discount FLOAT
) USING DELTA;
COPY INTO northwind.order_details FROM '/Volumes/main/datalake/raw/northwind/order_details.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.orders;
CREATE TABLE northwind.orders (
    order_id INT,
    customer_id STRING,
    employee_id INT,
    order_date TIMESTAMP,
    required_date TIMESTAMP,
    shipped_date TIMESTAMP,
    ship_via INT,
    freight DECIMAL(19,4),
    ship_name STRING,
    ship_address STRING,
    ship_city STRING,
    ship_region STRING,
    ship_postal_code STRING,
    ship_country STRING
) USING DELTA;
COPY INTO northwind.orders FROM '/Volumes/main/datalake/raw/northwind/orders.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.products;
CREATE TABLE northwind.products (
    product_id INT,
    product_name STRING,
    supplier_id INT,
    category_id INT,
    quantity_per_unit STRING,
    unit_price DECIMAL(19,4),
    units_in_stock SMALLINT,
    units_on_order SMALLINT,
    reorder_level SMALLINT,
    discontinued BOOLEAN
) USING DELTA;
COPY INTO northwind.products FROM '/Volumes/main/datalake/raw/northwind/products.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.region;
CREATE TABLE northwind.region (
    region_id INT,
    region_description STRING
) USING DELTA;
COPY INTO northwind.region FROM '/Volumes/main/datalake/raw/northwind/region.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.shippers;
CREATE TABLE northwind.shippers (
    shipper_id INT,
    company_name STRING,
    phone STRING
) USING DELTA;
COPY INTO northwind.shippers FROM '/Volumes/main/datalake/raw/northwind/shippers.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.suppliers;
CREATE TABLE northwind.suppliers (
    supplier_id INT,
    company_name STRING,
    contact_name STRING,
    contact_title STRING,
    address STRING,
    city STRING,
    region STRING,
    postal_code STRING,
    country STRING,
    phone STRING,
    fax STRING,
    home_page STRING
) USING DELTA;
COPY INTO northwind.suppliers FROM '/Volumes/main/datalake/raw/northwind/suppliers.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');

DROP TABLE IF EXISTS northwind.territories;
CREATE TABLE northwind.territories (
    territory_id STRING,
    territory_description STRING,
    region_id INT
) USING DELTA;
COPY INTO northwind.territories FROM '/Volumes/main/datalake/raw/northwind/territories.csv' FILEFORMAT = CSV FORMAT_OPTIONS('header' = 'true', 'mode' = 'FAILFAST');
