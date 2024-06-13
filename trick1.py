'''
Move all zeros to the end of an array.
i/p:[0,1,2,3,0,5]
o/p: [1,2,3,5,0,0]
o/p: [0,0,1,2,3,5]
'''
l=[0,1,2,3,0,5]
op1=[]
op2=[]
for i in l:
    if i>0:
        op1.append(i)
    elif i==0:
        op2.append(i)



print(op2+op1)
