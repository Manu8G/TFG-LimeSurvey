from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.utils import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dto.token import Token
from dto.user import User
from dto.seccion import Seccion
from dto.encuesta import Encuesta 

from service.seccion_service import seccionService
from service.encuesta_service import encuestaService 
from service.user_service import UserService
from service.admin_service import AdminService

from utils.Lime_API_run import api

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()

@router.post("/create_survey")
async def crear_encuesta(encuesta: Encuesta):
    try:
        service = encuestaService()
        service.crear_encuesta(nombre_encuesta=encuesta.nombre_encuesta, idioma=encuesta.idioma)
        return {"message": "seccion created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
