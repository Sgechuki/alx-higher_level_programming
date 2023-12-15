-- 12  Genre ID by show
-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT shw.title, gnr.genre_id
FROM tv_shows shw
LEFT OUTER JOIN tv_show_genres gnr ON shw.id = gnr.show_id
WHERE gnr.genre_id IS NULL
ORDER BY 1, 2;
