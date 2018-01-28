a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = ['thing', 'another', 'example','mixed', 'with', 'numbers', 0, 1, 2]


def first_last(s):
    last = s[-1]
    first = s[0]
    middle = s[1:-1]

    if type(s) == str:
        new_s = last + middle + first
        return new_s
    elif type(s) == tuple:
        ls = list(s)
        ls[0] = last
        ls[-1] = first
        return tuple(ls)
    else:
        ls = s
        ls[0] = last
        ls[-1] = first
        return ls

assert first_last(a_string) == "ghis is a strint"
assert first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert first_last(a_list) == [2, 'another', 'example','mixed', 'with', 'numbers', 0, 1,'thing']