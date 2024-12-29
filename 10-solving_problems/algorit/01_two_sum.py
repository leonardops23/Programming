
"""
Given an array of integers nums and an integer target, return the indices 
of the two numbers that add up to target.

Assume that each input has exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
"""

def two_sum(arr: list[int], target: int) -> list[int]:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]

    return []

if __name__ == "__main__":
    arr1 = [2, 4, 1, 15]
    arr2 = [4, 54, 4, 10, 6, 1]
    arr3 = [1, 4, 10, 1, 8]
    target1 = 8
    target2 = 5
    target3 = 8

    print(two_sum(arr1, target1))
    print(two_sum(arr2, target2))
    print(two_sum(arr3, target3))
