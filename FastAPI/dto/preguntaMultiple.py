from pydantic import BaseModel
from typing import List

class PreguntaMultiple(BaseModel):
    nombre_real: str
    cuerpo_pregunta: str
    id_encuesta: str
    id_seccion: str
    tipo_pregunta: str
    respuestas: List[str]