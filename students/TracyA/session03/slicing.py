# Programming in python B Winter 2018
# February 4, 2017
# Slicing Lab
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in
#     the remaining sequence.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order

#!/usr/bin/env python3


def exchange_first_last(seq):
    """Exchange the first and last items in list"""
    return seq[-1:] + seq[1:len(seq) - 1] + seq[:1]


def remove_every_other(seq):
    """Remove every other word using step"""
    return seq[::2]


def remove_4_then_every_other(seq):
    """Remove first 4 and last 4 then every other"""
    return seq[4:][:-4][::2]


def reverse(seq):
    """Reverse the order of the whole list"""
    return seq[::-1]


def thirds(seq):
    """Print every third item out of order"""
    everythirds = int(round(len(seq) // 3))
    middlethirds = int(everythirds * 2)
    updatedseq = seq[everythirds:middlethirds] + seq[middlethirds:] \
        + seq[:everythirds]
    return updatedseq


mylist = (2, 7, 19, 17, 41, 601,  4, 126, 1210, 14, 31, 1, -17, 11, 1, -4)
mystring = 'this is my test string'

# Lets test the list
print("Complete List: ", mylist)
print("Switch First and Last: ", exchange_first_last(mylist))
print("Remove Every Other: ", remove_every_other(mylist))
print("Remove 4th then Every Other: ", remove_4_then_every_other(mylist))
print("Reverse order: ", reverse(mylist))
print("Thirds: ", thirds(mylist))


print("This is and string portion-----------------\n\n")

# Lets test the mystring
print("Complete List: ", mystring)
print("Switch First and Last: ", exchange_first_last(mystring))
print("Remove Every Other: ", remove_every_other(mystring))
print("Remove 4th then Every Other: ", remove_4_then_every_other(mystring))
print("Reverse order: ", reverse(mystring))
print("Thirds: ", thirds(mystring))
