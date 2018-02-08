#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html#exercise-list-lab

Series 1

Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using "+" and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with "P", using a for loop.
"""
print("Series 1:")
fruits = [ "Apples", "Pears", "Oranges", "Peaches" ]
print(fruits)

response = input("Enter the name of another fruit > ")
# TODO Validate input is an legit string.
fruits += [ response ]
print(fruits)

response = int(input("Enter the number of a fruit > "))
while response < 0 or response > len(fruits):
    response = int(input("Invalid number, reenter > "))

print("{}: {}".format(response, fruits[response - 1]))

fruits.insert(0, "Pineapple")
print(fruits)

for fruit in fruits:
    if fruit[0] == "P": print(fruit)

fruits_series1 = fruits[:]

"""
Series 2

Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""
print("Series 2")
print(fruits)
fruits = fruits[:-1]
print(fruits)

doublefruits = fruits * 2
response = input("Enter the name of a fruit to delete > ")
while not response in fruits:
    response = input("Not found, reenter > ")
while response in doublefruits:
    doublefruits.remove(response)
print(doublefruits)


"""
Series 3

Again, using the list from series 1:

Ask the user for input displaying a line like "Do you like apples?" for each fruit in the list (making the fruit all lowercase).
For each "no", delete that fruit from the list.
For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
"""
print("Series 3")
fruits = fruits_series1[:]

for fruit in fruits:
    response = input("Do you like {}? ".format(fruit))
    while response != "no" and response != "yes":
        response = input("Do you like {} (enter \"yes\" or \"no\")? ".format(fruit))
    if response == "no": fruits.remove(fruit)
print(fruits)

"""
Series 4

Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
Next  Previous
"""
print("Series 4")
fruits = fruits_series1[:]

reversed_fruits = [ ]
for fruit in fruits:
    reversed_fruits.append(fruit[::-1])
fruits = fruits[:-1]
print(fruits)
print(reversed_fruits)
