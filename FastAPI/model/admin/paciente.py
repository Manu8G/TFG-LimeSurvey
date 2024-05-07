from sqlalchemy import Column, Integer, String
from model import Base

class User(Base):
    __tablename__ = 'users'

    id_usuario = Column(Integer, primary_key=True)
    username = Column(String , nullable=False)
    password = Column(String(128), nullable=False) 
    DNI = Column(String(9) , nullable=True)
    ...
    sessions = relationship("SessionHospital", backref="user")