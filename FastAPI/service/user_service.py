from repository.user_repository import UserRepository
from dto.user import UserInDB

class UserService:
  def __init__(self):
    self.user_repository = UserRepository()

  def get_user(self, username: str) -> UserInDB:
    try:
      return self.user_repository.get_user_db(username = username)
    except Exception as e:
      raise RuntimeError(f"Something goes wrong {str(e)}")