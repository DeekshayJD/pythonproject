

out_list=[]
def flat_list(list1):
    for i in list1:
        if type(i)==list:
            flat_list(i)
        else:
            out_list.append(i)

nestedlist=[1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
flat_list(nestedlist)
print(out_list)
