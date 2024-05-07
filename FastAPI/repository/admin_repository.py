from utils.db_connection import create_db_connection
from dto.survery import Survery

class AdminRepository():
    engine = create_db_connection()
    
    
    def create_survery(data: Survery):
        list_user = self.engine.query(User).all()
        list_user_id_filter = self.engine.query(User).filter(User.id_usuario == data.id_usuario).first()
        #[User(id_usuario =1 , name= juan), User(id_usuario =1 , name= juan),]
        usuario_one = list_user[0] if list_user else None

        return usuario_one.sessions


        # Select * from Session where User.id_usuario == "0001" join ......
