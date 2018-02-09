def format_string(test_str):
    """
    Creates a new string that is formatted as such: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    :param test_str: the sequence we are testing over
    :return:a new string that has the elements formatted as shown above
    """
    new_str = 'file_{:03d}:\t{}, {:.2E}, {:.2E}'.format(test_str[0], round(test_str[1], 2),
                                                      test_str[2], test_str[3])
    return new_str


def format_string_2(test_str):
    """
    Creates a new string that is formatted as such: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    by using a different method than the function above
    :param test_str: the sequence we are testing over
    :return: a new string that has the elements formatted as shown above
    """
    new_str = f"file_{test_str[0]:03}:\t{round(test_str[1], 2)}, " \
                     f"{test_str[2]:.2E}, {test_str[3]:.2E}"
    return new_str

def dynamicBuild(test_str):
    """
    Given an unknown tuple length, print out how many numbers are in the tuple
    and what the numbers are
    :param test_str: the tuple we are extracting the information from
    :return:a string that states how many numbers are in the tuple and the numbers
    stored in the tuple
    """
    form_string = " {},"
    total_nums = len(test_str)
    new_str = "the {} numbers are: ".format(total_nums)
    for i in range(total_nums):
        new_str += (form_string)
    return new_str.format(*test_str).rstrip(',')


def task_4(test_str):
    """
    format a 5 element tuple as such: '02 27 2017 04 30'
    original tuple: ( 4, 30, 2017, 2, 27)
    :param test_str: the tuple we are testing over
    :return: a new string formatted as shown above
    """
    new_str = '{:02d} {:02d} {} {:02d} {:02d}'.format(test_str[3], test_str[4],
                                                      test_str[2], test_str[0],
                                                      test_str[1])
    return new_str

def fstring(test_str):
    """
    Given four element list, create a string showing the the fruit and weight
    of the fruit by using fstring formatting
    :param test_str: the list we extract the information from
    :return:a string that displays a sentence similar to the one below:
    The weight of an orange is 1.3 and the weight of a lemon is 1.1
    """
    new_str = f'The weight of an {test_str[0]} is {test_str[1]}' \
              f' and the weight of a {test_str[2]} is {test_str[3]}'
    new_str2 = f'The weight of an {test_str[0].upper()} is {test_str[1]*1.2}' \
               f' and the weight of a {test_str[2].upper()} is {test_str[3]*1.2}'
    return new_str, new_str2

def createColumns(test_str1, test_str2, test_str3):
    """
    print data stored in a sequence in formatted columns where all elements
    are properly aligned
    :param test_str1: elements to be stored in column 1
    :param test_str2: elements to be stored in column 2
    :param test_str3: elements to be stored in column 3
    :return: a string displaying the elements stored in the sequences in
    formatted columns
    """
    new_str = ""
    for index, row in enumerate(test_str1):
        new_str += "{0:<20}{1:<20}{2:<20}\n".format(row, test_str2[index], test_str3[index])
    print(new_str)



print('TASK 1:')
test_string = (2, 123.4567, 10000, 12345.67)
new_form_string = format_string(test_string)
print(new_form_string)
print()

print('TASK 2:')
new_form_string_2 = format_string_2(test_string)
print(new_form_string_2)
print()

print("TASK 3:")
task_3_tuple = (1,2,3, 100)
task_3_test = dynamicBuild(task_3_tuple)
print(task_3_test)
print()

print("TASK 4:")
five_element_tup = (4,30,2017,2,27)
new_five_element_tup = task_4(five_element_tup)
print(new_five_element_tup)
print()

print("TASK 5:")
fstring_tuple = ("oranges", 1.3, "lemons", 1.1)
fstring_test, fstring_test2 = fstring(fstring_tuple)
print(fstring_test)
print(fstring_test2)
print()

print("TASK 6:")
column_1 = ("first", "second", "third", "fourth", "fifth")
column_2 = (99, 100.10, 1, 5000000, 2.553)
column_3 = ("Navdeep", "Henry", "Nick", "Torin", "Lorenzo")
createColumns(column_1, column_2, column_3)