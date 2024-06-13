#method_overloading
class Test:
    def m1(self,a,b=0):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.m1(10)
t.m1(10,20)
t.display()








class Myclass:
    def outer_method(self):
        def inner_method():
            print("inner method")

        print("outer method")
        inner_method()


myclass=Myclass()
myclass.outer_method()