'''
a=[[1,2,3],[4,5,6],[7,8,9]]
b=(zip(a[0],a[1],a[2]))
c=[]
for i in b:
 c.append(list(i))

print(c)
'''
a = [[1,2,3],[4,5,6],[7,8,9]]
b = zip(*a)  # Unpacking the list a into zip function to transpose it
c = [list(i) for i in b]

print(c)

'''
a=[[1,2,3],[4,5,6],[7,8,9]]
c=0
l1=[]
l2=[]
for i in range(len(a[0])):
    for j in a:
        l1.append(j[c])
        l2.append(l1)
        l1 = []
        c = c+1
print(l2)
'''