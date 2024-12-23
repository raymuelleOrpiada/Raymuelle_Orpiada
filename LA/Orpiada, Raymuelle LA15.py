class Dog:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name)


class Cat:
    def __init__(self,name):
         self.name=name
    def speak(self):
        print(self.name)
        



class Bird:
    def __init__(self,name):
         self.name=name
    def speak(self):
        print(self.name)  
        

class Fish:
    def __init__(self,name):
         self.name=name
    def speak(self):
        print ("...")
def animal_sound(animal):
    animal.speak()

arf=Dog("Bark!")
mewo=Cat("Meow!")
birdie=Bird("Chirp!")
fish=Fish("Blop")

animals=[arf, mewo,birdie,fish]
for animal in animals:
    animal_sound(animal)