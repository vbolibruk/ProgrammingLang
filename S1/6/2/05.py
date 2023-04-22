# Create an abstract class named Element that holds properties of elements, including their symbol, atomic number, and atomic weight. Include a constructor that requires values for all three properties and a get method for each value. (For example, the symbol for carbon is C, its atomic number is 6, and its atomic weight is 12.01. You can find these values by reading a periodic table in a chemistry reference or by searching the Web.) Also include an abstract method named describeElement().
# Create two extended classes named MetalElement and NonMetalElement. Each contains a describeElement() method that displays the details of the element and a brief explanation of the properties of the element type. For example, metals are good conductors of electricity, while nonmetals are poor conductors. Write an application named ElementArray that creates and displays an array that holds at least two elements of each type. Save the files as Element.java, MetalElement.java, NonMetalElement.java, and ElementArray.java.

from abc import ABC, abstractmethod

class Element(ABC):

    def __init__(self, symbol = "", number= 0.0,weight=0.0):
        self.symbol =  symbol
        self.number =  number
        self.weight =  weight

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.number

    def get_weight(self):
        return self.weight

    @abstractmethod
    def describeElement(self):
        pass

class MetalElement(Element):
    
    def __init__(self,symbol , number,weight):
        super().__init__(symbol , number,weight)
        self.describeElement()

    def describeElement(self):
        print("metals are good conductors of electricity")

class NonMetalElement(Element):
    
    def __init__(self,symbol , number,weight):
        super().__init__(symbol , number,weight)
        self.describeElement()

    def describeElement(self):
        print("nonmetals are poor conductors")


def ElementArray():

    m1 = MetalElement("Fe",1,0.1)
    m2 = MetalElement("Mg",2,0.12)
    nm1 = NonMetalElement("Ar",1,0.1)
    nm2 = NonMetalElement("He",1,0.1)
    arr = [m1,m2,nm1,nm2]
ElementArray()