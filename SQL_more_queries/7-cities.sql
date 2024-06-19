-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS cities
       (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id)
);