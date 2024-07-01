from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__= "posts2"

    id=Column(Integer , primary_key=True, nullable=False)
    title=Column(String, nullable=False )
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='TRUE',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users1.id",ondelete="CASCADE"),nullable=False)

    owner=relationship("Users")

class Users(Base):
    __tablename__="users1"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_number=Column(String)

class Voting(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts2.id",ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users1.id",ondelete="CASCADE"),primary_key=True)
    