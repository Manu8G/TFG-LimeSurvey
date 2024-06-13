from pydantic import BaseModel
from typing import List

class Flujo(BaseModel):
    id_usuario: str
    tipo_de_flujo: str
    encuestas: List[str]