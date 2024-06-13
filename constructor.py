class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def display_info(self):
        if self.name is not None and self.age is not None:
            print(f"Name: {self.name}, Age: {self.age}")
        else:
            print("Information not available")

# Non-parameterized constructor
person1 = Person()
person1.display_info()  # Output: Information not available

# Parameterized constructor
'''
person2 = Person("Alice", 30)
person2.display_info()  # Output: Name: Alice, Age: 30

'''