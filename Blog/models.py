from sqlalchemy import Column, Integer, String,ForeignKey,DateTime
from sqlalchemy.orm import relationship,declarative_mixin
from database import Base
from datetime import datetime



@declarative_mixin
class BaseMixin:
    """Common columns for all tables."""

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(String, nullable=True)
    updated_by = Column(String, nullable=True)
class BlogModel(Base):
    __tablename__="blogs"
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String(255))
    body=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))
    creator=relationship("UserModel",back_populates="blogs")

    def __repr__(self):
        return f"<Blog(title={self.title}, body={self.body})>"
    

class RoleModel(Base):
    __tablename__="roles"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),unique=True)

    def __repr__(self):
        return f"<Role(name={self.name})>"

class UserModel(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    role=Column(Integer,ForeignKey("roles.id"))
    name=Column(String(100))
    email=Column(String(100),unique=True,index=True)
    password=Column(String(100))
    blogs=relationship("BlogModel",back_populates="creator")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"  