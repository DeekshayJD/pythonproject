def fibnoci():
    a,b=1,2
    while True:
        yield a
        a,b=b,a+b


fib=fibnoci()
for i in range(10):
    print(next(fib))