#!/usr/bin/env python3

"""
========
Series 1:    
========
"""

"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”."""
mylist = ["Apples", "Pears", "Oranges", "Peaches"]

"""Display the list """
print(mylist)

"""Ask the user for another fruit and add it to the end of the list."""
fruit = input("Please enter a fruit name to add to the list:  ")
mylist.append(fruit)

"""Display the list """
print(mylist)

"""
Ask the user for a number and display the number back to the user and the fruit corresponding 
to that number (on a 1-is-first basis).  Remember that Python uses zero-based indexing, so you 
will need to correct.
"""

num = input("Please enter a number:  ")
index = int(num) - 1
choice = mylist[index]
print("number={} fruit={}".format(num, choice))

"""Add another fruit to the beginning of the list using “+” and display the list."""
myfruit = ["Mango"]
mylist = myfruit + mylist
print(mylist)

"""Add another fruit to the beginning of the list using insert() and display the list."""
mylist.insert(0, "Blue Berries")
print(mylist)

"""Display all the fruits that begin with “P”, using a for loop."""
for f in mylist:
	if f[0].upper() == 'P':
		print(f)


"""
========
Series 2: 
	Using the list created in series 1 above:
========
"""

"""Display the list """
print(mylist)

"""Remove the last fruit from the list."""
mylist.pop(len(mylist) - 1)

"""Display the list """
print(mylist)

"""Ask the user for a fruit to delete, find it and delete it"""
fruitResponse = input("Please  provide name of fruit to delete from the list:  ")
for index, f, in enumerate(mylist):
	if f.upper() == fruitResponse.upper():
		mylist.pop(index)

"""Display the list """
print(mylist)		

"""
========
Series 3:  
	Again, using the list from series 1:
		Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
		For each “no”, delete that fruit from the list.
		For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
		Display the list.
========
"""
for f in mylist:
	if f:
		myquestion = "do you like {}?  ".format(f.lower())
		myanswer = input(myquestion)
		passthrough = False
		while passthrough:
			if (myanswer.upper() == "NO" or (myanswer.upper() == "YES")):
				passthrough = True				
			else:
				myanswer = input("please answer yes, or no:  ")
		if myanswer.upper() == 'NO':
			mylist.remove(f)
		print(mylist)
	else:
		print("No items in the list")

"""
========
Series 4:
		Once more, using the list from series 1:
========
"""

"""Make a copy of the list and reverse the letters in each fruit in the copy."""
mynewlist = mylist.copy()
for index, f,  in enumerate(mynewlist):
	mynewlist[index] = f[::-1]


"""Delete the last item of the original list. Display the original list and the copy."""
mylist.pop(len(mylist) - 1)
print(mylist)
print(mynewlist)
