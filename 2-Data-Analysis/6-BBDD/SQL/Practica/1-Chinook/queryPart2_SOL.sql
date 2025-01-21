--PART 2
--ex1
SELECT
CONCAT(t2.firstname, ' ', t2.lastname) AS NombreCliente,
t1.InvoiceId AS IDFactura,
t1.InvoiceDate AS FechaFactura,
t1.BillingCountry AS PaisFactura
FROM invoices AS t1
INNER JOIN customers AS t2 ON t1.CustomerId = t2.CustomerId
WHERE t2.Country = 'Brazil'

--ex2
SELECT
t1.*,
CONCAT(t3.firstname, ' ', t3.lastname) AS NombreEmpleado
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
WHERE t3.Title = 'Sales Support Agent';

--ex3
SELECT
CONCAT(t2.firstname, ' ', t2.lastname) AS NombreCliente,
t2.Country AS PaisCliente,
CONCAT(t3.firstname, ' ', t3.lastname) AS NombreEmpleado,
t1.Total
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
;

SELECT
CONCAT(t2.firstname, ' ', t2.lastname) AS NombreCliente,
t2.Country AS PaisCliente,
CONCAT(t3.firstname, ' ', t3.lastname) AS NombreEmpleado,
SUM(t1.Total) AS VolumenVentas,
COUNT(t1.Total) AS NumCompras
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
GROUP BY 1,2,3
;

--ex4
SELECT
tracks.Name AS NombreCancion,
invoice_items.*
FROM invoice_items
INNER JOIN tracks ON invoice_items.TrackId = tracks.TrackId

--ex5
SELECT
t1.Name AS NombreCancion,
t2.Name AS Formato,
t4.Title AS Album,
t3.Name AS Genero
FROM tracks t1
INNER JOIN media_types t2  ON t1.MediaTypeId = t2.MediaTypeId
INNER JOIN genres t3  ON t1.GenreId = t3.GenreId
INNER JOIN albums t4 ON t1.AlbumId = t4.AlbumId

--ex6
SELECT
playlists.PlaylistId,
playlists.Name AS Playlist,
COUNT(playlist_track.trackid) AS NumCanciones
FROM playlist_track
INNER JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
GROUP BY 1,2
ORDER BY 3 DESC

--ex7
SELECT
t3.EmployeeId,
CONCAT(t3.firstname, ' ', t3.lastname) AS NombreEmpleado,
SUM(t1.Total) AS VolumenVentas,
COUNT(DISTINCT t1.InvoiceID) AS NumCompras,
COUNT(DISTINCT t2.CustomerID) AS NumClientes
--SUM(t4.Quantity) AS NumCanciones
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
--INNER JOIN invoice_items t4 ON t1.InvoiceID = t4.InvoiceID
GROUP BY 1,2
ORDER BY 3 DESC
;

SELECT
t3.EmployeeId,
CONCAT(t3.firstname, ' ', t3.lastname) AS NombreEmpleado,
SUM(t4.UnitPrice) AS VolumenVentas,
COUNT(DISTINCT t1.InvoiceID) AS NumCompras,
COUNT(DISTINCT t2.CustomerID) AS NumClientes,
SUM(t4.Quantity) AS NumCanciones
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
INNER JOIN invoice_items t4 ON t1.InvoiceID = t4.InvoiceID
GROUP BY 1,2
ORDER BY 3 DESC



SELECT
t3.EmployeeId,
t2.CustomerId,
t1.InvoiceId
--t4.TrackId
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
--INNER JOIN invoice_items t4 ON t1.InvoiceID = t4.InvoiceID

--ex8
SELECT
t3.EmployeeId,
CONCAT(t3.firstname, ' ', t3.lastname) AS NombreEmpleado,
SUM(t4.UnitPrice) AS VolumenVentas,
COUNT(DISTINCT t1.InvoiceID) AS NumCompras,
COUNT(DISTINCT t2.CustomerID) AS NumClientes,
SUM(t4.Quantity) AS NumCanciones
FROM invoices t1
INNER JOIN customers t2 ON t1.CustomerId = t2.CustomerId
INNER JOIN employees t3 ON t2.SupportRepId = t3.EmployeeId
INNER JOIN invoice_items t4 ON t1.InvoiceID = t4.InvoiceID
WHERE strftime('%Y', t1.InvoiceDate) = '2009'
GROUP BY 1,2
ORDER BY 3 DESC

--ex9
SELECT
t1.ArtistID,
t1.Name AS Artista,
SUM(t4.UnitPrice) AS VV,
COUNT(t4.TrackId) AS NumCanciones,
COUNT(DISTINCT t4.InvoiceId) AS NumFacturas
FROM artists t1
INNER JOIN albums t2 ON t1.artistID = t2.Artistid
INNER JOIN tracks t3 ON t2.AlbumId = t3.AlbumID
INNER JOIN invoice_items t4 ON t3.TrackID = t4.TrackID
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 3

