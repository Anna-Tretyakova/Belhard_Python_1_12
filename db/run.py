from db import get_session
from db.tables import tables
from sqlalchemy.sql import table, column, select
from sqlalchemy import update

with get_session as db_session:
INSERT INTO user_types (id, name)
VALUES ('USER', 'User')

INSERT INTO user_types (id, name)
VALUES ('ADMIN', 'Administrator')

INSERT INTO  genres (id, name)
VALUES ('ACTION', 'Action');

res = genres.delete().where(genres.c.id == 'ACTION')

res_1 = select([genres].where(genres.c.name) == 'Action')

stmt = (
    update(genres).where(genres.c.name == 'Action').
    values(name ='Action+')
)

 db_session.commit()