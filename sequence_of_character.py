
def occurence(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    return dic
s="ABCABCABBCDE"
result=occurence(s)
for k,v in result.items():
    print(f"values{k}=number of times repeated{v}")
#print(values,occurence)

#print(f"values{k}=number of times repeted{y}")




















'''
s="ABCDABBCDABBBCCCDDEEEF"
s1=[]
for x in s:
    if x not in s1:
        s1.append(x)
output="".join(s1)
print(output)
for i in sorted(set(s)):
    print(i,end="")
s="befcd4fk21"
#output=bcdefk124
s1=s2=output=""
for i in sorted(s):
    if i.isalpha():
        s1+=i
    else:
        s2+=i
#output=sorted(s1)+sorted(s2)
output=s1+s2
print(output)
s1=s2=output=""
for i in s:
    if i.isalpha():
        s1+=i
    else:
        s2+=i
#print(s1,s2)
for x in sorted(s1):
    output+=x
for x in sorted(s2):
    output+=x
print(output)
'''