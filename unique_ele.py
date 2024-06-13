def unique(l):
    repeated_element=[]
    unique_element=[]
    for i in l:
        if l.count(i)>=2 and i not in repeated_element:
            repeated_element.append(i)
        elif l.count(i)==1:
            unique_element.append(i)
    return f"repeated element{repeated_element},unique element {unique_element}"
    #return f"unique element {uniqu}"




l=[1,2,2,3,4,5,5]
print(unique(l))