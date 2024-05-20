from fastapi import APIRouter
from security import User
from fastapi.responses import JSONResponse
from service.admin_service import AdminService
from dto.paciente.survey import SurveryResponse

from utils.db_conncetions import create_db_connection

router = APIRouter(prefix="/admin", tags="Admin")
service = AdminService()

@router.get("/create-survery", response=SurveryResponse)
def create_survary(data: Survery, user:User):
    if "admin.survery" in user.permission:
        try:
            ...
            #Llamada al servicio
            return service.create_survery(data=data)
        except Exception as e:
            JSONResponse(status=500, content={"status":500, "data": f"Something goes wrong: {str(e)}"})

    else:
        JSONResponse(status=403, content={"status":403, "data": "Missing permission to perfor that action"})

@router.post("/create-post")
def create_post():
    ...
