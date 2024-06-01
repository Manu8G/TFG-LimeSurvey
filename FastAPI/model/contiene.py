from sqlalchemy import Column, Integer
from .database import Base

class Contiene(Base):
    tablename = "Contiene"

    id_contiene = Column(Integer, primary_key=True, index=True)
    id_pregunta = Column(Integer, index=True)
    id_version_formulario = Column(Integer,  index=True)
    id_formulario = Column(Integer, index=True)
