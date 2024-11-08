
arr = [1, 2, 3, 4, 50, 6]

# comprobar cada elemento

def value_max_min(arr):
    num_max = arr[0]
    num_min = arr[0]

    for x in arr:
        if x > num_max:
            num_max = x
        if x < num_min:
            num_min = x

    print(f"Value maxime is: {num_max}")
    print(f"Value min is: {num_min}")


value_max_min(arr=arr)
