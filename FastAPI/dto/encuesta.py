from pydantic import BaseModel

class Encuesta(BaseModel):
    nombre_encuesta: str
    idioma: str
