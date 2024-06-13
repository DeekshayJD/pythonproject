class Animal():
    def __init__(self,name):
        self.name=name
     #pass
    def speak(self):
        print("animal speak")
class Dog(Animal):
    def speak(self):
        print(self.name+" dog speaks")
        #pass

class Cat(Animal):
    def speak(self):
        print("cat speak")
def make_sound(animal):
    animal.speak()

dog=Dog("brownie")
cat=Cat("pem")

make_sound(dog)
make_sound(cat)
