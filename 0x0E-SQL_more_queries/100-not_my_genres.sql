-- 17. Not my genre
-- list all genres not linked to the show Dexter
SELECT DISTINCT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (SELECT genre_id FROM tv_shows ts INNER JOIN tv_show_genres tsg ON tsg.show_id = ts.id WHERE title = 'Dexter')
ORDER BY 1 ASC
;
