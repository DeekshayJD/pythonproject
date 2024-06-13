#Remove duplicates by preserving order of the list  a = [[1,2],[1,3],[1,2],[1,3],[1,5],[5,1],[1,4]]

a = [[1, 2], [1, 3], [1, 2], [1, 3], [1, 5], [5, 1], [1, 4]]
a1=[]
print(len(a))
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        a1.append(a[i])
print(a1)

