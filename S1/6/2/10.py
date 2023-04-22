# Create an abstract class called GeometricFigure. Each figure includes a height, a width, a figure type, and an area. Include an abstract method to determine the area of the figure. Create two subclasses called Square and Triangle. Create an application that demonstrates creating objects of both subclasses, and store them in an array. Save the files as GeometricFigure.java, Square.java, Triangle.java, and UseGeometric.java.

from abc import ABC, abstractmethod
 
class GeometricFigure(ABC):

     def __init__(self, height , width,figure , area):
        self.height =  height
        self.width =  width
        self.figure =  figure
        self.area =  area

     @abstractmethod
     def getArea(self):
         pass
 

 
class Square(GeometricFigure):
    def __init__(self, height , width,figure , area = 0):
        super().__init__(height , width,figure , area = 0)
        self.getArea()
 
    # overriding abstract method
    def getArea(self):
        self.area = self.height*self.height
        print(self.area)
 
class Triangle(GeometricFigure):
    def __init__(self, height , width,figure , area = 0):
        super().__init__(height , width,figure , area = 0)
        self.getArea()

    # overriding abstract method
    def getArea(self):
        self.area  =  1/2 * self.height * self.width
        print(self.area)
 
def UseGeometric():
    square = Square(2,2,"Square")
    triangle = Triangle(2,2,"Triangle")
    arr = [square,triangle]
UseGeometric()