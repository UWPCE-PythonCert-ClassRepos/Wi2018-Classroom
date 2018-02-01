my_string_1 = "camelot"
my_string_2 = "spam"
foo = [1, 2, 3, 4, 5]

def exchange_first_last(seq):
    try:
        new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    except TypeError:
        print("Error: something went wrong.")
    return new_seq

assert exchange_first_last(my_string_1) == "tameloc"
assert exchange_first_last(my_string_2) == "mpas"
assert exchange_first_last(foo) == [5, 2, 3, 4, 1]
