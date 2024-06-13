class Employee:
    def getempvalues(self):
        self.eno=int(input("Enter Emp Number:"))
        self.ename=input("Enter Emp Name:")
        self.dsg=input("Enter Emp Designation:")
    def dispempvalues(self):
        print("Emp Number: {}".format(self.eno))
        print("Emp Name: {}".format(self.ename))
        print("Emp Designation: {}".format(self.dsg))
    #main program
eo1=Employee() # when we create an object, it must initlized by


eo1.getempvalues()
eo1.dispempvalues()
#print("content of eo1=", eo1.__dict__)