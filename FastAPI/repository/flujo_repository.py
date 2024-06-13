from model.user import User 
from model.paciente import Paciente
from model.flujo import Flujo
from model.formado import Formado

from utils.utils import pwd_context
from utils.db_connections import create_db_connection
from typing import List

class FlujoRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()


    def list_flujo(self):
        flujo_list = []
        flujos = self.db.query(Flujo)
        
        for u in flujos:
            flujo_list.append((u.id_flujo, u.tipo_de_flujo))

        return flujo_list


    def create_flujo(self, id_usuario: int, tipo_de_flujo: str, encuestas: List[str]):
        db_flujo = Flujo(id_usuario=id_usuario, tipo_de_flujo=tipo_de_flujo)
        self.db.add(db_flujo)
        self.db.commit()
        self.db.refresh(db_flujo)


        id_flujo_nuevo = self.db.query(Flujo).order_by(Flujo.id_flujo.desc()).first()
        id_formado_nuevo = self.db.query(Formado).order_by(Formado.id_formado.desc()).first()
        id_formadoso = id_formado_nuevo.id_formado + 1
        cont = 1

        for id_formulario_encuesta in encuestas:
            db_formado = Formado(id_flujo=id_flujo_nuevo.id_flujo, id_formado=id_formadoso, id_version_formulario=int(id_formulario_encuesta), id_formulario=int(id_formulario_encuesta), numero_orden=cont)
            self.db.add(db_formado)
            self.db.commit()
            self.db.refresh(db_formado)
            cont += 1
            id_formadoso += 1
        # 614399
        return db_flujo
    


    def listar_flujos(self):
        flujos = []
        flujodb = self.db.query(Flujo)
        
        for u in flujodb:
            flujos.append((u.id_flujo ,u.tipo_de_flujo))

        return flujos
    

    def asignar_flujos(self, id_usuario: int, tipo_de_flujo: str, encuestas: List[str]):
        db_flujo = Flujo(id_usuario=id_usuario, tipo_de_flujo=tipo_de_flujo)
        self.db.add(db_flujo)
        self.db.commit()
        self.db.refresh(db_flujo)

        return db_flujo