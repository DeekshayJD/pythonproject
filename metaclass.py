# Define a metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, dct)


# Define a class using the metaclass
class MyClass(metaclass=Meta):
    def __init__(self, x):
        self.x = x

    def display(self):
        print("Value of x:", self.x)


# Creating an instance of MyClass
obj = MyClass(10)
obj.display()
