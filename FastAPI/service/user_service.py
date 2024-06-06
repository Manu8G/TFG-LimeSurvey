from repository.user_repository import UserRepository
from dto.user import User

class UserService:
  def __init__(self):
    self.user_repository = UserRepository()

  def get_user(self, name: str) -> User:
    try:
      return self.user_repository.get_user_db(name = name)
    except Exception as e:
      raise RuntimeError(f"Something goes wrong {str(e)}")
    
  def crear_usuario(self, name: str, password: str):
    print("EStamos en user_service.py")
    try:
      print(name, password, name)
      return self.user_repository.create_user(name=name, password=password)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    
  # def create_user(self, name: str, password: str, name: str):
    try:
      print(name, password, name)
      return self.user_repository.create_user(name=name, password=password)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")