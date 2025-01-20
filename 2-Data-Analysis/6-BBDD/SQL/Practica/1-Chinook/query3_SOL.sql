SELECT * FROM tracks LIMIT 10;

SELECT * 
FROM tracks 
WHERE composer = 'AC/DC';

SELECT COUNT(*)
FROM tracks 
WHERE composer = 'AC/DC';


SELECT
tracks.*
FROM artists
INNER JOIN 
	albums ON artists.ArtistId = albums.ArtistId
INNER JOIN
    tracks ON albums.AlbumId = tracks.AlbumId
WHERE artists.Name = 'AC/DC';


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

/*
SELECT
COUNT(tracks.TrackId)
FROM tracks
--WHERE albumid IN (1,4);*/

