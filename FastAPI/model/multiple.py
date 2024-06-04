from sqlalchemy import Column, Integer
from model import Base

class Multiple(Base):
    tablename = "Multiple"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)