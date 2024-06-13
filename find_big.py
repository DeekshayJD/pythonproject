l=[1,2,3,2,4,5,3,4]
l1=[]
for i in l:
    if l.count(i)>1 and i not in l1:
        l1.append(i)
        print(i,l.count(i))

