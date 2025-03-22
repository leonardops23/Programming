'''
Write a list comprenhension to create a list of the lengths of each word
in given a list
'''

def length_words(arr: list) -> list:
    # return [len(x) for x in arr]
    return [sum(1 for _ in word) for word in arr]

x = length_words(["Python", "is", "fun"])
print(x)

