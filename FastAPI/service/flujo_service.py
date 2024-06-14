from utils.Lime_API_run import api
from repository.flujo_repository import FlujoRepository
from typing import List

class flujoService:
  
  def __init__(self):
    self.flujo_repository = FlujoRepository()
    
#   def crear_flujo(self, nombre_encuesta: str, idioma: str):
#     try:
#       return api.add_survey(nombre_encuesta, idioma)
#     except Exception as e:
#       raise RuntimeError(f"EncuestaServices: algo fue mal en create_encuesta: {str(e)}")
    

  def list_flujo(self):
    try:
      return self.flujo_repository.list_flujo()
    except Exception as e:
      raise RuntimeError(f"FlujoService: algo fue mal en listar_encuestas: {str(e)}")
    

  def create_flujo(self, id_usuario: int, tipo_de_flujo: str, encuestas: List[str]):
    try:
      return self.flujo_repository.create_flujo(id_usuario=id_usuario, tipo_de_flujo=tipo_de_flujo, encuestas=encuestas)
    except Exception as e:
      raise RuntimeError(f"FlujoService: algo fue mal en crear_flujo: {str(e)}")
    

  def listar_flujos(self):
    try:
      return self.flujo_repository.listar_flujos()
    except Exception as e:
      print("ERROR LISTAR FLUJOS "+e)
      raise RuntimeError(f"FlujoService: algo fue mal en crear_flujo: {str(e)}")
    

  def asignar_flujo(self, id_flujo: str, id_usuario: str):
    try:
      return self.flujo_repository.asignar_flujo(id_flujo=id_flujo, id_usuario=id_usuario)
    except Exception as e:
      raise RuntimeError(f"FlujoService: algo fue mal en crear_flujo: {str(e)}")
    

  def get_caso(self, id: str):
    try:
      return self.flujo_repository.get_caso(id)
    except Exception as e:
      print("ERROR LISTAR FLUJOS "+e)
      raise RuntimeError(f"FlujoService: algo fue mal en crear_flujo: {str(e)}")