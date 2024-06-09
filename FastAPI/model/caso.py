from sqlalchemy import Column, Integer
from model import Base

class Caso(Base):
    __tablename__ = "CasoEsdetipoEsdeun"

    id_caso = Column(Integer, primary_key=True, index=True)
    nivel_actual = Column(Integer, index=True)
    id_flujo = Column(Integer, index=True)
    id_usuario = Column(Integer, index=True)
    