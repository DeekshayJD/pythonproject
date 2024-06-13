class person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

class Employee(person):

    def __init__(self,name=None,age=None,eno=None,esal=None):
        super().__init__(name,age)
        self.eno=eno
        self.sal=esal

    def display(self):
        print(self.name)
        print(self.eno)
        print(self.sal)
        print(self.age)
e=Employee("deekshay",26,132,30000)
e.display()
#e1=Employee("akshay",28)
#e2=Employee()
#e2.display()