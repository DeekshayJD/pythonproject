
def compare(l1,l2):

    try:
        if not l1 or not l2:
            raise ValueError("list shoul not be empty")
        l3 = []
        for i in l1:
            if i in l2:
                l3.append(i)
        print(l3)
    except ValueError as e:
        print(e)




l1=[6,7,8,5,9]
l2=[5,6,7,8]
compare(l1,l2)

