#!/usr/bin/env python
import pathlib
import os
"""
Paths and File Processing
"""

"""The Function will print the full path for all files in the current directory, one per line"""
def print_path_currentdir():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(os.path.abspath(f))
	
	
"""The Function copies a file from a source, to a destination """
def copy_file(source, destination):
    chunksize=1
    if source.endswith(".txt"):
        with open(source, "r") as infile:
            f = infile.read()		
            with open(destination, "w") as outfile:
                outfile.write(f)
    else:
        with open(source, "rb") as infile:
            outfile = open(destination, "wb")
            chunck = infile.read(chunksize)
            while chunck:
                chunck = infile.read(chunksize)
                outfile.write(chunck)				            
    infile.close()
    outfile.close()
				

"""
File reading and parsing
"""
languages = ['java', 'python', 'bash', 'sql', 'c', 'c++', 'lisp', 'fortran', 'perl', 'shell', 'vb', 'r', 'visualbasic', 'c#', 'powershell', 'ansible', 'erlang', 'matlab', 'ruby', 'javascript', 'typescript']
def file_read_parse(filename):
    mylist=[]	
    with open(filename, "r") as infile:
        line = infile.readline()
        while line:
            if "Nickname" not in line:
                print("Student Name:   ", line.split(":")[0])			
                mylist, lan_number = get_student_languages(line.split(":")[1])
                print("List of languages:   ", mylist)			
                print("Number of languages:   ", lan_number)				
                print("---------------------------")			
            line = infile.readline()
    infile.close()
	
def get_student_languages(student_languages_raw_list):
    student_lan_list = []
    for language in student_languages_raw_list.split(","):
        for lan_value in languages: 
            if language.strip().lower() == lan_value:
                student_lan_list.append(language.strip()) 
    return student_lan_list, len(student_lan_list)