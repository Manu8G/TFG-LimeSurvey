from sqlalchemy import Column, Integer, String
from model import Base

class Flujo(Base):
    __tablename__ = "FlujoCreado"

    id_flujo = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, index=True)
    tipo_de_flujo = Column(Integer, index=True)

