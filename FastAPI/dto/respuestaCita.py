from pydantic import BaseModel

class respuestaCita(BaseModel):
    id_paciente: str
    respuesta: str