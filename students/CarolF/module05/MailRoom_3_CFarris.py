#!/usr/bin/env Python3

################################
##Created By: Carol Farris
##Date: February 13th 2018
##Goal: MailRoom Part 3 Assignment. 
##Changes: Moved around code from Mailroom2 version to improve testability (for Mailroom 4).
##Added try catch exception to while loop managing selection at bottom. Couldn't find a good   
##place to add comprehension--Will try in Mailroom 4 after I have refactored code a bit more. 
################################


usersChoice = {1: 'Send Thank You', 2: 'Create Report', 3 : 'Send letters to everyone', 4: 'Quit'}
donorDict = {'Peter_Piper' : [100.00, 200.00 , 3000.00], 'Lucille_Ball': [100.00,200.00], 'Barak_Obama': [100.00,2000.00,3000.00],
             'Mary_Poppins': [1000, 2000.5], 'Bill_Gates': [100.0, 2000.0, 1000.0]} 
#For Mailroom 4, put donorDict into function to create dummy donor list. then pass to needed functions 
             


def findDonorName():
    """This function identifies the donor information to be used"""
    donorName = str(input("Please provide the donor name for the thank you or type 'list' to see the list of donors >"))

    while donorName == 'list': #as long as user types list, it will return the donor list
        for key in donorDict:  print(key) #dictionary version to provide list
        donorName = str(input("Please enter the donor name to compose the thank you >"))

    return(donorName)

def retrieveDonationAmount(donorName):
    """requests donor information and will append new contibution to former donor"""
    newContribution = float(input("please enter new contribution amount....> "))
    
    if(donorName in donorDict):
         newListValue = donorDict[donorName] 
         donorDict[donorName].append(newContribution)       
    else:
        donorDict[donorName] = [newContribution] #turned value into single value list in anticipation of adding contributions in the future

    return(newContribution)

def printLetter(donorName, newContribution):
    """completes and prints Thank you letter then calls getAction method to request new action"""
    print("\nDear {},".format(donorName)) #added newlines to improve readability
    print("Thank you for your generous contribution of ${} ".format(newContribution))
    print("Your contribution is greatly appreicated and will be used to grow our operations and will reinforce our commitment to innovation.")
    print("Sincerely,")
    print("The Entire Team at PyCert.com\n")


#still need to call and improve formattting.
def createReportData():
    print('{:<15}'.format("Donor Name"), '{:<20}'.format('|  Total Given  |'),
                 '{:>5}'.format('Number of Gifts  |'),'{:>20}'.format('Average Gift  |')) 
    print('_'*77)
    dataForDonationReport = []
    for key in donorDict:
        donorNumTotal = sum(donorDict[key])
        numbGifts = (len(donorDict[key]))
        donorAverage = "$ {0:.2f}".format(float((sum(donorDict[key]))/numbGifts))
        dataForDonationReport.append([donorNumTotal,key,numbGifts,donorAverage]) 
    
    sortedReport = sorted(dataForDonationReport)
    ascendingReport =sortedReport[::-1]
    
    for donor in ascendingReport:
        donorTotal = "$ {0:.2f}".format(donor[0]) 
        print('{:<20}'.format(donor[1]),'{:<15}'.format(donorTotal),
                '{:>5}'.format(donor[2]),'{:>25}'.format(donor[3]))   
    print('_'*77)
    print('\n') 
    print('Please indicate your next action')   


def sendLettersToAll():
    """Prints to local directory thank you letters to all contributors."""      
    print("Get Ready for some thank yous!")
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
    printLetter(foundDonors, foundDonation)



if __name__ == "__main__" :
  """Only the action list is listed as that method routes the user to the desired action  """

validSelection = False
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



