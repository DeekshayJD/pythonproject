def square_of_num(n):

    for i in range(0,n-1):
        yield i**2

gen_1=square_of_num(5)

for num in gen_1:
    print(num)