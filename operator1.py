s = "abcabcbb"
l="";l1=[]
for  i in range(len(s)):
  for j in range(i,len(s)):
    if s[j] not in l:
       l=l+s[j]
    else:
        l1+=[len(l)]
        l=""
        break
print(max(l1))








'''
a,b=[int(x) for x in input("enter two numbers :-").split(",")]
print(a*b)
'''