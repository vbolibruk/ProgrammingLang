# Create a class named Horse that contains data fields for the name, color, and
# birth year. Include get and set methods for these fields. Next, create a subclass
# named RaceHorse, which contains an additional field that holds the number of
# races in which the horse has competed and additional methods to get and set
# the new field. Write an application that demonstrates using objects of each class. 


from Horse import Horse


class RaceHorse(Horse):

    def __init__(self, name, color, birth , races):
        super().__init__(name, color, birth)
        self._races = races
   
    def get_races(self):
        return self._races

    def set_races(self, races):
        self._races = races