from sqlalchemy import Column, Integer, String, Boolean, Date, Time
from .database import Base

class Sesion(Base):
    tablename = "SesionAsisteProporciona"

    id_sesion = Column(Integer, primary_key=True, index=True)
    numero_sesion = Column(String, unique=True, index=True)
    fecha = Column(Date, index=True)
    hora = Column(Time, index=True)
    asistencia = Column(String, index=True)
    observaciones = Column(Boolean, index=True)
    id_usuario_profesional = Column(Integer, index=True)
    id_usuario_paciente = Column(Integer, index=True)
    