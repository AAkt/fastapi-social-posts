
from fastapi import FastAPI, status, HTTPException ,Response,Depends
from . import models, schema ,utils
from .database import engine ,get_db
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


     
@app.get("/")
def root():
    return {"message": "Hello World,, Hello asra you could do it, You will make it till the end just doo not stop"}

@app.get("/posts",response_model=List[schema.Post])
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_posts(post: schema.PostCreate,db:Session=Depends(get_db)):
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}",response_model=schema.Post)
def get_post(id : int,db:Session=Depends(get_db)):
    p=db.query(models.Post).filter(models.Post.id==id).first()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    return  p

@app.delete("/posts/{id}")
def delete_post(id :int, status_code=status.HTTP_204_NO_CONTENT,db:Session=Depends(get_db)):
    p=db.query(models.Post).filter(models.Post.id==id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    p.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",response_model=schema.Post)
def updata_post(id :int , post: schema.PostCreate,db:Session=Depends(get_db)):
    p=db.query(models.Post).filter(models.Post.id==id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    p.update(post.dict(),synchronize_session=False)
    db.commit()

    return p.first()

@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schema.UserRes)
def create_user(user: schema.UserCreate,db:Session=Depends(get_db)):
    hash_password=utils.get_password_hash(user.password)
    user.password=hash_password
    new_user=models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{id}",response_model=schema.UserRes)
def get_user(id: int,db:Session=Depends(get_db)):
    us=db.query(models.Users).filter(models.Users.id==id).first()
    if us==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user with id:{id} is not found")
    return us







