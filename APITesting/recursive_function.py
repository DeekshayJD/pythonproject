#recursive_function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

year=int(input("enter year:-"))
if (year%4==0 and year%100!=0)or (year%400==0):
    print("its a leap year")


