-- 19. Rotten tomatoes
-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, SUM(rate) rating
FROM tv_shows ts
INNER JOIN tv_show_ratings tsr ON tsr.show_id = ts.id
GROUP BY title
ORDER BY 2 DESC;
