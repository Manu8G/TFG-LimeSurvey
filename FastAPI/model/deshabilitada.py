from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Deshabilitada(Base):
    tablename = "Deshabilitada"

    id_pregunta = Column(Integer, primary_key=True, index=True)