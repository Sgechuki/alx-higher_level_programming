-- 11  Genre ID by show
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- If a show doesn’t have a genre, display NULL
SELECT shw.title, gnr.genre_id
FROM tv_shows shw
LEFT OUTER JOIN tv_show_genres gnr ON shw.id = gnr.show_id
ORDER BY 1, 2;
