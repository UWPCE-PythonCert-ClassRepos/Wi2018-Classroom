#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html#exercise-string-formatting

Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""

mytup = ( 2, 123.4567, 10000, 12345.67)
print("file_{0[0]:03d} : {0[1]:03.2f}, {0[2]:d}, {0[3]:5.2f}".format(mytup))

"""
Using your results from Task One, repeat the exercise, but this time using an
alternate type of format string (hint: think about alternative ways to use
.format() (keywords anyone?), and also consider f-strings if you’ve not used
them already).
"""
print(f"file_{mytup[0]:03d} : {mytup[1]:03.2f}, {mytup[2]:d}, {mytup[3]:5.2f}")

"""
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

to take an arbitrary number of values.
"""
def formatter(tup):
    fmtstr = "the {:d} numbers are: ".format(len(tup))
    for i in tup:
        fmtstr += "{:d}, "
    fmtstr = fmtstr[:-2] # trim trailing ", "

    return (fmtstr.format(*tup))

print(formatter((1, 2, 3)))
print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))

"""
Here’s a task for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names of the
fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
"""
mylist = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {mylist[0][:-1]} is {mylist[1]} and \
the weight of a {mylist[2][:-1]} is {mylist[3]}")
print(f"The weight of an {mylist[0][:-1].upper()} is {mylist[1] * 1.2} and \
the weight of a {mylist[2][:-1].upper()} is {mylist[3] * 1.2}")

"""
Suppose you’d like to display something like:

‘First $99.01 Second $88.09 ‘
One way to do that is:

'{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')
In this simple example everything aligns nicely. But that will not be the case
when the numbers to the left of the decimal place vary. Then you will need to
use alignment specifiers. Do some research on this using the links below. Then:

Write some Python code to print a table of several rows, each with a name, an
age and a cost. Make sure some of the costs are in the hundreds and thousands
to test your alignment specifiers.

And for an extra task, given a tuple with 10 consecutive numbers, can you work
how to quickly print the tuple in columns that are 5 charaters wide? It’s
easily done on one short line!
"""
print('{:<20}{:>10}\t{:<20}{:>8}'.format('First', '$99.01', 'Second', '$88.09'))
print('{:<20}{:>10}\t{:<20}{:>8}'.format('First', '$912319.01', 'Second', '$8888.09'))
print()

def print_table(tab):
    print('{:<20}{:>4}{:>15}'.format(*tab))

print_table(("peter", 100, "$79.99"))
print_table(("paul", 20, "$2579.99"))
print_table(("mary", 50, "$179.99"))

consec = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in consec: print(f"{i:>5}", end="")
print()