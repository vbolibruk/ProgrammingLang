from abc import ABC, abstractmethod
from custombooks.Book  import Book


class Fiction(Book):
    
    def __init__(self,title,price):
        super().__init__(title,price)
        self.setPrice()

    def setPrice(self):
        self.__price = 24.99

class NonFiction(Book):
    
    def __init__(self,title,price):
        super().__init__(title,price)
        self.setPrice()

    def setPrice(self):
        self.__price = 37.99


