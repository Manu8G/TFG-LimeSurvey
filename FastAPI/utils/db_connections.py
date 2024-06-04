# from utils.config import ConfigLoader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

from utils.config import Config

config = Config()

print(config.__dict__)

def create_db_connection():

    engine = create_engine(config.get("MYSQL.URL"), echo=True)
    # engine = create_engine(config.get_config()["MYSQL"]["HOST"], echo=True)
    # Crea una sesión
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()

def init_db():
    engine = create_engine(config.get("MSQL.URL"), echo=True)
    Base.metadata.create_all(engine)
    
    session = create_db_connection(engine)
    