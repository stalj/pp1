class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def change_page(self,page):
        self.current_page = page

book = Book(
        "Harry Potter and the Philosopher's Stone",
        "J. K. Rowling",223)

print(f"My favorite book is {book.title}, ",end="")
print(f"written by {book.author}. ",end="")
print(f"This book has {book.pages} pages.")

book.open()
book.change_page(15)

if book.is_open:
    print(f"Reading the book, page {book.current_page}")
else:
    print("I am going to read the book later.")
