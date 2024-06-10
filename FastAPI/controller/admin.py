from fastapi import APIRouter, Cookie, Response
from fastapi.responses import JSONResponse

from utils.utils import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dto.token import Token
from dto.user import User
from dto.encuesta import Encuesta 
from dto.seccion import Seccion
from dto.pregunta import Pregunta
from dto.preguntaMultiple import PreguntaMultiple 
from dto.id import IdModel

from service.encuesta_service import encuestaService 
from service.seccion_service import seccionService
from service.pregunta_service import preguntaService
from service.user_service import UserService
from service.admin_service import AdminService

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()
ususu = UserService()
survey = encuestaService()
section = seccionService()
question = preguntaService()

@router.post("/token", response_model=Token)
async def login_for_access_token(usuario: User):
    user = ususu.get_user(name=usuario.name)
    rol = ususu.obtener_rol(name=usuario.name)
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

    # ACABAR LO DEL ROLE
    return {"access_token": access_token, "token_type": "bearer", "role":rol}


@router.post("/create_user")
async def crear_user(user: User):
    try:
        ususu.crear_usuario(name=user.name, password=user.password)
        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_survey")
async def crear_encuesta(encuesta: Encuesta):
    try:
        return survey.crear_encuesta(nombre_encuesta=encuesta.nombre_encuesta, idioma=encuesta.idioma)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_section")
async def crear_seccion(seccion: Seccion):
    try:
        return section.crear_seccion(nombre_seccion=seccion.nombre_seccion, id_encuesta=seccion.id_encuesta)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.post("/create_text_question")
async def create_text_question(pregunta: Pregunta):
    print("Estamos dentro")
    try:
        return question.crear_pregunta_texto(pregunta.id_encuesta, pregunta.id_seccion, pregunta.nombre_real, pregunta.cuerpo_pregunta)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_multiple_question")
async def create_multiple_question(pregunta: PreguntaMultiple):
    try:
        return question.crear_pregunta_multiple(pregunta.id_encuesta, pregunta.id_seccion, pregunta.nombre_real, pregunta.cuerpo_pregunta, pregunta.respuestas)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.get("/get_survey_id")
async def listar_encuestas():
    try:
        return survey.listar_encuestas()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.post("/get_section_id")
async def listar_secciones(id_survey: IdModel):
    try:
        return section.listar_secciones(id_survey.id)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.get("/list_users_for_admin")
async def list_users_for_admin():
    try:
        return ususu.list_users_for_admin()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.get("/list_users_for_profesional")
async def list_users_for_profesional():
    try:
        return ususu.list_users_for_profesional()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})