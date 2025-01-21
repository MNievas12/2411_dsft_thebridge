--PART 1
--ex4
SELECT 
CONCAT(firstname, ' ', lastname) AS NombreCompleto,
--firstname || ' ' || lastname AS NombreCompleto
CustomerId AS ID,
country AS Pais
FROM customers
WHERE country <> 'USA';

--ex5
SELECT
CONCAT(firstname, ' ', lastname) AS NombreCompleto,
city || ' ' || State || ' ' || Country AS Direccion,
Email
FROM employees
WHERE title = 'Sales Support Agent';

--ex6
SELECT DISTINCT
billingcountry
FROM invoices;

SELECT
billingcountry,
COUNT(invoiceid) AS NumFacturas
FROM invoices
GROUP BY 1
ORDER BY 2 DESC;

--ex7
SELECT
COUNT(customerid) AS NumClientes,
state AS Estado
FROM customers
WHERE country = 'USA'
GROUP BY Estado
ORDER BY NumClientes DESC;

--ex8
SELECT
--invoiceid,
SUM(quantity) AS NumArticulos,
COUNT (DISTINCT trackid) AS NumProductos
FROM invoice_items
WHERE invoiceid = 37
--GROUP BY 1

--ex9
SELECT
	COUNT(t3.TrackId)
FROM 
	artists AS t1
INNER JOIN 
	albums AS t2 ON t1.ArtistId = t2.ArtistId
INNER JOIN
    tracks AS t3 ON t2.AlbumId = t3.AlbumId
WHERE 
	t1.Name = 'AC/DC';

--ex10
SELECT
invoiceid,
SUM(quantity) AS NumArticulos,
COUNT (DISTINCT trackid) AS NumProductos
FROM invoice_items
--WHERE invoiceid = 37
GROUP BY 1
ORDER BY 2 DESC;

--ex11
SELECT
billingcountry,
COUNT(invoiceid)
FROM invoices
GROUP BY 1
ORDER BY 2 DESC;

--ex12
SELECT
strftime('%Y', invoicedate) AS Año,
COUNT(invoiceid)
FROM invoices
WHERE Año IN ('2009', '2011')
GROUP BY 1

--ex13
SELECT
CAST(strftime('%Y', invoicedate) as int) AS Año,
COUNT(invoiceid)
FROM invoices
WHERE Año BETWEEN 2009 AND 2011
--WHERE Año IN ('2009', '2010', '2011')
GROUP BY 1

--ex14
SELECT
country,
COUNT(customerid)
FROM customers
WHERE country IN ('Brazil', 'Spain')
GROUP BY 1

--ex15
SELECT
*
FROM tracks
WHERE Name LIKE 'You %';











