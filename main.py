from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return{"message":"welcome to FastAPI!"}

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