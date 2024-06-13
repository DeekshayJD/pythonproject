class student:
    def __init__(self,marks,name):
        self.name=name
        self.marks=marks

    def display(self):
        print("hi",self.name)

    def display(self):
        print("hello",self.name)
    def grade(self):
        if self.marks>80:
            print("first grad")
        elif self.marks>60:
            print("second grade")

s=student(90,"deekshay")
s.display()
s.grade()