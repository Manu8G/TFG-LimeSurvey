from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Respuesta(Base):
    tablename = "RespuestaPoseeResponde"

    id_participacion = Column(Integer, primary_key=True, index=True)
    id_respuesta = Column(Integer, primary_key=True, index=True)
    id_pregunta = Column(Integer, index=True)