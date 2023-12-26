-- 19. Temperatures #1
-- displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month IN (7,8)
GROUP BY city
ORDER BY 2 desc
LIMIT 3;
