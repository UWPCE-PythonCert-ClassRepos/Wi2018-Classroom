#!/usr/bin/env python3

"""
The module should provide at least one function called rot13 that takes any amount of text and returns that same text encrypted by ROT13.
This function should preserve whitespace, punctuation and capitalization.
Your module should include an if __name__ == '__main__': block with tests (asserts) that demonstrate that your rot13 function and any helper functions you add work properly.
"""

my_list = list()

def rot13(my_text):    
    for letter in my_text:
        if str(letter).isnumeric():	
            my_list.append(chr(letter))
        else:
            my_list.append(ord(letter))	
    if not str(my_list[0]).isnumeric():
        return ''.join(my_list)       	
    return my_list
	

	
if __name__ == '__main__':
    assert rot13(rot13(my_list)) == my_list