from pydantic import BaseModel

class Correo(BaseModel):
    id_encuesta: str
    id_usuario: str
