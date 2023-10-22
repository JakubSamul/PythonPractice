class Books():
    def __init__(self):
        self.books = {}
        self.numbers = 0

    def add_books(self, book):
        self.numbers += 1
        self.books[self.numbers] = book

    def __str__(self):
        return str(self.books)
    

class StoreBooks():
    @staticmethod
    def save_books(filename, books):
        with open(filename, "w") as f:
            f.write(str(books))

b = Books()
b.add_books('Book A')
b.add_books('Book B')
print(f"The books I have read are : {b}")

s = StoreBooks()
s.save_books("read_books.txt", b)