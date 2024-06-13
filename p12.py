



def replicate_zip(l1):
   return [list(i) for i in zip(*l1,*l2)]

l1=[[1,2],[3,4],[5,6],[7,8]]
l2=[[3,2],[6,4],[5,6],[7,8]]
print(replicate_zip(l1))















#0/0=[6,2,3,4,5,1]
def swap(l):
    size=len(l)
    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp
    return l
l=[1,2,3,4,5,6]
print(swap(l))