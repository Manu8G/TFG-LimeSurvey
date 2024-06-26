from model.caso import Caso
from model.formulario import Formulario 
from model.flujo import Flujo
from model.formado import Formado

from utils.utils import pwd_context
from utils.db_connections import create_db_connection
from typing import List

class FlujoRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()


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
            db_formado = Formado(id_formado=id_formadoso, id_flujo=id_flujo_nuevo.id_flujo, id_version_formulario=int(id_formulario_encuesta), id_formulario=int(id_formulario_encuesta), numero_orden=cont)
            self.db.add(db_formado)
            self.db.commit()
            self.db.refresh(db_formado)
            cont += 1
            id_formadoso += 1

        return db_flujo
    


    def list_flujo(self):
        flujos = []
        flujodb = self.db.query(Flujo)
        
        for u in flujodb:
            flujos.append({'id':u.id_flujo , 'nombre':u.tipo_de_flujo})

        return flujos
    

    def asignar_flujo(self, id_flujo: str, id_usuario: str):
        try:
            db_caso = Caso(id_usuario=id_usuario, id_flujo=id_flujo, nivel_actual=1)
            self.db.add(db_caso)
            self.db.commit()
            self.db.refresh(db_caso)

            return db_caso
        except Exception as e:
            raise RuntimeError(f"FlujoResponse: algo fue mal en crear_flujo: {str(e)}")
        
        
    def get_caso(self, id: str):
        try:
            encuestas = []
            db_caso = self.db.query(Caso)
            usuario_caso = db_caso.filter(Caso.id_usuario == id).first()
            db_flujo = self.db.query(Flujo)
            usuario_flujo = db_flujo.filter(Flujo.id_flujo == usuario_caso.id_flujo).first()
            db_formado = self.db.query(Formado)
            usuario_formado = db_formado.filter(Formado.id_flujo == usuario_caso.id_flujo)
            db_formulario = self.db.query(Formulario)
            

            for i in usuario_formado:
                encuesta = db_formulario.filter(Formulario.id_formulario == i.id_formulario).first()
                encuestas.append({'tipo_de_flujo': usuario_flujo.tipo_de_flujo, 
                                  'id_formulario':i.id_formulario, 
                                  'nombre_encuesta':encuesta.nombre, 
                                  'numero_orden': i.numero_orden, 
                                  'nivel_actual': usuario_caso.nivel_actual})
                
            return encuestas
        except Exception as e:
            raise RuntimeError(f"FlujoResponse: algo fue mal en crear_flujo: {str(e)}")    