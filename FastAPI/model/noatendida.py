from sqlalchemy import Column, Integer
from model import Base

class NoAtendida(Base):
    __tablename__ = "NoAtendidaPospone"

    id_sesion = Column(Integer, primary_key=True, index=True)
    id_sesion_no_atendida = Column(Integer, index=True)
    