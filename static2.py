class Test:
    x = 10

    def __init__(self):
        Test.y = 20

    def m1(self):
        Test.z = 30

    @classmethod
    def m2(cls):
        cls.a = 40

    @staticmethod
    def m3():
        Test.b = 50

# Accessing class method variable
Test.m2()  # Call the class method to set cls.a to 40
print(Test.a)  # Accessing class method variable using class name

# Accessing static variable
Test.m3()  # Call the static method to set Test.b to 50
print(Test.b)  # Accessing static variable using class name

# Create an instance of Test class
t = Test()

# Call the method m1 on the instance
t.m1()

# Access the method variable z using the class name
print(Test.z)


class Test:
    x=10
    def __init__(self):
        self.y=20
    '''
        def m1(self):#t.m1() print(t.z)
      self.z=30
    '''
    def m1(self):#t.m1() print(Test.z)
      Test.z=30
    @classmethod
    def m2(cls):#Test.m2() print(Test.a)

        cls.a=40

    @staticmethod  #Test.m3() print(Test.b)

    def m3():
        Test.b=50
t=Test()
print(t.y)
t.m1()
print(Test.z)
Test.m2()
print(Test.a)
Test.m3()
print(Test.b)