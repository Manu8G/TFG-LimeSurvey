from sqlalchemy import Column, Integer
from model import Base

class RespuestaLibre(Base):
    __tablename__ = "RespuestaLibre"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)
    longitud = Column(Integer, index=True)