"""
Prime numbers: Write a list comprehension to generate all
prime numbers between 1 and 50.

Expected Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""

def prime_numbers() -> list:
    return [x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

print(2**0.5)  

x = prime_numbers()
print(x)