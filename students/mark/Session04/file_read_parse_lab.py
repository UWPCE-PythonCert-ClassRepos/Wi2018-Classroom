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


### Note: we could assume we know all the languages, however, we're instead going to assumet everyone capitalizes thier nickname.
valid_language=(
    "ansible",
    "bash",
    "c",
    "c#",
    "c++",
    "db",
    "erlang",
    "fortran",
    "java",
    "javascript",
    "lisp",
    "matlab",
    "mysql",
    "nothing",
    "perl",
    "php",
    "powershell",
    "python",
    "r",
    "rex",
    "ruby",
    "shell",
    "sql",
    "typescript",
    "vb",
    "visualbasic",
    )


students_file="./students.txt"

with open(students_file, 'r') as f:
    read_data = f.readlines()

languages={}    # dict of languages
nick_names={}   # dict or nick_names

# Delete the header on the file
read_data.reverse() # invert list order
read_data.pop()     # pop off the header
read_data.reverse() # put list back in orig order

### build the list of languages
for i in read_data:
    language_list=i.split(':')[1].strip()
    for z in language_list.split(','):
        z="".join(z.split())  #handle removal of all whitespace not just spaces
        if z in languages.keys():
            count = languages[z] + 1
            languages.update({z:count})
        else:
            languages.update({z:1})

# Output the language and build a list of nick_names if the name is not a language
print("\n\n\n[+] Your languages are: \n*second column is count of languages used")
for i in languages.keys():
    if i:
        if i[0].islower():
            print(i, " ", languages[i])
        else:
            #build an name dictionary
            if i in nick_names.keys():
                name_count = nick_names[i] + 1
                nick_names.update({i:name_count})
            else:
                nick_names.update({i:1})


print("\n\n\n[+]: Your nicknames are: ")
for x in nick_names.keys():
    print(x,nick_names[x])
