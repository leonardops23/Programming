"""
Create a list called numbers containing the numbers 1 to 5. 
Add the number 6 to the end of the list
Change the third item in the list to 10.
"""

numbers = [1, 2, 3, 4, 5]
add_number = 6
change_number = 10

numbers.append(add_number)

# change element
numbers[2] = change_number


print(numbers)
