-- 14 My genres
-- lists all genres of the show Dexter
SELECT tgr.name
FROM tv_shows shw
INNER JOIN tv_show_genres gnr ON shw.id = gnr.show_id
INNER JOIN tv_genres tgr ON tgr.id = gnr.genre_id
WHERE shw.title = 'Dexter'
ORDER BY tgr.name
