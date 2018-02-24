'''
Program name: Mailroom
Dependencies: math functions
Program description: Store donor names and their different donations. Add new donors and donotion amounts.
Program is also writes and sends thank you notes to donors. Generate a donoation report.

Think of the architecture in reverse. What does the code block need to know first to function. Split program into parts.

The prompt handler responds to the different possible inputs from the prompt by providing functions. Define these functions before the
prompt handler.  
'''

import math

#First step. Donor List in global namespace. 
DonorList= [['Alis Smith',500,350,400],
['Neha Johnson', 1000, 3452,431,333],
['Mohan Judge', 780,570],
['Sree Richards', 1500],
['Yash Kim',800]]

def FindOrAddDonor(EnterName):
    for row in DonorList:
        if EnterName.strip().lower() == row[0].lower():
            return row
    #Creating tuple of one item (the donor name)
    DonorList.append([EnterName])
    return DonorList[-1]
    

def PrintReport():
	#1. Create and empty list
    report=[]
	#2. loop through donor_list computing values. Append new values to empty list using variables
    for row in DonorList:
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
      
	#3.Create a layout fo the report, then pass variables into the report and print 
    
    print("{:20s}|{:^20s}|{:^20s}|{:23s}|".format("Name","Number of Donations","Total $ Donated","Average Donation Amount"))
    print("_"*87)
    
    for row in report:
        print("{:20s}|{:20d}|{:^20.2f}|{:^23.2f}| ".format(*row))
    print()
    
def Letter(name):
    # The letter returned to general space
    return 'Thank you {} for your generous donation!'.format(name)

def SendThankYou():
    print("Current donor list:")
    PrintReport()
    
         
    EnterName = input("Type donor's full name, or enter new name, then press enter (q- main menu): ").strip().title()
    # a name in the donorlist
    if EnterName == "q":
        return
    # Now the donor name is stored in "EnterName"

    while True:
        StrDonation=input("Enter donor's donation (0-to quit): ").strip()
        NewDonation=float(StrDonation)
        if NewDonation == 0:
            return
        else:
            break

    # Handle EnterName and NewDonation
    donor = FindOrAddDonor(EnterName)
    # Record the donation
    # Note how the donor object can be manipulated while it is in the donors list.
    #donor is a list
    donor.append(NewDonation)

    print(Letter(donor))



def MainMenu():
#Mailroom user interface.
    print("Welcome to the charity mailroom program!")
    print("n - add donation and send thank you")
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
        prompt = MainMenu()

#Handle the prompt input response from the main menu
        if prompt=='n':
            SendThankYou()
        elif prompt=='p':
            PrintReport()
        elif prompt=='q':
            running=False
        else:
            print("Error! Selection invalid")