
def mul_2(func):
    def wrapper(*args,**kwargs):
        result= func(*args,**kwargs)
        return result*2
    return wrapper

def add_one(func):
    def wrapper(*args,**kwargs):
        result= func(*args,**kwargs)
        return result+1
    return wrapper


@mul_2
@add_one
def my_function(x):
    return x

result=my_function(3)
print(result)