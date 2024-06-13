lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
#l2=[lst1+lst2 ,zip(lst1,lst2)]
l2=[i+j for i,j in zip(lst1,lst2)]

print(l2)