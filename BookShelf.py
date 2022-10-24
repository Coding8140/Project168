class BookShelf:
    def __init__(self,name,author,price,published):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_published = published
  
    def add_book(self):
        print("Book Name: "+self.book_name)
        print("Book Author: "+str(self.book_author))
        print("Book Price: "+self.book_price)
        print("Book was Published in:"+self.book_published)
        print("Book Added")
        
book1 = BookShelf("Harry Potter and the Philosopher's Stone ","J. K. Rowling","1928", "1997")
book1.add_book()

book2 = BookShelf("Dairy of a Wimpy Kid","Jeff Kinney","700", "2017")
book2.add_book()
  
