class student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks

    def getmarks(self):
        return self.marks

s=student()
s.setName("deekshay")
s.setmarks(90)
print(s.getmarks())
print("hi",s.getName())