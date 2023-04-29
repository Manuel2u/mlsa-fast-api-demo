from fastapi import FastAPI, Response, HTTPException
from models import Books
from typing import List, Union


app = FastAPI()

books = [
    {
        "id": 1,
        "author": "Manuel",
        "title": "Arseine Lupin",
        "pages": 435,
    },
    {
        "id": 2,
        "author": "Kofi",
        "title": "Babone",
        "pages": 445,
    },
    {
        "id": 3,
        "author": "Dr Martin",
        "title": "How to Dream big",
        "pages": 485,
    },
    {
        "id": 4,
        "author": "Manuel Dev",
        "title": "How to Reap where you did not sow",
        "pages": 495,
    },
    {
        "id": 5,
        "author": "Aki Ola",
        "title": "Hardworking Pays",
        "pages": 335,
    },
]

# get route to get all books


@app.get("/books", response_model=List[Books])
async def getBooks():
    return books


@app.get("/book/{book_id}", response_model=Union[Books, str])
async def getSingleBook(book_id: int, response: Response):
    book = None
    for item in books:
        if item["id"] == book_id:
            book = item
            break
    if book == None:
        response.status_code = 404
        return "Book not found"
    return book


@app.post('/create-books', response_model=Books, status_code=201)
async def createBook(book: Books):
    book_dict = book.dict()
    if (len(books) > 0):
        max_id = max(book["id"] for book in books)
    else:
        max_id = 0

    new_id = max_id + 1
    book_dict["id"] = new_id
    books.append(book_dict)
    return book_dict


@app.put("/update-book/{book_id}", response_model=Books, status_code=200)
async def update_book(book_id: int, book: Books):
    if book_id >= len(books):
        print(len(books))
        raise HTTPException(status_code=404, detail="Book not found")
    book_dict = book.dict()
    books[book_id] = book_dict
    return book_dict


@app.delete("/delete-book/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(i)
            return {"message:" f"Book with Id {book_id} deleted"}
    raise HTTPException(
        status_code=404, detail=f"Book with ID {book_id} not found")
