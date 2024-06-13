class Test:
    x=10
    def __init__(self):
        Test.y=20
    def m1(self):
        Test.z=30
    @classmethod
    def m2(cls):
        cls.a=40

    @staticmethod
    def m3(self):
        Test.b=50

Test.m2()
print(Test.a)


