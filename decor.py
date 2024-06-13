
def decor_func2(func):
    def sum_of_cube(a,b):
        return func(a**3,b**3)
    return sum_of_cube


def decor_func(func):
    def sum_of_square(a,b):
        return func(a**2,b**2)
    return sum_of_square





@decor_func2
#decor_func2
@decor_func
def sum_value(a,b):


    return a+b
print(sum_value(2,3))