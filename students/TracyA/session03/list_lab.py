# Programming in python B Winter 2018
# February 4, 2017
# list Lab
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom

# Series 1
# Create a list that contains Apples, Pears, Oranges and Peaches.

#!/usr/bin/env python3

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print("These are the fruits in my list: ")
print(fruits)

# External input in cmd prompt for another fruit. Append the input to the list.
newfruit = input("Please add another fruit to the list: ")
fruits.append(newfruit)
print(fruits)

# Now there's a list of fruits. Return the fruit based on the number input
# from cmd prompt 1 to n
# Pad the list make the fruit items have a non-zero index.
fruits.insert(0, '0index_pad')
print("Identify a fruit. Pick a number 1 to " + str(len(fruits) - 1))
pick_number = input(": ")

# make sure it is an integer
int_number = int(pick_number)
print(fruits[int_number])
print()

# Insert 2 fruits fruit to the front of the list.
print("Now adding Grapes to the list...")
fruits.insert(1, "Grapes")

print("The fruits in the list are" "\r")
print(fruits[1:])

# Loop through each item in the list. Print the items that begin with P.
print("Which fruits begin with 'P'?")
for fruit in fruits:
    if 'P' in fruit:
        print(fruit)
