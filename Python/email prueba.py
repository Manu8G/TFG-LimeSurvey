import requests

# Configuración de LimeSurvey
URL_API = 'http://your-limesurvey-site/index.php/admin/remotecontrol'
USERNAME = 'your_username'
PASSWORD = 'your_password'
SURVEY_ID = 'your_survey_id'

def get_session_key(url_api, username, password):
    data = {
        'method': 'get_session_key',
        'params': [username, password],
        'id': 1,
    }
    response = requests.post(url_api, json=data).json()
    return response['result']

def add_participants(url_api, session_key, survey_id, participants):
    data = {
        'method': 'add_participants',
        'params': [session_key, survey_id, participants, True],  # True para crear tokens
        'id': 1,
    }
    response = requests.post(url_api, json=data).json()
    return response['result']

def send_invitations(url_api, session_key, survey_id, participant_ids):
    data = {
        'method': 'invite_participants',
        'params': [session_key, survey_id, participant_ids, True],  # True para enviar correos
        'id': 1,
    }
    response = requests.post(url_api, json=data).json()
    return response['result']

def release_session_key(url_api, session_key):
    data = {
        'method': 'release_session_key',
        'params': [session_key],
        'id': 1,
    }
    requests.post(url_api, json=data)

# Iniciar sesión en LimeSurvey y obtener una clave de sesión
session_key = get_session_key(URL_API, USERNAME, PASSWORD)

# Lista de participantes a añadir
participants = [
    {'firstname': 'John', 'lastname': 'Doe', 'email': 'john.doe@example.com'},
    # Añade más participantes según sea necesario
]

# Añadir participantes
added_participants = add_participants(URL_API, session_key, SURVEY_ID, participants)
participant_ids = [participant['tid'] for participant in added_participants]

# Enviar invitaciones por correo electrónico a los participantes añadidos
send_invitations(URL_API, session_key, SURVEY_ID, participant_ids)

# Liberar la clave de sesión
release_session_key(URL_API, session_key)

print("Usuarios añadidos e invitaciones enviadas.")
