class Myclass:
    def __init__(self,name):
        self.name=name

    def print_id(self):
        print(id(self))

obj=Myclass("deekshay")
obj1=Myclass("akshay")
obj.print_id()
print(id(obj))
print(id(obj1))