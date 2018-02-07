# Programming in python B Winter 2018
# February 5, 2017
# list Lab #4
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


#!/usr/bin/env python3

# Create a list  with Apples, Pears, Oranges, and Peaches. Print the list.
print("List of fruit. Then revers the letters of each fruit. Compare lists. ")
fruits4 = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits4)

# Make a copy of the list.
fruits4_copy = fruits4[:]

# Reverse the letters in each fruit in the list copy. Print list.


def reverse(f):
    """This will reverse the fruit list"""
    for fruit in fruits4_copy:
        return fruit[::-1]


print(reverse(fruits4_copy))
