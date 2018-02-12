def exchange_first_last(seq):
	return seq[-1:] + seq[1:-1] + seq[:1]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)


def every_other(seq):
	return seq[::2]

assert every_other(a_string) == "ti sasrn"


def first_last_four_removed(seq):
	return seq[4:-4]


assert first_last_four_removed("asdfTESTasdf") == "TEST"


def reverse(seq):
	return seq[::-1]

assert reverse("asdfasdf") == "fdsafdsa"


def move_thirds(seq):
	thirdsize = len(seq) // 3
	return seq[thirdsize:] + seq[:thirdsize]


assert move_thirds("abcdefghi") == "defghiabc"