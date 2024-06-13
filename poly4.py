class Dog:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"{self.name} says bow bow")
class cat:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} says meow meow")


def animal(obj):
    #obj.talk()
   if hasattr(obj,"talk"):
       obj.talk()
   elif hasattr(obj,"bark"):
       obj.bark()

c=cat('deekshay')
animal(c)
c=Dog("akshay")
animal(c)


'''
class Dog:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"{self.name} says bow bow")
class cat:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"{self.name} says meow meow")

class duck:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"{self.name} says qyack quack")
def f1(animal):
    animal.talk()


animals=[Dog("browni"),cat("puppi"),duck("quack")]
for animal in animals:
    f1(animal)

'''