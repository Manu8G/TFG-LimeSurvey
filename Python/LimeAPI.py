import json
import sys
import random

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from csv import DictReader
from time import sleep


class Api:

    def get_json(self, data):
        data_bytes = data.encode('utf-8')
        req = urllib2.Request(url=self.url, data=data_bytes)
        # req = urllib2.Request(url=self.url, data=data)
        req.add_header('content-type', 'application/json')
        req.add_header('connection', 'Keep-Alive')
        
        try:
            with urllib2.urlopen(req) as f:
                response = f.read().decode('utf-8')
                return json.loads(response)
        except urllib2.URLError as e:
            print(f"Error al abrir la URL: {e}")
            return None
        

    def __init__(self, url, user, pw):
        self.url = url
        self._user = user
        self._password = pw

        data = """{   "id": 1,
                    "method": "get_session_key",
                    "params": { "username": "%s",
                                "password": "%s" } } """ % (user, pw)
        self.session_key = self.get_json(data)['result']


    def check_if_exists_survey(self, sid):
        surveys = self.list_surveys()
        for survey in surveys: 
            if(str(sid) == survey[0]):
                numero_aleatorio = random.randint(100000, 999999)
                print("La encuesta "+ str(sid)+" existe, este seria un sustituto: "+str(numero_aleatorio))
                return numero_aleatorio
        print("La encuesta "+str(sid)+" no existe.")
        return None


    def add_survey(self, survey_title, survey_languaje, format="G"):
        numero_aleatorio = random.randint(100000, 999999)
        self.check_if_exists_survey(numero_aleatorio)
        data = """{ "id": 1,
                    "method": "add_survey",
                    "params": { "sSessionKey": "%s","iSurveyID": %s, 
                    "sSurveyTitle": "%s", "sSurveyLanguage": "%s", "sformat": "%s" } }""" % (self.session_key,
                                                          numero_aleatorio, survey_title,survey_languaje,
                                                          format)
        return self.get_json(data)['result']


    def add_section(self, sid, section_title):
        data = """{ "id": 1,
                    "method": "add_group",
                    "params": { "sSessionKey": "%s","iSurveyID": %s, 
                    "sGroupTitle": "%s" } }""" % (self.session_key,
                                                          sid, section_title)
        return self.get_json(data)['result']


    def add_question(self, sid, gid, question_title, question_body, question_type, languaje):
        print("Estamos dentro de add_question 1")
        data = """{ "id": 1,
                    "method": "add_question",
                    "params": { "sSessionKey": "%s","iSurveyID": "%s",
                    "iGroupID": "%s", "sQuestionTitle": %s,
                    "sQuestion": %s, "sQuestionType": %s, "sLanguage": %s } }""" % (self.session_key,
                                                          sid, gid, question_title, question_body, 
                                                          question_type, languaje)
        print("Data: "+str(self.get_json(data)['result']))
        return self.get_json(data)['result']

    # para el languaje hay q poner "es"
    def add_answer(self, sid, qid, answer_text, answer_code, languaje):
        data = """{ "id": 1,
            "method": "add_question",
            "params": { "sSessionKey": "%s", "iSurveyID": "%s",
            "iQuestionID": "%s", "sAnswerText": "%s", "sAnswerCode": "%s",
            "sLanguage": "%s" } }""" % (self.session_key, sid, qid, answer_text, answer_code, languaje)
        return self.get_json(data)['result']


    def delete_survey(self, sid):
        data = """{ "id": 1,
                    "method": "delete_survey",
                    "params": { "sSessionKey": "%s",
                                "iSurveyID": %s } }""" % (self.session_key,
                                                          sid)
        return self.get_json(data)['result']


    def set_survey_property(self, sid, prop, value):
        data = """{ "id": 1,
                    "method": "set_survey_properties",
                    "params": { "sSessionKey": "%s",
                                "iSurveyID": %s,
                                "aSurveySettings": { "%s": "%s" }
            } }""" % (self.session_key, sid, prop, value)
        return self.get_json(data)['result']


    def get_survey_properties(self, sid, settings=None):

        if settings is None:
            settings = """ [
            "sid","savetimings","allowprev","tokenanswerspersistence",
            "showgroupinfo","showwelcome","owner_id","template","printanswers",
            "assessments","shownoanswer","showprogress","admin","language",
            "ipaddr","usecaptcha","showqnumcode","allowjumps","active",
            "additional_languages","refurl","usetokens","bouncetime",
            "navigationdelay","expires","datestamp","datecreated",
            "bounce_email","bounceprocessing","nokeyboard","startdate",
            "usecookie","publicstatistics","attributedescriptions",
            "bounceaccounttype","alloweditaftercompletion","adminemail",
            "allowregister","publicgraphs","emailresponseto",
            "bounceaccounthost","googleanalyticsstyle","anonymized",
            "allowsave","listpublic","emailnotificationto","bounceaccountpass",
            "googleanalyticsapikey","faxto","autonumber_start","htmlemail",
            "tokenlength","bounceaccountencryption","format","autoredirect",
            "sendconfirmation","showxquestions","bounceaccountuser" ] """

        data = """{ "id": 1,
                    "method": "get_survey_properties",
                    "params": { "sSessionKey": "%s",
                                "iSurveyID": %s,
                                "aSurveySettings": %s
            } }""" % (self.session_key, sid, settings)
        return self.get_json(data)['result']


    def get_summary(self, sid):
        data = """{ "id": 1,
                    "method": "get_summary",
                    "params": { "sSessionKey": "%s",
                                "iSurveyID": %s,
                                "sStatname": "all" } }""" % (self.session_key,
                                                             sid)
        return self.get_json(data)['result']


    def activate_survey(self, sid):
        data = """{ "id": 1,
                    "method": "activate_survey",
                    "params": { "sSessionKey": "%s",
                                "SurveyID": %s } }""" % (self.session_key, sid)
        return self.get_json(data)['result']


    def import_survey(self, datos, titulo, sid, tipo='lss'):
        data = """{ "id": 1,
                    "method": "import_survey",
                    "params": { "sSessionKey": "%s",
                                "sImportData": "%s",
                                "sImportDataType": "%s",
                                "sNewSurveyName": "%s",
                                "DestSurveyID": %d } }""" \
               % (self.session_key, datos, tipo, titulo, sid)
        return self.get_json(data)['result']


    def release_session_key(self):
        data = """ { "method": "release_session_key",
                     "params": { "sSessionKey" : "%s"},
                     "id":1}' }""" % (self.session_key)
        return self.get_json(data)['result']


    def export_responses(self, sid):
        data = """ {    "id" : 1,
                        "method":"export_responses",
                        "params": { "sSessionKey": "%s",
                                    "iSurveyID":  %s,
                                    "sDocumentType": "json",
                                    "sLanguageCode": "ca",
                                    "sCompletionStatus":"all",
                                    "sHeadingType": "code",
                                    "sResponseType": "long"
                        } } """ % (self.session_key, sid)
        return self.get_json(data)['result']


    def export_responses_by_token(self, sid, token, language_code):
        data = """ {    "id" : 1,
                        "method":"export_responses_by_token",
                        "params": { "sSessionKey": "%s",
                                    "iSurveyID":  %s,
                                    "sDocumentType": "json",
                                    "sToken":  "%s",
                                    "$sLanguageCode": "%s",
                                    "sCompletationStatus": "all",
                                    "sHeadingType": "code",
                                    "sResponseType": "long"
                        } } """ % (self.session_key, sid, token, language_code)
        return self.get_json(data)['result']


    def add_response(self, sid, response_data):
        data = """ {          "id": 1,
                              "method":"add_response",
                              "params": { "sSessionKey": "%s",
                                          "iSurveyID": %s,
                                          "aResponseData": %s }
                    } """ % (self.session_key, sid, response_data)
        return self.get_json(data)['result']


    def update_response(self, sid, response_data):
        data = """ {          "id": 1,
                              "method":"update_response",
                              "params": { "sSessionKey": "%s",
                                          "iSurveyID": %s,
                                          "aResponseData": %s }
                    } """ % (self.session_key, sid, response_data)
        return self.get_json(data)['result']


    def impor_from_file(self, sid, file):
        """Esto no funciona!"""

        with open(file) as csv:
            datos = []
            for line in csv.readlines():
                datos.append(line.rstrip().split('\t'))

        columns = datos[1]
        for d in datos[2:]:
            r = dict(zip(columns, d))
            r['id'] = ""
            self.add_response(sid, json.dumps(r))
            sleep(1)


    def list_surveys(self):
        json_list_surveys = self.list_surveys_json()

        surveys = []
        for e in json_list_surveys:
            survey = e['sid'], e['surveyls_title']
            surveys.append(survey)
        return surveys


    def list_surveys_json(self):
        """Devuelve el JSON ENTERO"""
        data = """{ "id": 1,
                    "method": "list_surveys",
                    "params": { "sSessionKey": "%s" } }""" % (self.session_key)

        return self.get_json(data)['result']


    def list_sections_json(self, sid):
        data = """ {          "method":"list_groups",
                              "params": { "sSessionKey": "%s",
                                          "iSurveyID": %s },
                            "id": 1 } """ % (self.session_key, sid)
        return self.get_json(data)['result']


    def list_sections(self, sid):
        sections = []
        try:
            json_list_section = self.list_sections_json(sid)
            # print('Semos dentro: '+ str(json_list_section))
            for sect in json_list_section:
                # print('\nsec: '+str(sect))
                section = sect['sid'], sect['group_name']
                sections.append(section)
        except:
            None
        return sections

    def get_section_id_by_name(self, survey_id, section_name):
        groups = self.list_sections_json(survey_id)
        for group in groups:
            # print("Group: "+str(group))
            if group['group_name'] == section_name:
                # print('ID del grupo'+group['gid'])
                return group['gid']
        return None

    def list_questions_json(self, sid, gid):
        data = """ {          "method":"list_questions",
                              "params": { "sSessionKey": "%s",
                                          "iSurveyID": %s,
                                          "iGroupID": %s },
                            "id": 1 } """ % (self.session_key, sid, gid)
        return self.get_json(data)['result']


    def list_questions(self, sid, gid):
        questions = []
        try:
            json_list_questions = self.list_questions_json(sid, gid)
            print('sid: '+str(sid)+', gid: '+str(gid))
            for q in json_list_questions:
                question = q['id']['qid'], q['question']
                questions.append(question)
        except:
            None
        return questions
    
    def get_survey_info(self):
        surveys = self.list_surveys_json()
        print("Seleccione una encuesta: ")
        opciones = []
        contador = 0
        for survey in surveys:
            # print(str(survey))
            print('Opcion '+str(contador)+': ID -> '+str(survey['sid'])+', Nombre de la encuesta -> '+str(survey['surveyls_title']))
            opciones.append(survey)
            contador += 1
        opcion = input("Cual opcion eliges?: ") # ['sid']
        print(opciones[int(opcion)])
        return opciones[int(opcion)]
    
    def get_survey_id(self):
        survey = self.get_survey_info()
        return survey['sid']
    
    def get_survey_info_by_name(self, name):
        surveys = self.list_surveys_json()
        opciones = []
        contador = 0
        noEncontrada = True
        for survey in surveys:
            if str(survey['surveyls_title']) == str(name):
                noEncontrada = False
                return survey['sid']
            
        if noEncontrada:
            return 'ERROR-NO ENCONTRADA'
        
        
    
    def get_survey_id_by_name(self, name):
        survey_id = self.get_survey_info_by_name(name) 
        return survey_id


    def get_section_info(self, sid):
        sections = self.list_sections_json(sid)
        print("Seleccione una seccion: ")
        opciones = []
        contador = 0
        for section in sections:
            # print(str(section))
            print('Opcion '+str(contador)+': ID -> '+str(section['gid'])+', Nombre de la seccion -> '+str(section['group_name']))
            opciones.append(section)
            contador += 1
        opcion = input("Cual opcion eliges?: ") # ['sid']
        return opciones[int(opcion)]
    
    def get_section_id(self, sid):
        section = self.get_section_info(sid)
        return section['gid']

    def get_question_info(self, sid, gid):
        questions = self.list_questions_json(sid, gid)
        print("Seleccione una pregunta: ")
        opciones = []
        contador = 0
        for question in questions:
            # print(str(question))
            print('Opcion '+str(contador)+': ID -> '+str(question['qid'])+', Nombre de la seccion -> '+str(question['question']))
            opciones.append(question)
            contador += 1
        opcion = input("Cual opcion eliges?: ") # ['sid']
        return opciones[int(opcion)]
    
    def get_question_id(self, sid, gid):
        question = self.get_question_info(sid, gid)
        return question['qid']

    # Añadir participantes a la encuesta
    def add_participant(self, sid, participant, token):
        data = """{ "id": 1,
                    "method": "add_participants",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "aParticipantData": "%s", 
                     "bCreateToken": "%s" } }""" % (self.session_key, sid, participant, token)

        return self.get_json(data)['result']
    
    def delete_participant(self, sid, token):
        data = """{ "id": 1,
                    "method": "delete_participants",
                    "params": { "sSessionKey": "%s",
                                "iSurveyID": %s,
                                "$aTokenIDs": "%s" } }""" % (self.session_key, sid, token)
        return self.get_json(data)['result']
    
    # def get_participant_properties(self, sid, tokenQuery, tokenProperties):
        data = """{ "id": 1,
                    "method": "get_participant_properties",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "aTokenQueryProperties": "%s", 
                     "aTokenProperties": "%s" } }""" % (self.session_key, sid, tokenQuery, tokenProperties)
        
        return self.get_json(data)['result']
    
    # Mandar invitaciones a los participantes
    def invite_participant(self, sid, tokenId):
        # EL id es el del participante de la encuesta
        data = """{ "id": 1,
                    "method": "invite_participants",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "aTokenIds": "%s", 
                     "bEmail": "%s" } }""" % (self.session_key, sid, tokenId, True)
        
        return self.get_json(data)['result']
    
    def list_participants(self, sid, start=0, limit=10, unused=False):
        data = """{ "id": 1,
                    "method": "list_participants",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "iStart": "%s", 
                     "iLimit": "%s",
                     "bUnused": "%s" } }""" % (self.session_key, sid, start, limit, 
                                                   unused)
        
        return self.get_json(data)['result']

    def mail_registered_participants(sid, conditions):
        data = """{ "id": 1,
                    "method": "list_participants",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "overrideAllConditions": "%s" } }""" % (self.session_key, sid, conditions)
        
        return self.get_json(data)['result']
    