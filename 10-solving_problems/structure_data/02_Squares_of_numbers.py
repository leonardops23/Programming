"""
Write a list comprehension that generates a 
list of squares for numbers from 1 to 10.
"""

def square_numbers() -> list:
    return [x ** 2 for x in range(1, 11)]

x = square_numbers()
print(x)
