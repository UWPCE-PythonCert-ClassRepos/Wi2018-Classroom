##String Formatting Lab-practice with different string formats


def printtupleEle(tupleEle):
    """prints numeric tuple/array with the numbers in correct decimal and numeric noation"""
    file_sorting = "file 00,".format(tupleEle[0])
    floating_point = " {0:.2f},".format(tupleEle[1])
    integer_value = "{:.2e},".format(tupleEle[2])
    float_value = "{:.2e}".format(tupleEle[3])
    #for tupleEle in printtupleEle
    print(file_sorting,floating_point,integer_value,float_value) #print(tupleEle)
	

def printtupleEle(tupleEle):
    """prints numberic tuple using f string"""
    file_sorting = f"file 00{tupleEle[0]},"
    floating_point = '{:.5},'.format((tupleEle[1]))
    integer_value = f"{tupleEle[2]:.2e},"
    float_value = f"{tupleEle[3]:.2e}"
    print(file_sorting,floating_point,integer_value,float_value)

def printFormatter(in_tuple):
    """Prints formatted string that includes each value"""
    tupleLength =  len(in_tuple)
    print(("the {} numbers are: " + "{:d}, " *(tupleLength -1) + '{:d}') .format(tupleLength, * in_tuple))

def printTaskFourTuple(taskFour):
    """Prints tuple values in desired order"""
    print( taskFour[-2],taskFour[-1],taskFour[-3],taskFour[0],taskFour[1])
 
def printTaskFive(taskFive):
    """method accepts tuple and prints in formatted string. The second string brings the tuple strings to upper case, and increases 
         the numeric values by 20%"""    
    chopLastChar = taskFive[0]
    chopLastChar2 = taskFive[2]
    print(f'The weight of an {chopLastChar[:-1]} is {taskFive[1]} and the weight of a {chopLastChar2[:-1]} is {taskFive[-1]}')
    print(f'The weight of an {chopLastChar[:-1].upper()} is {(taskFive[1]*1.2)} and the weight of a {chopLastChar2[:-1].upper()} is {(taskFive[-1]*1.2)}')
    #print(f'The weight of an {chopLastChar[:-1].upper()} is {(taskFive[1]*0.2) + (taskFive[1])} and the weight of a {chopLastChar2[:-1].upper()} is {(taskFive[-1]*.2)+ (taskFive[-1])}')

def printAtable(table_of_rows):
    """"This method accepts a tuple or list with 9 values and prints into a table."""
    print('{:<10}'.format("Name"),'{:>5}'.format("Age"),'{:>10}'.format("Cost")) 
    print('_'*33)    
    print('{:<10}'.format(table_of_rows[0]),'{:>5}'.format(table_of_rows[1]),'{:>15}'.format(table_of_rows[2]))
    print('{:<10}'.format(table_of_rows[3]),'{:>5}'.format(table_of_rows[4]),'{:>15}'.format(table_of_rows[5]))
    print('{:<10}'.format(table_of_rows[6]),'{:>5}'.format(table_of_rows[7]),'{:>15}'.format(table_of_rows[8]))

def print10ConsecNumbers(rev_tuple):
    """Print 10 columns each five characters wide""" 
    tupleLength = int(len(rev_tuple))
    print("The Reverse of the numbers")
    print(("{:>5}" *(tupleLength -1) + '{:>5}') .format(*rev_tuple))
   
          

if __name__ == "__main__" :
    tupleEle = ( 2, 123.4567, 10000, 12345.67)
    in_tuple = (1, 2, 3)
    taskFour = ( 4, 30, 2017, 2, 27)
    taskFive = ['oranges', 1.3, 'lemons', 1.1]
    table_of_rows=['Albert', 52.00,   '$5000.00', 'Marry',28,'$8999.00', 'Leonardo', 48,   '6000.00','Jon', 52, "$100.00", 'Mario',48, '$1000.00', 'Addis', 35, '7000.00']
    rev_tuple = (1,2,3,4,5,6,7,8,9,10)
    printtupleEle(tupleEle)
    printtupleEle(tupleEle)
    printFormatter(in_tuple)
    printAtable(table_of_rows)
    print10ConsecNumbers(rev_tuple)
