from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, event
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
from sqlalchemy_utils.functions import create_database, drop_database
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite3.db')
engine.connect()

metadata = MetaData(engine)

user_table = Table(
    'user', 
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
)


class User:

    def __init__(self, *args, **kwargs):
        pass


def receive_load(target, context):
    print("listen for the 'load' event")
    print(target)
    print(context)

def receive_refresh(target, context, only_load_props=None):
    print("listen for the 'refresh' event")


event.listen(User, 'load', receive_load)
event.listen(User, "refresh", receive_load)

Base = declarative_base()

mapper(User, user_table)


session_factory = scoped_session(sessionmaker(engine),)

new_session = session_factory()

# Event should fire here when I run this line
obj = new_session.query(User).filter_by(id=1).first()
drop_database(engine.url)
