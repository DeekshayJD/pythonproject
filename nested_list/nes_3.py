l=[[1,2],[3,4]]
m=1
for i in range(0,2):
    m*=10
    for j in range(0,2):
        l[i][j]*=m
print(l)