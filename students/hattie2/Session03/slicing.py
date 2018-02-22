#Done


def exchange_first_last(seq):
    """takes a sequence and returns sequence that swaps first and last items"""
    a_new_sequence = seq[-1:]+seq[1:-1]+seq[:1]
    return a_new_sequence

def remove_every_other(seq):
    """takes a sequence and returns a sequence after removing everyother item"""
    a_new_sequence=(seq[0:-1:2])
    return a_new_sequence

def four_gone_and_everyother(seq):
    """takes a sequence and returns a sequence with the first 4 and the last 4 items removed, and then every other item in between.
"""
    a_new_sequence= seq[4:-4:2]
    return a_new_sequence

def elements_reversed(seq):
    """Reverses elements"""
    a_new_sequence = seq[::-1]
    return a_new_sequence

def elements_swapsied(seq):
    """takes a sequence and returns that with the middle third, then last third, then the first third in the new order.
"""
    third = len(seq)//3
    a_new_sequence =seq[third:third*2]+seq[third*2:]+seq[:third]
    return a_new_sequence

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

assert four_gone_and_everyother(a_string) == " sas"
assert four_gone_and_everyother(a_tuple) == ()

assert elements_reversed(a_string) == "gnirts a si siht"
assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

assert elements_swapsied(a_string) == "is a stringthis "
assert elements_swapsied(a_tuple) == (13, 12, 5, 32, 2, 54)

