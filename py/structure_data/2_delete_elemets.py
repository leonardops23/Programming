
fruit_to_delete = "banana"

def remove_fruit():
    fruits = ["apple", "banana", "cherry", "orange"]
    arr = []
    for fruit in fruits:
        if fruit_to_delete == fruit:
            continue
        else:
            arr.append(fruit)
    return arr
print(remove_fruit())
