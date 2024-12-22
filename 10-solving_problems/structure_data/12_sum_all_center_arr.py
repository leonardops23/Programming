
arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

def center_sum_all(arr: list[list[int]]) -> int:
    x = 0
    for i in arr:
        r = len(arr) // 2
        x += i[r]
    return x

x = center_sum_all(arr)
print(x)
