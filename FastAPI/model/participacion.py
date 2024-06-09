from sqlalchemy import Column, Integer, Date
from model import Base

class User(Base):
    __tablename__ = "Usuario"

    id_particion = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)
    id_usuario = Column(Integer, index=True)
    id_version_formulario = Column(Integer, index=True)
    id_formulario = Column(Integer, index=True)
    id_caso = Column(Integer, index=True)
