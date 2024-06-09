from sqlalchemy import Column, Integer
from model import Base

class Multiple(Base):
    __tablename__ = "Multiple"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)