
from fastapi import FastAPI, status, HTTPException ,Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()
class Post(BaseModel):
    title: str
    content:  str
    published: bool = True
while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='root',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("DAtabase Connection was successfull")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)
     
@app.get("/")
def root():
    return {"message": "Hello World,, Hello asra you could do it, You will make it till the end just doo not stop"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    return {"data":posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts ("Title","Content") VALUES (%s,%s) RETURNING *""",(post.title,post.content))
    post=cursor.fetchone()
    conn.commit()

    return {"data": post}

@app.get("/posts/{id}")
def get_post(id : int):
    cursor.execute("""SELECT * FROM posts WHERE "ID" = %s""",(str(id)),)
    p=cursor.fetchone()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    return {"data": p}

@app.delete("/posts/{id}")
def delete_post(id :int, status_code=status.HTTP_204_NO_CONTENT):
    cursor.execute("""DELETE FROM posts WHERE "ID" = %s RETURNING * """,(str(id)),)
    p=cursor.fetchone()
    conn.commit()
    if p == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def updata_post(id :int , post: Post):
    cursor.execute("""UPDATE posts SET "Title"= %s , "Content" =%s WHERE "ID" = %s RETURNING * """,(post.title,post.content,str(id)))
    p=cursor.fetchone()
    conn.commit()

    if p == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")

    return {"data":p}


