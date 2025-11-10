from fastapi import FastAPI
app = FastAPI()
from .database import Base, engine
from sqlalchemy import inspect
from .routers import blogs, users


# Base.metadata.drop_all(bind=engine)


Base.metadata.create_all(bind=engine)

app.include_router(blogs.router)
app.include_router(users.router)

@app.on_event("startup")
def show_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("✅ Tables in the database:", tables)

