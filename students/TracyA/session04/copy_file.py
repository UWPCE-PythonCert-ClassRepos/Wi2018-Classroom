#!/usr/bin/env python
# Programming in python B Winter 2018
# February 11, 2017
# Copy file Lab - Section 4
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# File Copy steps
# Provide a file orginial file name
source = input("Enter the source file name: ")
output = input("Enter the destination file name:")
while (source == output):
    print("Please provide unique file name:")
    output = input("Enter the destination file name:")

with open(source, 'rb') as infile, open(output, 'wb') as outfile:
    outfile.write(infile.read())
