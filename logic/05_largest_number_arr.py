"""
Write a program thar finds the second largest numbers in an array
"""

arr = [10, 5, 3, 65, 2, 1] # 10


def second_largest_number(arr: list) -> int:
    """
    1 ordenar la list
        sacando el menor tras menor
    """
    n = arr[0]
    for index, number in enumerate(n):
        if n > number:
            

print(second_largest_number(arr))
