# Return a copy of the sequence given after ordering transformation.

def split(s,x):
    """Given a sequence break into three variables defined globally."""
    first = s[:x]
    last = s[-x:]
    middle = s[x:-x]
    return first, last, middle


def first_last(s):
    """Return a copy of a given sequence with first and last items swapped."""
    first, last, middle = split(s,1)
    ls = last + middle + first
    return ls


def every_other(s):
    """Return a copy of a given sequence, but with every other item removed."""
    new_s = s[::2]
    return new_s


def fl4_every_other(s):
    """Return copy of a given sequence with the first and last 4 items removed, and every other item in between."""
    return every_other(s[4:-4])


def reverse(s):
    """Return copy of a given sequence in the reverse order."""
    new_s = s[::-1]
    return new_s


def sort_thirds(s):
    """Return copy of given sequence with the middle third, then last third, then the first third in the new order."""
    x = int(len(s)/3)
    first, last, middle = split(s,x)
    ls = middle + last + first
    return ls


# Test block to verify the functions above work properly, throws error if not.

a_string = "this is a string"
a_tuple = (2, 54, 13, 77, 12, 5, 32, 1, 0, 33, 45, 19, 100)
a_list = ['thing', 'another', 'example','mixed', 'with', 'numbers', 0, 1, 2]
assert first_last(a_string) == "ghis is a strint"
assert first_last(a_tuple) == (100, 54, 13, 77, 12, 5, 32, 1, 0, 33, 45, 19, 2)
assert first_last(a_list) == [2, 'another', 'example','mixed', 'with', 'numbers', 0, 1,'thing']
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 12, 32, 0, 45, 100)
assert every_other(a_list) == ['thing', 'example', 'with', 0, 2]
assert fl4_every_other(a_string) == ' sas'
assert fl4_every_other(a_tuple) == (12, 32, 0)
assert fl4_every_other(a_list) == ['with']
assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == (100, 19, 45, 33, 0, 1, 32, 5, 12, 77, 13, 54, 2)
assert reverse(a_list) == [2, 1, 0, 'numbers', 'with', 'mixed', 'example', 'another', 'thing']
assert sort_thirds(a_string) == 'is a stringthis '
assert sort_thirds(a_tuple) == (12, 5, 32, 1, 0, 33, 45, 19, 100, 2, 54, 13, 77)
assert sort_thirds(a_list) == ['mixed', 'with', 'numbers', 0, 1, 2, 'thing', 'another', 'example']
