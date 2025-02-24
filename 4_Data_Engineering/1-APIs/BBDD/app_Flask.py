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
    title = request.args.get('title')
    if title:
        filtered_books = [book for book in books if book['title'].lower() == title.lower()]
        return jsonify(filtered_books)
    else:
        return jsonify(books)

# 2. Obtener un libro por su ID utilizando try/except
@app.route('/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        filtered_books = [book for book in books if book['id'] == book_id]
        return jsonify(filtered_books[0])
    except Exception as e:
        # return jsonify({"error": "Libro no encontrado. Error: " + str(e)}) , 404
        return jsonify({"error": "Libro no encontrado"}) , 404

# 3. Añadir un nuevo libro (se espera un JSON en el cuerpo de la solicitud)
@app.route('/v1/books', methods=['POST'])
def add_book():
    if not request.is_json:
        return jsonify({"error":"Debes hacer la petición con un json."}), 400
    data = request.get_json()
    campos = ['id', 'published', 'author', 'first_sentence', 'title']
    if not all(field in data for field in campos):
        return jsonify({"error":f"Debes enviar todos los campos de un libro: {campos}"}), 400
    books.append(data)
    # return jsonify(books)
    return jsonify({"mensaje": "Libro añadido"}), 200

# 4. Actualizar un libro existente utilizando try/except
@app.route('/v1/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book = [book for book in books if book['id'] == book_id][0]
        # book = request.get_json()
        book['title'] = request.args.get('title', book['title'])
        book['published'] = request.args.get('published', book['published'])
        book['first_sentence'] = request.args.get('first_sentence', book['first_sentence'])
        book['author'] = request.args.get('author', book['author'])
        return jsonify(book)
    except Exception as e:
        # return jsonify({"error": "Libro no encontrado. Error: " + str(e)}) , 404
        return jsonify({"error": "Libro no encontrado para modificar"}) , 404

# 5. Eliminar un libro 
@app.route('/v1/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        book = [book for book in books if book['id'] == book_id][0]
        books.remove(book)
        return jsonify({"mensaje": f"Libro {book['title']} eliminado exitosamente"})
    except Exception as e:
        # return jsonify({"error": "Libro no encontrado. Error: " + str(e)}) , 404
        return jsonify({"error": "Libro no encontrado para modificar"}) , 404

if __name__ == '__main__':
    app.run()