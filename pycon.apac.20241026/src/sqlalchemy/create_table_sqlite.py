from item import Base
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite://", echo=True)
Base.metadata.create_all(engine)
