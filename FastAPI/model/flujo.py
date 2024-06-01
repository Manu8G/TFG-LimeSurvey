from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Flujo(Base):
    tablename = "FlujoCreado"

    id_flujo = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, index=True)
    tipo_flujo = Column(Integer, index=True)

