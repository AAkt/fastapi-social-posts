from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content:  str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserRes(BaseModel):
    email:EmailStr
    id: int
    created_at:datetime
    class Config:
        orm_model=True


        
class Post(PostBase):
    id: int
    created_at:datetime
    owner_id:int
    owner : UserRes

    class Config:
        orm_model=True

class PostOut(BaseModel):
    Post: Post
    Vote:int
    class Config:
        orm_model=True


class UserCreate(BaseModel):
    email:EmailStr
    password:str



class Login(BaseModel):
    email:EmailStr
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str]=None

class Vote(BaseModel):
    post_id:int
    dir: bool

