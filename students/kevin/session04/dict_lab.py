def dictValuesToTCount(myDict):
    """Returns modified dict, replacing values with number of 't's"""
    for Ke, v in myDict.items():
        myDict[Ke] = str(v).lower().count('t')

    return myDict
    

def main():
    from array import array
    import numpy as np

    myDict = dict(name='Chris',city='Seattle',cake='Chocolate')

    print(myDict)

    # Delete last entry in dict
    myDict.popitem()

    print(myDict)

    # Add new entry to dict
    myDict['fruit'] = 'Mango'

    # Print keys
    print("myDict keys:", myDict.values())
    # Print values
    print("myDict values: ", myDict.values())


    print('cake' in myDict.keys())
    print('Mango' in myDict.values())

    
    # Count number of "t"s in dict values
    print(dictValuesToTCount(myDict))


    print('\nSets Time!')

    # Sets s2, s3, s4 = sets containing numbers from 0 - 20 divisible by 2, 3, and 4
    s2 = set(range(2,21,2))
    s3 = set(range(3,21,3))
    s4 = set(range(4,21,4))

    # Display sets
    print('s2:',s2,'\ns3:',s3,'\ns4:',s4)

    # Is s3 subset of s2?
    print(s3.issubset(s2))

    # Is s4 a subset of s2?
    print(s4.issubset(s2))

    # Sets Round2
    # Create set with 'Python'
    pSet = set()
    for i in 'Python': pSet.add(i)

    # Add 'i' to set
    pSet.add('i')

    # Create frozen set with 'marathon'
    mSet = set()
    for i in 'marathon': mSet.add(i)
    frozenMSet = frozenset(mSet)

    # Show union and intersection of two sets
    print('Union:', pSet.union(frozenMSet), '\nIntersection:', pSet.intersection(frozenMSet))

    
if __name__=="__main__":
    main()
