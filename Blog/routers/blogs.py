from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import BlogModel
from ..schema import Blog,ShowBlog
from sqlalchemy.orm import joinedload
from ..repository.blogs import get_all,get_by_id
from ..oauth2 import get_current_user

router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:Blog,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    new_blog=BlogModel(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShowBlog])
def all(db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    blogs =get_all(db)  
    return blogs

#get by id
@router.get("//{id}",response_model=ShowBlog)
def show(id:int,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
   blog=get_by_id(db,id)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    new_blog=db.query(BlogModel).filter(BlogModel.id==id)
    if not new_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    db.delete(new_blog.first())
    db.commit() 
    

@router.patch("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:Blog,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    blog=db.query(BlogModel).filter(BlogModel.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    blog.title=request.title
    blog.body=request.body
    db.commit()
    db.refresh(blog)
    return blog