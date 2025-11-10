from  ..models import BlogModel
from sqlalchemy.orm import joinedload
from fastapi import HTTPException,status

def get_all(db):
    blogs=db.query(BlogModel).options(joinedload(BlogModel.creator)).all()
    return blogs

def get_by_id(db,id:int):
    blog=db.query(BlogModel).filter(BlogModel.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
        # Response(status_code=status.HTTP_404_NOT_FOUND)
        # return {"detail":f"Blog with the id {id} is not available"}
    return blog