class Test:

    def m2(self):
       self.z=50
    @staticmethod
    def m3():
        Test.a=40

t=Test()
t.m2()
print(t.z)
