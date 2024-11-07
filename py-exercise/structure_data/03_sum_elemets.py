"""
Write a function call sum_list and return sum all elements
"""

arr = [1, 2, 4, 5, 4, 21]

def sum_list(arr: list) -> int:
    total = 0
    for num in arr:
        total += num
    return total

print(sum_list(arr=arr))
