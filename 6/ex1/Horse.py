# Create a class named Horse that contains data fields for the name, color, and
# birth year. Include get and set methods for these fields. Next, create a subclass
# named RaceHorse, which contains an additional field that holds the number of
# races in which the horse has competed and additional methods to get and set
# the new field. Write an application that demonstrates using objects of each class.
# Save the files as Horse.java, RaceHorse.java, and DemoHorses.java.

class Horse:

    def __init__(self, name, color, birth):
        self._name = name
        self._color = color
        self._birth = birth
   
    def get_name(self):
        return self._name
    def get_color(self):
        return self._color
    def get_birth(self):
        return self._birth

    def set_name(self,name):
        self._name = name
    def set_color(self,color):
        self._color = color
    def set_birth(self, birth):
        self._birth = birth