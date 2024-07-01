from .. import schema,models,utils
from fastapi import FastAPI, status, HTTPException ,Response,Depends,APIRouter
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/users",
    tags=["User"]
)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserRes)
def create_user(user: schema.UserCreate,db:Session=Depends(get_db)):
    hash_password=utils.get_password_hash(user.password)
    user.password=hash_password
    new_user=models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schema.UserRes)
def get_user(id: int,db:Session=Depends(get_db)):
    us=db.query(models.Users).filter(models.Users.id==id).first()
    if us==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user with id:{id} is not found")
    return us
