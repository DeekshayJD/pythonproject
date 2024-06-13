l1=[11,33,33,33,55,33,44,11,22,66,55,77,88,33,33,11]
count_dic={}
max_count=0
max_repeated_eleemnt=None
for i in l1:
    if i in count_dic:
        count_dic[i]+=1
    else:
        count_dic[i]=1
    if l1.count(i)>max_count:
        max_count=l1.count(i)
        max_repeated_eleemnt=i
print(count_dic)

print(max_repeated_eleemnt,max_count)





'''
l1="deekshay is good boy boy boy"
dic={}
for i in l1.split():
     dic[i]=dic.get(i,0)+1
print(dic.items())

'''