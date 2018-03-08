#!/usr/bin/env python
# Programming in python B Winter 2018
# February 11, 2017
# Dictionary Lab - Section 4
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# Dictionaries 1

ta_dictionary = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(ta_dictionary)
# Remove cake from the dictionary
ta_dictionary.pop('cake')
# Display the Dictionary
print(ta_dictionary)
# Add Fruit to Dictionary
ta_dictionary['fruit'] = 'Mango'
# Print the Dictionary
print(ta_dictionary)
# Display keys
print(ta_dictionary.keys())
# Display Values
print(ta_dictionary.items())
# Display if cake is in Dictionary
# This only works on the key
print('cake' in ta_dictionary)
# See if Mango is in dictionary. use .Values
print('Mango' in ta_dictionary.values())

# Dictionaries 2
# Make a dictionay from the earlier with t as key


nDict = {}
for k, v in ta_dictionary.items():
    nDict[k] = v.lower().count('t')
print('--------New Dict ----------\n')
print(nDict)


s2 = []
s3 = []
s4 = []
for i in range(20):
    if i % 2 == 0:
        s2.append(i)
    if i % 3 == 0:
        s3.append(i)
    if i % 4 == 0:
        s4.append(i)
s2 = set(s2)
s3 = set(s3)
s4 = set(s4)

print('--------This is S2 ----------\n')
print(s2)
print('--------This is S3 ----------\n')
print(s3)
print('--------This is S4 ----------\n')
print(s4)

# Print subset information
print('-------- S3 sub of s2---------\n')
print(s3.issubset(s2))
print('-------- S4 sub of s2---------\n')
print(s4.issubset(s2))

# Create set with python as the list
python_set = set(list('Python'))
print('--------python_set---------\n')
print(python_set)
python_set.add('i')
print('--------python_set plus i---------\n')
print(python_set)

# Create a frozenset with the letters in ‘marathon'.
frozen_set = frozenset(list('marathon'))
print(frozen_set)
# Union and intersection.
print('--------Print union of the sets---------\n')
print(frozen_set.union(python_set))
print('--------Print intersection of the sets---------\n')
print(frozen_set.intersection(python_set))
