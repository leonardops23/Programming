"""
Write a remove_duplicates function that takes
a list and returns a new list with no duplicates."""

arr = [12, 4, 2, 4, 2, 4, 2, 1, 12]

def remove_deplicates(arr):
    new_arr = []
    for x in arr:
        if x not in new_arr:
            new_arr.append(x)
    return new_arr

x = remove_deplicates(arr=arr)
print(x)
