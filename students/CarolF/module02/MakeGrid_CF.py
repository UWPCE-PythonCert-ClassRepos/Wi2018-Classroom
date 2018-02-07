#!usr/local/bin/python3

"""
Created by: Carol Farris  

Grid Printer Excercise for Week 2 in class work. This file contains two methods. They are called at the end. 

Method 1: Method 2 satisfies part 2 of the excercise. print_Grid takes in one (usrValue)parameter and draws a 
2x2 grid. usrValue is used as the sum of alternating  space and - lines. these are flanked by + signs. The empty rows have 
pipes flanking usrValue spaces to complete the grid.

Method 2: print_Vari_Grid accepts 2 parameters and prints a 2x2 grid each square consists of 4 pipes tall and 4 " - " long.
Method 2 satisfies part 1 and part 3 of the excercise. 

Note: This could definitely be improved upon! Submitting but hoping to go back and make this code more concise and streamined. Any feedback is greatly appreciated. 
"""

 

def print_Grid(usrValue):
    
    makeLine = ""
    makeMiddle = ""
    for j in range (2):
        makeLine = makeLine + "+"
        makeMiddle = makeMiddle+ "|"  
        for i in range (1,(usrValue+1)):
            makeMiddle = makeMiddle + " " 
            if  i % 2 != 0:
                makeLine = makeLine +" "
                #print(i, makeLine)
            elif i%2 == 0:
                makeLine = makeLine + "-"
                #print(i,makeLine)
    print(makeLine+ "+")
 
    for k in range (2):
        if usrValue %2 != 0:
            for i in range ((usrValue -1)//2):   
                print(makeMiddle+ "|")
        else: 
            for i in range (usrValue/2):
                print(makeMiddle + "|")
        print(makeLine + "+")
 
 
print_Grid(15)
print_Grid(3)
print_Grid(11)

usrValue = 9
rowsAndColumns = 3

def print_Vari_Grid(rowsAndColumns,usrValue):
    usrValue = ((usrValue*2)+1 )
    makeLine = ""
    makeMiddle = ""
    for j in range (rowsAndColumns):
        makeLine = makeLine + "+"
        makeMiddle = makeMiddle+ "|"  
        for i in range (1,(usrValue+1)):
            makeMiddle = makeMiddle + " " 
            if  i % 2 != 0:
                makeLine = makeLine +" "
                #print(i, makeLine)
            elif i%2 == 0:
                makeLine = makeLine + "-"
                #print(i,makeLine)
    print(makeLine+ "+")
 
    for k in range (rowsAndColumns):
        if usrValue %2 != 0:
            for i in range ((usrValue -1)//2):   
                print(makeMiddle+ "|")
        else: 
            for i in range (usrValue/2):
                print(makeMiddle + "|")
        print(makeLine + "+")

print_Vari_Grid(4,3)
print_Vari_Grid(5,3)
print_Vari_Grid(2,4)




