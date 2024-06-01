from sqlalchemy import Column, Integer, String, Date
from model import Base

class User(Base):
    tablename = 'Paciente'

    id_usuario = Column(Integer, primary_key=True)
    dni = Column(String , nullable=False)
    estado = Column(String , nullable=False) 
    nacionalidad = Column(String , nullable=True)
    fecha_nacimiento = Column(Date , nullable=True)
    email = Column(String , nullable=True)

