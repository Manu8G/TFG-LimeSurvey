from sqlalchemy import Column, Integer, String, Date
# from .database import Base

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+mysqlconnector://limeuser:EstaEsLaCon@localhost:3306/integradb'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Acceso(Base):
    tablename = "AccesoInicia"

    id_acceso = Column(Integer, primary_key=True, index=True)
    numero_acceso = Column(Integer, index=True)
    comienzo = Column(Date, index=True)
    id_usuario = Column(Integer, index=True)