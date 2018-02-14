#!/usr/bin/env python3

def displayDict(test_dict):
    """
    Will print out the keys and values associated with the
    dictionary
    :param test_dict: the dictionary we want to print
    """
    for key,value in test_dict.items():
        print(key + ":" + str(value))
    print()

def deleteValue(test_dict):
    del test_dict["cake"]

def displayKeys(test_dict):
    """
    Will display the keys in the dictionary
    :param test_dict: the dictionary we are accessing
    """
    for key in test_dict:
        print(key)
    print()

def displayValues(test_dict):
    """
    Displays the values in the dictionary
    :param test_dict: the dictionary we are accessing
    """
    for key in test_dict:
        print(test_dict[key])
    print()

def addValue(test_dict, new_key = None, new_value = None):
    """
    Adding a new key/value to the dictionary
    :param test_dict:
    :param new_key: the key we are adding
    :param new_value: the value we are adding
    """
    if new_key == None:
        return
    else:
        test_dict[new_key] = new_value

def keyExists(test_dict, key = None):
    """
    Returns boolean stating whether or not a key is in the
    dictionary
    :param test_dict: the dictionary we are accessing
    :param key: the key we are searching for in the dictionary
    :return: a boolean, True if key does exist, False otherwise
    """
    return(key in test_dict)

def valueExists(test_dict, value = None):
    """
    Returns boolean stating whether or not a value is in the
    dictionary
    :param test_dict: the dictionary we are accessing
    :param value: the value we are searching for in the dictionary
    :return: a boolean, True if value does exist, False otherwise
    """
    return (value in test_dict.values())

def countT(test_dict):
    t_dict = {}
    t_count = None
    for key,value in test_dict.items():
        t_count = 0
        t_count = value.lower().count('t')
        t_dict[key] = t_count
    return t_dict

def createSet(set1 = None, set2 = None, set3 = None):
    for i in range(0,21):
        if i % 2 == 0:
            set1.update([i])
        if i % 3 == 0:
            set2.update([i])
        if i % 4 == 0:
            set3.update([i])

def displaySet(test_set):
    print(test_set)

def testSubset(test_set1, test_set2):
    return(test_set1.issubset(test_set2))

def addLetters(test_set):
    test_set.update(['p','y','t','h','o','n'])

def unionSets(test_set1, test_set2):
    new_set = test_set1.union(test_set2)
    return new_set

def intersectSets(test_set1, test_set2):
    new_set = test_set1.intersection(test_set2)
    return new_set

print("DICTIONARY 1:")

new_dict = {"name": "Chris", "city":"Seattle", "cake":"Chocolate"}
displayDict(new_dict)
deleteValue(new_dict)
displayDict(new_dict)
displayKeys(new_dict)
displayValues(new_dict)
addValue(new_dict, "fruit", "mango")
displayDict(new_dict)
key_exist = keyExists(new_dict, "cake")
print(key_exist)
value_exist = valueExists(new_dict, "mango")
print(value_exist)

print("DICTIONARY 2: ")
new_t_dict = countT(new_dict)
displayDict(new_t_dict)

print("SETS:")
s2 = set()
s3 = set()
s4 = set()
createSet(s2,s3,s4)
displaySet(s2)
displaySet(s3)
displaySet(s4)
print(testSubset(s3, s2))
print(testSubset(s4, s2))
print()
print("SETS 2:")
python_set = set()
addLetters(python_set)
displaySet(python_set)
python_set.add('i')
displaySet(python_set)
fset = frozenset(('m','a','r','a','t','h','o','n'))
uniSet = unionSets(python_set, fset)
displaySet(uniSet)
intSet = intersectSets(python_set, fset)
displaySet(intSet)

donors = {"Navdeep": [1000], "Nick": [5, 2], "Henry": [100],
          "Lorenzo": [1000], "Torin": [200.5]}
print(donors["Nick"][1])
for donor, metrics in donors.items():
    print("{:<15}\t\t\t$ {:<20} {:<20} $ {:<20}".format(donor, metrics[0], metrics[1], metrics[2]))