
from fastapi import FastAPI, status, HTTPException ,Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()
class Post(BaseModel):
    title: str
    content:  str
    published: bool = True
    rating: Optional[int] =None

my_posts=[{"title":"fav_food","content":"tikiya chawal","id":4},{"title":"Favourite Color","content":"Black","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
def index(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i      

        
        
@app.get("/")
def root():
    return {"message": "Hello World,, Hello asra you could do it, You will make it till the end just doo not stop"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(new_Post: Post):
    pos=new_Post.dict()
    pos['id']=randrange(0,1000000)
    my_posts.append(pos)
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id : int):
    p=find_post(id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")

    return {"data": p}

@app.delete("/posts/{id}")
def delete_post(id :int, status_code=status.HTTP_204_NO_CONTENT):
    p=index(id)
    if p == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    my_posts.pop(p)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def updata_post(id :int , post: Post):
    p=post.dict()
    p['id']=id
    ind1=index(id)
    if ind1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    my_posts[ind1]=p
    return {"data":p}


