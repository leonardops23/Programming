"""
Remplaza el numero y devuelve la list con el valor modificado
"""

def new_element_in_list(n: int, index: int, my_list: list) -> list:

    if index >= len(my_list):
        print("Not found")
    else:
        if my_list[index]:
            my_list[index] = n

    return my_list

print(new_element_in_list(34, 0, [43, 3, 2, 5, 1, 4]))
print(new_element_in_list(4, 5, [3, 6, 4, 5, 2, 3]))
print(new_element_in_list(455, -1, [4, 44, 2, 2, 55, 24]))
