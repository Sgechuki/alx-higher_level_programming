-- 18. Temperatures #0
-- displays the average temperature (Fahrenheit) by city 
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY 2 DESC;
