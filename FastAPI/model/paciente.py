from sqlalchemy import Column, Integer, String, Date
from model import Base

class Paciente(Base):
    __tablename__ = 'Paciente'

    id_usuario = Column(Integer, primary_key=True)
    dni = Column(String , nullable=False)
    estado = Column(String , nullable=False) 
    nacionalidad = Column(String , nullable=True)
    fecha_nacimiento = Column(Date , nullable=True)
    email = Column(String , nullable=True)

