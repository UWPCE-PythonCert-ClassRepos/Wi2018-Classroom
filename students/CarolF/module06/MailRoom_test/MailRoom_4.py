#!/usr/bin/env Python3

################################
##Created By: Carol Farris
##Date:March 4th 2018
##Goal: MailRoom Part 4 Assignment. 
##Changes: Refactored code in most every function to improve testability. Added error handling for donation amount
## Added comprehension in createReportData(), created test_MailRoom.py which had 5 tests pass. Would love 
## feedback on how to better improve re-factoring code (previous feedback was very useful) and increasing testability.
## Note: you need to change validSelection to False to run Mailroom_4.py from command line. Set to true to run test file.
################################


usersChoice = {1: 'Send Thank You', 2: 'Create Report', 3 : 'Send letters to everyone', 4: 'Quit'}
donorDict = {'Peter_Piper' : [100.00, 200.00 , 3000.00], 'Lucille_Ball': [100.00,200.00], 'Barak_Obama': [100.00,2000.00,3000.00],
             'Mary_Poppins': [1000, 2000.5], 'Bill_Gates': [100.0, 2000.0, 1000.0]} 
#For Mailroom 4, put donorDict into function to create dummy donor list. then pass to needed functions 
             


def findDonorName(donorName=False):
    """This function identifies the donor information to be used"""
    if not donorName:
        donorName = str(input("Please enter donor name, type 'list' to see the list of donors or 'quit' to exit >"))

    while donorName == 'list': #as long as user types list, it will return the donor list
        for key in donorDict:  print(key) #dictionary version to provide list
        donorName = str(input("Please enter donor name, type 'list' to see the list of donors or 'quit' to exit >"))

    if donorName == 'quit':
        exit()    

    return(donorName)

def retrieveDonationAmount(donorName, newContribution=False):
    """requests donor information and will append new contibution to former donor"""
    if  not newContribution:   
        newContribution = (input("please enter new contribution amount or type 'quit' to exit> "))
        if newContribution == 'quit':   exit()

    try:
        newContribution=float(newContribution)
    except ValueError:
        print('Please provide a number or type quit to exit')
        retrieveDonationAmount(donorName)             
    
    recordDonation(donorName, newContribution)
    return(newContribution)


def recordDonation(donorName,newContribution):
    if(donorName in donorDict):
        newListValue = donorDict[donorName] 
        donorDict[donorName].append(newContribution)       
    else:
        donorDict[donorName] = [newContribution] #turned value into single value list in anticipation of adding contributions in the future


def printLetter(donorName, newContribution=0):
    """completes and prints Thank you letter then calls getAction method to request new action"""
    return("\nDear {},\nThank you for your donation of ${}.\nSincerely,\nThe Team\n".format(donorName,newContribution)) 


def createReportData(defaultList=False): 
    dataForDonationReport = [[sum(donations), donor,len(donations),sum(donations)//len(donations) ] for donor, donations in donorDict.items() ]  
    sortedReport = sorted(dataForDonationReport)
    ascendingReport =sortedReport[::-1]
    printReportData(ascendingReport)
    if defaultList == True:
        return ascendingReport


def printReportData(ascendingReport):
    print('{:<15}'.format("Donor Name"), '{:<20}'.format('|  Total Given  |'),
                 '{:>5}'.format('Number of Gifts  |'),'{:>20}'.format('Average Gift  |')) 
    print('_'*77)
    for donor in ascendingReport:
        donorTotal = "$ {0:.2f}".format(donor[0]) 
        print('{:<20}'.format(donor[1]),'{:<15}'.format(donorTotal),
                '{:>5}'.format(donor[2]),'{:>25}'.format(donor[3])) 
    print('_'*77)
    print('\n')


def sendLettersToAll():
    """Prints to local directory thank you letters to all contributors."""      
    for key in donorDict:
        with open(f'{key}.txt', 'w')as f:
            f.write(f'Dear {key},\n')
            f.write(f'Thank you for your generous support of ${sum(donorDict[key])} to our company. ')
            f.write(f'It is through the support of contributors such as yourself that we\n')
            f.write(f'are able to  bring our innovative spirit into the marketplace. ' )
            f.write(f'Please enjoy the enclosed shrubbery one of our team members grew\nfor you! ')
            f.write(f'With our deepest appreciation,\n Our team at PyCert')


def printThankYouLetter(): 
    foundDonors = findDonorName()
    foundDonation = retrieveDonationAmount(foundDonors)
    print(printLetter(foundDonors, foundDonation))



if __name__ == "__main__" :

#validSelection = False  
validSelection=True  ##this is used to test the code. Otherwise validSelection is set to False. 
while validSelection == False: ##Ensure user enters coorect selection 
    try: 
        for key, value in usersChoice.items():    print('%s: %s' % (key, value))
        response = int(input("Please type a numeric selection from the above actions >"))  
    except ValueError:
        print("\nInput must be an integer. Try again")
    else: 
        if response != 1 and response != 2 and response != 3 and response != 4:
            print("Invalid entry. Expected a '1', '2', '3', or '4' ")
        else:
            validSelection = True           

    if response ==4:
        print("Goodbye")
        exit()

    if response ==3:
        print("Send Letters to All")
        sendLettersToAll()
        validSelection = False      

    if response ==2:
        createReportData()
        validSelection = False  

    if response == 1: 
        printThankYouLetter()
        validSelection = False



