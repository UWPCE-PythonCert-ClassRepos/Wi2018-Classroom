#!/usr/bin/env python3

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
    for i in range(1, 20):
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
    return fS.union(nS)

# Activity 2: File Lab
def activity2():
    """Return the resutls of Activity 2"""
    # TODO: Write a program which prints the full path for all files in the current directory, one per line
    # TODO: Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
    print('hello')

# Tests functions above, returns Error if something goes wrong
# assert activity1() == frozenset({'P', 'r', 'o', 'a', 'i', 't', 'n', 'm', 'h', 'y'})
