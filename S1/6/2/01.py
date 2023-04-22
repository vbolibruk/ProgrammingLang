# Create an abstract class named Book. Include a String field for the book’s title and a double field for the book’s price. Within the class, include a constructor that requires the book title, and add two get methods—one that returns the title and one that returns the price. Include an abstract method named setPrice(). Create two child classes of Book: Fiction and NonFiction. Each must include a setPrice() method that sets the price for all Fiction Books to $24.99 and for all NonFiction Books to $37.99. Write a constructor for each subclass, and include a call to setPrice() within each. Write an application demonstrating that you can create both a Fiction and a NonFiction Book and display their fields. Save the files as Book.java, Fiction.java, NonFiction.java, and UseBook.java.
from abc import ABC, abstractmethod

class Book(ABC):
    
    def __init__(self, title = "", price= 0.0):
        self.title =  title
        self.price =  price

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    @abstractmethod
    def setPrice(self):
        pass

class Fiction(Book):
    
    def __init__(self,title,price):
        super().__init__(title,price)
        self.setPrice()

    def setPrice(self):
        self.price = 24.99

class NonFiction(Book):
    
    def __init__(self,title,price):
        super().__init__(title,price)
        self.setPrice()

    def setPrice(self):
        self.price = 37.99

newFiction = Fiction("Ono",13)
print(newFiction.price)
newNonFiction = NonFiction("911",14)
print(newNonFiction.price)
