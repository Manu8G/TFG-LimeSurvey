from fastapi import APIRouter, Cookie, Response
from fastapi.responses import JSONResponse
import json

from utils.utils import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dto.token import Token
from dto.user import User
from dto.nuevoUsuario import nuevoUsuario
from dto.encuesta import Encuesta 
from dto.seccion import Seccion
from dto.pregunta import Pregunta
from dto.preguntaMultiple import PreguntaMultiple 
from dto.id import IdModel
from dto.nuevoPaciente import nuevoPaciente
from dto.encuestaDB import encuestaDB
from dto.flujo import Flujo 
from dto.caso import Caso

from service.encuesta_service import encuestaService 
from service.seccion_service import seccionService
from service.pregunta_service import preguntaService
from service.user_service import UserService
from service.admin_service import AdminService
from service.flujo_service import flujoService

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()
ususu = UserService()
survey = encuestaService()
section = seccionService()
question = preguntaService()
flujo = flujoService()

@router.post("/token", response_model=Token)
async def login_for_access_token(usuario: User):
    user = ususu.get_user(name=usuario.name)
    rol = ususu.obtener_rol(name=usuario.name)
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
    return {"access_token": access_token, "token_type": "bearer", "id": "2", "role":rol} # ARREGLAR ID


@router.post("/create_user")
async def crear_user(user: nuevoUsuario):
    try:
        ususu.crear_usuario(nombre_y_apellidos=user.name, password=user.password, role=user.role)
        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_patient")
async def create_patient(paciente: nuevoPaciente):
    try:
        ususu.create_patient(nombre_y_apellidos=paciente.nombre_y_apellidos, password=paciente.password, dni=paciente.dni, estado=paciente.estado, nacionalidad=paciente.nacionalidad, fecha_nacimiento=paciente.fecha_nacimiento, email=paciente.email)
        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_survey")
async def crear_encuesta(encuesta: Encuesta):
    try:
        return survey.crear_encuesta(nombre_encuesta=encuesta.nombre_encuesta, idioma=encuesta.idioma)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})


@router.post("/create_survey_in_db")
async def create_survey_in_db(encuesta: encuestaDB):
    try:
        return survey.create_survey_in_db(nombre=encuesta.nombre, id_usuario=encuesta.id_usuario)
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
        return section.listar_secciones(id_survey.Id)
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
    
@router.get("/list_flujo")
async def list_flujo():
    try:
        return flujo.list_flujo()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})

@router.get("/listar_flujos")
async def listar_flujos():
    try:
        return flujo.listar_flujos()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.post("/get_user_id")
async def get_user_id(usuario: nuevoUsuario):
    try:
        return ususu.get_user_id(usuario.name, usuario.password, usuario.role)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    
    
@router.post("/create_flujo")
async def create_flujo(flu: Flujo):
    try:
        return flujo.create_flujo(flu.id_usuario, flu.tipo_de_flujo, flu.encuestas)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.post("/asignar_flujo")
async def asignar_flujo(caso: Caso):
    try:
        return flujo.asignar_flujo(caso.id_flujo, caso.id_usuario)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
    

@router.post("/get_caso")
async def get_caso(id: IdModel):
    print('recibido 1')
    try:
        return flujo.get_caso(id.Id)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})