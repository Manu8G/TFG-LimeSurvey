from pydantic import BaseModel

class Seccion(BaseModel):
    nombre_seccion: str
    id_encuesta: str
