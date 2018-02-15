#!/usr/bin/env python3

"""
Week2 Fibonacci Excercise
Created by : Carol Farris
Goal: create a function labeled Fibonacci that returns teh nth value in the fibonacci series.
"""


def fibonacci (n):
    """function creates fibonacci values and prints the nth value in series"""	
    count = 0 
    previousNumb = 0
    currentNumb = 1
    if  n < 0:
        return None
    elif  n == 0:
        return 0
    elif  n ==1:
        return 1
    else:
        for i in range (0,n+1):  
            if i == 0:
                count = 0
            if i ==1:
                count = 1
                currentNumb = 1
                previousNumb = 0
            if i >1:
                count =  previousNumb + currentNumb
                previousNumb= currentNumb
                currentNumb = count

    return(count)
  

n = 20
def lucas (n):
    """function creates lucas values and prints the nth value in series"""		 
    count = 0 
    if  n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:    
        for i in range (0, n+1): # represents the range they pass through
            if  i == 1:    
                currentNumb = 1 
                count = 1
            if  i == 0: 
                previousNumb = 2 
                count = 2
            if  i > 1:
                count =previousNumb + currentNumb
                previousNumb= currentNumb
                currentNumb = count
   
    return(count)


n = 20
def sum_series(n, previousNumb = 0, currentNumb = 1): #set default to fibonacci
    """function creates n = (n-2) + (n-1) series with user specified inputs (or default fibonacci) and prints the nth value in series"""
    count = 0 
    currentNumb = currentNumb
    previousNumb = previousNumb
    if  n < 0:
        return None
    elif  n == 0:
        return previousNumb
    elif  n ==1:
        return currentNumb
    else:
        for i in range (0,n+1): 
            if i == 0: 
                count = previousNumb     
            if i == 1:    
                count = currentNumb 
            if i > 1:
                count =previousNumb + currentNumb
                previousNumb= currentNumb
                currentNumb = count

    return(count)


if __name__ == "__main__": 
    """test functions using assert methods. Used answer key to help set up assert statements correctly"""
    
    assert fibonacci(-1) is None
    assert fibonacci(-44) is None

    assert fibonacci(0)== 0
    assert fibonacci(1)== 1
    assert fibonacci(2)== 1 
    assert fibonacci(3)== 2
    assert fibonacci(4)== 3
    assert fibonacci(5)== 5
    assert fibonacci(6)== 8 
    assert fibonacci(7)== 13

    assert lucas(-1) is None
    assert lucas(-44) is None
    
    tests = [(0,2),
             (1,1),
             (2,3),
             (3,4),
             (4,7),
             (5,11),
             (6,18),
             (7,29),
             ]
    for input, output in tests:
        assert lucas(input) == output 

    # test if sum_series matched Fibonacci
    for n in range(0, 10):
        assert sum_series(n) == fibonacci(n)        

    # test if sum_series matched lucas
    for n in range(0, 10):
        assert sum_series(n, 2, 1) == lucas(n)

    print("tests passed!")

  