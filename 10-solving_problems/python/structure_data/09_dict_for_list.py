"""
Create a dictionary from two lists: Given two lists, use a list
comprehension to create a dictionary where the first list
contains the keys and the second 
list contains the values.

Input: keys = ["name", "age", "city"], values = ["Alice", 25, "New York"]
Expected Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
"""

def list_to_dict(arr1: list, arr2: list) -> dict:
    #return dict(zip(arr1, arr2))
    new_dict = {arr1[i]: arr2[i] for i in range(len(arr1))}
    return new_dict




x = list_to_dict(["name", "age", "city"], ["Alice", 25, "New York"])
print(x)