from sqlalchemy import create_engine, MetaData

from .env import ConnectionOptionsDataBase as db


__connection_string = (
    f'mysql+pymysql://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}'
)

engine = create_engine(__connection_string)

meta = MetaData()

connection = engine.connect()
