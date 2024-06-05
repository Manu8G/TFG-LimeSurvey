from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

class UserInDB(User):
    hashed_password: str