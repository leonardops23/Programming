"""
Write a program that finds the second largest
number in an array.

Expected Output: For input [10, 5, 8, 12]
the output should be 10.

"""

def largest_number(arr: list) -> int:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[1]


print(largest_number([23, 2, 4, 1, 5]))
print(largest_number([23, 2, 4, 21, 54]))
print(largest_number([23, 12, 24, 1, 45]))

