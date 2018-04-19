#!/usr/bin/env python3


###########################################
## Dictionary and Set Lab from Week 4
## Created by: Carol Farris
## February 9, 2018
###########################################


"""
Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the same keys but with 
the number of ‘t’s in each value as the value (consider upper and lower case?). """

def makeDictioaryWithCount (my_Dict):
    new_Dict = {}
    for key in my_Dict.keys():
        new_Dict[key] = my_Dict[key].lower().count('t')
    print(new_Dict)

"""Dictionary 1
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html#exercise-dict-lab

Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True)."""

def makeAndExpandDictionary ():
    my_Dict = {'name': 'Chris','city': 'Seattle', 'cake': 'chocolate'}
    print(my_Dict)
    del my_Dict['cake']
    print(my_Dict)
    my_Dict['fruit']='Mango'
    print(my_Dict.keys())
    print(my_Dict.values())
    print('cake' in my_Dict)
    print('Mango' in my_Dict.values())
    makeDictioaryWithCount (my_Dict) #call Method to create new dictionary using parts of my_Dict
    return my_Dict

makeAndExpandDictionary()

"""
Sets
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True). """

##Below was my test stuff from iPython

def makeMultipleSets ():
    multiple2set = set()
    multiple3set = set()
    multiple4set = set()

    for x in range (21):
        if x%2 ==0:
            multiple2set.update([x])
        if x%3 ==0:
            multiple3set.update([x])
        if x%4 ==0:
            multiple4set.update([x])        

    print(multiple2set) #display the sets created above
    print(multiple3set)
    print(multiple4set)

    print("Is set3 a multiple of set 2?")
    print(multiple3set.issubset(multiple2set)) #report subsets
    print("Is set 4 a multiple of set 2?")
    print(multiple4set.issubset(multiple2set)) #report subsets


makeMultipleSets()

"""
Sets 2
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets. """

def makeFrozenSets():
     stringSet = set(['P','y','t','h','o','n'])
     stringSet.update(['i'])
     print("Set #1: " , stringSet)
     frStringSet = frozenset(['m','a','r','a','t','h','o','n'])
     print("frozen string set : ", frStringSet)
     print("union of the two: ", stringSet.union(frStringSet))
     print("intersection of the two: ", stringSet.intersection(frStringSet))

makeFrozenSets()







