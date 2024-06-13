from pydantic import BaseModel

class encuestaDB(BaseModel):
    nombre: str
    id_usuario: int
    