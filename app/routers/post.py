from .. import schema,models,auth2
from fastapi import FastAPI, status, HTTPException ,Response,Depends,APIRouter
from typing import List,Optional
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
router=APIRouter(
    prefix="/posts",
    tags=["Post"]
)

@router.get("/",response_model=List[schema.PostOut])
def get_posts(db:Session=Depends(get_db),current_user:int =Depends(auth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    # posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts=db.query(models.Post,func.count(models.Voting.post_id).label("Vote")).join(models.Voting,models.Post.id==models.Voting.post_id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_posts(post: schema.PostCreate,db:Session=Depends(get_db),current_user:int =Depends(auth2.get_current_user)):
    new_post=models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}",response_model=schema.Post)
def get_post(id : int,db:Session=Depends(get_db),current_user:int =Depends(auth2.get_current_user)):
    p=db.query(models.Post).filter(models.Post.id==id).first()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    # if p.owner_id!=current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"You are not Authorized")
    return  p

@router.delete("/{id}")
def delete_post(id :int, status_code=status.HTTP_204_NO_CONTENT,db:Session=Depends(get_db),current_user:int =Depends(auth2.get_current_user)):
    p_query=db.query(models.Post).filter(models.Post.id==id)
    p=p_query.first()
    if p == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    if p.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"You are not Authorized")
    
    p_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schema.Post)
def updata_post(id :int , post: schema.PostCreate,db:Session=Depends(get_db),current_user:int =Depends(auth2.get_current_user)):
    p_query=db.query(models.Post).filter(models.Post.id==id)
    p=p_query.first()
    if p== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    if p.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"You are not Authorized")
    p_query.update(post.dict(),synchronize_session=False)
    db.commit()

    return p