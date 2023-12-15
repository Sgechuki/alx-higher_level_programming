-- 9 cities_by_state_join.sql
-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM states s
INNER JOIN cities c ON s.id = c.state_id;
