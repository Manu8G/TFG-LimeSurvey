from sqlalchemy import Column, Integer
from model import Base

class Seleccion(Base):
    tablename = "Seleccion"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)