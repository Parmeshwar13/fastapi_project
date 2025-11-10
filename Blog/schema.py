from pydantic import BaseModel
from typing import Optional

class ShowUser(BaseModel):
    name:str
    email:str
    class Config:
        from_attribute = True

class Blog(BaseModel):
    title: str
    body: str
    user_id:int

    class Config:
        orm_mode = True




class ShowBlog(BaseModel):
    title: str
    body: str
    user_id:int
    creator: ShowUser

    class Config:
       from_attribute=True

class User(BaseModel):
    name:str
    email:str
    password:str
    class Config:
        orm_mode = True 

class Login(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:Optional[str]=None
