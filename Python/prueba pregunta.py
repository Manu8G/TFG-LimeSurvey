import requests
import json

api_url = 'https://tu-servidor-limesurvey.com/index.php/admin/remotecontrol'
api_key = 'Tu-API-Key'


survey_id = 123  
section_title = 'Nueva Sección'
question_title = 'Nueva Pregunta'
question_type = 'T' 

# Crea la sección
section_data = {
    "method": "add_group",
    "params": {
        "sSessionKey": api_key,
        "iSurveyID": survey_id,
        "sGroupTitle": section_title
    }
}

response = requests.post(api_url, json=section_data)

if response.status_code == 200:
    print("Sección creada con éxito.")
else:
    print("Error al crear la sección:", response.text)

section_id = json.loads(response.text)['result']

question_data = {
    "method": "add_question",
    "params": {
        "sSessionKey": api_key,
        "iSurveyID": survey_id,
        "iGroupID": section_id,
        "sQuestionTitle": question_title,
        "sQuestion": "Escribe aquí tu pregunta",
        "sQuestionType": question_type
    }
}

response = requests.post(api_url, json=question_data)

if response.status_code == 200:
    print("Pregunta creada con éxito.")
else:
    print("Error al crear la pregunta:", response.text)
