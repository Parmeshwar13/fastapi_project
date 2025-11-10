from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import UserModel
from ..schema import User,ShowUser  
from ..hashing import Hash
from sqlalchemy.orm import joinedload
from ..oauth2 import get_current_user

router=APIRouter(
    prefix="/user",
    tags=['Users']
)





@router.get("/getuser",response_model=list[ShowUser])
def getuser(db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    user=db.query(UserModel).all()
    return user

@router.post("/create_user")
def createuser(request:User,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    new_user=UserModel(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/me")
def read_profile(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(UserModel).filter(UserModel.email == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": user.email, "name": user.name}
