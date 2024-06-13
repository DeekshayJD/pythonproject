
def reverse_int(x):
    if x<0:
        x1=str(x)[1:]
        reverse_int=-int(x1[::-1])
    else:
        reverse_int=str(x)[::-1]
    return reverse_int
x=-123
print(reverse_int(x))


'''
n=123
str1=str(123)
reverse_str=str1[::-1]
print(reverse_str)
reverse_int=int(reverse_str)
print(reverse_int)

'''