import logging
from controller.admin import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.config import Config
config=Config()
logging.info(config.get("MSQL"))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permite a Angular acceder
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(router)

