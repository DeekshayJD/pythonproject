def max_min(l1):
    max=1
    min=1
    for i in l1:
        if i>max:
            max=i
        elif i <min:
            min=i
    return max,min



l1=[1,2,3,4,5]
print(max_min(l1) )

