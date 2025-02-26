from fastapi import FastAPI, requests, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
import uvicorn

app = FastAPI()

class Book(BaseModel):
    # id: None
    published: int
    author: str
    title: str
    first_sentence: str


conn = sqlite3.connect('books.db')
cursor = conn.cursor()

def query_db(results, cursor):
    
    # Obtener los nombres de las columnas
    column_names = [column[0] for column in cursor.description]
    
    # Convertir cada tupla en un diccionario
    books = [dict(zip(column_names, book)) for book in results]
    return books

@app.get("/")
async def hello():
    return "Hello world"

# 1.Ruta para obtener todos los libros
@app.get("/v1/books", response_model=List[Book])
async def get_books():
    query = "SELECT published,author,title,first_sentence FROM books"
    results = cursor.execute(query).fetchall()
    return query_db(results, cursor)


# 2.Ruta para obtener los libros de un autor
@app.get("/v1/author/{author}/books", response_model=List[Book])
async def get_author_books(author:str):
    query = """
    SELECT published,
           author,
           title,
           first_sentence 
    FROM books
    WHERE author LIKE ?
    """
    results =  cursor.execute(query, (f"%{author}%",)).fetchall()
    return query_db(results, cursor)

# 3.Ruta para añadir un libro
@app.post("/v1/books")
async def create_book(book: Book):
    try:
        query = """
        INSERT INTO books (published, author, title, first_sentence)
        VALUES (?,?,?,?)
        """
        cursor.execute(query, (book.published, book.author, book.title, book.first_sentence))
        conn.commit()
        return {"message": f"Book {book.title} added sucessfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error inserting the book")



uvicorn.run(app)