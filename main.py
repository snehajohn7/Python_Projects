from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Request/Response Models
class Book(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class BookResponse(BaseModel):
    message: str
    book: Book

class ItemResponse(BaseModel):
    item_id: int
    q: Optional[str] = None

class ItemUpdateResponse(BaseModel):
    item_name: str
    item_id: int

class RootResponse(BaseModel):
    Hello: str

# Endpoints with response models properly instantiated
@app.get("/", response_model=RootResponse)
def read_root():
    return RootResponse(Hello="World")

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, q: Optional[str] = None):
    return ItemResponse(item_id=item_id, q=q)

@app.put("/items/{item_id}", response_model=ItemUpdateResponse)
def update_item(item_id: int, item: Book):
    return ItemUpdateResponse(item_name=item.name, item_id=item_id)

@app.post("/books", response_model=BookResponse)
def create_book(book: Book):
    return BookResponse(
        message="Book created successfully",
        book=book
    )