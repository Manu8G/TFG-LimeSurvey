from sqlalchemy import Column, Integer, String
from model import Base

class Valor(Base):
    tablename = "ValortieneRespuesta"

    id_valor = Column(Integer, primary_key=True, index=True)
    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)
    valor = Column(String, index=True)