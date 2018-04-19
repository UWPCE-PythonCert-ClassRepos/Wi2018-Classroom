#!/usr/bin/env Python3

################################
##Created By: Carol Farris
##Date: February 13th 2018
##Goal: MailRoom Part 1 Assignment
################################


def getAction():
    """This method will prompt the user for a specific action: Send thank you, create report or quit, then route it to correct method""" 
    response = int(input("Please type a numeric selection from the following three actions: \n(1)Send a thank you \n(2)Create a Report \n(3) quit > "))
    
    if response != 1 and response != 2 and response != 3:
        print("Invalid entry. Please enter a '1', '2' or '3' ")
        response = int(input("Please type a numeric selection from the following three actions: \n(1)Send a thank you \n(2)Create a Report \n(3) quit > "))

    if response ==3:
        print("Goodbye")
        exit()   

    if response ==2:
        createReportData()	

    if response == 1: 
        findDonorName()

def findDonorName():
    """This function identifies the donor information to be used"""
    donorName = str(input("Please provide the donor name for the thank you or type 'list' to see the list of donors >"))

    while donorName == 'list': #as long as user types list, it will return the donor list
        for donor in donorList:
            print(donor[0])

        donorName = str(input("Please provide the donor name to compose the thank you >"))
        print("The name entered:" ,donorName) ###REMOVE AFTER DEBUGGING
    
    if(donorName not in justDonors): 
        print(donorName, "Is not in list. It will be added to donor list") #remove after debugging
        isNewDonor = True
        justDonors.append(donorName)
        retrieveDonationAmount(donorName, isNewDonor)
        
    elif (donorName in justDonors):
        print("Donor was found. You want to send a thank you to ", donorName)  #remove after debugging
        isNewDonor = False
        retrieveDonationAmount(donorName, isNewDonor)



def retrieveDonationAmount(donorName, isNewDonor):
    """requests donor information and will append new contibution to former donor"""
    newContribution = float(input("please enter new contribution amount....> "))
    if isNewDonor is False:
        for donor in donorList:
        	if donor[0] == donorName:
        		donor.append(newContribution)
        		printLetter(donorName,newContribution)
    else:
        donorList.append([donorName,newContribution]) 
        printLetter(donorName,newContribution)

    print(donorList)

def printLetter(donorName, newContribution):
    """completes and prints Thank you letter then calls getAction method to request new action"""
    print("\nDear {} ,\n".format(donorName))
    print("Thank you for your generous contribution of ${} ".format(newContribution))
    print("We will try to spend it wisely. No company trips to the DQ, pinky swear.")
    print("Sincerely,")
    print("Us\n")
    getAction()


#still need to call and improve formattting.
def createReportData():
    print('{:<15}'.format("Donor Name"), '{:<20}'.format('|  Total Given  |'),
                 '{:>5}'.format('Number of Gifts  |'),'{:>20}'.format('Average Gift  |')) 
    print('_'*77)
    dataForDonationReport = []
    for donor  in donorList: # prepare the report list
        donorNumTotal =sum(donor[1:])
        numbGifts = (len(donor)-1)
        donorAverage = "$ {0:.2f}".format(float((sum(donor[1:]))/numbGifts)) #subtract 1 to acocunt for name placeholder in List[0]
        dataForDonationReport.append([donorNumTotal,donor[0],numbGifts,donorAverage])
    
    sortedReport = sorted(dataForDonationReport)
    ascendingReport =sortedReport[::-1]
    
    for donor in ascendingReport:
        donorTotal = "$ {0:.2f}".format(donor[0]) 
        print('{:<20}'.format(donor[1]),'{:<15}'.format(donorTotal),
                '{:>5}'.format(donor[2]),'{:>25}'.format(donor[3]))
    getAction()                     


if __name__ == "__main__" :
  """   """
donorList = [['Peter_Piper' ,100.00, 200.00 , 3000.00],['Lucille_Ball',100.00,200.00], ['Barak_Obama', 100.00,2000.00,3000.00],
              ['Mary_Poppins', 1000, 2000.5], ['Bill_Gates', 100.0, 2000.0, 1000.0]]
justDonors = ['Peter_Piper','Lucille_Ball', 'Barak_Obama', 'Mary_Poppins', 'Bill_Gates']


getAction()

