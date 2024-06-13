def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Find all coprime numbers within 20
def co_prime(num):
    co_prime=[]
    for i in range(1,num):
        if gcd(num,i)==1:
            co_prime.append(i)
    return co_prime
numbers=[10,15,28,20,35]
coprimes_dict={}
for num in numbers:
    coprimes_dict[num]=co_prime(num)

for num,coprimes in coprimes_dict.items():
    print(f"coprimes of {num}:{co_prime(num)}")
'''
def co_prime(num):
    co_prime=[]
    for i in range(1,num):
        if gcd(num,i)==1:
            co_prime.append(i)
    return co_prime
num=20
print(f"coprime of {num}:{co_prime(num)}")
'''
"""
coprime_pairs = []
for i in range(1, 21):
    for j in range(i+1, 21):
        if gcd(i, j) == 1:
            coprime_pairs.append((i, j))
print("Coprime numbers within 20:")
for pair in coprime_pairs:
    print(pair)
            

"""
# Print the coprime pairs
