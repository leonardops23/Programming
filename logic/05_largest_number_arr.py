"""
Write a program thar finds the second largest numbers in an array
"""

arr = [10, 5, 3, 65, 2, 1] # 10

def second_largest_number(arr: list) -> int:
    """--- start -------"""
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr[-2]

print(second_largest_number(arr))
