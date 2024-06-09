from utils.Lime_API_run import api


class seccionService:
  def __init__(self):
    None
    
  def crear_seccion(self, nombre_seccion: str, id_encuesta: str):
    try:
      return api.add_section(id_encuesta,nombre_seccion)
    except Exception as e:
      raise RuntimeError(f"SeccionServices: something goes wrong: {str(e)}")
    

  def listar_secciones(self, id_encuesta):
    try:
      sections = api.list_sections(id_encuesta)
      cont = 0
      datos = {}
      for gid, group_name in sections:
          datos[f"{gid}"] = group_name
          cont += 1
      return datos
    except Exception as e:
      raise RuntimeError(f"SeccionServices: algo fue mal en listar_seccion: {str(e)}")