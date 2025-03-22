#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion():
    """

    """
    s = "07:05:45PM"
    s_hour, s_minute, s_rest = s[:-2].split(':')

    am_pm = s[-2:]

    hours = int(s_hour)
    minute = int(s_minute)
    second = int(s_rest)

    if am_pm.upper() == "PM" and hours != 12:
        hours += 12
    if am_pm.upper() == "AM" and hours == 12:
        hours = 0

    return "{:02d}:{:02d}:{:02d}{}".format(hours, minute, second, am_pm)

result = timeConversion()
print(result)


"""
if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
"""
