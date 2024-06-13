def reverse_int(x):
    if x<0:
        x1=str(x)[1:]
        reverse_int=-int(x1)[::-1]

    else:
        reverse_int=str(x)[::-1]
    return reverse_int




i=123
print(reverse_int(i))