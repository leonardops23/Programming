
"""
Flatten a nested list: Flatten a 2D list into a 1D list 
using a list comprehension.

Input: [[1, 2, 3], [4, 5], [6, 7, 8]]
Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]

"""


def flatten_list(arr : list[int]):
    return [x for i in arr for x in i]

x = [[1, 2, 3], [4, 5], [6, 7, 8]]
print(flatten_list(x))


