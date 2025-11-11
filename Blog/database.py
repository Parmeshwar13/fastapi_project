from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker     
# DATABASE_URL="sqlite:///.blog.db"
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/blogdb"
engine = create_engine(DATABASE_URL)


# engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False},echo=True )
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()


def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()