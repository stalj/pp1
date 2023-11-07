class ebook:
    def __init__(self):
        self.is_open=False
        self.pagenumber=1
        self.currentpage=1
    def book_status(self):
        if self.is_open==True:
            print('Book is open')
        else:
            print("Book is closed")
    def create_book(self,book_title,book_author,number_of_pages):
        self.author=book_author
        self.title=book_title
        self.nop=number_of_pages
        print(book_author, book_title)
    def open_book(self):
        self.is_open=True
    def close_book(self):
        self.is_open=False
    def page_switch_forward(self):
        if self.is_open==True:
            if self.nop>0:
                if self.currentpage>0:
                    self.currentpage+=1
        else:
            print("You can not read a closed book dummy")
    def page_switch_backwards(self):
        if self.is_open==True:
            if self.nop>0:
                if self.currentpage<=self.nop:
                    self.currentpage-=1
        else:
            print("You can not read closed book dummy")
    def show_page_number(self):
        if self.is_open==True:
            print(self.currentpage)
        else:
            print("Open a book first, you dummy!")
eb=ebook()

eb.create_book("Dookoła swiata raz jeszcze", 'Szymon Kuczynski',10)
eb.book_status()
eb.open_book()
eb.page_switch_forward()
eb.book_status()
eb.page_switch_backwards()
eb.book_status()
eb.show_page_number()
eb.close_book()
eb.show_page_number()
