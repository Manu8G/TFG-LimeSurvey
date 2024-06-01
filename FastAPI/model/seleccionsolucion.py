from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class SeleccionSolucion(Base):
    tablename = "SeleccionSolucionEscoge"

    id_respuesta = Column(Integer, primary_key=True, index=True)
    id_valor = Column(Integer, index=True)
    id_participacion = Column(Integer, index=True)
    id_tipo_pregunta = Column(Integer, index=True)
    