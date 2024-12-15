"""
Create a list of all even numbers between 1 and 
20 using a list comprehension
"""

def even_numbers() -> list:
    return [i for i in range(1, 21) if i % 2 == 0]

x = even_numbers()
print(x)
