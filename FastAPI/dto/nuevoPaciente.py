from pydantic import BaseModel

class nuevoPaciente(BaseModel):
    nombre_y_apellidos: str
    password: str
    dni: str
    estado: str
    nacionalidad: str
    fecha_nacimiento: str
    email: str

