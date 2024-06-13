s="pwwkewwwgftr"
l=""
l1=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not  in l:
            l+=s[j]

        else:
            l1+=[len(l)]
            l=""
            break
print(l)
print(max(l1))
