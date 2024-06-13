class Test:
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=10
        print(self.a)
        print(self.b)

    def m2(self):
        self.b=20
        print(self.a)
        print(self.b)

t=Test()
t.m1()
t.m2()