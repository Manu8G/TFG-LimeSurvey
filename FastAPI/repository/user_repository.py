import json
from sqlalchemy.orm import Session
from model.user import User
from model.administrador import Administrador
from model.profesional import Profesional 
from model.paciente import Paciente
from model.caso import Caso
from model.versionformulario import VersionFormulario
from model.formulario import Formulario
from model.flujo import Flujo
from model.sesion import Sesion
from model.formado import Formado

from fastapi import HTTPException
from utils.utils import pwd_context
from utils.db_connections import create_db_connection
from utils.Lime_API_run import api

class UserRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()

    def get_user_db(self, name: str):
        return self.db.query(User).filter(User.nombre_y_apellidos == name).first()

    def create_user(self, nombre_y_apellidos: str, password: str, role: str):
        try:
            # Crea una contraseña hasheada simulada
            fake_hashed_password = pwd_context.hash(password)
            db_user = User(password=fake_hashed_password, nombre_y_apellidos=nombre_y_apellidos)
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            
            # Asumiendo que quieres capturar el ID del usuario recién creado
            id_nuevo_paciente = self.db.query(User).order_by(User.id_usuario.desc()).first()
            db_profesional = Profesional(id_usuario=id_nuevo_paciente.id_usuario)
            self.db.add(db_profesional)
            self.db.commit()
            self.db.refresh(db_profesional)
            
            if role == 'admin':
                db_admin = Administrador(id_usuario=id_nuevo_paciente.id_usuario)
                self.db.add(db_admin)
                self.db.commit()
                self.db.refresh(db_admin)
            
            return db_user

        
        except Exception as e:
            print(f"Error general: {e}")
            # Si no quieres especificar que es un error de la base de datos
            raise HTTPException(status_code=500, detail="Error al procesar la solicitud")

    def create_patient(self, nombre_y_apellidos: str, password: str, dni: str, estado: str, nacionalidad: str, fecha_nacimiento: str, email: str,):
        fake_hashed_password = pwd_context.hash(password)
        db_user = User(password=fake_hashed_password, nombre_y_apellidos=nombre_y_apellidos)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        id_nuevo_paciente = self.db.query(User).order_by(User.id_usuario.desc()).first()
        db_patient = Paciente(id_usuario=id_nuevo_paciente.id_usuario,dni=dni, estado=estado, nacionalidad=nacionalidad, fecha_nacimiento=fecha_nacimiento, email=email)
        self.db.add(db_patient)
        self.db.commit()
        self.db.refresh(db_patient)

        return db_patient

    
    def obtener_rol(self, name: str):
        user = self.db.query(User).filter(User.nombre_y_apellidos == name).first()
        if user:
            id_actual = user.id_usuario
            roleA = self.db.query(Administrador).filter(Administrador.id_usuario == id_actual).first()
            roleB = self.db.query(Profesional).filter(Profesional.id_usuario == id_actual).first()
            roleC = self.db.query(Paciente).filter(Paciente.id_usuario == id_actual).first()
            if roleA != None:
                return 'admin'
            elif roleB!= None:
                return 'profesional'
            elif roleC != None:
                return 'paciente'
        else:
            return None
        return None
    
    def list_users_for_admin(self):
        admin_view = []
        users = self.db.query(User)
        patient = self.db.query(Paciente)
        profesional = self.db.query(Profesional)
        admin = self.db.query(Administrador)
        for u in users:
            if patient.filter(Paciente.id_usuario == u.id_usuario).first():
                admin_view.append({'id':u.id_usuario , 'nombre': u.nombre_y_apellidos, 'rol':'Paciente'})

            elif profesional.filter(Profesional.id_usuario == u.id_usuario).first() and not admin.filter(Administrador.id_usuario == u.id_usuario).first():
                admin_view.append({'id':u.id_usuario , 'nombre': u.nombre_y_apellidos, 'rol':'Profesional'})
        
        return admin_view

    def list_users_for_profesional(self):
        profesional_view = []
        users = self.db.query(User)
        patient = self.db.query(Paciente)
        
        for u in users:

            if patient.filter(Paciente.id_usuario == u.id_usuario).first():
                profesional_view.append({'id':u.id_usuario , 'nombre': u.nombre_y_apellidos, 'rol':'Paciente'})

        return profesional_view


    def get_user_id(self, nombre_y_apellidos: str, password: str, role: str):
        fake_hashed_password = pwd_context.hash(password)
        usu = self.db.query(User).filter(User.nombre_y_apellidos == nombre_y_apellidos).first()
        
        return usu.id_usuario
    

    def get_user_info(self, id: str):
        usu = self.db.query(User).filter(User.id_usuario == id).first()
        paciente = self.db.query(Paciente).filter(Paciente.id_usuario == id).first()

        return {'Nombre': usu.nombre_y_apellidos, 'Email': paciente.email, 'Estado':paciente.estado,
                'DNI':paciente.dni, 'Nacionalidad': paciente.nacionalidad, 'Fecha_nacimiento':paciente.fecha_nacimiento}


    def delete_user(self, id: str):
        usu = self.db.query(User).filter(User.id_usuario == id).first()
        paciente = self.db.query(Paciente).filter(Paciente.id_usuario == id).first()
        profesional = self.db.query(Profesional).filter(Profesional.id_usuario == id).first()
        administrador = self.db.query(Administrador).filter(Administrador.id_usuario == id).first()

        if paciente != None:
            caso = self.db.query(Caso).filter(Caso.id_usuario == id).first()
            self.db.delete(caso)
            self.db.commit()
            self.db.delete(paciente)
            self.db.commit()

        if administrador != None:
            verison = self.db.query(VersionFormulario).filter(VersionFormulario.id_usuario == id).first()
            self.db.delete(verison)
            self.db.commit()
            formulario = self.db.query(Formulario).filter(Formulario.id_usuario == id).first()
            self.db.delete(formulario)
            self.db.commit()
            flujo = self.db.query(Flujo).filter(Flujo.id_usuario == id).first()
            self.db.delete(flujo)
            self.db.commit()
            self.db.delete(administrador)
            self.db.commit()
            self.db.delete(profesional)
            self.db.commit()

        if profesional != None:
            try:
                verison = self.db.query(VersionFormulario).filter(VersionFormulario.id_usuario == id).first()
                self.db.delete(verison)
                self.db.commit()
            except:
                None
            try:
                formulario = self.db.query(Formulario).filter(Formulario.id_usuario == id).first()
                self.db.delete(formulario)
                self.db.commit()
            except:
                None
            
            try:
                flujo = self.db.query(Flujo).filter(Flujo.id_usuario == id).first()
                self.db.delete(flujo)
                self.db.commit()
            except:
                None
            self.db.delete(profesional)
            self.db.commit()

        self.db.delete(usu)
        self.db.commit()


        return {'result':'Usuario eliminado con exito'}


    def cita_user(self, descripcion: str, fecha: str, hora: str, id_paciente: str, id_profesional: str):
        hora_ajustada = hora + ':00'
        
        try:
            db_sesion = Sesion(
                numero_sesion='1',
                fecha=fecha, 
                hora=hora_ajustada, 
                asistencia='PC', 
                observaciones=True, 
                id_usuario_profesional=id_profesional, 
                id_usuario_paciente=id_paciente
            )
            self.db.add(db_sesion)
            self.db.commit()
            self.db.refresh(db_sesion)
            return {'resultado': 'todo ok'}
        except Exception as e:
            self.db.rollback()
            print(f"Error2342342: {e}")
            raise HTTPException(status_code=500, detail=str(e))


    def get_cita(self, id: str):
        
        try:
            sesion = self.db.query(Sesion).filter(Sesion.id_usuario_paciente == id).first()
            return {'fecha': sesion.fecha, 'hora':sesion.hora, 'asistencia': sesion.asistencia}
        except Exception as e:
            self.db.rollback()
            print(f"Error2342342: {e}")
            raise HTTPException(status_code=500, detail=str(e))


    def respuesta_cita(self, id_paciente: str, respuesta: str):
        
        try:
            
            sesion = self.db.query(Sesion).filter(Sesion.id_usuario_paciente == id_paciente).order_by(Sesion.id_sesion.desc()).first()
            if respuesta == '0':
                sesion.asistencia = 'No'
            else:
                sesion.asistencia = 'Si'

            self.db.commit()
            self.db.refresh(sesion)


            return {'resultado': 'Todo ok'}
        except Exception as e:
            self.db.rollback()
            print(f"Error2342342: {e}")
            raise HTTPException(status_code=500, detail=str(e))
        

    def estado_encuesta(self, id: str):
        
        try:
            usuario = self.db.query(User).filter(User.id_usuario == id).first()
            nombre_y_apellidos = usuario.nombre_y_apellidos
            nombre = nombre_y_apellidos.split(' ', 1)
            casoUsuario = self.db.query(Caso).filter(Caso.id_usuario == id).first()
            flujoUsuario = self.db.query(Formado).filter(Formado.id_flujo == casoUsuario.id_flujo).first()
            idUsuario = ''

            respuestas = api.get_responses(flujoUsuario.id_formulario)
            participantesL = api.list_participants(flujoUsuario.id_formulario)
            for i in participantesL: 
                nombreEncuestado =  i['participant_info']
                if nombre[0] == nombreEncuestado['firstname']:
                    idUsuario = i['tid']
                    break
            datosRespuesta = json.loads(respuestas)
            
            ids = [response[next(iter(response))]['id'] for response in datosRespuesta['responses']]
            if idUsuario in ids:
                return {'result':'YES'}
            else:
                return {'result':'NO'}

        except Exception as e:
            self.db.rollback()
            print(f"Error2342342: {e}")
            raise HTTPException(status_code=500, detail=str(e))