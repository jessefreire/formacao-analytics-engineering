# Northwind — Referência do Banco de Dados

Banco clássico de exemplo da Microsoft, simulando uma empresa de importação e
distribuição de alimentos (`bancoNorthwind.txt`, script T-SQL criado no schema
`dbo`). Ideal para treinar `SELECT`, `WHERE`, `JOIN`, agregações e funções.

> **Já convertido para CSV** na pasta `northwind_csv/` (11 tabelas, snake_case,
> UTF-8, datas ISO) — pronto para carregar no Databricks/Neon. Veja
> `carregar_bancos.md`. A referência abaixo mostra o schema original SQL Server
> (CamelCase).

## Tabelas e relacionamentos

```
Categories 1──N Products
Suppliers  1──N Products
Products   1──N "Order Details"
Orders     1──N "Order Details"
Customers  1──N Orders
Employees  1──N Orders
Shippers   1──N Orders (ShipVia)
Employees  1──N Employees (ReportsTo — auto-ref)
```

### Principais tabelas (schema)

**Customers** (`CustomerID` PK)
| Coluna | Tipo | Observação |
|--------|------|------------|
| `CustomerID` | nchar(5) | PK |
| `CompanyName` | nvarchar(40) | |
| `ContactName` | nvarchar(30) | |
| `ContactTitle` | nvarchar(30) | |
| `Address` / `City` / `Region` / `PostalCode` / `Country` | nvarchar | Endereço |
| `Phone` / `Fax` | nvarchar(24) | |

**Orders** (`OrderID` PK)
| Coluna | Tipo | Observação |
|--------|------|------------|
| `OrderID` | int identity | PK |
| `CustomerID` | nchar(5) | FK → Customers |
| `EmployeeID` | int | FK → Employees |
| `OrderDate` / `RequiredDate` / `ShippedDate` | datetime | |
| `ShipVia` | int | FK → Shippers |
| `Freight` | money | Frete (default 0) |
| `ShipName` / `ShipAddress` / `ShipCity` / ... | nvarchar | Endereço de entrega |

**Order Details** (PK composta: `OrderID` + `ProductID`)
| Coluna | Tipo | Observação |
|--------|------|------------|
| `OrderID` | int | FK → Orders |
| `ProductID` | int | FK → Products |
| `UnitPrice` | money | Preço no momento do pedido |
| `Quantity` | smallint | Quantidade |
| `Discount` | real | 0 a 1 (ex: 0.15 = 15%) |

**Products** (`ProductID` PK)
| Coluna | Tipo | Observação |
|--------|------|------------|
| `ProductID` | int identity | PK |
| `ProductName` | nvarchar(40) | |
| `SupplierID` | int | FK → Suppliers |
| `CategoryID` | int | FK → Categories |
| `QuantityPerUnit` | nvarchar(20) | Ex: "24 - 12 oz bottles" |
| `UnitPrice` | money | |
| `UnitsInStock` / `UnitsOnOrder` / `ReorderLevel` | smallint | Estoque |
| `Discontinued` | bit | 1 = descontinuado |

**Employees** (`EmployeeID` PK)
| Coluna | Tipo | Observação |
|--------|------|------------|
| `EmployeeID` | int identity | PK |
| `LastName` / `FirstName` | nvarchar | |
| `Title` / `TitleOfCourtesy` | nvarchar | Cargo |
| `BirthDate` / `HireDate` | datetime | |
| `Address` / `City` / ... | nvarchar | |
| `ReportsTo` | int | FK auto-ref (chefe) |
| `Notes` | ntext | |

**Outras:** `Categories`, `Suppliers`, `Shippers`, `Region`, `Territories`,
`EmployeeTerritories` (N:N empregados×territórios), `CustomerDemographics` e
`CustomerCustomerDemo` (N:N clientes×segmentos).

## Queries de referência

```sql
-- Pedidos com nome do cliente e data
SELECT o.OrderID, c.CompanyName, o.OrderDate
FROM Orders o
JOIN Customers c ON c.CustomerID = o.CustomerID;

-- Receita por produto (preço * quantidade, sem desconto)
SELECT p.ProductName,
       SUM(od.Quantity * od.UnitPrice) AS receita
FROM [Order Details] od
JOIN Products p ON p.ProductID = od.ProductID
GROUP BY p.ProductName
ORDER BY receita DESC;

-- Valor líquido por pedido, considerando desconto
SELECT od.OrderID,
       SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS liquido
FROM [Order Details] od
GROUP BY od.OrderID;

-- Empregado e seu chefe (auto-join)
SELECT e.FirstName + ' ' + e.LastName AS funcionario,
       m.FirstName + ' ' + m.LastName AS gerente
FROM Employees e
LEFT JOIN Employees m ON m.EmployeeID = e.ReportsTo;

-- Produtos caros (preço acima da média)
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products)
ORDER BY UnitPrice DESC;
```

## Dicas

- **Nomes com espaço** precisam de colchetes: `[Order Details]`.
- `Freight` é `money`, `Discount` é `real` (0–1): multiplique por `(1 - Discount)`.
- Tabelas de "ponte" N:N: `EmployeeTerritories` e `CustomerCustomerDemo`.
