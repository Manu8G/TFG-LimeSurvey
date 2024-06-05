from utils.Lime_API_run import api


class seccionService:
  def __init__(self):
    None
    
  def create_user(self, seccion_name: str, id_encuesta: str):
    try:
      return api.add_section(id_encuesta,seccion_name)
    except Exception as e:
      raise RuntimeError(f"SeccionServices: something goes wrong: {str(e)}")
    