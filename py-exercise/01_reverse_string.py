"""
Write a function that takes a string as input
and returns the string in reverse order.
"""

text1 = "Hello Python"

def reverse_string(text: str) -> str:
    return text[::-1]

print(reverse_string(text1))
