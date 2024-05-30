import yaml

with open("credential.yml", "r") as f:
    credential = yaml.reader(f)

# from utils.config import ConfigLoader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import User

# config = ConfigLoader()

def create_db_connection():
    engine = create_engine(credential["URL"], echo=True)
    # engine = create_engine(config.get_config()["MYSQL"]["HOST"], echo=True)
    # Crea una sesión
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()

