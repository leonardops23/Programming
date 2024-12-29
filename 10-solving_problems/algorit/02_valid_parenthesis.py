
"""
Given a string s containing just the characters (, ), {, }, [ and ]
determine if the input string is valid.

An input string is valid if:
Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
Example:
Input: s = "()[]{}" Output:true`

Input: s = "(]"
Output: false

"""

def valid_parentheses(s: str) -> bool:
	parentheses_map = {"(": ")","[": "]","{": "}"}
	stack = []

	for i in s:
		if i in parentheses_map:
			stack.append(i)
		elif stack and i == parentheses_map[stack[-1]]:
			stack.pop()
		else:
			return False

	return not stack		


if __name__ == "__main__":
    s1 = "()[]{}"
    print(valid_parentheses(s1))  # Output: True

    s2 = "(]"
    print(valid_parentheses(s2))  # Output: False

    s3 = "([)]"
    print(valid_parentheses(s3))  # Output: False

    s4 = "{[]}"
    print(valid_parentheses(s4))  # Output: True

    s5 = ""
    print(valid_parentheses(s5)) # Output: True

    s6 = "["
    print(valid_parentheses(s6)) # Output: False