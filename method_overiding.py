#method_overiding
class Animal:
    def make_sound(self):
        print("generic sound")

class Dog(Animal):
    def make_sound(self):
        print("bow bow")

class Cat(Animal):
    def make_sound(self):
        print("meow")

#animal=Animal()
dog=Dog()
cat=Cat()
#animal.make_sound()
dog.make_sound()