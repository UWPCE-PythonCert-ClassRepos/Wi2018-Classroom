# Programming in python B Winter 2018
# February 5, 2017
# list Lab #2
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


#!/usr/bin/env python3

# Series 2 of list lab exercises
# Create a list with Apples, Pears, Oranges, and Peaches. Print the list.

print("Fruits is my list: ")
fruits2 = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits2)

# Pop the last fruit from the list. Print the list.
print("Removing the last fruit from the list, the new list is: ")
fruits2.pop(-1)
print(fruits2)

# Remove fruit from list. Use cmd prompt intry for the input. Print the list.
removeit = input("Type a fruit from the list to remove: ")
fruits2.remove(removeit)
print("The new list is ")
print(fruits2)
