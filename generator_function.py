def gen_function(a,b):
    sum=a+b
    yield sum
    #return sum*2
    yield sum*2

obj_gen=gen_function(10,20)

print(next(obj_gen))
print(next(obj_gen))














def fibnocci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib=fibnocci()
for i in range(10):
    print(next(fib),end=" ")
