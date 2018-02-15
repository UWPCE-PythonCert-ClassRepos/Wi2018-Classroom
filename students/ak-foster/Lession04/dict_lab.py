#!/usr/bin/env python3
import os

# Activity 1: Dictionaries 1


def activity1():
    """Return results for Activity 1"""
    dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(dict)

    del dict['cake']
    print(dict)

    dict['fruit'] = 'Mango'
    print(dict)

    print(dict.keys())
    print(dict.values())
    print('cake' in dict)
    print(('Mango' in dict.values()))

    # Activity 1: Dictionaries 2
    nDict = {}
    for k, v in dict.items():
        nDict[k] = v.lower().count('t')
    print(nDict)

    # Activity 1: Sets 1
    s2 = []
    s3 = []
    s4 = []
    for i in range(20):
        if i % 2 == 0:
            s2.append(i)
        if i % 3 == 0:
            s3.append(i)
        if i % 4 == 0:
            s4.append(i)

    s2 = set(s2)
    s3 = set(s3)
    s4 = set(s4)

    print(s2, s3, s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

    # Activity 1: Sets 2
    nS = set(list('Python'))
    nS.add('i')
    fS = frozenset(list('marathon'))
    print(fS.union(nS))

# Activity 2: File Lab


def list_files():
    """Print the full path for all files in the current directory, one per line."""
    fp = os.getcwd()
    for file in os.listdir():
        print(f"{fp}/{file}")


def copy_files(filename):
    """Copy a file from a source, to a destination (without using shutil, or the OS copy command)."""
    with open(filename, 'rb') as source_file:
        with open('copy-'+ filename, 'wb') as destination_file:
            destination_file.write(source_file.read())
    print(f"A copy of {filename} has been created in the current directory.")
    return filename == destination_file

# Tests functions above, returns Error if something goes wrong -- how do I test file copying and file paths?
# assert copy_files('test.txt') == True
