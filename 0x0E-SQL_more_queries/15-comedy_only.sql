-- 15 Only Comedy
-- lists all Comedy shows in the database
SELECT title FROM tv_shows shw
JOIN tv_show_genres tsg ON shw.id=tsg.show_id
JOIN tv_genres gnr ON gnr.id=tsg.genre_id
WHERE gnr.name = 'Comedy'
ORDER BY title;
