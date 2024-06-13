class Animal():
    def __init__(self,name):
        self.name=name

    def  speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Bow'

class Cat(Animal):
    def speak(self):
        return "meow"

d=Dog("brownie")
c=Cat("pussy")
print(d.name +"says"+d.speak())
print(c.name +"says"+c.speak())


