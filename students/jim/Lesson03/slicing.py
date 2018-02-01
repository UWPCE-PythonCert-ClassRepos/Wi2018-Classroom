my_string_1 = "camelot"
my_string_2 = "spam"
foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
city_1 = "seattlewashington"
city_2 = "philadelphiapennsylvania"

def exchange_first_last(seq):
    try:
        new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    except TypeError:
        print("Error: something went wrong.")
    return new_seq

assert exchange_first_last(my_string_1) == "tameloc"
assert exchange_first_last(my_string_2) == "mpas"
assert exchange_first_last(foo) == [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]


def remove_every_other(seq):
    new_seq = seq[::2]
    return new_seq

assert remove_every_other(my_string_1) == "cmlt"
assert remove_every_other(my_string_2) == "sa"
assert remove_every_other(foo) == [1, 3, 5, 7, 9]


def first_last_four(seq):
    new_seq = seq[4:-4][::2]
    return new_seq

assert first_last_four(city_1) == "teahn"
assert first_last_four(city_2) == "aepipnsl"
