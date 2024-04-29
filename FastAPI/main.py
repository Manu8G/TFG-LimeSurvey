from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from LimeAPI import Api

url = "http://localhost/limesurvey/index.php/admin/remotecontrol"
username = "manuel"
password = "1234Lime"

api = Api(url, username, password)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permite a Angular acceder
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

@app.post("/create_survey/")
async def create_survey(data: Dict):
    
    if "survey_name" in data  and "survey_languaje" in data:
        api.add_survey(str(data["survey_name"]), str(data["survey_languaje"]))
        survey_id = api.get_survey_id_by_name(data["survey_name"])
        data.update({"survey_id": survey_id})
        print("Data en python: " + str(data))
        return data
    else:
        print("Algun error")
        data.update({"survey_id": "ERROR al enviar los datos"})
        return data


@app.post("/create_section/")
async def create_section(data: Dict):
    
    if "section_name" in data  and "survey_id" in data:
        api.add_section(str(data["survey_id"]), str(data["section_name"]))
        section = api.list_sections_json(data["survey_id"])
        data.update({"section_confirm": section})
        # print("Data en python: " + str(data))
        return data
    else:
        print("Algun error")
        data.update({"section_confirm": "ERROR al enviar los datos"})
        return data


@app.post("/create_question/")
async def create_question(data: Dict):
    
    if "survey_id" in data and "section_id" in data and "question_title" in data and "question_body" in data and "question_type" in data:
        api.add_question(str(data["survey_id"]), str(data["section_id"]), str(data["question_title"]), str(data["question_body"]), str(data["question_type"]))
        question = api.list_questions_json(data["survey_id"], data["section_id"])
        data.update({"question_confirm": question})
        # print("Data en python: " + str(data))
        return data
    else:
        print("Algun error")
        data.update({"question_confirm": "ERROR al enviar los datos"})
        return data


@app.post("/get_survey_id/")
async def create_survey(data: Dict):
    surveys = api.list_surveys()
    cont = 0
    datos = {}
    for sid, survey_title in surveys:
        # print(f"Survey ID: {sid}, Survey Title: {survey_title}")    
        dato = ('{cont}', '{sid}-{survey_title}')
        datos[f"{sid}"] = survey_title
        cont += 1  
    
    # print(f"DARTA: {datos}")
    return datos