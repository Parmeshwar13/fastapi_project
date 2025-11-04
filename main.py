from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
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

class Blog(BaseModel):
    title:str
    description:str
    publshed:Optional[bool]=False
@app.post("/blog/")
def create_blog(request:Blog):
    return{"message":f"Blog created! {request.title}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)