"""
Write a function that takes a list of numbers as input and returns
the sum of all the elements in the list.
"""

def sum_list(numbers: list) -> int:
    total = 0
    for i in numbers:
        total += i

    return total

x = sum_list([12, 2, 1, 3, 5])
print(x)


def sum_list1(numbers: list) -> int:
    return sum(numbers)


y = sum_list1([12, 3, 2, 1, 1])
print(y)
