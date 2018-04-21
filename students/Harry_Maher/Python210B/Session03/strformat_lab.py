#!/usr/bin/env python3

"""
Three string tasks!
Task One

    Write a format string that will take the following four element tuple:

        ( 2, 123.4567, 10000, 12345.67)

        and produce:

        'file_002 :   123.46, 1.00e+04, 1.23e+04'

"""

four_element_tuple = (2, 123.4567, 10000, 12345.67)


def sorted(lst):
	return "file_{0:03d}:   {1:.2f}, {2:.2e}, {3:.2e}".format(lst[0],lst[1],lst[2],lst[3])

#print(sorted(four_element_tuple))

"""
Task three
In [20]: formatter((2,3,5))
Out[20]: 'the 3 numbers are: 2, 3, 5'

In [21]: formatter((2,3,5,7,9))
Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'
"""

def formatter(numbers):
	stra = "the {} numbers are:".format(len(numbers))
	strb = ""
	for num in numbers:
		strb+= " {},".format(num)
	return stra+strb[:-1] #Super lazy, sorry.

#print(formatter((1,2)))
#print(formatter((2,3,5,7,9)))


"""
Task Four

    Given a 5 element tuple:

        ( 4, 30, 2017, 2, 27)

        use string formating to print:

        '02 27 2017 04 30'

"""
t = ( 4, 30, 2017, 2, 27)

#print("{:02d} {} {} {:02d} {}".format(t[3],t[4],t[2],t[0],t[1]))

"""
task 5

Given the following four element list:

    ['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

    The weight of an orange is 1.3 and the weight of a lemon is 1.1

"""

fruits_and_weights = ['oranges', 1.3, 'lemons', 1.1]
#print(f"The weight of an {fruits_and_weights[0][:-1]} is {fruits_and_weights[1]} and the weight of a {fruits_and_weights[2][:-1]} is {fruits_and_weights[3]}")


"""
task 6


Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It’s easily done on one short line!


Here, this I guess:
print('{:>20}{:>10}{:>20}{:>8}'.format('First', '$9889.01', 'Second', '$88.09'))
print('{:>20}{:>10}{:>20}{:>8}'.format('First', '$999.01', 'Second', '$88.09'))
print('{:>20}{:>10}{:>20}{:>8}'.format('First', '$9889.01', 'Second', '$888.09'))
print('{:>20}{:>10}{:>20}{:>8}'.format('First', '$999.01', 'Second', '$8877.09'))

"""