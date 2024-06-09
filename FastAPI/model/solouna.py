from sqlalchemy import Column, Integer
from model import Base

class SoloUna(Base):
    __tablename__ = "SoloUna"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)