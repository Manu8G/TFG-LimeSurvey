from pydantic import BaseModel

class Cita(BaseModel):
    descripcion: str
    fecha: str
    hora: str
    id_paciente: str
    id_profesional: str
