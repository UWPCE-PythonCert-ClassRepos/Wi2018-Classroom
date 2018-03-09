#!/usr/bin/env python

"""
===============
Dictionaries 1
===============
"""
"""
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
"""
my_dictonary = {"name": "Chris", "City": "Seattle", "Cake":"Chocolate"}

"""
Display the dictionary.
"""
print(my_dictonary.items())

"""
Delete the entry for “cake”.
"""
my_dictonary.pop('City')

"""
Display the dictionary.
"""
print(my_dictonary.items())

"""
Add an entry for “fruit” with “Mango” and display the dictionary.
"""
my_dictonary["fruit"] = "mango"

"""
Display the dictionary keys.
"""
print(my_dictonary.keys())

"""Display the dictionary values.
"""
print(my_dictonary.values())

"""
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
"""
print("Cake is a key in the dictionary:   ", "cake" in my_dictonary)

"""
Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""
print("Mango is a value in the dictionary:   ", 'mango' in my_dictonary.values())

"""
===============
Dictionaries 2
===============

Using the dictionary from item 1: Make a dictionary using the same keys but with the number 
of ‘t’s in each value as the value (consider upper and lower case?).
"""

my_dictonary = {"name": "Chris", "City": "Seattle", "Cake":"Chocolate"}
for k, v, in my_dictonary.items():
    if v.upper().count('T'):
        my_dictonary[k] = v.upper().count('T')

print(my_dictonary.items())		

"""
===============
Sets
===============
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""
s2 = set()
s3 = set()
s4 = set()

for num in range(0,20):
    if num % 2 == 0:
        s2.update([num])
    elif num % 3 == 0:
        s3.update([num])
    elif num % 4 == 0:
        s4.update([num])
print("printing s2: ", s2)		
print("printing s3: ", s3)
print("printing s4: ", s4)	

print("S3 in subset of s2:   ", s3 in s2)
print("S4 in subset of s2:   ", s4 in s2)

"""
===============
Sets 2
===============
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets.
"""

set_python = set(['P', 'y', 't', 'h', 'o', 'n'])
set_python.update(['i'])
set_marathon = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print("The union of the set_python and set_marathon is:  ", set_python.union(set_marathon))
print("The intersection of the set_python and set_marathon is:  ", set_python.intersection(set_marathon))


