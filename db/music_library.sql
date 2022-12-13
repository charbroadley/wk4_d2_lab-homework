-- write your tables in here. 

DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    year INT,
    artist_id INT NOT NULL REFERENCES artists(id)
);
