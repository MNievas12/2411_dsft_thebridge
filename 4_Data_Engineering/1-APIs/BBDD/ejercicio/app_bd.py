from fastapi import FastAPI, requests, HTTPException
from pydantic import BaseModel
import sqlite3
import uvicorn

app = FastAPI()

class Book(BaseModel):
    published: int
    author: str
    title: str
    first_sentence: str


conn = sqlite3.connect('books.db')
cursor = conn.cursor()

@app.get("/")
async def hello():
    return "Hello world"

# 1.Ruta para obtener todos los libros


# 2.Ruta para obtener los libros de un autor


# 3.Ruta para añadir un libro

