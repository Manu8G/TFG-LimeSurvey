from sqlalchemy import Column, Integer
from model import Base

class Administrador(Base):
    tablename = 'Administrador'

    id_usuario = Column(Integer, primary_key=True)
    