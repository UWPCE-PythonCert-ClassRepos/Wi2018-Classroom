#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html#exercise-dict-lab

Sets
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""

s2 = set()
s3 = set()
s4 = set()

for i in range(21): # *through* twenty
    if i % 2 == 0: s2.add(i)
    if i % 3 == 0: s3.add(i)
    if i % 4 == 0: s4.add(i)

print("s2: ", s2)
print("s3: ", s3)
print("s4: ", s4)

s3.issubset(s2)
s3.issubset(s2)

"""
Sets 2
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets.
"""

myset = set(['P', 'y', 't', 'h', 'o', 'n'])
myset.add('i')
myfrozen = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print("Union: ", myset.union(myfrozen))
print("Intersection: ", myset.intersection(myfrozen))