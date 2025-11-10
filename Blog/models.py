from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class BlogModel(Base):
    __tablename__="blogs"
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String,max_length=255)
    body=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))
    creator=relationship("UserModel",back_populates="blogs")

    def __repr__(self):
        return f"<Blog(title={self.title}, body={self.body})>"
    

class UserModel(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,max_length=100)
    email=Column(String,max_length=100,unique=True,index=True)
    password=Column(String,max_length=100)
    blogs=relationship("BlogModel",back_populates="creator")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"  