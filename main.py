from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def root():
    return {  "message " : "Hai welcome to home page "}


# for post api or any other api which send data to the backend 
# we use pydantic data model to enforce a particular data 
# struture for that created a model using the BASEMODEL


class Student(BaseModel):
    name : str
    age : int
    number : int

@app.post("/add-student")
def createStudent(data : Student):

    newStudent ={
        "name":data.name,
        "age":data.age,
        "number":data.number
    }

    return {
        "message": "student created ",
        "data" : newStudent
    }
