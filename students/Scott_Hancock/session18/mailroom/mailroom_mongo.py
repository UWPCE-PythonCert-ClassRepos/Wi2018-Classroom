#!/usr/bin/env python

"""
Mailroom.py refactored to use MongoDB
"""

import login_database

class DonorCollection:

    def __init__(self):
        self.donorList = list()

    def addDonor(self, searchName):
        """ Add new donor to database with name == searchName """
        return mailroomdb.insert_one({'name': searchName})

    def findDonor(self, searchName):
        """ Return donor result based on searchName """
        return mailroomdb.find_one({'name': searchName})

    def listDonors(self):
        """ Print a list of the donors in the database by name """
        cursor = mailroomdb.find({})
        for donor in cursor:
            print(donor['name'])

    def addDonation(self, searchName, donationAmount):
        """ Push new donation amount into the donation array for a donor with name == searchName """
        return mailroomdb.update({'name': searchName},{'$push': {'donationList': donationAmount}})

    def getNumDonations(self, dlist):
        """ Get the number of donations in a donation list """
        return len(dlist)

    def getAvgDonation(self, dlist):
        """ Get the average value of the donations in a donation list """
        try:
            return self.getTotDonation(dlist)/self.getNumDonations(dlist)
        except ZeroDivisionError:
            return 0.0

    def getTotDonation(self, dlist):
        """ Get the total value of the donations in a donation list """
        return sum(dlist)

    def createThankYouEmail(self, searchName):
        """ Return donation thank you e-mail text based on the donor name and the donated amount """
        cursor = mailroomdb.find_one({'name': searchName})
        result = ("\nDear {:s},\n\n"
            "\tThank you so much for your generous donation of ${:,.2f}!\n\n"
            "\tIt will be put to very good use.\n\n"
            "\t\tSincerely,\n\t\t\t- The Team".format(cursor['name'], self.getTotDonation(cursor['donationList']))
            )
        return result

    def storeThankYouLetters(self):
        """ Save each thank you e-mail text to a file on disk """
        cursor = mailroomdb.find({})
        for donor in cursor:
            f = open("{:s}.txt".format(donor['name']).replace(" ", "_"), 'w')
            f.write(self.createThankYouEmail(donor['name']))
            f.close()

    def getReport(self):
        """ Create a report of all the donors in the database """
        cursor = mailroomdb.find({})
        result = ("\nDonor Name          | Total Given | Num Gifts | Average Gift"
            "\n------------------------------------------------------------")
        for donor in cursor:
            result += "\n{:20s}| ${:10.2f} |{:10d} | ${:10.2f}".format(donor['name'], self.getTotDonation(donor['donationList']), self.getNumDonations(donor['donationList']), self.getAvgDonation(donor['donationList']))
        return result

donors = DonorCollection()
# donors.loadCollection({'donor00': {'name': 'John Doe', 'donationList': [100.0, 200.0]}, 'donor01': {'name': 'Scottie D', 'donationList': [50.0, 75.0]}})

def menu_selection(prompt, dispatch_dict):
    """ Run the basic menu(s) of the program """
    while True:
        response = input(prompt).lower()
        if dispatch_dict[response]() == 'quit':
            break

def getDonorDB():
    return donors

def sendThankYou():
    """ Adds donors and donations and prints out donation thank you e-mails """
    while True:
        nameEntry = input("Enter a full name (or list to view a list of existing names): ")
        if nameEntry.strip() == 'list':
            ''' show list of donor names '''
            donors.listDonors()
        elif nameEntry.strip() == '':
            break
        else:
            currentDonor = donors.findDonor(nameEntry)
            if currentDonor is None:
                donors.addDonor(nameEntry)
                currentDonor = donors.findDonor(nameEntry)
                print(f"Created a new donor named {currentDonor['name']}")
            else:
                print(f"Found existing donor named {currentDonor['name']}")
            try:
                amountEntry = float(input("Enter donation amount: "))
            except ValueError:

            donors.addDonation(nameEntry, amountEntry)
            print(donors.createThankYouEmail(nameEntry))
            break

def viewReport():
    print(donors.getReport())

def repopulate():
    mailroomdb.remove({})
    mailroomdb.insert_many([{'name': 'Bill Gates', 'donationList': [100.0, 200.0]}, {'name': 'Scottie D', 'donationList': [50.0, 75.0]}])

def quit():
    """ Quits the main menu """
    return 'quit'

main_prompt = ("\nWelcome to the MongoDB Mailroom.py prompt:\n"
    "1. Send a Thank You\n"
    "2. View a Report\n"
    "3. Send letters to everyone\n"
    "4. Repopulate with Defaults\n"
    "q. Quit\n"
    ">-> "
    )
main_dispatch = {"1": sendThankYou,
    "2": viewReport,
    "3": donors.storeThankYouLetters,
    "4": repopulate,
    "q": quit,
    }

if __name__ == '__main__':
    with login_database.login_mongodb_cloud() as dbclient:
        db = dbclient['dev']
        mailroomdb = db['mailroom']
        menu_selection(main_prompt, main_dispatch)






