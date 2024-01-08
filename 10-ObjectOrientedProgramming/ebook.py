class Ebook():
    def __init__(self, title, author, page_number):
        self.title = title
        self.author = author
        self.page_number = page_number
        self.current_page = 1
        self.is_open = False
    def open_book(self):
        self.is_open = True
    def close_book(self):
        self.is_open = False
    def read(self, number):
        if self.is_open:
            if self.current_page + number <= self.page_number:
                self.current_page += number
            else:
                print(f"There is only {self.page_number-self.current_page} pages left")
        else:
            print("You cannot read from a closed book")
    def show_status(self):
        print(f"'{self.title}' by {self.author} has {self.page_number} pages. The book is {'open' if self.is_open else 'closed'}. You are currentlly on a page number {self.current_page}")
