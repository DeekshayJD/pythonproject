class father:
    def __init__(self):
        self.__variable = "I am father"

    def get_private_attribute(self):
        return self.__private_attribute

class Child(father):
    def __init__(self):
        super().__init__()

child_obj = Child()
print(child_obj.__variable)
#print(child_obj.pr)
# Trying to access private attribute directly will raise an AttributeError
print(child_obj.get_private_attribute() ) # This will raise an AttributeError

# Accessing private attribute indirectly using getter method
#print(child_obj.get_private_attribute())  # Output: "I am private"
