# Faculty—Faculty descends from CollegeEmployee. This class also includes
# a Boolean field that indicates whether the Faculty member is tenured, as well as methods that override the CollegeEmployee methods to accept and display this additional piece of information.


from Person import Person
from CollegeEmployee import CollegeEmployee

class Faculty(CollegeEmployee):

    def __init__(self, tenured = False):
        super().__init__()
        self.tenured  = tenured

    def setVars(self):
        self.name = input("Enter name value: ")
        self.lastName = input("Enter lastName value: ")
        self.streetAddress = input("Enter streetAddress value: ")
        self.zip = input("Enter zip value: ")
        self.phone = input("Enter phone value: ")
        self.SSN = input("Enter SSN value: ")
        self.salary = input("Enter salary value: ")
        self.depName = input("Enter depName value: ")
        self.tenured = input("Enter tenured value: ")

        print(f"name: {self.name} ,  lastName  {self.lastName}, streetAddress :  {self.streetAddress} , zip: {self.zip} , SSN: {self.SSN}, salary: {self.salary} , depName: {self.depName}, name: {self.tenured} ")