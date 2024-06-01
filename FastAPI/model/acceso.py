from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Acceso(Base):
    tablename = "AccesoInicia"

    id_acceso = Column(Integer, primary_key=True, index=True)
    numero_acceso = Column(Integer, index=True)
    comienzo = Column(Date, index=True)
    id_usuario = Column(Integer, index=True)