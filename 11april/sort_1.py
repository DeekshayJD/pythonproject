l1=[1,3,4,2,5,86,5]
n=len(l1)
l2=[]
for i in range(0,n):
    for j in range(0,n-1):

        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)
print(list(set(l1)))