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

    def create_user(self, name: str, password: str):
        fake_hashed_password = pwd_context.hash(password)
        db_user = User(password=password, nombre_y_apellidos=name)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
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
                admin_view.append(u.nombre_y_apellidos)

            elif profesional.filter(Profesional.id_usuario == u.id_usuario).first() and not admin.filter(Administrador.id_usuario == u.id_usuario).first():
                admin_view.append(u.nombre_y_apellidos)
        
        return admin_view

    def list_users_for_profesional(self):
        profesional_view = []
        users = self.db.query(User)
        patient = self.db.query(Paciente)
        
        for u in users:

            if patient.filter(Paciente.id_usuario == u.id_usuario).first():
                profesional_view.append(u.nombre_y_apellidos)

        return profesional_view
