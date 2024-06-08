from fastapi import APIRouter, Cookie, Response
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
ususu = UserService()
 
@router.post("/token", response_model=Token)
async def login_for_access_token(usuario: User):
    user = ususu.get_user(name=usuario.name) # hermano arreglame porfa
    # print("User.password del malo: "+ usuario.password)
    # print("User.password del malo2: "+ user.password)
    if not user or not verify_password(usuario.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect name or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.nombre_y_apellidos}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

# @router.post("/token")
# async def login_for_access_token(response: Response, usuario: User):
#     user = ususu.get_user(name=usuario.name) # hermano arreglame porfa
#     # print("User.password del malo: "+ usuario.password)
#     # print("User.password del malo2: "+ user.password)
#     if not user or not verify_password(usuario.password, user.password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect name or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.nombre_y_apellidos}, expires_delta=access_token_expires
#     )
#     response.set_cookie(key="access_token", value=access_token, httponly=True)
#     return {"Not error": "Login correcto"}

# @router.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = ususu.get_user(name=form_data.username) # hermano arreglame porfa
#     print(str(user))
#     # La siguiente funcion le pasa primero la contraseña introducida y despues 
#     #la de bd para comprobar si es correcto
#     print("User.password del malo: "+ user.password)
#     if not user or not verify_password(form_data.password, user.password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect name or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.nombre_y_apellidos}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

@router.post("/create_user")
async def crear_user(user: User):
    try:
        service = UserService()

        service.crear_usuario(name=user.name, password=user.password)

        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_survey")
async def crear_encuesta(encuesta: Encuesta):
    try:
        service = encuestaService()
        service.crear_encuesta(nombre_encuesta=encuesta.nombre_encuesta, idioma=encuesta.idioma)
        return {"message": "seccion created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_section")
async def crear_seccion(seccion: Seccion):
    try:
        service = seccionService()
        service.crear_seccion(nombre_seccion=seccion.nombre_seccion, id_encuesta=seccion.id_encuesta)
        return {"message": "seccion created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    
@router.get("/get_survey_id")
async def listar_encuestas():
    try:
        service = encuestaService()
        return service.listar_encuestas()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})