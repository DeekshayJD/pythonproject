
l1 = []
def nes_2(nested_list):

    for i in nested_list:
        if type(i) is list:
            nes_2(i)
        else:
            l1.append(i)

nested_list=[["lion","deer",["girafe","dinosorus"],"cub"],["cat","dog","cow"]]
nes_2(nested_list)
print(l1)