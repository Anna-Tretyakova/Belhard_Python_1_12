CREATE DATABASE film_zone;

USE film_zone;




CREATE TABLE persons (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
surname VARCHAR(50) NOT NULL,
birth_date DATETIME NOT NULL
);


CREATE TABLE user_types (
id VARCHAR(50) NOT NULL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);

INSERT INTO  user_types (id, name) VALUES ('USER', 'User');
INSERT INTO  user_types (id, name) VALUES ('ADMIN', 'Administrator');

CREATE TABLE users (
login VARCHAR(50) NOT NULL PRIMARY KEY,
password VARCHAR(50) NOT NULL,
user_type_id VARCHAR(50) NOT NULL REFERENCES user_types(id),
person_id INT NOT NULL REFERENCES persons(id)
);


CREATE TABLE emails (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(50) NOT NULL,
user_login VARCHAR(50) NOT NULL REFERENCES users(login)
);


CREATE TABLE genres (
id VARCHAR(50) NOT NULL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);

INSERT INTO  genres (id, name) VALUES ('ACTION', 'Action');
INSERT INTO  genres (id, name) VALUES ('ADVENTURE', 'Adventure');
INSERT INTO  genres (id, name) VALUES ('COMEDY', 'Comedy');
INSERT INTO  genres (id, name) VALUES ('DRAMA', 'Drama');



CREATE TABLE films (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
duration INT NOT NULL,
name VARCHAR(50) NOT NULL,
release_date DATETIME NOT NULL,
director_id INT NOT NULL REFERENCES persons(id)
);


CREATE TABLE user_favorite_films (
user_login VARCHAR(50) NOT NULL REFERENCES users(login),
film_id INT NOT NULL REFERENCES films(id)
);


CREATE TABLE films_genres (
film_id INT NOT NULL REFERENCES films(id),
film_genre_id INT NOT NULL REFERENCES genres(id)
);


CREATE TABLE characters (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
comment VARCHAR(50),
film_id INT NOT NULL REFERENCES films(id)
);



CREATE TABLE characters_actors (
character_id INT NOT NULL REFERENCES characters(id),
person_id INT NOT NULL REFERENCES persons(id)
);
