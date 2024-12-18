#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr: list[list]) -> int:
    left_diagonal = sum(arr[i][i] for i in range(len(arr)))
    right_diagonal = sum(arr[i][len(arr) - i -1] for i in range(len(arr)))
    return abs(left_diagonal - right_diagonal)


arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(len(arr))

for i in range(len(arr)):
    print(arr[i][len(arr) -i -1])

print(diagonalDifference(arr))