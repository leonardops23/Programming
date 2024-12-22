"""
Description: Given two strings, 
determine if they are anagrams (contain the same letters, but in
different order).
"""

def anagrama(ar1: list, ar2: list) -> bool:
    str1 = convert_str(ar1)
    str2 = convert_str(ar2)

    print(sorted(str1) == sorted(str2))

def convert_str(ar: list) -> str:
    str = ''
    for s in ar:
        str += s.lower().replace(' ', '')
    return str

anagrama(["listen"], ["silent"])
anagrama(["listen"], ["silent"])
anagrama(["triangle"], ["integral"])
anagrama(['triangle'], ["triangli"])
