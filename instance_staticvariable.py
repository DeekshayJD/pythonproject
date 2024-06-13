class Test:
    x=10
    def t1(self):
        self.y=20
        print(self.y)
    def __init__(self):
        self.z=30

t=Test()
print(t.x)
t.t1()
print(t.z)
