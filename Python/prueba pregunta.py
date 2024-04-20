import requests
import json

# Configura la URL de la API de LimeSurvey y tu clave de API
api_url = 'https://tu-servidor-limesurvey.com/index.php/admin/remotecontrol'
api_key = 'Tu-API-Key'

# Define los datos para la sección y la pregunta
survey_id = 123  # Reemplaza con el ID de la encuesta existente
section_title = 'Nueva Sección'
question_title = 'Nueva Pregunta'
question_type = 'T'  # Tipo de pregunta (puedes ajustarlo según tus necesidades)

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

# Obtén el ID de la sección recién creada (necesario para la pregunta)
section_id = json.loads(response.text)['result']

# Crea la pregunta en la sección
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
