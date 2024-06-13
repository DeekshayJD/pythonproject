l=[1,-1,3,2,-7,-5,11,6]
left=[]
right=[]
for i in l:
    if i<0:
        left.append(i)
    else:
        right.append(i)
print(right+left)
