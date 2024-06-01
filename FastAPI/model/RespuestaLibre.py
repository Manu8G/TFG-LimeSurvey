from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class RespuestaLibre(Base):
    tablename = "RespuestaLibre"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)
    longitud = Column(Integer, index=True)