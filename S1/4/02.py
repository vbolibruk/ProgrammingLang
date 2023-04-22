# Bolibruk Vlad


# When gasoline is $100 per barrel, then the consumers price at the pump is between $3.50
# and $4.00 per gallon. Create a class named GasPrices. Its main() method holds an integer
# variable named pricePerBarrel to which you will assign a value entered by a user at the
# keyboard. Create a method to which you pass pricePerBarrel. The method displays the
# range of possible prices per gallon. For example, if gas is $120 per barrel, then the price at
# the pump should be between $4.20 and $4.80. Save the application as GasPrices.java.
class Ex04_1_5:
   def __init__(self , pricePerBarrel):
      self.__pricePerBarrel = pricePerBarrel
      self.pricePerBarrel(self.__pricePerBarrel)

   def pricePerBarrel(self,pricePerBarrel):
      if(pricePerBarrel == 120):
        print("should be between $4.20 and $4.80")

pricePerBarrel = input("Enter c: ")
pricePerBarrel = Ex04_1_5(pricePerBarrel)

# There are 2.54 centimeters in an inch, and there are 3.7854 liters in a U.S. gallon.
# Create a class named MetricConversion. Its main() method accepts an integer value
# from a user at the keyboard, and in turn passes the entered value to two methods.
# One converts the value from inches to centimeters and the other converts the same
# value from gallons to liters. Each method displays the results with appropriate
# explanation. Save the application as MetricConversion.java.

class Ex04_1_6:
   def __init__(self , value):
      self.value = value
      self.inchesToCentimeters(self.value)
      self.gallonsToLiters(self.value)

   def inchesToCentimeters(self,value):
      return value*2.54

   def gallonsToLiters(self,value):
      return value*3.7854

# Assume that a gallon of paint covers about 350 square feet of wall space. Create an
# application with a main() method that prompts the user for the length, width, and
# height of a rectangular room. Pass these three values to a method that does the
# following:
# l Calculates the wall area for a room
# l Passes the calculated wall area to another method that calculates and returns the
# number of gallons of paint needed
# l Displays the number of gallons needed
# l Computes the price based on a paint price of $32 per gallon, assuming that
# the painter can buy any fraction of a gallon of paint at the same price as a
# whole gallon
# l Returns the price to the main() method
# The main() method displays the final price. For example, the cost to paint a
# 15- by-20-foot room with 10-foot ceilings is $64. Save the application as
# PaintCalculator.java.


class Ex04_1_7:
   def __init__(self , length , width , height ):
      self.length = length
      self.width = width
      self.height = height
      self.calc(length , width , height)
      self.price =  self.gneeded * 32
      print("The cost to paint" + str(self.length) + " by " + str(self.width) + " with "+ str(self.height) + " is " +str(self.price))

   def calc(self,length , width , height):
      self.area =  2 * (length * height) + 2 * ( width * height)
      self.calc1(self.area)

   def calc1(self,area):
      
      self.gneeded = area /350
      if isinstance(self.gneeded, float):
        self.gneeded += 1
      
      print(self.gneeded)
      


# Create a class named Student. A Student has fields for an ID number, number of
# credit hours earned, and number of points earned. (For example, many schools
# compute grade point averages based on a scale of 4, so a three-credit-hour class in
# which a student earns an A is worth 12 points.) Include methods to assign values
# to all fields. A Student also has a field for grade point average. Include a method
# to compute the grade point average field by dividing points by credit hours
# earned. Write methods to display the values in each Student field. Save this class
# as Student.java.
# b. Write a class named ShowStudent that instantiates a Student object from the
# class you created and assign values to its fields. Compute the Student grade point
# average, and then display all the values associated with the Student. Save the
# application as ShowStudent.java.
# c. Create a constructor for the Student class you created. The constructor should
# initialize each Students ID number to 9999, his or her points earned to 12, and
# credit hours to 3 (resulting in a grade point average of 4.0). Write a program that
# demonstrates that the constructor works by instantiating an object and displaying
# the initial values. Save the application as ShowStudent2.java.

# Ex04_1_12

class Student:
   def __init__(self , iD = 9999, hours = 3, points = 12 ):
        self.id = iD
        self.hours = hours
        self.points = points
        print(self.computeAverage())

   def set_id(self,iD):
        self.id = iD
   def set_hours(self,hours):
        self.hours = hours
   def set_points(self, points):
        self.points = points

   def get_id(self):
    return self.id
   def det_hours(self):
    return self.hours
   def det_points(self):
    return self.points

   def computeAverage(self, points, hours):
        return points/hours

class ShowStudent:
   def __init__(self):
    newSt = Student(8585,325,5)
    print(newSt.get_id())
    print(newSt.det_hours())
    print(newSt.det_points())
    newSt2 = Student()
    print(newSt2.get_id())
    print(newSt2.det_hours())
    print(newSt2.det_points())


# Create a class named Painting that contains fields for a painting’s title, artist,
# medium (such as water color), price, and gallery commission. Create a
# constructor that initializes each field to an appropriate default value, and
# create instance methods that get and set the fields for title, artist, medium, and
# price. The gallery commission field cannot be set from outside the class; it is
# computed as 20 percent of the price each time the price is set. Save the class as
# Painting.java.
# b. Create a class named TestPainting whose main() method declares three
# Painting items. Create a method that prompts the user for and accepts values
# for two of the Painting objects, and leave the third with the default values
# supplied by the constructor. Then display each completed object. Finally, display
# a message that explains the gallery commission rate. Save the application as
# TestPainting.java

# Ex04_1_14:

class Painting:
   def __init__(self , title ="No title", artist = "Unknown", medium = "water color" , price = 0 ):
        self.title = title
        self.artist = artist
        self.medium = medium
        self.price = price
        self.__commission = self.price * 0.2

   def set_title(self,title):
        self.title = title
   def set_artist(self,artist):
        self.artist = artist
   def set_medium(self,medium):
        self.medium = medium
   def set_price(self, price):
        self.price = price

   def get_title(self,title):
        self.title = title
   def get_artist(self,artist):
        self.artist = artist
   def get_medium(self,medium):
        self.medium = medium
   def get_price(self, price):
        self.price = price
   def get_commission(self, commission):
        self.commission = commission

class TestPainting:
    def __init__(self):
        title = input("Enter title: ")
        artist = input("Enter artist: ")
        medium = input("Enter medium: ")
        price = input("Enter price: ")
        newP =  Painting(title,artist,medium,price)
        print(newP.get_title())
        print(newP.get_artist())
        print(newP.get_medium())
        print(newP.get_price())
        print(newP.get_commission())

        title = input("Enter title: ")
        artist = input("Enter artist: ")
        medium = input("Enter medium: ")
        price = input("Enter price: ")

        newP2 =  Painting(title,artist,medium,price)
        print(newP2.get_title())
        print(newP2.get_artist())
        print(newP2.get_medium())
        print(newP2.get_price())
        print(newP2.get_commission())
