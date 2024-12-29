"""
Given an array containing n distinct numbers in
the range [0, n] return missing number.
"""

def missing_number(arr: list[int]) -> int:
    arr.sort()
    if not arr:
        return None
    if len(arr) == 1:
        if len(arr) != 1:
            return 1
        else:
            return None
    if arr[0] != 1:
        return 1
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            return arr[i] -1
    return None

if __name__ == "__main__":
    print(missing_number([3, 2, 1, 5]))
