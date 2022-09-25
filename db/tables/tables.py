from sqlalchemy import *

metadata = MetaData()


persons = Table('persons', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(50), nullable=False),
    Column('surname', String(60), nullable=False),
    Column('birth_date ', Datetime, nullable=False),


user_types  = Table('user_types', metadata,
    Column('id', String(50), primary_key=True, nullable=False),
    Column('name', String(50), nullable=False),


users = Table('users', metadata,
    Column('login', String(50), primary_key=True, nullable=False),
    Column('password', String(50), nullable=False),
    Column('user_type_id', String(60), nullable=False, ForeignKey("user_types.id")),
    Column('person_id ',Integer, nullable=False, ForeignKey("persons.id")),


emails = Table('emails', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(50), nullable=False),
    Column('user_login', String(60), nullable=False, ForeignKey("users.login")),


genres = Table('genres', metadata,
    Column('id', String(50), primary_key=True, nullable=False),
    Column('name', String(50), nullable=False),


films = Table('films', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('duration', Integer, nullable=False),
    Column('name', String(50), nullable=False),
    Column('release_date', Datetime, nullable=False),
    Column('director_id', Integer, ForeignKey("persons.id")),

user_favorite_films = Table('user_favorite_films', metadata,
    Column('user_login', String(50), ForeignKey("users.login"),nullable=False),
    Column('film_id', String(50), ForeignKey("films.id"),nullable=False),


films_genres = Table('films_genres', metadata,
    Column('film_id', Integer, ForeignKey("films.id"),nullable=False),
    Column('film_genre_id', Integer, ForeignKey("genres.id"),nullable=False),


characters = Table('characters', metadata,
    Column('id', Integer, primary_key=True,nullable=False),
    Column('name', String(50), nullable=False),
    Column('comment', String(50)),
    Column('film_id', Integer, ForeignKey("films.id"),nullable=False),


characters_actors = Table('characters_actors', metadata,
    Column('character_id', Integer, ForeignKey("characters.id"),nullable=False),
    Column('person_id', Integer, ForeignKey("persons.id"),nullable=False),


