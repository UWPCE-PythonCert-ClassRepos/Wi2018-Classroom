"""Task 1:
 Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'"""

tuple_1 = ( 2, 123.4567, 10000, 12345.67)

file_data = 'file_{:0>3} :      {:.2f}, {:.2e}, {:.2e}'.format(*tuple_1)

print(file_data)


"""Task2, Do the same thing a different way"""


print(f'file_{tuple_1[0]:0{3}} :      {tuple_1[1]:.2f}, {tuple_1[2]:.2e},{tuple_1[3]: .2e}')


"""Task 3:
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.
Hint: You can pass in a tuple of values to a function with a *:"""

def formatter(in_tuple):
    t_length = len(in_tuple)
    form_string = f"the {t_length} numbers are: "
    for a_number in in_tuple:
        form_string += f'{a_number}, '
    form_string = form_string[0:-2]
    return form_string.format(in_tuple)

assert(formatter((2,3,5,7,9)) == 'the 5 numbers are: 2, 3, 5, 7, 9')
assert(formatter((2,3,5)) == 'the 3 numbers are: 2, 3, 5')

"""Task 4 
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
"""

the_tuple = (4, 30, 2017, 2, 27)

the_string = f'{the_tuple[3]:0{2}} {the_tuple[-1]} {the_tuple[2]} {the_tuple[0]:0{2}} {the_tuple[1]}'
print(the_string)

"""Here’s a task 5 for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names 
of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
That's shady. """

the_list = ['oranges', 1.3, 'lemons', 1.1]
the_string = ''

the_string = f'The weight of an {the_list[0][:-1]} is {the_list[1]} and the weight of {the_list[2][:-1]} is' \
             f' {the_list[3]}'

print(the_string)

the_string = f'The weight of an {the_list[0][:-1].upper()} is {the_list[1]*1.2} and the weight of'\
    f' {the_list[2][:-1].upper()} is {the_list[3]*1.2}'

print(the_string)

"""6th Task
Write some Python code to print a table of several rows, each with a name, 
an age and a cost. Make sure some of the costs are in the hundreds and thousands 
to test your alignment specifiers.

And for an extra task, given a tuple with 10 consecutive numbers, can you work how 
to quickly print the tuple in columns that are 5 charaters wide? 
It’s easily done on one short line!
"""

table_1 = '{:<20}{:<10}\n{:<20}{:<8}'.format('First', '$9999.01', 'Second-est', '$88.09')

print(table_1)

the_tuple = (1,2,3,4,5,6,7,8,9,20)

print(('{:<5}'.format(*the_tuple))*10)
# I tried!

