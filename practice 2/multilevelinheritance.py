
#multi_level inheritance is subclass inherite from superclass and anothe sublass inherte from sublcass forming chain inheritance
class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return " dog bow bow"

class Cat(Dog):
    def speak(self):
        return " cat Meow meow"

D=Dog("browni")
c=Cat("lid")
print(D.name+ "says"+ D.speak())
print(c.name+"says"+ c.speak())


