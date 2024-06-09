from sqlalchemy import Column, Integer, String
from model import Base

class Formulario(Base):
    __tablename__ = "FormularioCrea"

    id_formulario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    id_usuario = Column(Integer, index=True)
    