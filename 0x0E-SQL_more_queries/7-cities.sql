-- 7 Cities table
-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT AUTO_GENERATED PRIMARY KEY UNIQUE NOT NULL,
	state_id INT NOT NULL FOREIGN KEY(cities_states_fk) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
)
