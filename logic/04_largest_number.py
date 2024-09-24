"""
Develop an algorithm to find the largest of three numbers
"""

def largest_number(n1: int, n2: int, n3: int):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    if n3 > n1 and n3 > n2:
        return n3
    
result = largest_number(344, 65, 400)

print(result)
