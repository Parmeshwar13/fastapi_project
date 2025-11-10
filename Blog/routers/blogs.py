from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import BlogModel
from ..schema import Blog,ShowBlog
from sqlalchemy.orm import joinedload
from ..repository.blogs import get_all

router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post("/blog/",status_code=status.HTTP_201_CREATED)
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog=BlogModel(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog", status_code=status.HTTP_200_OK, response_model=list[ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs =get_all(db)  
    return blogs

#get by id
@router.get("/blog/{id}",response_model=ShowBlog)
def show(id:int,db:Session=Depends(get_db)):
    blog=db.query(BlogModel).filter(BlogModel.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
        # Response(status_code=status.HTTP_404_NOT_FOUND)
        # return {"detail":f"Blog with the id {id} is not available"}
    return blog

@router.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
    new_blog=db.query(BlogModel).filter(BlogModel.id==id)
    if not new_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    db.delete(new_blog.first())
    db.commit() 
    

@router.patch("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
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