from sqlalchemy import Column, Integer
from model import Base

class Seleccion(Base):
    __tablename__ = "Seleccion"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)