class Dog:

 def __init__(self, name):

   self.name = name
 def sit(self):

   print(self.name + " is sitting.")
my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
#my_dog.sit()

class SARDog(Dog):
     #Represent a search dog.
  def __init__(self, name):
 #"""Initialize the sardog."""
   super().__init__(name)
     #self.name=name
  def search(self):
 #"""Simulate searching."""
   print(self.name + " is searching.")
my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
#my_dog.sit()
my_dog.search()
