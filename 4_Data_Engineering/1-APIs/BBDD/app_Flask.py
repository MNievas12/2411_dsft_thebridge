from flask import Flask, jsonify, request
from datos_dummy import books 

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Mi API de Libros</h1><p>API prototipo para la gestión de libros.</p>"

# 1. Obtener todos los libros (opcionalmente filtrar por título mediante query parameters)
@app.route('/v1/books', methods=['GET'])
def get_books():
    return jsonify(books)

# 2. Obtener un libro por su ID utilizando try/except para capturar StopIteration
@app.route('/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return

# 3. Añadir un nuevo libro (se espera un JSON en el cuerpo de la solicitud)
@app.route('/v1/books', methods=['POST'])
def add_book():
    return

# 4. Actualizar un libro existente utilizando try/except
@app.route('/v1/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    return

# 5. Eliminar un libro 
@app.route('/v1/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return

if __name__ == '__main__':
    app.run()