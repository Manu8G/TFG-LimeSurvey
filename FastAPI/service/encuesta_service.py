from utils.Lime_API_run import api


class encuestaService:
  def __init__(self):
    None
    
  def crear_encuesta(self, nombre_encuesta: str, idioma: str):
    try:
      return api.add_survey(nombre_encuesta, idioma)
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en create_encuesta: {str(e)}")
    
  def listar_encuestas(self):
    try:
      surveys = api.list_surveys()
      cont = 0
      datos = {}
      for sid, survey_title in surveys:
          # print(f"Survey ID: {sid}, Survey Title: {survey_title}")    
          dato = ('{cont}', '{sid}-{survey_title}')
          datos[f"{sid}"] = survey_title
          cont += 1
      return datos
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en listar_encuestas: {str(e)}")
    