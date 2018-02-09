#!/usr/bin/env python
# Programming in python B Winter 2018
# February 5, 2017
# list Lab #4
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# Task 1 to print out data
test = (2, 123.4567, 10000, 12345.67)
output1 = 'file_00' + str(test[0]) + ':   ' + str(round(test[1], 2)) + \
    ', ' + '{:.2e}'.format(test[2]) + ', ' + '{:.2e}'.format(test[3])
print(output1)

# Task 2 Print with keywords
filename = 'file_00'
filenum = str(test[0])
roundnum = str(round(test[1], 2))
scient1 = '{:.2e}'.format(test[2])
scient2 = '{:.2e}'.format(test[3])

output2 = filename + filenum + ':   ' + roundnum + \
    ', ' + scient1 + ', ' + scient2
print(output2)

# Task 3 Print dynamically
# I could not get this to work correctly.

# Task 4
# Given a 5 element tuple:
mytuple = (4, 30, 2017, 2, 27)
# Print the output
myoutput = ('{:02d} ' * 4 + '{:d}').format(mytuple[-2], mytuple[-1],
                                           mytuple[2], mytuple[0], mytuple[1])
print(myoutput)


# Task 5
my_tuple5 = ['oranges', 1.3, 'lemons', 1.1]
tuple5_to_print = f'The weight of an {my_tuple5[0]} is {my_tuple5[1]} and the weight of a {my_tuple5[2]} is {my_tuple5[3]}'
print(tuple5_to_print)


# Make the answers all uppercase and multipy the weight by 1.2
tuple5a_to_print = f'The weight of an {my_tuple5[0].upper()} is {my_tuple5[1] * 1.2} and the weight of a {my_tuple5[2].upper()} is {my_tuple5[3] * 1.2}'
print(tuple5a_to_print)
