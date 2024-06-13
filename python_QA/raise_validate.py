def div(a,b):

    if b==0:
        raise ZeroDivisionError("enter value greater then zero")
    return a//b
try:
    result=div(20,int(input("enter B value :-")))
    print(result)
except ZeroDivisionError as e:
    print("check formate")