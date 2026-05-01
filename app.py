from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List #It helps you describe data types more clearly 

app = FastAPI(title="Crud FastApi_Crud_Application")

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "publisher": "Avery",
        "published_date": "2018-10-16",
        "page_count": 320,
        "language": "English"
    },
    {
        "id": 2,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperOne",
        "published_date": "1988-01-01",
        "page_count": 208,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "publisher": "Plata Publishing",
        "published_date": "1997-04-01",
        "page_count": 336,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Ikigai",
        "author": "Héctor García",
        "publisher": "Penguin",
        "published_date": "2016-01-01",
        "page_count": 208,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Deep Work",
        "author": "Cal Newport",
        "publisher": "Grand Central Publishing",
        "published_date": "2016-01-05",
        "page_count": 304,
        "language": "English"
    },
    {
        "id": 6,
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "publisher": "New World Library",
        "published_date": "1997-01-01",
        "page_count": 236,
        "language": "English"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


# 1. get the list of all books
@app.get("/books", response_model = List[Book]) #decorator
def get_all_books()-> List[Book]:
    return books

#2. Add a new to the In memory db
@app.post("/books", status_code = status.HTTP_201_CREATED)
async def create_a_book(Book_data : Book): # Book_data is of obj type
    new_book = Book_data.model_dump() # dump_modle() converts obj to dict. so new_bbok is of dict type
    books.append(new_book) # append makes no error
    return new_book

# the newly add book can de veiwed but again giving get/books.

# 3. Retrive a Book from the in memory DB
@app.get('/books/{book_id}')
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
             return book
    raise HTTPException(status_code =404, detail="Book not found")
    


