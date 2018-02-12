#!/usr/bin/env python3


"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

#with the first and last items exchanged.
#with every other item removed.
#with the first and last 4 items removed, and every other item in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.
"""

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def swapBeginningAndEnd(s):
    """This method swaps the beginning and ending item in a string or tuple. It returns the swapped value"""
    if type(s) is str:	
        new_item = (s[-1]+ s[1:-1]+s[0])
        return(new_item)
    elif type(s) is tuple:
        new_tuple1 = s[-1 :]
        new_tuple2 = s[1:-1]
        new_tuple3 = s[:1]
        final_tuple = (new_tuple1 + new_tuple2 + new_tuple3)
        return(final_tuple)
        
 
def everyOtherItemRemoved(s):
    """This method accepts a string or a tuple and returns a new string/tubple with every other item removed"""   
    if type(s) is str:	
        new_item = (s[0:-1:2])
        return(new_item)
    elif type(s) is tuple:
        new_tuple1 = s[0:-1:2]
        return(new_tuple1)

def firstAndLast4Removed(s):
    """with the first and last 4 items removed, and every other item in between."""
    if type(s) is str:
        new_item = (s[4:-4:2])
        return(new_item)
    elif type(s) is tuple:
        new_tuple1 = s[4:-4:2]
        return(new_tuple1)

 def reverseUsingSlicing(s):
     new_tuple =       


new_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
veryLongString= "This is a very long String!"
firstAndLast4Removed(veryLongString)
firstAndLast4Removed(new_tuple)        


if __name__ == "__main__" :

    assert swapBeginningAndEnd(a_string) == "ghis is a strint"
    assert swapBeginningAndEnd(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert everyOtherItemRemoved(a_string)=="ti sasrn"
    assert everyOtherItemRemoved(a_tuple)==(2,13,5)
    assert firstAndLast4Removed(veryLongString)==" savr ogSr"
    assert firstAndLast4Removed(new_tuple)==(5,7,9) 

    print("tests passed!")