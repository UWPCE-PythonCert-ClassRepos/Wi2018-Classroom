#!/usr/bin/env python3

"""
Count Even Numbers

This is from CodingBat “count_evens” (http://codingbat.com/prob/p189616)

Using a list comprehension, return the number of even integers in the given list.

Note: the % “mod” operator computes the remainder, e.g. 5 % 2 is 1.

"""

def count_evens(numbers):
    return len([number for number in numbers if number % 2 == 0])

assert count_evens([2,41,23,4,556,745,65]) == 3
assert count_evens([41,23,4,-556,745,65]) == 2
assert count_evens([0]) == 1


"""
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

Working with this dict:

    Print the dict by passing it to a string format method, so that you get something like:

    “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”

"""
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print("{name} from {city} likes {cake} cake, {fruit}, {salad} salad, and {pasta}.".format(**food_prefs))

"""
Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). (the hex() function gives you the hexidecimal representation of a number as a string)

    Do the previous entirely with a dict comprehension – should be a one-liner
"""

print("\nlist comprehension to dict:", dict([(i,hex(i)) for i in range(15)]))

print("\ndict comprehension:",{i:hex(i) for i in range(15)})


"""
    Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!
"""

new_one = {key: food_prefs[key].count("a") for key in food_prefs}
print("\ncount of 'a's:",new_one)
new_one = {key: value.count("a") for key, value in food_prefs.items()}
print("\ncount of 'a' 2:",new_one)
"""
    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

            Do this with one set comprehension for each set.
"""
s2 = {i for i in range(21) if i%2==0}
s3 = {i for i in range(21) if i%3==0}
s4 = {i for i in range(21) if i%4==0}

"""
            What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
                create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.
                loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets – one set for each divisor in your sequence.
                The idea here is that when you see three (Or more!) lines of code that are almost identical, then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.
            Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)
"""

ex_credit = [{i for i in range(21) if i%j==0} for j in range(2,5)]

assert ex_credit == [s2,s3,s4]