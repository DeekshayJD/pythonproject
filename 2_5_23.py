l=[1,2,3,4,5]
l1=[x for x in l if x%2==0]
print(l1)
l=list(filter(lambda x:x%2==0,l))
print(l)
#d={k:v for k,v in d.items()}