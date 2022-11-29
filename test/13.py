# Create an abstract class called Student. The Student class includes a name and a
# Boolean value representing full-time status. Include an abstract method to determine
# the tuition, with full-time students paying a flat fee of $2,000 and part-time students
# paying $200 per credit hour. Create two subclasses called FullTime and PartTime.
# Create an application that demonstrates how to create objects of both subclasses.
# Save the files as Student.java, FullTime.java, PartTime.java, and UseStudent.java.

from abc import ABC, abstractmethod

class Student(ABC):
    
    def __init__(self, name = "", time=False):
        self.name =  name
        self.time =  time

    @abstractmethod
    def getTuition(self):
        pass

class FullTime(Student):
    
    def __init__(self,name):
        super().__init__(name,True)
        print(self.getTuition())

    def getTuition(self):
        return 2000

class PartTime(Student):
    
    def __init__(self,name):
        super().__init__(name,False)
        print(self.getTuition())

    def getTuition(self):
        return 200

fullTime = FullTime("Vlad")
partTime = PartTime("George")