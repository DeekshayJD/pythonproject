class Test:


    def m2(self):
        self.a=20



    @staticmethod
    def m1():
        Test.x=10
t=Test()
t.m2()
print(t.a)
Test.m1()
print(Test.x)
