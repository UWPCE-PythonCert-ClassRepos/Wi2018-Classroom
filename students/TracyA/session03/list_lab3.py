#!/usr/bin/env python
# Programming in python B Winter 2018
# February 5, 2017
# list Lab #3
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# Series 3 of list lab exercises
# Create a list with Apples, Pears, Oranges, and Peaches. Print the list.
fruits3 = ["Apples", "Pears", "Oranges", "Peaches"]

for fruit in fruits3:
    rep = input('Do you like ' + fruit.lower() + ' ? ')
    while (rep.lower() != 'yes') and (rep.lower() != 'no'):
        rep = input("Please respond with 'yes' or 'no': ")
    if rep.lower() == 'no':
        del fruits3[fruit.index(fruit)]
print(fruits3)
