from fastapi import APIRouter
from fastapi.responses import JSONResponse
from service.admin_service import AdminService

from service.user_service import UserService
from utils.utils import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dto.token import Token
from dto.user import User
from utils.Lime_API_run import api
from service.seccion_service import seccionService

from dto.seccion import Seccion

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()
 
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserService.get_user(name=form_data.name)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect name or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/create_user")
async def create_user(user: User):
    try:
        service = UserService()

        service.create_user(name=user.name, password=user.password)

        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_section")
async def create_seccion(seccion: Seccion):
    try:
        service = seccionService()
        service.create_user(seccion_name=seccion.nombre_seccion, id_encuesta=seccion.id_encuesta)
        return {"message": "seccion created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    
@router.get("/get_survey_id")
async def get_survey_id():
    try:
        return api.list_surveys()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})