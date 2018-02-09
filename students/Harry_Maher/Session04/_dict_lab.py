#!/usr/bin/env python3

"""

    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
        Display the dictionary keys.
        Display the dictionary values.
        Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
        Display whether or not “Mango” is a value in the dictionary (i.e. True).

"""


my_d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}

print(my_d)

del my_d["cake"]

print(my_d)

my_d["fruit"] = "Mango"

print(my_d)

for key in my_d:
    print(key)
for val in my_d.values():
    print(val)

print("cake" in my_d) #.keys() isn't necessary here
print("Mango" in my_d.values())


"""
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
"""
my_d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
new_d = {}
for key, val in my_d.items():
    new_d[key]=0
    for letter in val:
        if letter.lower() == "t":
            new_d[key]+=1
#print(new_d)


#Alternatively, can use the .count() method:

new_d = {}
for key, val in my_d.items():
    new_d[key]= val.lower().count("t")
#print(new_d)



"""
Sets

    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).

"""
s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if (i%2==0):
        s2.add(i)
    if i%3==0:
        s3.add(i)
    if i%4==0:
        s4.add(i)

print(s2)
print(s3)
print(s4)


print(s3.issubset(s2))
print(s4.issubset(s2))

"""
Sets 2

    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’.
    display the union and intersection of the two sets.
"""

s = set("Python")
s.add("i")
print(s)
fs = frozenset("marathon")

print(s.union(fs))
print(s.intersection(fs))
