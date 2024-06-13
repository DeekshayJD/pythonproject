def decor_func1(func):
    def sum_of_cube(x,y):
        return func(x**3, y**3)
    return sum_of_cube



def decor_func(func):
    def sum_of_square(x,y):
        return func(x**2, y**2)
    return sum_of_square

decor_func1
#decor_func
def sum(a,b):
    return a+b

print(sum(2,4))