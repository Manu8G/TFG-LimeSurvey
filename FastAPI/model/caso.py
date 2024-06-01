from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Caso(Base):
    tablename = "CasoEsdetipoEsdeun"

    id_caso = Column(Integer, primary_key=True, index=True)
    nivel_actual = Column(Integer, index=True)
    id_flujo = Column(Integer, index=True)
    id_usuario = Column(Integer, index=True)
    