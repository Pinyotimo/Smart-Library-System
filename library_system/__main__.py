from .core import Book, Library
from .utils import track_access, permission_check, borrow_item

class SmartLibrary(Library):
    @permission_check("Admin")
    def add_book(self, book):
        self.books.append(book)

    @track_access
    def borrow_book(self, book):
        borrow_item(book)


def demo():
    lib = SmartLibrary(role="Admin")
    book1 = Book("Python Tricks", "Dan Bader", 250)
    book2 = Book("1984", "George Orwell", 328)

    lib.add_book(book1)
    lib.add_book(book2)

    print("Library contents:")
    for b in lib:
        print(b)

    lib.borrow_book(book1)


if __name__ == "__main__":
    demo()