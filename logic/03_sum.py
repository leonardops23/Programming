"""
Write a program that takes two numbers and prints
their sum
"""

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

def sum(a: int, b: int) -> int:
    return (a + b)

result = sum(number_1, number_2)

print(f"Result is: {result}")
