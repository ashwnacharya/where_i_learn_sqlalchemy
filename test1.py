from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, event
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
from sqlalchemy_utils.functions import create_database, drop_database
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite3.db')
engine.connect()

metadata = MetaData(engine)

user_table = Table('user', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
)

class User:

    def __init__(self, *args, **kwargs):
        pass


Base = declarative_base()

mapper(User, user_table)


create_database(engine.url)
metadata.create_all()

session_factory = scoped_session(sessionmaker(engine),)

session = session_factory()

user = User()
user.id = 1
user.name = 'ashwin'

session.add(user)
session.flush()
session.commit()
