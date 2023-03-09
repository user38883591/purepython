class Animal:  #parent class
    def __init__(self,name):
        self.myname=name

    def talk(self):  # define the class
        raise NotImplementedError("subclass must implement abstract method")
class  Cat(Animal):  #child class
    def talk(self):
        return "meow"

class  Dog(Animal):  # child class
    def talk(self):
        return "woof"
paka=Cat("Menince")   # calling the class
doggy=Dog("Scott")  #calling the class

print(paka.myname + ":" + paka.talk())
print(doggy.myname + ":"+ doggy.talk())
class Donkey(Animal):
    def talk(self):
        return "ihoo iho"
class Cow(Animal):
    def talk(self):
        return "mooow"
class Horse(Animal):
    def talk(self):
        return "Neigh"

donkey=Donkey("Richie")
cow=Cow("Madoon")
horse=Horse("Whitney")

print(donkey.myname +":" +donkey.talk())
print(cow.myname+":" +cow.talk())
print(horse.myname +":" +horse.talk())
