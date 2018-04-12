#!/usr/bin/env python3

"""


Series 1

    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
'''
# commenting out cause this is annoying 
print(fruits)

new = input("Can you add another fruit pls? ")
fruits.append(new)

numb = int(input("Which of the fruits do you want, by number? "))-1
print("You selected the {}!".format(fruits[numb]))

fruits = ["Pineapples"] + fruits
print(fruits)
fruits.insert(0, "Guavas")
print(fruits)
for fruit in fruits:
	if fruit[0]=="P":
		print(fruit)
'''


"""
Series 2

Using the list created in series 1 above:

    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

"""

'''
# commenting out cause this is annoying 
print(fruits)
fruits.pop()
print(fruits)
del_this_fruit = input("Which fruit should we delete? ")

fruits.remove(del_this_fruit)
print(fruits)
'''

"""
Series 3
    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.
"""

# There are definitely better ways to do this, but this works for now. Commenting out cuz annoying
'''
like = ""
remove_these = []
for fruit in fruits:
	while (like != "yes") and (like != "no"):
		like = input("Do you like {}".format(fruit.lower())).lower()
	if like == "no":
		remove_these.append(fruit)
	like = ""

for remove_this in remove_these:
	if remove_this in fruits:
		fruits.remove(remove_this)

print(fruits)

'''

"""
Once more, using the list from series 1:

    Make a copy of the list and reverse the letters in each fruit in the copy.
    Delete the last item of the original list. Display the original list and the copy.
"""

copied = []

for fruit in fruits:
	copied.append(fruit[::-1])

copied.pop()

print("OG list:", fruits)
print("New list:", copied)