from sqlalchemy.orm import Session
from model.user import User
from dto.user import UserInDB 
from utils.utils import pwd_context
from utils.db_connection import create_db_connection

class UserRepository:
    
    def __init__(self) -> None:
        self.db = create_db_connection()

    def get_user_db(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, user: UserInDB):
        fake_hashed_password = pwd_context.hash(user.password)
        db_user = User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
 

