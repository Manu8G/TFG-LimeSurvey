import logging
from controller.admin import router
from fastapi import FastAPI

from utils.config import Config
config=Config()
logging.info(config.get("MSQL"))
app = FastAPI()

app.include_router(router)