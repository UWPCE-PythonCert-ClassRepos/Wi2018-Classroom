#!/usr/bin/env python3

"""
The module should provide at least one function called rot13 that takes any amount of text and returns that same text encrypted by ROT13.
This function should preserve whitespace, punctuation and capitalization.
Your module should include an if __name__ == '__main__': block with tests (asserts) that demonstrate that your rot13 function and any helper functions you add work properly.
"""

def rot13(my_text):
    my_list = list()
    is_number = False    
    for letter in my_text:
        if str(letter).isnumeric():	
            my_list.append(chr(letter))
            is_number = True
        else:
            my_list.append(ord(letter))	
    if is_number:
        return ''.join(my_list)       	
    return my_list
	

test_list = "Zntargvp sebz bhgfvqr arne pbeare"	
if __name__ == '__main__':
    assert rot13(rot13(test_list)) == test_list
	
