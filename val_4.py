class Employee:
    def __init__(self,eno,esal):
        self.eno=eno
        self.esal=esal

    def display(self):
        print(self.eno)
        print(self.esal)

class Test(Employee):
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.display()

e=Employee(101,1000)
Test.modify(e)
