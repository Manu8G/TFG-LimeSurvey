from sqlalchemy import Column, Integer, Date
from model import Base

class Finalizada(Base):
    __tablename__ = "Finalizada"

    id_acceso = Column(Integer, primary_key=True, index=True)
    fin = Column(Date, unique=True, index=True)