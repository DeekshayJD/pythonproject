class animal:
    def speeak(self):
        pass

class dog(animal):
    def speak(self):
        return "madura bow bow"
class cat(animal):
    def speak(self):
        return "athge cat"
class bird(animal):
    def speak(self):
        return "anna pear"
def animal_make_sound(deek):
    print(deek.speak())
c=cat()
d=dog()
b=bird()
animal_make_sound(b)