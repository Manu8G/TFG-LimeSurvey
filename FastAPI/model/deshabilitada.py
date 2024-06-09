from sqlalchemy import Column, Integer
from model import Base

class Deshabilitada(Base):
    __tablename__ = "Deshabilitada"

    id_pregunta = Column(Integer, primary_key=True, index=True)