#write a python program to find common letter between 2 string
s1="NAINA"
s2="REENE"
s=[]
for i in s1:
    if i in s2 and i not in s:
        s.append(i)
    output="".join(s)
print(output)
print(type(s))


