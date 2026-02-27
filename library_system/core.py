# core.py
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author


class Library:
    def __init__(self, role="User"):
        self.books = []
        self.role = role

    def __getitem__(self, index):
        return self.books[index]

    def __len__(self):
        return len(self.books)