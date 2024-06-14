from pydantic import BaseModel

class Caso(BaseModel):
    id_flujo: str
    id_usuario: str