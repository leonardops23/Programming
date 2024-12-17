"""
Reverse strings: Use a list comprehension to 
reverse each string in a list.

Input: ["hello", "world", "Python"]
Expected Output: ['olleh', 'dlrow', 'nohtyP']
"""

def reverse_strings(arr: list[str]) -> list[str]:
    return [x[::-1] for x in arr]


x = reverse_strings(["hello", "world", "Python"])
print(x)
