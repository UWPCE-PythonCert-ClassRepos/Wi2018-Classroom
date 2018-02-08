#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html#exercise-slicing

Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.
"""
debug = False

def exchange_first_last(seq):
    """ return a copy of sequence with the first and last items exchanged"""
    newseq = seq[-1:] # this doesn't work: newseq = seq[-1] -- that's an atom not a sequence
    newseq += seq[1:-1]
    newseq += seq[0:1]
    if debug: print(newseq)
    return newseq

def remove_every_other(seq):
    """ return a copy of sequence with every other item removed"""
    if debug: print(seq[::2])
    return seq[::2]

def remove_four_and_skip(seq):
    """ return a copy of sequence with the first 4 and the last 4 items removed, and then every other item in between """
    if debug: print(seq[4:-4:2])
    return seq[4:-4:2]

def reverse(seq):
    """ return a copy of sequence with the elements reversed (just with slicing) """
    if debug: print(seq[::-1])
    return seq[::-1]

def rotate_thirds(seq):
    """ return a copy of sequence with the middle third, then last third, then the first third in the new order """
    third = len(seq) // 3 # TODO: How does this work with len(seq) % 3 != 0?
    if debug: print(seq[third:-third] + seq[-third:] + seq[:third])
    return seq[third:-third] + seq[-third:] + seq[:third]

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

assert remove_four_and_skip(a_string) == " sas"
assert remove_four_and_skip(a_tuple) == ()

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

assert rotate_thirds(a_string) == "is a stringthis "
assert rotate_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
