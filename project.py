from fastapi import FastAPI ,Depends
from db import get_DB,engine


from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class Bookstore(BaseModel):
    id : int
    title : str
    author : str
    published_by : str

@app.post("/books")
def create_book(data:Bookstore , db:Session=Depends(get_DB)):
    new_book = model.Book(
        id = data.id,
        title = data.title,
        author = data.author,
        published_by = data.published_by
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
