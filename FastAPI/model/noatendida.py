from sqlalchemy import Column, Integer
from .database import Base

class NoAtendida(Base):
    tablename = "NoAtendidaPospone"

    id_sesion = Column(Integer, primary_key=True, index=True)
    id_sesion_no_atendida = Column(Integer, index=True)
    