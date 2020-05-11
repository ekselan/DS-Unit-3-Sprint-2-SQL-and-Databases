# DS-Unit-3-Sprint-2-SQL-and-Databases
SQL and Databases for Data Science

# README
Looks like this may include markdown mostly - notes on SQL commands?


# Commands

```
-- all invoices where billing country is germany (28 rows)
SELECT *
FROM invoices -- 412 rows
WHERE BillingCountry in ('Germany', 'Canada', 'USA')
```

```
-- how many invoices in Germany, Canda or US
SELECT
	count(distinct InvoiceId) as invoice_count --175 (nunique)
	,count(distinct CustomerId) as customer_count --25 (nunique)
FROM invoices -- 412 rows
WHERE BillingCountry in ('Germany', 'Canada', 'USA')
```

```
/*
comments
*/
```

```
-- how many invoices per country (Germany, Canada or USA)?
-- row per country 
-- two columns (country name, then count of invoices)
SELECT
	BillingCountry
	,count(distinct InvoiceId) as invoice_count --175 (nunique)
FROM invoices -- 412 rows
WHERE BillingCountry in ('Germany', 'Canada', 'USA')
GROUP BY BillingCountry -- we want results as "row per country"

-- whatever you're grouping by, you should SELECT
```


```
SELECT
	BillingCountry
	,count(distinct InvoiceId) as invoice_count --175 (nunique)
FROM invoices -- 412 rows
WHERE BillingCountry in ('Germany', 'Canada', 'USA')
GROUP BY BillingCountry -- we want results as "row per country"
--can order by columns
ORDER BY BillingCountry DESC
```


```
-- which countries have the most invoices? (top 3)
SELECT
	BillingCountry
	,count(DISTINCT InvoiceId) as invoice_count
FROM invoices
GROUP BY BillingCountry
ORDER BY invoice_count DESC
LIMIT 3
```