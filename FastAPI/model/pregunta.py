from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Pregunta(Base):
    tablename = "PreguntaElaboraTieneTipo"

    id_pregunta  = Column(Integer, primary_key=True, index=True)
    nombre_real  = Column(String, unique=True, index=True)
    nombre_variable  = Column(String, unique=True, index=True)
    id_usuario  = Column(Integer, index=True)
    id_tipo_pregunta  = Column(Integer, index=True)