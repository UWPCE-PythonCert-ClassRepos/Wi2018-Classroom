def exchange(test_seq):
    """
    This function will reverse the first and last element in the sequence
    :param test_seq: the sequence we are reversing
    :return: a new sequence with the first and last element switched
    """
    if len(test_seq) <= 1:
        return test_seq
    else:
        new_seq = None
        new_first = test_seq[-1:]
        new_last = test_seq[:1]
        middle = test_seq[1:len(test_seq) - 1]
        new_seq = new_first + middle + new_last
        return new_seq

def remove_every_other(test_seq):
    """
    Removes every other element in the sequence
    :param test_seq: the sequence we are testing on
    :return: a new sequence with every other element removed
    """
    new_seq = test_seq[0:len(test_seq):2]
    return new_seq

def first_last_4(test_seq):
    """
    Removes first and last 4 elements from a sequence and every
    other item in the middle
    :param test_seq: the sequence we are testing on
    :return: a new sequence with the first and last 4 elements removed
    and every other element in the middle
    """
    new_seq = None
    if len(test_seq) <= 8:
        return new_seq
    else:
        new_seq = test_seq[4:len(test_seq) - 5:2]
        return new_seq

def reverse_elements(test_seq):
    """
    Reverses all elements in the original sequence
    :param test_seq: the sequence we are testing on
    :return: a new sequence that reverses the order of the test
    sequence
    """
    new_seq = test_seq[-1::-1]
    return new_seq

def thirds(test_seq):
    """
    The middle third, last third and first third will all be in a new order
    :param test_seq: the sequenc we are testing on
    :return:a new sequence where each 1/3rd section has a new order
    """
    new_seq = None
    if len(test_seq) == 0:
        return test_seq
    elif len(test_seq) <= 3:
        new_seq = test_seq[-1:]
        return new_seq
    else:
        thirdSections = len(test_seq)//3
        print(thirdSections)
        first_third = test_seq[0:thirdSections]
        middle_third = test_seq[thirdSections:(thirdSections + thirdSections)]
        end_third = test_seq[(thirdSections + thirdSections):len(test_seq)]
        new_seq = first_third[-1::-1] + middle_third[-1::-1] + end_third[-1::-1]
        return new_seq

a_tuple = (2, 54, 13, 12, 5, 32)
a_string = "this is a string"

xchange_string = exchange(a_string)
xchange_tuple = exchange(a_tuple)
print(xchange_string)
print(xchange_tuple)
print()

every_other_string = remove_every_other(a_string)
every_other_tuple = remove_every_other(a_tuple)
print(every_other_string)
print(every_other_tuple)
print()

reverse_string = reverse_elements(a_string)
reverse_tuple = reverse_elements(a_tuple)
print(reverse_string)
print(reverse_tuple)
print()

larger_tuple = (2, 54, 13, 12, 5, 32, 11, 9, 10, 100)
larger_string = "this is a larger string to deal with"

fourstring = first_last_4(larger_string)
fourtuple = first_last_4(larger_tuple)
print(fourstring)
print(fourtuple)
print()

a_tuple_third = (2, 54, 13, 12, 5, 32, 0)
thirds_tuple = thirds(a_tuple)
thirds_string = thirds(a_string)
print(thirds_tuple)
print(thirds_string)