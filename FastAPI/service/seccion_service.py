from utils.Lime_API_run import api


class seccionService:
  def __init__(self):
    None
    
  def crear_seccion(self, nombre_seccion: str, id_encuesta: str):
    try:
      return api.add_section(id_encuesta,nombre_seccion)
    except Exception as e:
      raise RuntimeError(f"SeccionServices: something goes wrong: {str(e)}")
    