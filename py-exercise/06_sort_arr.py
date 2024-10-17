"""
Develoment an algorithm to sort an array of interger using
bubble sort

Expected Output: For input [9, 2, 6, 3],
the output should be [2, 3, 6, 9].
"""

def sort_arr(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


print(sort_arr([9, 2, 6, 3])) # [2, 3, 6, 9]
print(sort_arr([2, 22, 64, 4])) # [2, 4, 22, 64]
print(sort_arr([100, 5, 44, 3])) # [3, 5, 44, 100]
