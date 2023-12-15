-- 13 Number of shows by genre
--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT gnr.name AS genre, COUNT(*) number_of_shows
FROM tv_show_genres shw
INNER JOIN tv_genres gnr ON gnr.id = shw.genre_id
GROUP BY gnr.name
ORDER BY 2 DESC;
