from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Multiple(Base):
    tablename = "Multiple"

    id_tipo_pregunta = Column(Integer, primary_key=True, index=True)