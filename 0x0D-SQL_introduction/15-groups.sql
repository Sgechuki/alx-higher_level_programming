-- 15 number by score
-- lists the number of records with the same score
SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY 2;
