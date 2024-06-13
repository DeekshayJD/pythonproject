str1="silent"
str2="listen"
l1=list(str1.upper())
l2=list(str2.upper())
l1.sort(),l2.sort()
if l1.sort()==l2.sort():
    print(True)
else:
    print(False)
