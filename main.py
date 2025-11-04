from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def index(limit=10 ,published:bool=True ,sorted:Optional[bool]=None):
    if published:
        return{"message":f"{limit} published welcome to FastAPI!"}

    return{"message":f"{limit} welcome to FastAPI!"}

@app.get("/about")
def about():
    return{"message":"This is the about page of the FastAPI application."}

@app.get("/blog/unpublished")
def unpublished():
    return{"message":"All unpublished blogs."}

@app.get("/blog/{blog_id}")
def blog(blog_id: int):
    return{"blog":blog_id}



@app.get("/blog/{id}/comments/{comment_id}")
def comments(id:int, comment_id:int):
    return{"comments":comment_id}

@app.get("/blog/{id}/comments/")
def comments(id:int):
    return{"comments":{1,2,3,4,5}}

