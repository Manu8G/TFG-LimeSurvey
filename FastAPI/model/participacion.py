from sqlalchemy import Column, Integer, String, Date
from .database import Base

class User(Base):
    tablename = "Usuario"

    id_particion = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)
    id_usuario = Column(Integer, index=True)
    id_version_formulario = Column(Integer, index=True)
    id_formulario = Column(Integer, index=True)
    id_caso = Column(Integer, index=True)
