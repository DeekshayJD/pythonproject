


class Myclass:
    def __init__(self,name):
        self.name=name
      #  print(f"this is self id{id(self)}")
        #print(id(self.name))

    def print_id(self):
        print(f"self id {id(self)} ")
        #print(id(self.name))
        #print(self.name)

obj=Myclass("obj1")
obj.print_id()
print(f"this is object id is {id(obj)}")
print(id(obj.name))

