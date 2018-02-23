'''
Program name: Mailroom
Dependencies: math functions
Program description: Store donor names and their different donations. Add new donors and donotion amounts.
Program is also writes and sends thank you notes to donors. Generate a donoation report.

Think of the architecture in reverse. What does the code block need to know first to function. Split program into parts.

The prompt handler responds to the different possible inputs from the prompt by providing functions. Define these functions before the
prompt handler.  
'''

#import packages math and dedent
import math

#First step. Donor List in global namespace. 
donor_list= [('Alis Smith',500,350,400),
('Neha Johnson', 1000, 3452,431,333),
('Mohan Judge', 780,570),
('Sree Richards', 1500),
('Yash Kim',800)]

def AddDonor():
    print("Current donor list:")
    for row in donor_list:
        print(row[0])
        print()
        '''
        print(input("Add donor y/n: "))
        if 'n':
            print("no")
        elif 'y':
            print("yes")
        else:
            print("Error!")
        '''

def PrintReport():
	#1. Create and empty list
    report=[]
	#2. loop through donor_list computing values. Append new values to empty list using variables
    for row in donor_list:
        new_row = []
        name = row[0]
        donation_count= len(row)-1
        total_donation= sum(row[1:])
        avg_amount= total_donation/donation_count
        new_row.append(name)
        new_row.append(donation_count)
        new_row.append(total_donation)
        new_row.append(avg_amount)
        report.append(new_row)
        # ***EDIT***Creates string. Instead make a multiple lists for each donor. 
      
	#3.Create a layout fo the report, then pass variables into the report and print 
    print("{:20s}|{:20s}|{:20s}|{:20s}".format("Name","Number of Donations","Total $ Donated","Average Donation Amount"))
    print("_"*80)
    
    print(report)
    for row in report:
    	#***EDIT***not working. needs to be iterable?
        print("{:20s} {:20.2f} {:20d} {:20.2f} ".format(*row))

def SendThankYou():
	pass

def main_menu_selection():
#Mailroom user interface.
    print("Welcome to the charity mailroom program!")
    print("a - add new donor and charitable gift")
    print("n - send thank you")
    print("p - print donor donation report")
    print("q - quit program")
    selection=input("Pick a menu selection: ")  
    print()
    return selection.strip()


#Iniate the program and define as a stand alone application.
#Computer will store all of the previous functions and then use them here. 


if __name__ == "__main__":
    running = True
    while running:
        prompt = main_menu_selection()

#Handle the prompt input response from the main menu
        if prompt=='n':
            SendThankYou()
        elif prompt=='p':
            PrintReport()
        elif prompt=='a':
            AddDonor()
        elif prompt=='q':
            running=False
        else:
            print("Error! Selection invalid")