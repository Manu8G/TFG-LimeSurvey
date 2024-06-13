from pydantic import BaseModel

class nuevoUsuario(BaseModel):
    name: str
    password: str
    role: str
    accessToken: str
