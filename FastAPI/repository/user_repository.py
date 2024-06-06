from sqlalchemy.orm import Session
from model.user import User
from utils.utils import pwd_context
from utils.db_connections import create_db_connection

class UserRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()

    def get_user_db(self, name: str):
        return self.db.query(User).filter(User.nombre_y_apellidos == name).first()

    def create_user(self, name: str, password: str):
        print("EStamos en user_repository.py")
        fake_hashed_password = pwd_context.hash(password)
        db_user = User(password=password, nombre_y_apellidos=name)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
 

