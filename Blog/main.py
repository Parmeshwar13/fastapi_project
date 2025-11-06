from fastapi import FastAPI,Depends,status,Response,HTTPException
from .schema import Blog,ShowBlog
app = FastAPI()
import os
from sqlalchemy.orm import Session
from .database import Base, engine,sessionlocal
from .models import BlogModel
from .schema import Blog
Base.metadata.create_all(bind=engine)

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog/",status_code=status.HTTP_201_CREATED)
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog=BlogModel(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog",status_code=status.HTTP_202_ACCEPTED,response_model=list[ShowBlog])
def all(db:Session=Depends(get_db)):
    blogs=db.query(BlogModel).all()
    return blogs

#get by id
@app.get("/blog/{id}",response_model=ShowBlog)
def show(id:int,db:Session=Depends(get_db)):
    blog=db.query(BlogModel).filter(BlogModel.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
        # Response(status_code=status.HTTP_404_NOT_FOUND)
        # return {"detail":f"Blog with the id {id} is not available"}
    return blog

@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
    new_blog=db.query(BlogModel).filter(BlogModel.id==id)
    if not new_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    db.delete(new_blog.first())
    db.commit() 
    

@app.patch("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:Blog,db:Session=Depends(get_db)):
    blog=db.query(BlogModel).filter(BlogModel.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    blog.title=request.title
    blog.body=request.body
    db.commit()
    db.refresh(blog)
    return blog