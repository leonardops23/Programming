"""
Check for Palindrome: Write a function that 
checks if a word is a palindrome.
"""

text = "Anita lava la tina"

def is_polindrome(s: str) -> bool:
    text = s.replace(' ', '').lower()
    return text == text[::-1]

print(is_polindrome(text))
