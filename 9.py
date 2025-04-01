from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 2, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 3, "title": "A Game of Thrones", "author": "George R.R. Martin", "year": 1996}
]

class BookList(Resource):
    def get(self):
        return jsonify(books)

    def post(self):
        new_book = request.get_json()
        new_book["id"] = max(book["id"] for book in books) + 1 if books else 1
        books.append(new_book)
        return jsonify(new_book), 201


class Book(Resource):
    def get(self, id):
        book = next((book for book in books if book["id"] == id), None)
        if book:
            return jsonify(book)
        return {"error": "Book not found"}, 404

    def put(self, id):
        book = next((book for book in books if book["id"] == id), None)
        if book:
            data = request.get_json()
            book.update(data)
            return jsonify(book)
        return {"error": "Book not found"}, 404

    def delete(self, id):
        global books
        books = [book for book in books if book["id"] != id]
        return {"message": "Book deleted"}, 200


api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)