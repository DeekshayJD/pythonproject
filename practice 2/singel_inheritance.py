#singlr_inheritance is subclass inherte from one super class
class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("animal barking")
        pass

class Dog(Animal):
    def bark(self):
        print(self.name+"      Dog barking")
    def speak(self):
        print(self.name,"barking bow bow")

dog=Dog("browni")
dog.speak()
dog.bark()