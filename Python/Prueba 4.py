import requests
import json
import urllib.request as urllib2
import sys
import xmlrpc.client

url = "http://localhost/limesurvey/index.php/admin/remotecontrol"
username = "manuel"
password = "1234Lime"

# Autenticación en la API de LimeSurvey
api_key_data = {
    "method":"get_session_key",
    "params":["manuel","1234Lime"],
    "jsonrpc": "2.0",
    "plugin": "Authd",
    "id": 1
}

def get_session_key():
    req = urllib2.Request(url, json.dumps(api_key_data).encode('utf-8'))
    req.add_header('content-type', 'application/json')
    req.add_header('connection', 'Keep-Alive')

    try:
        with urllib2.urlopen(req) as f:
            myretun = f.read()
            j = json.loads(myretun.decode('utf-8'))
            return j['result']
    except urllib2.URLError as e:
        return f"Error: {e}"




# Crear encuesta
def crear_encuesta2(titulo, descripcion):
    endpoint = "surveys"
    data = {
        "surveyls_title": titulo,
        "surveyls_description": descripcion,
        "format": "json",
    }
    response = requests.post(url + endpoint, headers, json=data)
    print("ESTE ES EL RESULTADO: \n", response.json(), "\nFIN")
    return response.json()
    



def crear_encuesta(titulo, descripcion):
    sesion_key=get_session_key()
    endpoint = "/asurveys"
    headers1 = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {sesion_key}"
    } 
    data = {
        "method":"add_survey",
        "sSessionKey": sesion_key,
        "sSurveyTitle": titulo,
        "sSurveyLanguage": "es",
        "format": "json",
    }

    req = urllib2.Request(url, json.dumps(data).encode('utf-8'))
    req.add_header('content-type', 'application/json')
    req.add_header('connection', 'Keep-Alive')

    try:
        with urllib2.urlopen(req) as f:
            myretun = f.read()
            #j = json.loads(myretun.decode('utf-8'))
            #return j['result']
            return myretun
    except urllib2.URLError as e:
        print(f"Error en la solicitud HTTP: {e}")
        print("Contenido de la respuesta:", myretun)
    
    response = requests.post(url, headers=headers1, json=data)

    print("Contenido de la respuesta:", response.status_code)
    print("Contenido de la respuesta:", response.text)
    if response.status_code == 200:
        print("ESTE ES EL RESULTADO: \n", response.json(), "\nFIN")
        return response.json()
    else:
        print(f"Error en la solicitud HTTP. Código de estado: {response.status_code}")
        return None

def crear_encuesta3():
    connection = xmlrpc.client.ServerProxy(url)
    api_key = get_session_key()
    # Obtener clave de sesión
    session_key = connection.get_session_key(username, api_key)

    # Crear encuesta
    survey_data = {
        "surveyls_title": "Mi Encuesta",
        "surveyls_description": "Descripción de la encuesta",
        "language": "es",
    }

    survey_id = connection.create_survey(session_key, "LimeSurvey", survey_data)

    # Imprimir el ID de la encuesta creada
    print(f"Encuesta creada con ID: {survey_id}")
    return survey_id


# Crear pregunta en una encuesta
def crear_pregunta(encuesta_id, tipo, texto_pregunta):
    endpoint = f"surveys/{encuesta_id}/groups"
    data = {
        "group_name": "Grupo 1",
        "group_order": 1,
        "questions": [
            {
                "type": tipo,
                "title": texto_pregunta,
                "question": texto_pregunta,
            }
        ],
    }
    response = requests.post(url + endpoint, headers=headers, json=data)
    return response.json()

# Ejemplo de uso
encuesta = crear_encuesta3()
print(encuesta)

print("MACARENA: \n")
encuesta_id = encuesta["id"]

pregunta = crear_pregunta(encuesta_id, "T", "¿Cuál es tu edad?")

print(f"Encuesta creada con ID: {encuesta_id}")
print(f"Pregunta creada con ID: {pregunta['id']}")
