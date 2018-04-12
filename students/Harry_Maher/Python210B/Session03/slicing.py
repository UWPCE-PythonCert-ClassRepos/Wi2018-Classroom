#!/usr/bin/env python3
"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

    with the first and last items exchanged.
    with every other item removed.
    with the first 4 and the last 4 items removed, and then every other item in between.
    with the elements reversed (just with slicing).
    with the middle third, then last third, then the first third in the new order.

"""

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
def exchange_first_last(seq):
	"""the first and last items exchanged."""
	return seq[-1]+seq[1:-1]+seq[0]

#print(exchange_first_last(a_string))

def every_other_removed(seq):
	"""every other item removed."""
	return seq[::2]

#print(every_other_removed(a_tuple))


def keep_middle(seq):
	""" the first 4 and the last 4 items removed, and then every other item in between."""
	return seq[4:-4:2]

#print(keep_middle(a_string))

def reverse_it(seq):
	return seq[::-1]

#print(reverse_it(a_string))

def reorder(seq):
	"""with the middle third, then last third, then the first third in the new order"""
	thrd = len(seq)//3
	return seq[thrd:-thrd]+seq[-thrd:]+seq[:thrd]


print(reorder(a_string))

