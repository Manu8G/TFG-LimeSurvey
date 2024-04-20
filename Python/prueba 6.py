import requests

# URL de la API de LimeSurvey y endpoint específico para crear una encuesta
api_url = 'https://tu-servidor-limesurvey.com/index.php/admin/remotecontrol'
create_survey_endpoint = 'surveys'

# Las credenciales de acceso a la API
api_key = 'Tu-API-Key'
username = 'Tu-Usuario'

# Headers necesarios para la autenticación
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {api_key}:{username}'
}

# Datos para crear una nueva encuesta
nueva_encuesta = {
    'title': 'Mi Encuesta',
    'language': 'es',
    # Agrega otros parámetros necesarios aquí
}

# Realizar la solicitud POST para crear la encuesta
response = requests.post(f'{api_url}/{create_survey_endpoint}', json=nueva_encuesta, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print('Encuesta creada con éxito.')
else:
    print('No se pudo crear la encuesta. Código de estado:', response.status_code)
    print('Mensaje de error:', response.text)
