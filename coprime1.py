def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(x, y):
    """
    Check if two numbers are coprime.
    """
    return gcd(x, y) == 1

# Test the function
if __name__ == '__main__':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if are_coprime(num1, num2):
        print(f"{num1} and {num2} are coprime.")
    else:
        print(f"{num1} and {num2} are not coprime.")
