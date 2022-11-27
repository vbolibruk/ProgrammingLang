# Student—Student descends from Person. In addition to the fields available in Person, a Student contains a major field of study and a grade point average as well as methods that override the Person methods to accept and display these additional facts.

from Person import Person

class Student(Person):

    def __init__(self, major = "" , grade = "" ):
        super().__init__()
        self.major = major
        self.grade  = grade
        self.setVars()


    def setVars(self):
        self.name = input("Enter name value: ")
        self.lastName = input("Enter lastName value: ")
        self.streetAddress = input("Enter streetAddress value: ")
        self.zip = input("Enter zip value: ")
        self.phone = input("Enter phone value: ")

        self.major = input("Enter major value: ")
        self.grade = input("Enter grade value: ")

        print(f"name: {self.name} ,  lastName  {self.lastName}, streetAddress :  {self.streetAddress} , zip: {self.zip} , major: {self.major} , grade: {self.grade} ")

newSt = Student()