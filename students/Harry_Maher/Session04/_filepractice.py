#!/usr/bin/env python3

"""
    Write a program which prints the full path for all files in the current directory, one per line
    Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
        Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
        This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
        Test it with both text and binary files (maybe jpeg or something of your choosing).
"""
import os

def print_all_files():
    for file in os.listdir():
        print(os.getcwd()+"/"+file) #though windows uses "\" for some reason sometimes?
 
print_all_files()


def copy_file(file,output_file):
    with open(file, 'rb') as infile, open(output_file, 'wb') as outfile:
        outfile.write(infile.read())

copy_file("copythis.txt", "output_this.txt")


"""

Write a little script that reads that students.txt, and generates a list of all the languages that have been used.

What might be the best data structure to use to keep track of bunch of values without duplication?
Extra challenge: keep track of how many students specified each language

"""

with open("students.txt") as f:
    students = f.read().splitlines()
languages = []
for student in students[1:]:
    newls = "".join(student.split(":")[1].split(" ")).split(",")
    languages += newls



l_counter = {}
final_languages = []
for l in languages:
    #instead of writing out the alphabet I could just do a l[0] != l[0].upper(). But this is more fun.
    if (len(l)>1) and (l[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"): # Apparently "nothing" is an esoteric language (ha) so removed: "and l!='nothing'" clause
        final_languages.append(l)
        #Extra challenge: keep track of how many students specified each language
        if l not in l_counter:
            l_counter[l] = 1
        else:
            l_counter[l] += 1


print(set(final_languages))
print(l_counter.items())