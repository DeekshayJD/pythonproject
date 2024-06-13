class Test:
    def __init__(self):
        self.name="deekshya"

    def output(self):
        print(id(self))
        print(id(self.name))

t=Test()
print(t.output())
print(id(t))