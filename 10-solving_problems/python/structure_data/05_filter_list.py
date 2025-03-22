"""
Filter strings: Given a list of mixed data types, use a list 
comprehension to extract only the strings.

Input: [1, 'hello', 3.5, 'world', 42, 'Python']
Expected Output: ['hello', 'world', 'Python']
"""

def filter_list(arr: list) -> list:
    """
    arr1 = []
    for s in arr:
        if isinstance(s, int):
            arr1.append(s)

    return arr1
    """
    return [i for i in arr if isinstance(i, str)]


x = [1, 'hello', 3.5, 'world', 42, 'Python']
print(filter_list(x))
