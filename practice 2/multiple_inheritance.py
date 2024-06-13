
#multiple inheritance allow to inherite from multiple super class
class A:
    def Method_a(self):
        print("this is method A")
class B:
    def Method_b(self):
        print("this is method B")

class C(A,B):
    def Method_c(self):
        pass

c=C()
c.Method_a()
c.Method_b()
