from  ..models import BlogModel
from sqlalchemy.orm import joinedload

def get_all(db):
    blogs=db.query(BlogModel).options(joinedload(BlogModel.creator)).all()
    return blogs