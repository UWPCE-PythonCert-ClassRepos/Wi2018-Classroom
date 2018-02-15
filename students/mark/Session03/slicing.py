#!/usr/bin/env python3

"""
Tasks

Write some functions that take a sequence as an argument, and return a copy of that sequence:

    - with the first and last items exchanged.
    - with every other item removed.
    - with the first 4 and the last 4 items removed, and then every other item in between.
    - with the elements reversed (just with slicing).
    - with the middle third, then last third, then the first third in the new order.

NOTE: These should work with ANY sequence – but you can use strings to test, if you like.

Your functions should look like:

def exchange_first_last(seq):
    return a_new_sequence



Tests:

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

Write a test or two like that for each of the above functions.


"""

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exFirstLastString(aString):
    """    with the first and last items exchanged."""

    if not aString:
        aString=[]

        concatString=aString[-1] + aString[1:-1] + aString[0]

        output=aString[-1], aString[1:-1], aString[0]

    return aString[-1] + aString[1:-1] + aString[0]


def exFirstLast(aString):
    """    with the first and last items exchanged."""

    if not aString:
        aString=[]
        """ notes: a slice returns a tuple / a value returns the value of the type"""

    return aString[-1:] + aString[1:-1] + aString[:1]

def everyOtherItem(aString):
    """- with every other item removed."""

    if not aString:
        aString=[]

    print(aString[:-1:2])

    return aString[:-1:2]

def first4Last4(aString):
    """- with the first 4 and the last 4 items removed, and then every other item in between."""

    """Work on this next"""

    if not aString:
        aString=[]

    print(aString[0:4] + aString[-4:])

    return 0

####
#### Main
####


print("a_string: ", a_string)
print("a_tuple: ", a_tuple)

for i in range(3):
    #print(exFirstLast(a_string))
    #print(exFirstLast(a_tuple))

    #print(everyOtherItem(a_string))
    #print(everyOtherItem(a_tuple))
    pass

print(first4Last4(a_string))
print(first4Last4(a_tuple))
