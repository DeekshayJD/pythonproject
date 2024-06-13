class Myclass:
    class_variable=10
    def __init__(self):
        self.name="deekshay"
    def print_id(self):
        print(id(self))
        #print(id(self.name))
        #pass
        print(id(Myclass.class_variable))



obj1=Myclass()
print(id(obj1))
obj1.print_id()
"""
obj2=Myclass("obj2")

print(id(obj1))
print(id(Myclass.class_variable))
obj1.print_id()
"""
