from typing import union
from fastapi import fastAPI

app = fastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/livro/livro_id")
def read_livro(livro_id: int, q:union[str, None] = None)
    return {"item_id": item_id, "q": q}
