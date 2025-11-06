from sqlalchemy import Column, Integer, String
from .database import Base

class BlogModel(Base):
    __tablename__="blogs"
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String,max_length=255)
    body=Column(String)

    def __repr__(self):
        return f"<Blog(title={self.title}, body={self.body})>"