my_string_1 = "camelot"
my_string_2 = "spam"

def exchange_first_last(seq):
    new_seq = None
    try:
        new_seq = seq[-1] + seq[1:-1] + seq[0]
    except TypeError:
        print("Error: something went wrong.")
    return new_seq

assert exchange_first_last(my_string_1) == "tameloc"
assert exchange_first_last(my_string_2) == "mpas"
