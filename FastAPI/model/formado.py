from sqlalchemy import Column, Integer, String
from model import Base

class Formado(Base):
    __tablename__ = "Formado"

    id_formado = Column(Integer, primary_key=True, index=True)
    id_flujo = Column(String, unique=True, index=True)
    id_version_formulario = Column(String, index=True)
    id_formulario = Column(Integer, index=True)
    numero_orden = Column(String, index=True)