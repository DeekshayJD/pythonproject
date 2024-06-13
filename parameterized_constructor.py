print("enter two number two divide:-")
print("enter {q} to quit")


b=int(input("enter second number :-"))
if b=="q":
    #break
    while True:
        a=int(input("enter first number :-"))
        if a=="q":
            try:
                result=a//b
                print(result)
            except ZeroDivisionError:
                print("dont divide by zero")




















class Test:
    def __init__(self,name,age):
        self.name=name
        self.age=age

t1=Test("deekshay",24)
print(t1.__dict__)

