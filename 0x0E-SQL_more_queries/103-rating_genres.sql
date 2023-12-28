-- 20. Best genre
-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) rating
FROM tv_genres tg
INNER JOIN tv_show_genres tsg ON tsg.genre_id = tg.id
INNER JOIN tv_show_ratings tsr ON tsr.show_id = tsg.show_id
GROUP BY name
ORDER BY 2 DESC;
