
"""
Print the square of the numbers from 1 to 10 using a for loop in a single line.

# Expected output: 1, 4, 9, 16, 25, ..., 100
"""

def square():
    return [x*x for x in range(1, 20)]

result = square()
print(result)
