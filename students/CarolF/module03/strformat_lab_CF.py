#!/usr/bin/env Python3

#############################
##Created by: Carol Farris
##February 18, 2018
##String Formatting Lab-practice with different string formats
############################



def printTaskOne(taskOneTuple):
    """prints numeric tuple/array with the numbers in correct decimal and numeric noation"""
    partA = "file_00{}:".format(taskOne[0])
    partB = " {0:.2f},".format(taskOne[1])
    partC = "{:.2e},".format(taskOne[2])
    partD = "{:.2e}".format(taskOne[3])
    print(partA,partB,partC,partD) 

def printTaskTwo(taskOneTuple):
    """prints numberic tuple/array wiht numbers in correct decimal and numeric notation"""
    part1 = f"file_00{taskOne[0]}:"
    part2 = '{:.5},'.format((taskOne[1]))
    part3 = f"{taskOne[2]:.2e},"
    part4 = f"{taskOne[3]:.2e}"
    print(part1,part2,part3,part4)

def printTaskThree(taskThree):
    """Prints formatted string that includes each value"""
    tupleLength =  len(taskThree)
    print(("the {} numbers are: " + " {:d}, " *(tupleLength -1) + '{:d}') .format(tupleLength, *taskThree))

def printTaskFourTuple(taskFour):
    """Prints tuple values in desired order"""
    print(taskFour[-2],taskFour[-1],taskFour[-3],taskFour[0],taskFour[1])

def printTaskFive(taskFive):
    """method accepts tuple and prints in formatted string. The second string brings the tuple strings to upper case, and increases 
         the numeric values by 20%"""    
    chopLastChar = taskFive[0]
    chopLastChar2 = taskFive[2]
    print(f'The weight of an {chopLastChar[:-1]} is {taskFive[1]} and the weight of a {chopLastChar2[:-1]} is {taskFive[-1]}')
    print(f'The weight of an {chopLastChar[:-1].upper()} is {(taskFive[1]*1.2)} and the weight of a {chopLastChar2[:-1].upper()} is {(taskFive[-1]*1.2)}')
    #print(f'The weight of an {chopLastChar[:-1].upper()} is {(taskFive[1]*0.2) + (taskFive[1])} and the weight of a {chopLastChar2[:-1].upper()} is {(taskFive[-1]*.2)+ (taskFive[-1])}')

def printTaskSix(taskSix):
    """"This method accepts a tuple or list with 9 values and prints into a table. 
        This method could be improvd by not hardcoding headers, or requiring 9 values to work. """ 
    print('{:<10}'.format("Car"),'{:>5}'.format("MFG_Date"),'{:>10}'.format("Cost")) 
    print('_'*33)    
    print('{:<10}'.format(taskSix[0]),'{:>5}'.format(taskSix[1]),'{:>15}'.format(taskSix[2]))
    print('{:<10}'.format(taskSix[3]),'{:>5}'.format(taskSix[4]),'{:>15}'.format(taskSix[5]))
    print('{:<10}'.format(taskSix[6]),'{:>5}'.format(taskSix[7]),'{:>15}'.format(taskSix[8]))

def print10ConsecNumbers(tenTuple):
    """Print 10 columns each five characters wide""" 
    tupleLength = int(len(tenTuple))
    print(("{:>5}" *(tupleLength -1) + '{:>5}') .format(*tenTuple))
   
          

if __name__ == "__main__" :
    taskThree = (1,2,3,4)
    taskOne = ( 2, 123.4567, 10000, 12345.67)	
    taskFour = ( 4, 30, 2017, 2, 27)
    taskFive = ['oranges', 1.3, 'lemons', 1.1]
    taskSix=['Toyota', 1990, "$200.00", 'Camry',2011, '$50000.00', 'Pinto', 1970, '1000.00']
    tenTuple =(1,2,3,4,5,6,7,8,9,10)
    printTaskOne(taskOne)
    printTaskTwo(taskOne)
    printTaskThree(taskThree)
    printTaskFourTuple(taskFour)
    printTaskFive(taskFive)
    printTaskSix(taskSix)
    print10ConsecNumbers(tenTuple)
  

