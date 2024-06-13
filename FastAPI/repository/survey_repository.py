from sqlalchemy.orm import Session
from model.formulario import Formulario
from model.versionformulario import VersionFormulario
from datetime import datetime

from utils.utils import pwd_context
from utils.db_connections import create_db_connection

class SurveyRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()

    def create_survey_in_db(self, nombre: str, id_usuario: int):
        id_maximo = self.db.query(Formulario).order_by(Formulario.id_formulario.desc()).first()
        nuevo_id = id_maximo.id_formulario + 1
        # FALLA EN EL SIGUINETE ID_USUARIO
        db_formulario = Formulario(id_formulario=nuevo_id, nombre=nombre, id_usuario=id_usuario)
        self.db.add(db_formulario)
        self.db.commit()
        self.db.refresh(db_formulario)

        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")

        db_Vformulario = VersionFormulario(id_formulario=nuevo_id, id_version_formulario=1, fecha=formatted_date)
        self.db.add(db_Vformulario)
        self.db.commit()
        self.db.refresh(db_Vformulario)
        return db_formulario
        