s="python is native language"
words=s.split()
output=[word[::-1] for word in words]
print(output)









'''
s="deekshay"
n=len(s)
i=-1
while i>=-n:
    print(s[i],end="")
    i-=1

s=["deekshay","akshay"]
print("-".join(s))
s=input("enter your city name:-")
s1=s.strip()
if s1=="Bangluru":
    print("hai localite")
elif s1=="mysore":
    print("hai mysurian")
    
while True:
    s = input("enter stirng :-")
    s1 = input("enter substring :-")
    try:
        if s.index(s1):
            print("value is exact")
            break
    except ValueError:
        print("plz check substring value before proceeding")
        #continue

'''