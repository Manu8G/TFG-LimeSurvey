from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Formulario(Base):
    tablename = "FormularioCrea"

    id_formulario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    id_usuario = Column(Integer, index=True)
    