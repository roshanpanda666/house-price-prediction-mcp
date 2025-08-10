from pydantic import BaseModel

class Thing(BaseModel):
    house:str
    price1:str
    price2:str
    price3:str
    year1:str
    year2:str
    year3:str
    area:str