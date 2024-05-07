from pydantic import BaseModel
from typing import Union
from datetime import datetime


class SurveryResponse(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None