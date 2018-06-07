#!/usr/bin/python3
import sys

# Recursion Error Exercise

# Here's an exercise that finally does not involve a ZeroDivisionError! Instead, 
# we'll be investigating a RecursionError.

# For the lesson activity, you'll be required to copy and your debugger output from this recursion exercise and paste it into the activity submission text box. Before beginning this video,
# visit the lesson activity to make sure that you understand what will be required.

# Use the interactive debugger to analyze the error in our program. In a couple of sentences, describe our error in the following terms:

#     What is wrong with our logic?
#     Why doesn't the function stop calling itself?
#     What's happening to the value of 'n' as the function gets deeper and deeper into recursion?


"What is wrong with our logic?  Logic expects n to be a positive number"
"Why doesn't the function stop calling itself? The logic does not contain and else statment to return False in case n != 2"
"What's happening to the value of 'n' as the function gets deeper and deeper into recursion?  n keeps getting infinitley smaller but never reaches 0"

def my_fun(n):
    if n == 2:
        return True
    else:
        return False
    return my_fun(n/2)


if __name__ == '__main__':
    #n = int(sys.argv[1])
    n = 20
    print(my_fun(n))
