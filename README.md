# DS-Unit-3-Sprint-2-SQL-and-Databases
SQL and Databases for Data Science

# README
Notes on SQL commands


# Commands - Lecture 1

### Invoices where billing country is GER, CAN or USA
```
-- all invoices where billing country is germany, canada or usa
SELECT *
FROM invoices -- 412 rows
WHERE BillingCountry in ('Germany', 'Canada', 'USA')
```

### How many invoices in Germany, Canda or US
```
-- how many invoices in Germany, Canda or US
SELECT
	count(distinct InvoiceId) as invoice_count --175 (nunique)
	,count(distinct CustomerId) as customer_count --25 (nunique)
FROM invoices -- 412 rows
WHERE BillingCountry in ('Germany', 'Canada', 'USA')
```

### How to add block comments
```
/*
comments
*/
```

### GROUP BY and Counts
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

### Joins
```
SELECT *
FROM artists
JOIN ____ ON ____ = _____
```

```
--FIRST APPROACH
-- how many tracks and albums per artist?
-- row per artist (275 rows)

-- are there any artisits w/o albums?
-- are there any albums w/o tracks?

SELECT 
	artists.ArtistId
	,artists.'Name' as ArtistName
	,count(DISTINCT albums.AlbumId) as AlbumCount
	,count(DISTINCT tracks.TrackId) as TrackCount
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON albums.AlbumId = tracks.AlbumId
GROUP BY artists.ArtistId
ORDER BY artists.ArtistId

-- this was an inner join, and resulted in fewer rows as some artists had no albums/no track
```

### Sub-query
```
--can also subquery:
SELECT
	avg(AlbumCount)
	,avg(TrackCount)
FROM (
	SELECT 
		artists.ArtistId
		,artists.'Name' as ArtistName
		,count(DISTINCT albums.AlbumId) as AlbumCount
		,count(DISTINCT tracks.TrackId) as TrackCount
	FROM artists
	JOIN albums ON artists.ArtistId = albums.ArtistId
	JOIN tracks ON albums.AlbumId = tracks.AlbumId
	GROUP BY artists.ArtistId
	ORDER BY artists.ArtistId
)
```

```
-- how many tracks and albums per artist?
-- row per artist (275 rows)

-- are there any artisits w/o albums?
-- are there any albums w/o tracks?

-- SECOND APPROACH
SELECT
	avg(AlbumCount)
	,avg(TrackCount)
FROM (
	SELECT 
		artists.ArtistId
		,artists.'Name' as ArtistName
		,count(DISTINCT albums.AlbumId) as AlbumCount
		,count(DISTINCT tracks.TrackId) as TrackCount
	FROM artists
	LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
	LEFT JOIN tracks ON albums.AlbumId = tracks.AlbumId
	GROUP BY artists.ArtistId
	ORDER BY artists.ArtistId
)
```