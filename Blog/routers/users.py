from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import UserModel
from ..schema import User,ShowUser  
from ..hashing import Hash
from sqlalchemy.orm import joinedload

router=APIRouter(
    prefix="/user",
    tags=['Users']
)





@router.get("/getuser",response_model=list[ShowUser])
def getuser(db:Session=Depends(get_db)):
    user=db.query(UserModel).all()
    return user

@router.post("/create_user")
def createuser(request:User,db:Session=Depends(get_db)):
    new_user=UserModel(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user