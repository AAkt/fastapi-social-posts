from .. import schema,models,utils,auth2
from fastapi import FastAPI, status, HTTPException ,Response,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post("/",response_model=schema.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    p=db.query(models.Users).filter(models.Users.email==user_credentials.username).first()
    if p==None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    if not utils.verify(user_credentials.password,p.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    token=auth2.create_access_token(data={"user_id":p.id})
    
    return {"access_token":token,"token_type":"bearer"}
        
