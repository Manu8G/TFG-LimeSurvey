from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class User(Base):
    tablename = "Usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_y_apellidos = Column(String, unique=True, index=True)
    password = Column(String, index=True)

    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)