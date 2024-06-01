from sqlalchemy import Column, Integer, Date
from .database import Base

class VersionFormulario(Base):
    tablename = "VersionFormularioTiene"

    id_formulario = Column(Integer, primary_key=True, index=True)
    id_version_formulario = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)