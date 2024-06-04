from sqlalchemy import Column, Integer
from model import Base

class TipoPreguntar(Base):
    tablename = "TipoPregunta"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)