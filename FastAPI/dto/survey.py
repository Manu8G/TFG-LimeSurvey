from pydantic import BaseModel


class SurveryResponse(BaseModel):
    id: str
    title: str
    


    # SE PPUEDE PONER EN EL MISMO NIVEL