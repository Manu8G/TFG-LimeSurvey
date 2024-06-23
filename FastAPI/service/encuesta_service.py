from utils.Lime_API_run import api
from repository.survey_repository import SurveyRepository


class encuestaService:
  def __init__(self):
    self.survey_repository = SurveyRepository()
    
  def crear_encuesta(self, nombre_encuesta: str, idioma: str):
    try:
      return api.add_survey(nombre_encuesta, idioma)
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en create_encuesta: {str(e)}")
    

  def create_survey_in_db(self, nombre: str, id_usuario: int):
    try:
      return self.survey_repository.create_survey_in_db(nombre=nombre, id_usuario=id_usuario)
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en create_encuesta: {str(e)}")


  def listar_encuestas(self):
    try:
      print('yes1')
      surveys = api.list_surveys()
      print('yes2')
      cont = 0
      print('yes3')
      datos = {}
      print('yes4')
      for sid, survey_title in surveys:
          print('yes 5 sid: '+sid)
          print('yes 6 sid: '+survey_title)
          datos[f"{sid}"] = survey_title
          print('yes7')
          cont += 1
          print('yes8')
      return datos
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en listar_encuestas: {str(e)}")
    

  def eliminar_encuesta(self, id: str):
    try:
      return self.survey_repository.eliminar_encuesta(id=id)
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en eliminar_encuesta: {str(e)}")
  

  def mandar_correo(self, id_encuesta: str, id_usuario: str):
    try:
      return self.survey_repository.mandar_correo(id_encuesta=id_encuesta, id_usuario=id_usuario)
    except Exception as e:
      raise RuntimeError(f"EncuestaServices: algo fue mal en eliminar_encuesta: {str(e)}")
