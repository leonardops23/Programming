
'''
Numbers divisible by both 3 and 5: Use a list comprehension to find 
numbers between 1 and 50 that are divisible by both 3 and 5.
'''


def divisible_by() -> list:
    x = [num for num in range(1, 51) if by_tree(num) and by_five(num)]
    return x

def by_tree(num):
    if num % 3 == 0:
        return num

def by_five(num):
    if num % 5 == 0:
        return num

x = divisible_by()
print(x)
