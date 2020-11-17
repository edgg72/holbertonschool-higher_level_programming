--  script that creates the table unique_id on your MySQL server.
-- same as 4 but the id must be unique

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
