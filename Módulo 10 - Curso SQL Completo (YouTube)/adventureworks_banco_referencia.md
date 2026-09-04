# AdventureWorks — Referência do Banco de Dados

Banco OLTP de exemplo da Microsoft (`AdventureWorks2017.bak`), simulando a
indústria fictícia "Adventure Works Cycles" (bicicletas e acessórios). Usado no
curso para os desafios (peso de produtos, empregados casados, cobrança de
cliente, etc.). Estrutura em **schemas**: `Person`, `HumanResources`,
`Production`, `Sales`, `Purchasing`, `dbo`.

## Schemas e tabelas principais

### `Production` — produtos e fábrica
| Tabela | Observação |
|--------|------------|
| `Product` | **PK `ProductID`** — produtos com `Weight`, `Color`, `ListPrice`, `Name`, `ProductNumber`, `SafetyStockLevel`, `StandardCost` |
| `ProductCategory` | **PK `ProductCategoryID`** — categorias de alto nível (Bikes, Components, Clothing, Accessories) |
| `ProductSubcategory` | FK → `ProductCategory` |
| `ProductModel` | Modelos dos produtos |
| `WorkOrder` / `BillOfMaterials` | Produção |

### `Sales` — vendas
| Tabela | Observação |
|--------|------------|
| `SalesOrderHeader` | **PK `SalesOrderID`** — pedidos: `OrderDate`, `DueDate`, `ShipDate`, `CustomerID`, `SalesPersonID`, `TerritoryID`, `SubTotal`, `TaxAmt`, `Freight`, `TotalDue`, `Status` |
| `SalesOrderDetail` | Itens do pedido: `SalesOrderID` + `SalesOrderDetailID` (PK), `ProductID`, `OrderQty`, `UnitPrice`, `UnitPriceDiscount`, `LineTotal` |
| `Customer` | **PK `CustomerID`** — `PersonID`, `StoreID`, `TerritoryID`, `AccountNumber` |
| `SalesPerson` / `SalesTerritory` | Vendedores e territórios |

### `Person` — pessoas físicas/jurídicas
| Tabela | Observação |
|--------|------------|
| `Person` | **PK `BusinessEntityID`** — `FirstName`, `LastName`, `PersonType`, `EmailPromotion` |
| `EmailAddress` | FK → `Person.BusinessEntityID`; coluna `EmailAddress` |
| `PhoneNumberType` / `PersonPhone` | Telefones |
| `Address` | **PK `AddressID`** — `AddressLine1`, `City`, `PostalCode` |
| `StateProvince` / `CountryRegion` | UF e país (`CountryRegionCode` = "US", "BR"...) |

### `HumanResources` — RH
| Tabela | Observação |
|--------|------------|
| `Employee` | FK `BusinessEntityID` — `JobTitle`, `MaritalStatus` ('M'/'S'), `SalariedFlag` (bit), `HireDate`, `Gender`, `NationalIDNumber` |
| `Department` / `EmployeeDepartmentHistory` | Departamentos e histórico |
| `Shift` | Turnos |

### `Purchasing` — compras
`Vendor`, `PurchaseOrderHeader`, `PurchaseOrderDetail`, `ProductVendor`.

### `dbo`
`AWBuildVersion`, `DatabaseLog`, `ErrorLog` (utilitárias).

## Queries de referência (desafios do curso)

```sql
-- DESAFIO: peças que pesam MAIS de 500 e NÃO MAIS de 700 kg
SELECT p.Name, p.Weight
FROM Production.Product p
WHERE p.Weight > 500 AND p.Weight <= 700;

-- DESAFIO: empregados casados e assalariados
SELECT e.BusinessEntityID,
       p.FirstName + ' ' + p.LastName AS nome,
       e.MaritalStatus,
       e.SalariedFlag
FROM HumanResources.Employee e
JOIN Person.Person p ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.MaritalStatus = 'M'
  AND e.SalariedFlag = 1;

-- DESAFIO: e-mail de um usuário (ex: "Ken") para cobrança
-- 1) achar o BusinessEntityID na Person; 2) buscar o e-mail
SELECT e.EmailAddress
FROM Person.EmailAddress e
JOIN Person.Person p ON p.BusinessEntityID = e.BusinessEntityID
WHERE p.FirstName = 'Ken';

-- Receita por categoria
SELECT pc.Name AS categoria,
       SUM(od.LineTotal) AS receita
FROM Sales.SalesOrderDetail od
JOIN Production.Product p      ON p.ProductID = od.ProductID
JOIN Production.ProductSubcategory psc ON psc.ProductSubcategoryID = p.ProductSubcategoryID
JOIN Production.ProductCategory pc      ON pc.ProductCategoryID = psc.ProductCategoryID
GROUP BY pc.Name
ORDER BY receita DESC;

-- Top 10 produtos mais vendidos (em quantidade)
SELECT TOP 10 p.Name, SUM(od.OrderQty) AS qtd
FROM Sales.SalesOrderDetail od
JOIN Production.Product p ON p.ProductID = od.ProductID
GROUP BY p.Name
ORDER BY qtd DESC;

-- Vendas por país (total devido)
SELECT cr.Name AS pais, SUM(soh.TotalDue) AS total
FROM Sales.SalesOrderHeader soh
JOIN Sales.Customer c        ON c.CustomerID = soh.CustomerID
JOIN Sales.SalesTerritory st ON st.TerritoryID = c.TerritoryID
JOIN Person.CountryRegion cr ON cr.CountryRegionCode = st.CountryRegionCode
GROUP BY cr.Name
ORDER BY total DESC;
```

## Dicas

- **Sempre qualifique com o schema**: `Production.Product`, não `Product`.
- `LineTotal` no detail já é `UnitPrice * OrderQty * (1 - discount)`.
- `PersonType` em `Person.Person`: 'SC' (loja/contato), 'IN' (indivíduo) etc.
- `MaritalStatus` é char único: 'M' = casado, 'S' = solteiro.
- Para carregar no Databricks/Neon: veja `carregar_bancos.md` deste módulo.
