# Create a program that find the gratest commom divisor of two numbers

def gcd(n1: int, n2: int) -> int:
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1



print(gcd(10, 5))
