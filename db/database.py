from config import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(engine)
