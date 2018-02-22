#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html#exercise-dict-lab
"""

"""
Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who
likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""
mydict = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
print(mydict)
mydict.pop('cake')
print(mydict)
mydict['fruit'] = 'Mango'
print("Keys:")
for d in mydict.keys(): print(d)
print("Values:")
for d in mydict.values(): print(d)
'cake' in mydict
for d in mydict.values():
    if d == "Mango": print("True")
    else: print("False")

"""
Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the same keys but with the
number of ‘t’s in each value as the value (consider upper and lower case?).
"""
mydict2 = { }
for d in mydict:
    mydict2[d] = mydict[d].lower().count('t')
print(mydict2)