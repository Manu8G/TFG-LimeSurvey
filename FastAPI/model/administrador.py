from sqlalchemy import Column, Integer
from model import Base

class Administrador(Base):
    __tablename__ = 'Administrador'

    id_usuario = Column(Integer, primary_key=True)
    
