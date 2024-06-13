l=[1,2,[3,4],[5,6]]
ans=False
for i in l:
    if type(i)==list:
        ans=True
        break
print("list contin nested values",str(ans))
