from sqlalchemy.orm import Session
from model.user import User
from model.administrador import Administrador
from model.profesional import Profesional 
from model.paciente import Paciente

from utils.utils import pwd_context
from utils.db_connections import create_db_connection

class UserRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()

    def get_user_db(self, name: str):
        return self.db.query(User).filter(User.nombre_y_apellidos == name).first()

    def create_user(self, nombre_y_apellidos: str, password: str, role: str):
        fake_hashed_password = pwd_context.hash(password)
        db_user = User(password=fake_hashed_password, nombre_y_apellidos=nombre_y_apellidos)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
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

