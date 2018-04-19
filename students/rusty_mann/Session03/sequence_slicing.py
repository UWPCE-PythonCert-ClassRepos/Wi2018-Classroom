
def switch_first_last(seq):
    mid = seq[1:-1]
    new = seq[-1:] + mid + seq[:1]
    return new

assert switch_first_last("this is a string") == "ghis is a strint"
assert switch_first_last([1,2,3,4,5,6,7,8,9,0]) == [0,2,3,4,5,6,7,8,9,1]
assert switch_first_last((1,2,3,4,5,6,7,8,9,0)) == (0,2,3,4,5,6,7,8,9,1)


def every_other(seq):
    return seq[::2]

assert every_other("this is a string") == "ti sasrn"
assert every_other([1,2,3,4,5,6,7,8,9,0]) == [1,3,5,7,9]


def remove_four(seq):
    seq = seq[4:-4]
    return seq[::2]

assert remove_four("0000102030405060708090000") == "123456789"
assert remove_four([0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0,0,0]) == [1,2,3,4,5,6,7,8,9]
assert remove_four((0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0,0,0)) == (1,2,3,4,5,6,7,8,9)

def reversed(seq):
    return seq[::-1]

assert reversed("this is a string") == "gnirts a si siht"
assert reversed([1,2,3,4,5,6,7,8,9,0]) == [0,9,8,7,6,5,4,3,2,1]


def thirds(seq):
    third1 = int(len(seq)/3)
    first_third = seq[:third1]
    remainder = seq[third1:]
    third2 = int(len(remainder)/2)
    second_third = remainder[:third2]
    third_third = remainder[third2:]
    return second_third + third_third + first_third

assert thirds("123456789") == "456789123"
assert thirds([1,2,3,4,5,6,7,8,9,]) == [4,5,6,7,8,9,1,2,3]
assert thirds((1,2,3,4,5,6,7,8,9,0)) == (4,5,6,7,8,9,0,1,2,3)

