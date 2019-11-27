from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
from sqlalchemy_utils.functions import create_database, drop_database


engine = create_engine('sqlite:///sqlite3.db')
engine.connect()
print(engine)

metadata = MetaData(engine)

user_table = Table('user', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
)

class User:

    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)


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

print('fetching ')
new_session = session_factory()

obj = new_session.query(User).filter_by(id=1).first()

print(obj.name)

drop_database(engine.url)