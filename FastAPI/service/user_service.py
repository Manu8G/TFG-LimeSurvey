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
    
  def crear_usuario(self, nombre_y_apellidos: str, password: str, role: str):
    try:
      return self.user_repository.create_user(nombre_y_apellidos=nombre_y_apellidos, password=password, role=role)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    

  def create_patient(self, nombre_y_apellidos: str, password: str, dni: str, estado: str, nacionalidad: str, fecha_nacimiento: str, email: str):
    try:
      return self.user_repository.create_patient(nombre_y_apellidos=nombre_y_apellidos, password=password, dni=dni, estado=estado, nacionalidad=nacionalidad, fecha_nacimiento=fecha_nacimiento, email=email)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")


  def obtener_rol(self, name: str):
    try:
      return self.user_repository.obtener_rol(name=name)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")


  # def create_user(self, name: str, password: str, name: str):
    try:
      return self.user_repository.create_user(name=name, password=password)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    

  def list_users_for_admin(self):
    try:
      return self.user_repository.list_users_for_admin()
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")


  def list_users_for_profesional(self):
    try:
      return self.user_repository.list_users_for_profesional()
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    

  def get_user_id(self, nombre_y_apellidos: str, password: str, role: str):
    try:
      return self.user_repository.get_user_id(nombre_y_apellidos=nombre_y_apellidos, password=password, role=role)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")


  def get_user_info(self, id: str):
    try:
      return self.user_repository.get_user_info(id=id)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    
  
  def delete_user(self, id: str):
    try:
      return self.user_repository.delete_user(id=id)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    

  def cita_user(self, descripcion: str, fecha: str, hora: str, id_paciente: str, id_profesional: str):
    try:
      return self.user_repository.cita_user(descripcion=descripcion, fecha=fecha, hora=hora, id_paciente=id_paciente, id_profesional=id_profesional)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    

  def get_cita(self, id: str):
    try:
      return self.user_repository.get_cita(id)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    
  def respuesta_cita(self, id_paciente: str, respuesta: str):
    try:
      return self.user_repository.respuesta_cita(id_paciente=id_paciente, respuesta=respuesta)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")
    
  def estado_encuesta(self, id: str):
    try:
      return self.user_repository.estado_encuesta(id=id)
    except Exception as e:
      raise RuntimeError(f"AdminService: something goes wrong: {str(e)}")