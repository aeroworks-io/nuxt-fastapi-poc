import random
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


class Quote(BaseModel):
    message: str
    author: str


@app.get("/")
def read_root():
    return {"Hello": "World", "Foo": "bar"}


@app.get("/quote", response_model=Quote)
def random_quote():
    quotes = [
        Quote(message="Hello, World", author="Yuichiro Smith"),
        Quote(message="Good Morning!", author="Mickey Mouse"),
        Quote(message="WHAT!?", author="Buzz Lightyear"),
    ]
    return random.choice(quotes)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
