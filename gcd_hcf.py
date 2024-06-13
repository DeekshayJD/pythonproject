def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    print(a,b)
    return abs(a*b)//gcd(a,b)

n1, n2 = 30, 45
result = gcd(n1, n2)
result1=lcm(n1,n2)
print(f"The GCD of {n1} and {n2} is: {result}")
print(f"The lcm of {n1} and {n2} is: {result1}")
