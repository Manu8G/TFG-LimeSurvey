from fastapi import APIRouter
from fastapi.responses import JSONResponse
from service.admin_service import AdminService

from service.seccion_service import seccionService

from dto.seccion import Seccion

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()

@router.post("/create_section")
async def create_seccion(seccion: Seccion):
    try:
        service = seccionService()
        service.crear_seccion(seccion_name=seccion.nombre_seccion, id_encuesta=seccion.id_encuesta)
        return {"message": "seccion created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})