
"""
Create a count_item function that receives a list and a specific value, 
and counts how many times that value appears in the list.

contar_elemento([1, 2, 3, 2, 4, 2], 2)  # Resultado: 3
"""

def count_item(arr, y) -> int:
    value = [i for i in arr if i == y]
    return len(value)

result = count_item([1, 2, 12, 1, 2, 1, 32, 2 , 1], 1)

print(result)
