from sqlalchemy.orm import Session
from model.formulario import Formulario
from model.user import User
from model.paciente import Paciente
from model.versionformulario import VersionFormulario
from datetime import datetime
from fastapi import HTTPException
from utils.Lime_API_run import api

from utils.utils import pwd_context
from utils.db_connections import create_db_connection

class SurveyRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()


    def create_survey_in_db(self, nombre: str, id_usuario: int):
        encuestas = api.list_surveys()
        for i in encuestas:
            if i[1] == nombre:
                id_formulario_version = i[0]
                break
        db_formulario = Formulario(id_formulario=id_formulario_version, nombre=nombre, id_usuario=id_usuario)
        self.db.add(db_formulario)
        self.db.commit()
        self.db.refresh(db_formulario)

        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")

        db_Vformulario = VersionFormulario(id_formulario=id_formulario_version, id_version_formulario=id_formulario_version, fecha=formatted_date)
        self.db.add(db_Vformulario)
        self.db.commit()
        self.db.refresh(db_Vformulario)
        return db_formulario
    

    def eliminar_encuesta(self, id: str):
        db_Vformulario = self.db.query(VersionFormulario).filter(VersionFormulario.id_formulario == id).first()
        db_formulario = self.db.query(Formulario).filter(Formulario.id_formulario == id).first()
        
        if not db_formulario:
            raise HTTPException(status_code=404, detail="Formulario no encontrado")

        self.db.delete(db_Vformulario)
        self.db.commit()
        # Eliminar el formulario encontrado
        self.db.delete(db_formulario)
        self.db.commit()

        api.delete_survey(id)
        # Puedes elegir qué devolver, aquí simplemente devolvemos un mensaje de éxito
        return {"mensaje": "Formulario eliminado correctamente"}
    

    def mandar_correo(self, id_encuesta: str, id_usuario: str):
        api.activate_survey(int(id_encuesta))
        api.add_participant_table(int(id_encuesta))
        db_usuario = self.db.query(User).filter(User.id_usuario == id_usuario).first()
        db_paciente = self.db.query(Paciente).filter(Paciente.id_usuario == id_usuario).first()
        nombre_y_apellidos = db_usuario.nombre_y_apellidos
        nombre = nombre_y_apellidos.split(' ',1)
        nombre_correo = ''
        apellido_correo = ''

        if nombre[0]:
            nombre_correo = nombre[0]
        else:
            nombre_correo = 'Nombre'
        try:
            if nombre[1]:
                apellido_correo = nombre[1]
            else:
                apellido_correo = 'Apellidos'
        except:
            None
        
        participante = [{'email': str(db_paciente.email), 'lastname': apellido_correo, 'firstname': nombre_correo}]
        api.add_participant(int(id_encuesta), participante)
        participantesL = api.list_participants(int(id_encuesta))
        participante = [participant['tid'] for participant in participantesL]
        tokensP = [participante[0]]
        api.invite_participant(int(id_encuesta), tokensP)
        
        # Puedes elegir qué devolver, aquí simplemente devolvemos un mensaje de éxito
        return {"mensaje": "Correo enviado correctamente"}
        