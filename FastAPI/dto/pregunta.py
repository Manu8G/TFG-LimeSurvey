from pydantic import BaseModel

class Pregunta(BaseModel):
    nombre_real: str
    cuerpo_pregunta: str
    id_encuesta: str
    id_seccion: str
    tipo_pregunta: str