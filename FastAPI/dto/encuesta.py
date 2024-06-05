from pydantic import BaseModel

class Seccion(BaseModel):
    nombre_encuesta: str
    id_encuesta: str
