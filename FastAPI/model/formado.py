from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Formado(Base):
    tablename = "Formado"

    id_formado = Column(Integer, primary_key=True, index=True)
    id_flujo = Column(String, unique=True, index=True)
    id_version_formulario = Column(String, index=True)
    id_formado = Column(String, index=True)
    numero_orden = Column(String, index=True)