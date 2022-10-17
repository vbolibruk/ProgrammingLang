from Horse import Horse
from RaceHorse import RaceHorse

simpleHorse =  Horse("Pinky","black","01-02-2010")

print(simpleHorse.get_name())
simpleHorse.set_name("Black Light")
print(simpleHorse.get_name())

try:
  print(simpleHorse.get_races())
except:
  print("An exception occurred get_races")


raceHorse =  RaceHorse("Rainbow","White","01-02-2015",10)

print(f"Races Rainbow took {raceHorse.get_races()}")
raceHorse.set_races(11)
print(f"Races Rainbow took after set {raceHorse.get_races()}")
