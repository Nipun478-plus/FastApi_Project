from pydantic import BaseModel


class empolyee(BaseModel):
    name:str
    email:str
    age:int
    country:str
    position:str
    salary:int
