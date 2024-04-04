from fastapi import Body,FastAPI
from fastapi.params import Body
from pydantic import BaseModel,EmailStr
from typing import Optional

app=FastAPI()

class UserIn(BaseModel):
    userid:str
    password:str
    email_id:EmailStr
    full_name:str|None=None
    
class UserOut(BaseModel):
    userid:str
    email_id:EmailStr
    full_name:str|None=None
    
class UserInDB(BaseModel):
    userid:str
    hashed_password:str
    email:EmailStr
    full_name:str|None=None
    
def fake_password_hasher(raw_password:str):
    return "supersecret" + raw_password

def fake_save_user(user_in:UserIn):
    hashed_password=fake_password_hasher(user_in.password)
    user_in_db=UserInDB(**user_in.dict(),hashed_password=hashed_password)
    print("User not saved")
    
@app.post("/user/",response_model=UserOut)
async def create_user(user_in:UserIn):
    user_saved=fake_save_user(user_in)
    return user_saved

@app.post("/create_complaints")
def create_complaints():
    return {"message":"complaints created successfully"}

@app.post("/create_suggestions")
def create_suggestions():
    return {"message":"suggestions created successfully"}

@app.post("/create_feedback")
def create_feedback():
    return {"message":"feedback created successfully"}

@app.get("/getuser")
def get_user():
    return {"message":"user"}

