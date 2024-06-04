from LimeAPI import Api
from passlib.context import CryptContext
# import base64  # to encode the surveys
# import config
# import json

url = "http://localhost/limesurvey/index.php/admin/remotecontrol"
username = "manuel"
password = "1234Lime"

# Open a session.
api = Api(url, username, password)

# ------------------------------------------ENCUESTAS, SECCIONES Y PREGUNTAS-------------------------------

'''
api.add_survey("prueba encuesta 4", "es")
survey_id = api.get_survey_id_by_name("prueba encuesta 4")
print('ESte es el id de la encuesta: ' + str(survey_id))
'''
'''
for survey in result:
    print("Datos de la encuesta: "+str(survey))
    sid = survey[0] 
    print("Esta es la SID de la encuesta: "+sid)

'''
'''
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print('Esta es la contraseña del user1: ' + str(pwd_context.hash('23PsR')))
print('ESte es la contraseña del user2: ' + str(pwd_context.hash('GpP2022')))
print('ESte es la contraseña del user3: ' + str(pwd_context.hash('UcR2024')))
Esta es la contraseña del user1: $2b$12$tGEZlbl1trH5H79w2WXg9uMbmQewYHvxZoZxW2bCza4SkkzVwenhm
ESte es la contraseña del user2: $2b$12$e/BblQBeEn33LSHhcV3kyOXXSiADBPAT975/yWtee9LZRI99MDXDC
ESte es la contraseña del user3: $2b$12$xjO4ZImnCL/vRb2LC7qTV.7HbvjOXTumy9HbbEAnp1Ax9rB2EyM7C
'''
# api.check_if_exists_survey(227517)

# <-----Añadir una encuesta----->
# api.add_survey("Prueba de API V2", "es")

# api.delete_survey('604020')
# result = api.list_surveys()

# <-----Añadir una seccion----->
# api.add_section(957144,"seccion datos personales")
# idseccion = api.list_sections(957144)
# idseccion = idseccion[0]
# idseccion = api.get_section_id_by_name(957144, "seccion datos personales")
# print("Esto se imprime asi: "+str(idseccion))

# <-----Añadir una pregunta----->
# api.add_question(957144, idseccion, "preguntaSeccionPersonal", "Como te llamas?", "T")

'''
# Ejemplo creacion de encuesta completa
api.add_survey("Encuesta simple de datos personales", "es")
api.add_section(957144,"seccion datos p0ersonales")
api.add_question(957144, idseccion, "preguntaSeccionPersonal", "Como te llamas?", "T")
'''

# print(str(api.get_survey_id()))
# print(str(api.get_section_id(957144)))
# print(str(api.get_question_id(957144, 2)))

'''
# Listar todas las encuestas, secciones y preguntas
result = api.list_surveys()
for survey in result:
    sid = survey[0] 
    print("Esta es la SID de la encuesta: "+sid)
    secciones = api.list_sections(sid)
    print("\n\nEstos son los datos de sus secciones: "+str(secciones))
    for section in secciones:
        print("Estos son los datos de la seccion: "+str(section))
        primero, segundo = section
        idseccion = api.get_section_id_by_name(section[0], section[1])
        questions = api.list_questions(sid, idseccion)
        print('Estos son los datos de las preguntas: '+str(questions))
        for question in questions:
            print("Estos son los datos de la pregunta: "+str((question)))

'''

'''
result = api.add_question(777423, 20, "Q001", "¿Como te llamas?", "T")
print(result)

api.add_question(777423, 20, "ColorOjos", "¿De que color tienes los ojos?", "L")
api.add_question(777423, 20, "ColorPelo", "¿De que color tienes el pelo?", "S")
api.add_question(777423, 20, "Mascota", "¿Que mascota/s tienes?", "M")
'''
# api.get_section_info(777423)
# api.add_answer(777423, 20, "")

# ---------------------------------------------------EMAIL---------------------------------------------------


# api.add_question(868618, 21, 1)

'''
resultadito = api.get_responses(957144)
print("Opcion resultado: "+ str(resultadito))
'''

'''
api.activate_survey(777423)
api.add_participant_table(777423)
participantes = [{'email': 'manuelmesias@correo.ugr.es', 'lastname': 'Guerrero', 'firstname': 'Manu' }]
api.add_participant(777423, participantes)
participantesL = api.list_participants(777423)
participante = [participant['tid'] for participant in participantesL]
print('ID del participante: ' + str(participante[0]))
tokensP = [participante[0]]
api.invite_participant(777423, tokensP)
'''

'''     Eliminar un participante de una encuesta
token = [1, 2]  # ELimina los participantes de la encuesta con ID 1 y 2
result = api.delete_participant("777423", token)
print('Resultado de la invitacion: ' + str(result))
'''


api.release_session_key()