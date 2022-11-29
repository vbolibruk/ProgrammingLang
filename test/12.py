# Create an interface called Player. The interface has an abstract method called play()
# that displays a message describing the meaning of “play” to the class. Create classes
# called Child, Musician, and Actor that all implement Player. Create an application
# that demonstrates the use of the classes. Save the files as Player.java, Child.java,
# Actor.java, Musician.java, and UsePlayer.java

from abc import ABC, abstractmethod

class Player(ABC):
    
    def __init__(self, name = ""):
        self.name =  name

    @abstractmethod
    def play(self):
        pass

class Child(Player):
    
    def __init__(self,name):
        super().__init__(name)
        print(self.play())

    def play(self):
        print("Child plays")

class Actor(Player):
    
    def __init__(self,name):
        super().__init__(name)
        print(self.play())

    def play(self):
        print("Actor plays")

class Musician(Player):
    
    def __init__(self,name):
        super().__init__(name)
        print(self.play())

    def play(self):
        print("Musician plays")
class UsePlayer(Player):
    
    def __init__(self,name):
        super().__init__(name)
        print(self.play())

    def play(self):
        print("UsePlayer plays")

Child1 = Child("Child1")
Musician1 = Musician("Musician1")