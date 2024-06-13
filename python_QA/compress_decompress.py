#compress
count=1
result=""
s="aaaaabbcc"
for i in range(len(s)):
    if i==len(s)-1:
        result+=s[i]+str(count)
    elif s[i]==s[i+1]:
        count+=1
    else:
        result+=s[i]+str(count)
        count=1
print(result)






'''

#decompress
s="a3b2c4"

result=""
for i in range(0,len(s),2):
    char=s[i]
    count=int(s[i+1])
    result+=char*count
print(result)

'''