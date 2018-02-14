#!/usr/bin/env python3


"""
File reading and parsing

Download this text file:

students.txt

In it, you will find a list of names and what programming languages they have used in the past.
This may be similar to a list generated at the beginning of this class.

Write a little script that reads that file, and generates a list of all the languages that have been used.

What might be the best data structure to use to keep track of bunch of values without duplication?
"""

students_file="./students.txt"

with open(students_file, 'r') as f:
    read_data = f.readlines()
f.closed

languages={}

read_data.reverse() # invert list order
read_data.pop()     # pop off the header
read_data.reverse() # put list back in orig order

for i in read_data:
    print(i.split(':'))
    print(i.split(':')[1].strip())
    language_list=i.split(':')[1].strip()
    for z in language_list.split(','):
        if z in languages.keys():
            print('working on lang z:', z)
            count = languages[z] + 1
            print(count)
            languages.update({z:count})
        else:
            languages.update({z:1})


print(languages)




myTXT="txt, text: x, y, z"
