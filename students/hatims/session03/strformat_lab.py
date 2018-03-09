#!/usr/bin/env python3

"""
Task One:
	Write a format string that will take the following four element tuple:
		( 2, 123.4567, 10000, 12345.67)
	and produce:
		'file_002 :   123.46, 1.00e+04, 1.23e+04'
	
	So you need to find a string formatting operator that will “pad” the number with zeros for you.
		The second element is a floating point number. You should display it with 2 decimal places shown.
		The third value is an integer, but could be any number. You should display it in scientific notation, 
		with 2 decimal places shown.
		The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
"""
mylist= ( 2, 123.4567, 10000, 12345.67)
print("file_00{}:  {:.2f}, {:.2e}, {:.2e}".format(mylist[0], mylist[1], mylist[2], mylist[3]))

"""
Task Two
	Using your results from Task One, repeat the exercise, but this time using an alternate type of format 
	string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings 
	if you’ve not used them already).
"""
print("------------------------------------------------------")
print(f"file_00{mylist[0]}:  {mylist[1]:.2f}, {mylist[2]:.2e}, {mylist[3]:.2e}")

"""
Task Three:
	Rewrite:
		"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3), to take an arbitrary number of values.
"""
print("------------------------------------------------------")
def formatter(in_tuple):
    first_text = "the {} numbers are:  ".format(len(in_tuple))
    second_text = "{:d}, " * (len(in_tuple) - 1)
    form_string = "{}{}{}".format(first_text, second_text, "{:d}")
    print(form_string.format(*in_tuple))
	
my_second_list = (1,34,50,7,8,12,20,31)
formatter(my_second_list)

"""
Task Four:
	Given a 5 element tuple:  ( 4, 30, 2017, 2, 27)
	use string formating to print:  '02 27 2017 04 30'
	
	Hint: use index numbers to specify positions.
"""
print("------------------------------------------------------")
task4_tuple = (4, 30, 2017, 2, 27)
task4_text = "{} " * (len(task4_tuple))
print(task4_text.format(*task4_tuple))

"""
Task Five:
	Given the following four element list:  ['oranges', 1.3, 'lemons', 1.1]
	Write an f-string that will display:
		The weight of an orange is 1.3 and the weight of a lemon is 1.1
		Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the 
		weight 20% higher (that is 1.2 times higher).
"""
print("------------------------------------------------------")
task5_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {task5_list[0]} is {task5_list[1]} and the weight of a {task5_list[2]} is {task5_list[3]}")

print(f"The weight of an {task5_list[0].upper()} is {task5_list[1]} and the weight of a {task5_list[2].upper()} is {task5_list[3]}")

"""
Task Six:
	Write some Python code to print a table of several rows, each with a name, an age and a cost. 
	Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
	And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple 
	in columns that are 5 characters wide? It’s easily done on one short line!
"""
print("------------------------------------------------------")
print('{:10}{:10}{:15}'.format('Name', 'Age', 'Cost($)'))
print('{:10}{:10}{:>15}'.format('Jack', '23', '$100,000.00'))
print('{:10}{:10}{:>15}'.format('Hatim', '52', '$500.00'))
print('{:10}{:10}{:>15}'.format('Jim', '19', '$200,000,000.00'))
print('{:10}{:10}{:>15}'.format('Mark', '35', '$20.00'))
print('{:10}{:10}{:>15}'.format('Thomas', '40', '$100,1789.00'))
print('{:10}{:10}{:>15}'.format('Nick', '27', '$0.00'))
