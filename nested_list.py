a=[[1,2,3],[4,5,6],[7,8,9]]

a1=zip(a[0],a[1],a[2])
result=[]
for i in a1:
    result.append(list(i))
print(result)