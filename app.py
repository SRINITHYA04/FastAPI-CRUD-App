from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List, Optional #It helps you describe data types more clearly 

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


class Book_Strict(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class Book_Flexible(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None

    # 1. Optional[str] -> Value can be str or None 
    # 2. = None -> Field is not required in request and  
    #           -> If not provided → it defaults to None


# 1. get the list of all books
@app.get("/books", response_model = List[Book_Strict]) #decorator
def get_all_books()-> List[Book_Strict]:
    return books

#2. Add a new to the In memory db
@app.post("/books", status_code = status.HTTP_201_CREATED)
async def create_a_book(Book_data : Book_Strict): # Book_data is of obj type
    new_book = Book_data.model_dump() # dump_modle() converts obj to dict. so new_bbok is of dict type
    books.append(new_book) # append makes no error
    return new_book

# the newly add book can de veiwed but again giving get/books.

# 3. Retrive a Book from the in-memory DB
@app.get('/books/{book_id}')
async def get_book(book_id: int)-> dict :
    for book in books:
        if book["id"] == book_id:
             return book
    raise HTTPException(status_code =404, detail="Book not found")


#  4. Update a Book in the in-memory DB
@app.patch('/books/{book_id}')
async def Update_book(book_id: int, book_update_data: Book_Flexible):
    for book in books:
        if book["id"] == book_id:
            book.update(book_update_data.model_dump(exclude_unset=True))
            return book
    raise HTTPException(status_code =404, detail="Book not found") 


#5. 



