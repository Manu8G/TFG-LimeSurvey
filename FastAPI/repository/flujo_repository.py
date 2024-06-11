from model.user import User 
from model.paciente import Paciente
from model.flujo import Flujo

from utils.utils import pwd_context
from utils.db_connections import create_db_connection

class FlujoRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()

    # def get_user_db(self, name: str):
    #     return self.db.query(User).filter(User.nombre_y_apellidos == name).first()

    # def create_flujo(self, name: str, password: str):
    #     fake_hashed_password = pwd_context.hash(password)
    #     db_user = User(password=password, nombre_y_apellidos=name)
    #     self.db.add(db_user)
    #     self.db.commit()
    #     self.db.refresh(db_user)
    #     return db_user


    def list_flujo(self):
        flujo_list = []
        flujos = self.db.query(Flujo)
        
        for u in flujos:
            flujo_list.append((u.id_flujo, u.tipo_de_flujo))

        return flujo_list
