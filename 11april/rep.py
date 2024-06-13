def rep(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1  # Increment count or initialize to 1 if not present
    return dic

s = "deeksh correct this\nayy"
print(rep(s))
def rep(s1):
    dic={}
    for i in s1:
       dic[i]=dic.get(i,0)+1
    return dic
str="deekshayy"
print(rep(str))
