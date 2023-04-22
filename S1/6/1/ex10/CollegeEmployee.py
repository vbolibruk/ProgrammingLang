# CollegeEmployee—CollegeEmployee descends from Person. A CollegeEmployee also includes a Social Security number, an annual salary, and a department name, as well as methods that override the Person methods to accept and display all CollegeEmployee data.

from Person import Person


class CollegeEmployee(Person):

    def __init__(self, SSN = 0, salary = 99999 ,depName =""):
        super().__init__()
        self.SSN  = SSN
        self.salary  = salary
        self.depName  = depName

    def setVars(self):
        self.name = input("Enter name value: ")
        self.lastName = input("Enter lastName value: ")
        self.streetAddress = input("Enter streetAddress value: ")
        self.zip = input("Enter zip value: ")
        self.phone = input("Enter phone value: ")
        self.SSN = input("Enter SSN value: ")
        self.salary = input("Enter salary value: ")
        self.depName = input("Enter depName value: ")

        print(f"name: {self.name} ,  lastName  {self.lastName}, streetAddress :  {self.streetAddress} , zip: {self.zip} , SSN: {self.SSN}, salary: {self.salary} , depName: {self.depName} ")