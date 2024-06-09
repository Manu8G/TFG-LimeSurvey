from sqlalchemy import Column, Integer, Date
from model import Base

class VersionFormulario(Base):
    __tablename__ = "VersionFormularioTiene"

    id_formulario = Column(Integer, primary_key=True, index=True)
    id_version_formulario = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)