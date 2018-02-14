def valsToCountTs(myDict):
    """Returns modified dict, replacing values with number of 't's"""
    for Ke, v in myDict.items():
        myDict[Ke] = str(v).lower().count('t')

    return myDict
    

def main():
    from array import array
    import numpy as np

    myDict = dict(name='Chris',city='Seattle',cake='Chocolate')

    print(myDict)

    myDict.popitem()

    print(myDict)

    myDict['fruit'] = 'Mango'

    # Print keys
    print("myDict keys:", myDict.values())
    # Print values
    print("myDict values: ", myDict.values())


    print('cake' in myDict.keys())
    print('Mango' in myDict.values())


    print(valsToCountTs(myDict))


    s2 = set(
    l2 = np.array([2]*21)
    myList = np.array(range(21))

    mathArray = l2 * 3
    
    print(mathArray)

if __name__=="__main__":
    main()
