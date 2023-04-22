# Розв’яжіть з підручника [M2] з глави 8 (Chapter 8, starting from page 436)
# задачі (Exercises): 4, 10.
# 5.1. У задачі 4 заповнюйте масив випадковими числами.
# 5.2. У задачі 10 після заповнення масивів виведіть у довільному порядку
# потрібні дані (тобто, наприклад, виводите дані для студента з ID = 4,
# потім для студента з ID = 9 і т.д.).

# Create an application containing an array that stores eight integers. The application should (1) display all the integers, (2) display all the integers in reverse order, (3) display the sum of the eight integers, (4) display all values less than 5, (5) display the lowest value, (6) display the highest value, (7) calculate and display the average, and (8) display all values that are higher than the calculated average value. Save
# the file as NumberListDemo.java.

from random import randint

class Ex04:
   def __init__(self):

      self.__array = []
      for _ in range(8):
        value = randint(-1000, 1000)
        self.__array.append(value)
      self.display()
      self.displayReverse()
      self.getAllValuesLessThan()
      self.getAverage()
      self.getCustom()
      self.getHigh()
      self.getLowest()
      self.getSum()

# (1) display all the integers
   def display(self):
    print(self.__array)

# (2) display all the integers in reverse order
   def displayReverse(self):
    print(self.__array[::-1])

# (3) display the sum of the eight integers
   def getSum(self):
    sum = 0
    for i in self.__array:
        sum = sum + i
    print(sum)
#  (4) display all values less than 5
   def getAllValuesLessThan(self, lessThan = 5):
    newArr  = []
    for i in self.__array:
        if(i<lessThan):
            newArr.append(i)
    print(newArr)
# (5) display the lowest value

   def getLowest(self):
    self.__array.sort()
    print( self.__array[0])


# (6) display the highest value
   def getHigh(self):
    sorted  =self.__array.sort()
    print(self.__array[7])

# (7) calculate and display the average,
   def getAverage(self):
    sum = 0
    for i in self.__array:
        sum = sum + i
    print(sum/8)
# (8) display all values that are higher than the calculated average value.
   def getCustom(self):
    sum = 0
    for i in self.__array:
        sum = sum + i
    for i in self.__array:
        if(i>sum/8):
            print(i)
newSt = Ex04()


# Write an application containing three parallel arrays that hold 10 elements each. The first array holds four-digit student ID numbers, the second holds first names, and the third holds the students’ grade point averages. Use dialog boxes to accept a student ID number and display the student’s first name and grade point average. If a match is not found, display an error message that includes the invalid ID number and allow the user to search for a new ID number. Save the file as StudentIDArray.java.

class Ex10:
   def __init__(self):

      self.__Ids = []
      for _ in range(10):
        value = randint(1000, 10000)
        self.__Ids.append(value)
      self.__Names = ["James","Mary","Robert"	,"Patricia","John","Jennifer","Michael"	,"Linda","David","Elizabeth"]
      self.__avgGrades = [4.0,3.5,2,4,3,3.2,4.1,5,2,4.7]
      self.displayDatabyId(self.__Ids[0])
      self.displayDatabyId(123)

   def displayDatabyId(self, id):
    index = self.__Ids.index(id)
    if(index != -1):
        print(self.__Names[index],self.__Names[index],self.__avgGrades[index])
newSt = Ex10()
