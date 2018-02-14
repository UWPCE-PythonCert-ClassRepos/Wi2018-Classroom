#!user/local/bin/python3

"""
Created by: Carol Farris
This is a lesson 1 excercise on creating 4 different kinds of exceptions--SyntaxError, TypeError, AttributeError and NameError.
Each function below creates a different exception. 
Tracked in Git just to practice Git workflow."""


#this function will break by Incorrect syntax notation for print().
#Error at 9, should be print(myString)
"""def breakBySyntaxError():
	myString = "Hello world"
	print myString #error here, as I need perenthesis around the print statement.
"""

#This function will break by TypeError of variables.
#It is unsupported operand types--I have a number first and a string following. 
#it thinks I want to evaluate as a math expression.
def breakByTypeError():
	myNumber = 5
	myString = "Hello again, world"
	print (myNumber + myString) #error here, as it is ambiguous whether I want to concatenate the string or evaluate a math expression.

def breakByAttributeError():
    myString = "Hello, dog, its me, Margret"
    print(myString.camelcase()) # error here, as there is no attribute called .camelcase()

def breakByNameError():
	print(myAbsentString) #error here, myAbsentString has not been defined.


def main():
	#breakBySyntaxError not included as it will break by uncommenting out function.
	#breakByTypeError()
	#breakByAttributeError()
	#breakByNameError()
	print("hello world")

main()	
	