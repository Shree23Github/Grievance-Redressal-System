from fastapi import Body,FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class User():
    Name:str
    Userid:str
    

@app.post("/create_complaints")
def create_complaints():
    return {"message":"complaints created successfully"}

    