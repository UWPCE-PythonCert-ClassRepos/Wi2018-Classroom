def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

def every_other_removed(seq):
    return seq[::2]

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other_removed(a_string) == "ti sasrn"
assert every_other_removed(a_tuple) == (2, 13, 5)


