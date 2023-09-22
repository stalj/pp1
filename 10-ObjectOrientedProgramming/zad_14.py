class Book():

    def __init__(self,title,author,all_pages):
        self.is_open=False
        self.title=title
        self.author=author
        self.all_pages=all_pages
        self.current_page=0

    def open(self):
        self.is_open=True

    def reading(self,pages):
        if self.current_page+pages<self.all_pages and self.is_open==True:
            self.current_page+=pages
        else:
            print("Congratulations, you have already finished the book")

    def close(self):
        self.is_open=False

    def show_status(self):
        if self.is_open==True:
            print("You are reading ",self.title,", you have already read ",self.current_page,"pages")
        else:
            print("Book is closed")

flawless=Book('flawless','Marta Łabęcka',420)
flawless.show_status()
flawless.open()
flawless.reading(72)
flawless.show_status()

flawless.reading(300)
flawless.show_status()
flawless.reading(100)
