"""
Realizar un triangulo equilatero
"""

height = int(input("Enter the height of the triangle: "))

def triangle(height: int) -> None:
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))
        

triangle(height)
