
def smart_div(func):
    def inner(a,b):
        if b==0:
            print("change denominator other then zero")
            
        else:
            return func(a,b)
    return inner






@smart_div
def division(a,b):
    return a/b

#print(division(10,2))
print(division(10,int(input("enter second digit:-"))))