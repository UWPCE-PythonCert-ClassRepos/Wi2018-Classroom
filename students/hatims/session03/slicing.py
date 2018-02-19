def exchange_first_last(seq):
"""
This function that take a sequence as an argument, and return a copy of that sequence:
with the first and last items exchanged.
"""
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_item_removed(seq):    
"""
This function that take a sequence as an argument, and return a copy of that sequence:
with every other item removed.
"""
    return seq[0::2]


def firstAndLast_4_removed_Then_every_other(seq):      
"""
This function that take a sequence as an argument, and return a copy of that sequence:
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
"""
    return seq[4:-4:2]


def reverse(seq):      
"""
This function that take a sequence as an argument, and return a copy of that sequence:
with the elements reversed (just with slicing).
"""
    return seq[::-1]


def midthird_lastthird_firstthird(seq):
"""
This function that take a sequence as an argument, and return a copy of that sequence:
with the middle third, then last third, then the first third in the new order.
"""
    length = int(len(seq) / 3)
    first = seq[0:length]
    mid = seq[length:length*2]  
    last = seq[length*2:]    
    return mid + last + first


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 9, 24, 60, 45, 99, 200, 205, 90, 7, 300)
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (300, 54, 13, 12, 5, 32, 9, 24, 60, 45, 99, 200, 205, 90, 7, 2)
assert every_other_item_removed(a_string) == 'ti sasrn'
assert every_other_item_removed(a_tuple) == (2, 13, 5, 9, 60, 99, 205, 7)
assert firstAndLast_4_removed_Then_every_other(a_string) == ' sas'
assert firstAndLast_4_removed_Then_every_other(a_tuple) == (5, 9, 60, 99)
assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == (300, 7, 90, 205, 200, 99, 45, 60, 24, 9, 32, 5, 12, 13, 54, 2)
assert midthird_lastthird_firstthird(a_string) == 'is a stringthis '
assert midthird_lastthird_firstthird(a_tuple) == (32, 9, 24, 60, 45, 99, 200, 205, 90, 7, 300, 2, 54, 13, 12, 5)