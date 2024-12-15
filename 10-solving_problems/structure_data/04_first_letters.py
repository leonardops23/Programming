"""
Given a list  of words, create a list of the firsts letters of
each words.
"""

def first_letters(arr: list) -> list:
    return [x[0].lower() for x in arr]


x = first_letters(['Dog', 'Lion', 'Snake', 'Cat'])
y = first_letters(['Melon', 'Lemon', 'Naranja', 'Apple'])

print(x, y)


def first_letters1(arr: list) -> list:
    for i in arr:
        print(i[0])


#first_letters1(x)

