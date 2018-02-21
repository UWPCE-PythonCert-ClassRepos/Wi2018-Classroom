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
    pass

def PrintReport():
	#1. Create and empty list
    report=[]
	#2. loop through donor_list computing values. Append new values to empty list using variables
    for (name, amount) in report:
        donation_count=len(amount)
        total_donation=sum(amount)
        avg_amount=total/donation_count
        report.append(name,donation_count,total_donation,avg_amount)

	#Create a layout fo the report, then pass variables into the report and print 
    print("{:20s}|{:20s}|{:20s}|{:20s}".format("Name","Number of Donations","Total $ Donated","Average Donation Amount"))
    print("_"*80)
    for row in report:
        print("{:20s}|{:20s}|{:20s}|{:20s}".format(row))

def SendThankYou():
	pass

def crejhgjhj():
	pass

#Iniate the program and define as a stand alone application.
#Computer will store all of the previous functions and then use them here. 

'''
if __name__ == "__main__":
    running = True
    while running:
        prompt = main_menu_selection()

#Handle the prompt input response from the main menu
        if prompt=='n':
            SendThankYou()
        elif prompt=='r':
            PrintReport()
        elif prompt=='a':
            AddDonor()
        elif prompt=='q':
            running=False
        else:
            print("Error! Selection invalid")
'''