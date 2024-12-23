class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book = Book("It's not me, It's you", "Vanessa Bennett")
print(f"Book: {book.title},  {book.author}")
del book.author
print(book.author)

book1 = Book("Red Dead", "By J. Marston")
print(f"Book: {book1.title},{book1.author}")