from utils.Lime_API_run import api
from typing import List

class preguntaService:
    def __init__(self):
        None
    
    def crear_pregunta_texto(self, id_encuesta: str, id_seccion: str, nombre_real: str, cuerpo_pregunta: str):
        print("Estamos dentro2")
        try:
            return api.add_text_question(id_encuesta, id_seccion, nombre_real, cuerpo_pregunta)
        except Exception as e:
            raise RuntimeError(f"PreguntaServices: algo fue mal en create_pregunta: {str(e)}")
        
    def crear_pregunta_multiple(self, id_encuesta: str, id_seccion: str, nombre_real: str, cuerpo_pregunta: str, respuestas: List[str]):
        try:
            return api.add_multiple_question(id_encuesta, id_seccion, nombre_real, cuerpo_pregunta, respuestas)
        except Exception as e:
            raise RuntimeError(f"PreguntaServices: algo fue mal en create_pregunta: {str(e)}")