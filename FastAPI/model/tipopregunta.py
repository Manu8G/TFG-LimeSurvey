from sqlalchemy import Column, Integer
from model import Base

class TipoPreguntar(Base):
    __tablename__ = "TipoPregunta"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)