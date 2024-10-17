"""
Write a algothim that count the number of vowels in a given a string.
"""

text = "Hello there"

def num_vowels(text: str) -> int:
    count_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in text:
        i.lower()
        for j in vowels:
            if i == j:
                count_vowels+=1
    
    return count_vowels

print(num_vowels("Hello there")) # 4
print(num_vowels("This is my text")) # 3
