class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def find_book(self, title: str):
        book = next((book for book in self.books if book.title == title), None)
        return book