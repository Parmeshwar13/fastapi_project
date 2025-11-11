from fastapi import APIRouter,Depends,HTTPException,status
from  schema import Login
from  models import UserModel
from sqlalchemy.orm import Session
from  database import get_db
from  hashing import Hash
from  token_utils import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES  
from datetime import timedelta


router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login/")
def login(request:Login,db:Session=Depends(get_db)):
          
    user=db.query(UserModel).filter(UserModel.email==request.email).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid UserName")
    print(user.password,request.password,'ppppppppppppppppppppppppppppppppppppppp')
    if  not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"invalid Credential")
    # access_token_expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email})

    
    
    return {"access_token":access_token,"token_type":"bearer"}