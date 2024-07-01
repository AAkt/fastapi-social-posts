from .. import schema,models,auth2
from fastapi import FastAPI, status, HTTPException ,Response,Depends,APIRouter
from typing import List,Optional
from ..database import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/vote",tags=["Voting"])

@router.post("/",status_code=status.HTTP_201_CREATED)
def Vote(vote:schema.Vote,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with {vote.post_id} does not exist")
    vote_query=db.query(models.Voting).filter(models.Voting.post_id==vote.post_id,models.Voting.user_id==current_user.id)
    found_vote=vote_query.first()
    if vote.dir==1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"The post id with {vote.post_id} is already voted by the user {current_user.email}")
        new_vote=models.Voting(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"succesfully added the vote"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message":"succesfully removed the vote"}