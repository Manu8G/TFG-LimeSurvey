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
