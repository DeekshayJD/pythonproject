#Heirarchail_inheritance is multiple subclass inheriting from single super class

class Animal():
    def speak(self):
        print("animal speak")

class Dog(Animal):
    def bark(self):
        print("Dog Bark")
class Cat(Animal):
    def meow(self):
        print("cat meow")

d=Dog()
c=Cat()
d.speak()
d.bark()
