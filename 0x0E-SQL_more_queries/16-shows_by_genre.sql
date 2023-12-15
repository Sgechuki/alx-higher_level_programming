-- 16 List shows and genres
-- lists all shows, and all genres linked to that show
SELECT title, gnr.name FROM tv_shows shw
LEFT JOIN tv_show_genres tsg ON shw.id=tsg.show_id
LEFT JOIN tv_genres gnr ON tsg.genre_id = gnr.id
ORDER BY title, gnr.name;
