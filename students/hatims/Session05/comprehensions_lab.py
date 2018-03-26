#!/usr/bin/env python


food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
	
"""Print the dict by passing it to a string format method, so that you get something like:  Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta"""	
def print_dict(mystring):
    my_values = [val for val in mystring.values()]
    my_keys = [k for k in mystring.keys()]
    print(f"{my_values[0]} is from {my_values[1]}, and he likes {my_values[2]} {my_keys[2]}, {my_values[3]} {my_keys[3]}, {my_values[4]} {my_keys[4]}, and {my_values[5]} {my_keys[5]}")

	
print_dict(food_prefs)

"""Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). 
(the hex() function gives you the hexidecimal representation of a number as a string)
"""
def number_dictionary_list_comprehension():
    print("\n\n", [{k:hex(k)} for k in range(15)])
	
number_dictionary_list_comprehension()

"""Do the previous entirely with a dict comprehension – should be a one-liner"""
def number_dictionary_dict_comprehension():
    print("\n\n",{k: hex(k) for k in range(15)})
	
number_dictionary_dict_comprehension()

"""
Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. 
You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!
"""
def make_dict():
    print("\n\n", {k: val.count('a') for k, val in food_prefs.items()})

make_dict()

"""
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Do this with one set comprehension for each set.
"""
def print_3_sets():
    my_range=20
    print("\n\nS2:  ", {num for num in range(my_range) if (num % 2) == 0})
    print("S3:  ", {num for num in range(my_range) if (num % 3) == 0})
    print("S4:  ", {num for num in range(my_range) if (num % 4) == 0})	
	
print_3_sets()

"""
What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.
loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets – one set for each divisor in your sequence.
The idea here is that when you see three (Or more!) lines of code that are almost identical, then you you want to find a way to generalize that code 
and have it act on a set of inputs, so the actual code is only written once.
"""
myset = [2,3,4,5,6]
def print_variable_sets(myset):
    my_range=20
    for divisor in myset:
        print("\nS{}:  ".format(divisor), {num for num in range(my_range) if (num % divisor) == 0})

print_variable_sets(myset)