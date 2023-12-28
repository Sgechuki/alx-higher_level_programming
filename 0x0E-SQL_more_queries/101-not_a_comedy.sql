-- 18 No Comedy tonight!
-- lists all shows without the genre Comedy
SELECT DISTINCT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (SELECT show_id FROM tv_genres tg INNER JOIN tv_show_genres tsg ON tsg.genre_id = tg.id WHERE name = 'Comedy')
ORDER BY 1 ASC
;
