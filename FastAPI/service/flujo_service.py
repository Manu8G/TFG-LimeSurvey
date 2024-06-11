from utils.Lime_API_run import api
from repository.flujo_repository import FlujoRepository

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
      raise RuntimeError(f"EncuestaServices: algo fue mal en listar_encuestas: {str(e)}")
    
