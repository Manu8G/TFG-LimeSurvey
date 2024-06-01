from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class RespuestaLibreSolucion(Base):
    tablename = "RespuestaLibresolucionCompleta"

    id_respuesta = Column(Integer, primary_key=True, index=True)
    id_participacion = Column(Integer, primary_key=True, index=True)
    texto_respuesta = Column(String, index=True)
    id_tipo_pregunta = Column(Integer, index=True)
