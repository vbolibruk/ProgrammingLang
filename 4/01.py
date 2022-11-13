# Bolibruk Vlad

class Ex03_1_9_1:
   def __init__(self , height = 1,  width = 2):
      self.height = height
      self.width = width

   def getArea(self):
      return self.height * self.width

   def getPerimeter(self):
      return 2*(self.height + self.width)
first = Ex03_1_9_1(35.9,3.5)
print(first.width)
print(first.height)
print(first.getArea())
print(first.getPerimeter())

second = Ex03_1_9_1(40,4)
print(second.width)
print(second.height)
print(second.getArea())
print(second.getPerimeter())

import datetime

class Ex03_1_9_7:
   def __init__(self , id = 0, balance = 0 , annualInterestRate = 0 ):
      self.__id = id
      self.__balance = balance
      self.__annualInterestRate = annualInterestRate
      self.__dateCreated = datetime.datetime.now()
   def getMonthlyInterestRate(self):
      return self.__balance * ( (self.__annualInterestRate/100)/12)

   def getMonthlyInterest(self):
      # CI = P (1 + r/100)n
      return self.__balance * (1+ self.__annualInterestRate/100)

   def withdraw(self, amount):
      self.__balance =  self.__balance - amount

   def deposit(self, amount):
      self.__balance =  self.__balance + amount

deposit= Ex03_1_9_7(1122,20000,4.5)
deposit.withdraw(2500)
deposit.deposit(3000)
print(deposit.getMonthlyInterestRate())
print(deposit.getMonthlyInterest())

class Ex03_1_9_8:
   SLOW = 1
   MEDIUM = 2
   FAST = 3
   def __init__(self , speed = 1, on = False , radius = 5,  color = "blue"):
      self.__speed = speed
      self.__on = on
      self.__radius = radius
      self.__color = color

   @property
   def speed(self):
      return self.__speed
   @property
   def on(self):
      return self.__on
   @property
   def radius(self):
      return self.__radius
   @property
   def color(self):
      return self.__color

   @speed.setter
   def speed(self,val):
      if val == 0:
         return
      self.__speed = val

   @on.setter
   def on(self,val):
      if val == 0:
         return
      self.__on = val  

   @radius.setter
   def radius(self,val):
      if val == 0:
         return
      self.__radius = val

   @color.setter
   def color(self,val):
      if val == 0:
         return
      self.__color = val

   def toString(self):
      if(self.__on):
         return  str(self.speed) + " "+  str(self.on) + " "+ str(self.radius) + " " +self.color
         
      else:
         return  "fan is off" + str(self.radius) + self.color

# def __init__(self , speed = SLOW, on = False , radius = 5,  color = "blue"):
 
fan1= Ex03_1_9_8(3,True,10,"yellow")
print(fan1.toString())
fan2= Ex03_1_9_8(3,False,5,"blue")
print(fan2.toString())


import math 

class Ex03_1_9_10:
   def __init__(self , a, b , c):
      self.__a = a
      self.__b = b
      self.__c = c

   def getDiscriminant(self):
      d =  self.__b*self.__b - 4*self.__a*self.__c
      return d
   def getRoot1(self):
      if(self.getDiscriminant()<0):
         return 0
      return (-self.__b + math.sqrt(self.getDiscriminant()))/2*self.__a
   def getRoot2(self):
      if(self.getDiscriminant()<0):
         return 0
      return (-self.__b - math.sqrt(self.getDiscriminant()))/2*self.__a

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")
solve= Ex03_1_9_10(a,b,c)
print(solve.getRoot1())