#!/usr/bin/env python3


"""
##############################################
## Week 3 Slicing lab
## Created By: Carol Farris
## Submitted: February 12, 2018
## Program modifies strings, tuples and lists using just slicing methods
## Includes swapping beginning and end values, reversing order, removing every other items, etc.
## Original slicing.py comitted with overly verbose code. This is an edited version for concision.
## Comments on how to improve greatly welcomed!!!
##############################################
"""

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [2, 54, 13, 12, 5, 32]
new_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
veryLongString= "This is a very long String!"

def swapBeginningAndEnd(s):
    """This method swaps the beginning and ending item in a string, list or tuple. It returns the swapped value"""
    swapEdges1 = s[-1 :]
    swapEdges2 = s[1:-1]
    swapEdges3 = s[:1]
    final_sequence = (swapEdges1 + swapEdges2 + swapEdges3)
    return(final_sequence)   
     
           
def everyOtherItemRemoved(s):
    """This method accepts a string or a tuple and returns a new string/tubple with every other item removed"""   
    everyOtherRM = s[0:-1:2]
    return(everyOtherRM)


def firstAndLast4Removed(s):
    """This function removes the first and last 4 items and every other item in between of provided sequence."""
    new_order = s[4:-4:2]
    return(new_order)  

def reverseOrder(s):
    """This function returns the reverse order of the provided sequence"""
    reversedInput = s[::-1]
    return reversedInput   

def thirdScramble(s): 
    """"This function returns a reorderd sequence which starts with the middle third, followed by the last third then the first third"""           
    sequenceLength = int(len(s)//3)
    if (len(s))%3 ==2: #if length/3 remainder is 2, split with first two
        first =s[:(sequenceLength+1)]
        middle=s[(sequenceLength+1):-sequenceLength]
        end = s[((2*sequenceLength)+2):] #end will have 1 less than first and middle if length%3 ==2
    else:
        first =s[:(sequenceLength)] 
        middle=s[(sequenceLength):-sequenceLength]
        end = s[(2*sequenceLength):] #end will have 1 less than first and middle if length%3==1
    return(middle+end+first)
       


if __name__ == "__main__" :
    """Test methods delcared above with expected values"""
    assert swapBeginningAndEnd(a_string) == "ghis is a strint"
    assert swapBeginningAndEnd(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert swapBeginningAndEnd(a_list)==[32, 54, 13, 12, 5, 2]
    assert everyOtherItemRemoved(a_string)=="ti sasrn"
    assert everyOtherItemRemoved(a_tuple)==(2,13,5)
    assert firstAndLast4Removed(veryLongString)==" savr ogSr"
    assert firstAndLast4Removed(new_tuple)==(5,7,9) 
    assert reverseOrder(new_tuple)==(14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert reverseOrder(veryLongString)=="!gnirtS gnol yrev a si sihT"
    assert reverseOrder(a_list)==[32, 5, 12, 13, 54, 2]
    assert thirdScramble(a_list)== [13, 12, 5, 32, 2, 54]
    assert thirdScramble(a_string)=='is a sstringthis '
    assert thirdScramble(new_tuple)==(6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5)


    print("tests passed!")