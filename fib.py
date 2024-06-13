def fibnocci():
    a,b=1,2
    while True:
        a,b=b,a+b
        yield a

fib=fibnocci()
for i in range(10):
    print(next(fib))