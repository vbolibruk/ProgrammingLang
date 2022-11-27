from custombooks.Book  import Book

class NonFiction(Book):
    
    def __init__(self,title,price):
        super().__init__(title,price)
        self.setPrice()

    def setPrice(self):
        self.__price = 37.99
