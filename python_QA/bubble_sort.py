def bubble_sort(l1):
    n=len(l1)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
               l1[j],l1[j+1]=l1[j+1],l1[j]

    print(l1)



l1 = [6, 4, 11, 15]
bubble_sort(l1)
