from ebook import Ebook
book = Ebook("After", "Anna Todd", 823)

book.show_status()
book.open_book()
book.show_status()
book.read(59)
book.show_status()
book.close_book()
book.show_status()
book.read(59)
book.show_status()
