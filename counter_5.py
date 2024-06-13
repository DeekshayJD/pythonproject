s="NETSETOSNET"
s1=[]
for i in s :
    if i not in s1 and s.count(i)<2 :
     s1.append(i)
result="".join(s1)
print(result)

a=[1,2,3,4,5]
print(a[-1:-3:1])