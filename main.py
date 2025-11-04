from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return{"message":"welcome to FastAPI!"}

@app.get("/about")
def about():
    return{"message":"This is the about page of the FastAPI application."}