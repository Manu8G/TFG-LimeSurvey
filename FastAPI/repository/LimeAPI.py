import json
import sys
import random
import base64
import xml.etree.ElementTree as ET
import os
import pandas as pd
import requests

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from csv import DictReader
from time import sleep
from io import StringIO

class Api:

    def get_json(self, data):
        data_bytes = data.encode('utf-8')
        req = urllib2.Request(url=self.url, data=data_bytes)
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
                return numero_aleatorio
        return None


    def add_survey(self, survey_title, survey_languaje, format="G"):
        numero_aleatorio = random.randint(100000, 999999)
        self.check_if_exists_survey(numero_aleatorio)

        data = {
            "id": 1,
            "method": "add_survey",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": numero_aleatorio,
            "sSurveyTitle":survey_title,
            "sSurveyLanguage": survey_languaje,
            "sformat": format
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    def delete_survey(self, sid):
        data = {
            "id": 1,
            "method": "delete_survey",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']
    

    def add_section(self, sid, section_title):
        data = {
            "id": 1,
            "method": "add_group",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "sGroupTitle":section_title
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    def add_text_question(self, sid, gid, question_name, question_body):
        current_directory = os.path.dirname(__file__)
        questions_ids = self.list_all_questions_ids()
        new_id = 1  
        while new_id in questions_ids:
            new_id += 1

        question_path = os.path.join(current_directory, '../utils/question_xmls/preguntaTexto.xml')
        tree = ET.parse(question_path)
        root = tree.getroot()

        for qid_element in root.findall(".//qid"):
            if qid_element.text == "PQID":
                qid_element.text = str(new_id)
            
        for qid_element in root.findall(".//sid"):
            if qid_element.text == "SID":
                qid_element.text = str(sid)

        for qid_element in root.findall(".//gid"):
            if qid_element.text == "GID":
                qid_element.text = str(gid)

        for qid_element in root.findall(".//type"):
            if qid_element.text == "TYPE":
                qid_element.text = 'S'

        for qid_element in root.findall(".//title"):
            if qid_element.text == "QCODE":
                qid_element.text = str(question_name)

        for qid_element in root.findall(".//question"):
            if qid_element.text == "QTEXT":
                qid_element.text = str(question_body)

        for qid_element in root.findall(".//question_order"):
            if qid_element.text == "ORDER":
                qid_element.text = str(new_id)

        question_result = os.path.join(current_directory, '../utils/question_xmls/result.xml')
        tree.write(question_result, encoding="UTF-8", xml_declaration=True)
        xml_str = ET.tostring(root, encoding='utf-8', method='xml')
        base64var = base64.b64encode(xml_str).decode('utf-8')
        import_data_type = "lsq"
        v1 = 'N'
        v2 = None
        
        data = {
            "id": 1,
            "method": "import_question",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "iGroupID": gid,
            "sImportData": base64var,
            "sImportDataType": import_data_type,
            "sMandatory": v1,
            "sNewQuestionTitle": v2,
            "sNewqQuestion": v2,
            "sNewQuestionHelp": v2
            }
        }
        data = json.dumps(data)

        return self.get_json(data)['result']


    def add_multiple_question(self, sid, gid, question_name, question_body, respuestas):
        current_directory = os.path.dirname(__file__)
        
        questions_ids = self.list_all_questions_ids()
        new_id = 1  
        while new_id in questions_ids:
            new_id += 1
            
        question_path = os.path.join(current_directory, '../utils/question_xmls/pregunta.xml')
        tree = ET.parse(question_path)
        root = tree.getroot()

        for qid_element in root.findall(".//qid"):
            if qid_element.text == "PQID":
                qid_element.text = str(new_id)
            
        for qid_element in root.findall(".//sid"):
            if qid_element.text == "SID":
                qid_element.text = str(sid)

        for qid_element in root.findall(".//gid"):
            if qid_element.text == "GID":
                qid_element.text = str(gid)

        for qid_element in root.findall(".//type"):
            if qid_element.text == "TYPE":
                qid_element.text = 'M'

        for qid_element in root.findall(".//title"):
            if qid_element.text == "QCODE":
                qid_element.text = str(question_name)

        for qid_element in root.findall(".//question"):
            if qid_element.text == "QTEXT":
                qid_element.text = str(question_body)

        for qid_element in root.findall(".//question_order"):
            if qid_element.text == "ORDER":
                qid_element.text = str(new_id)


        questionRows = root.find('.//subquestions/rows')
        archivo_salida = os.path.join(current_directory, '../utils/question_xmls/result.xml')

        if questionRows is not None:
            questionRows.clear()

        id_subquestion = int(new_id)
        for i in respuestas:
            subquestion_path = os.path.join(current_directory, '../utils/question_xmls/subpregunta.xml')
            subtree = ET.parse(subquestion_path)
            subroot = subtree.getroot()

            for qid_element in subroot.findall(".//qid"):
                if qid_element.text == "SQID":
                    id_subquestion += 1
                    qid_element.text = str(id_subquestion)

            for qid_element in subroot.findall(".//parent_qid"):
                if qid_element.text == "PQID":
                    qid_element.text = str(new_id)
                
            for qid_element in subroot.findall(".//sid"):
                if qid_element.text == "SID":
                    qid_element.text = str(sid)

            for qid_element in subroot.findall(".//gid"):
                if qid_element.text == "GID":
                    qid_element.text = str(gid)

            for qid_element in subroot.findall(".//type"):
                if qid_element.text == "TYPE":
                    qid_element.text = 'T'

            for qid_element in subroot.findall(".//title"):
                if qid_element.text == "SQCODE":
                    subquestionCode = str(i) + str(question_name)
                    qid_element.text = str(subquestionCode)

            for qid_element in subroot.findall(".//question"):
                if qid_element.text == "SQTEXT":
                    qid_element.text = str(i)

            for qid_element in subroot.findall(".//question_order"):
                if qid_element.text == "SQORDER":
                    qid_element.text = str(new_id)
            
            questionRows.append(subroot)
        

        tree.write(archivo_salida, encoding="UTF-8", xml_declaration=True)        
        xml_str = ET.tostring(root, encoding='utf-8', method='xml')
        base64var = base64.b64encode(xml_str).decode('utf-8')
        import_data_type = "lsq"
        v1 = 'N'
        v2 = None
        
        data = {
            "id": 1,
            "method": "import_question",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "iGroupID": gid,
            "sImportData": base64var,
            "sImportDataType": import_data_type,
            "sMandatory": v1,
            "sNewQuestionTitle": v2,
            "sNewqQuestion": v2,
            "sNewQuestionHelp": v2
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']


    def exits_question_list(self, q):
        if isinstance(q, list):
            return True

        elif isinstance(q, dict) and q.get('status') == 'No questions found':
            return False


    def list_all_questions_ids(self):
        questions = []
        sections_ids = []
        surveys = self.list_surveys()
        surveys_ids = [int(tup[0]) for tup in surveys]
        for survey_id in surveys_ids:
            sections = self.list_sections(survey_id)
            sections_ids = [int(tup[0]) for tup in sections]
            for section_id in sections_ids:
                json_list_questions = self.list_questions_json(survey_id, section_id)
                exist = self.exits_question_list(json_list_questions)
                if exist:
                    question_group = self.list_questions(survey_id, section_id)
                    for single_question in question_group:
                        questions.append(single_question[0])
                        
        return questions
    


    def add_answer(self, sid, qid, answer_text, answer_code, languaje):
        data = """{ "id": 1,
            "method": "add_question",
            "params": { "sSessionKey": "%s", "iSurveyID": "%s",
            "iQuestionID": "%s", "sAnswerText": "%s", "sAnswerCode": "%s",
            "sLanguage": "%s" } }""" % (self.session_key, sid, qid, answer_text, answer_code, languaje)
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
        data = {
            "id": 1,
            "method": "list_surveys",
            "params": {
            "sSessionKey": self.session_key
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']


    def list_sections(self, sid):
        sections = []
        try:
            json_list_section = self.list_sections_json(sid)
            for sect in json_list_section:
                section = sect['gid'], sect['group_name']
                sections.append(section)
        except:
            None
        return sections


    def list_sections_json(self, sid):
        data = {
            "id": 1,
            "method": "list_groups",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']


    def get_section_id_by_name(self, survey_id, section_name):
        groups = self.list_sections_json(survey_id)
        for group in groups:
            if group['group_name'] == section_name:
                return group['gid']
        return None


    def list_questions(self, sid, gid):
        questions = []
        try:
            json_list_questions = self.list_questions_json(sid, gid)
            for q in json_list_questions:
                question = q['id']['qid'], q['question']
                questions.append(question)
        except:
            None
        return questions


    def list_questions_json(self, sid, gid):
        data = {
            "id": 1,
            "method": "list_questions",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "iGroupID": gid
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']

    
    def get_survey_info(self):
        surveys = self.list_surveys_json()
        opciones = []
        contador = 0
        for survey in surveys:
            opciones.append(survey)
            contador += 1
        opcion = input("Cual opcion eliges?: ") 
        return opciones[int(opcion)]
    
    def get_survey_id(self):
        survey = self.get_survey_info()
        return survey['sid']
    
    def get_survey_info_by_name(self, name):
        surveys = self.list_surveys_json()
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
        opciones = []
        contador = 0
        for section in sections:
            opciones.append(section)
            contador += 1
        opcion = input("Cual opcion eliges?: ") 
        return opciones[int(opcion)]
    
    def get_section_id(self, sid):
        section = self.get_section_info(sid)
        return section['gid']

    def get_question_info(self, sid, gid):
        questions = self.list_questions_json(sid, gid)
        opciones = []
        contador = 0
        for question in questions:
            opciones.append(question)
            contador += 1
        opcion = input("Cual opcion eliges?: ") 
        return opciones[int(opcion)]
    
    
    def get_question_id(self, sid, gid):
        question = self.get_question_info(sid, gid)
        return question['qid']


    def activate_survey(self, sid):
        data = {
            "id": 1,
            "method": "activate_survey",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']


    def add_participant_table(self, sid):
        data = {
            "id": 1,
            "method": "activate_tokens",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    def add_participant(self, sid, participant):
        data = {
            "id": 1,
            "method": "add_participants",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "aParticipantData":participant
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    def delete_participant(self, sid, token):
        data = {
            "id": 1,
            "method": "delete_participants",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "aTokenIDs":token
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    # def get_participant_properties(self, sid, tokenQuery, tokenProperties):
        data = """{ "id": 1,
                    "method": "get_participant_properties",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "aTokenQueryProperties": "%s", 
                     "aTokenProperties": "%s" } }""" % (self.session_key, sid, tokenQuery, tokenProperties)
        
        return self.get_json(data)['result']
    

    def invite_participant(self, sid, tokenId):
        data = {
            "id": 1,
            "method": "invite_participants",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "aTokenIds":tokenId,
            "bEmail": True
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    def list_participants(self, sid, start=0, limit=10, unused=False):
        data = {
            "id": 1,
            "method": "list_participants",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "iStart": start,
            "iLimit": limit,
            "bUnused": unused
            }
        }

        data = json.dumps(data)
        return self.get_json(data)['result']


    def mail_registered_participants(self, sid, conditions):
        data = """{ "id": 1,
                    "method": "list_participants",
                    "params": { "sSessionKey": "%s",
                     "iSurveyID": "%s", 
                     "overrideAllConditions": "%s" } }""" % (self.session_key, sid, conditions)
        
        return self.get_json(data)['result']
    
    
    def get_responses(self, sid):
        data = {
            "id": 1,
            "method": "export_responses",
            "params": {
            "sSessionKey": self.session_key,
            "iSurveyID": sid,
            "sDocumentType":"json",
            "sLanguageCode":"es",
            "sCompletionStatus":"complete",
            "sHeadingType":"code",
            "sResponseType":"short",
            "iFromResponseID":None,
            "iToResponseID":None,
            "aFields":None
            }
        }

        data = json.dumps(data)
        datada = self.get_json(data)['result']
        
        decoded_data = base64.b64decode(datada).decode('utf-8')
        # datad = pd.read_json(StringIO(decoded_data))
         
        return decoded_data
        

    def release_session_key(self):
        data = {
            "id": 1,
            "method": "release_session_key",
            "params": {
            "sSessionKey": self.session_key
            }
        }

        data = json.dumps(data)

        return self.get_json(data)['result']
    

    