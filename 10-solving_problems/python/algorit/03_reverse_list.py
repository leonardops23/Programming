'''
Given the head of a singly linked list, reverse the list and return the reversed list.

Example:
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

'''

def reverse_list1(arr: list) -> list[int]:
    new_list = []
    for i in arr:
        new_list.insert(0, i)
    return new_list

def reverse_list(arr: list[int]) -> list[int]:
    return arr[::-1]

if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4, 5]))

