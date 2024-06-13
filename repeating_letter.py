str1=input("enter string 1:-")
str2=input("enter string 2:-")
str=[]
for i in str1:
    if i in str2 and i not in str:
        str.append(i)
s2="".join(str)
print(s2)
