from sqlalchemy import Column, Integer
from model import Base

class Profesional(Base):
    tablename = 'Profesional'

    id_usuario = Column(Integer, primary_key=True)
    
