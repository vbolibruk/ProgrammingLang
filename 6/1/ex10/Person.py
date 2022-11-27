# Person—A Person contains a first name, last name, street address, zip code, and phone number. The class also includes a method that sets each data field, using a series of dialog boxes and a display method that displays all of a Person’s information on a single line at the command line on the screen.

class Person:

    def __init__(self, name= "", lastName= "", streetAddress= "", zipC= "", phone= ""  ):
        self.name = name
        self.lastName  = lastName
        self.streetAddress  =streetAddress
        self.zip  = zipC
        self.phone  = phone

    def get_name(self):
        return self.name
    def get_lastName(self):
        return self.lastName
    def get_streetAddress(self):
        return self.streetAddress
    def get_zip(self):
        return self.zip
    def get_phone(self):
        return self.phone

    def set_name(self, name):
         self.name = name
    def set_lastName(self , lastName):
         self.lastName  = lastName
    def set_streetAddress(self, streetAddress):
         self.streetAddress  = streetAddress
    def set_zip(self, zipC):
         self.zip  = zipC
    def set_phone(self, phone ):
         self.phone  = phone

    def setVars(self):
        self.name = input("Enter name value: ")
        self.lastName = input("Enter lastName value: ")
        self.streetAddress = input("Enter streetAddress value: ")
        self.zip = input("Enter zip value: ")
        self.phone = input("Enter phone value: ")
        print(f"name: {self.name} ,  lastName  {self.lastName}, streetAddress :  {self.streetAddress} , zip: {self.zip} ")