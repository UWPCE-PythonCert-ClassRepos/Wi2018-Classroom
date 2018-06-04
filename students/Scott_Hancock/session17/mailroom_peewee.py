#!/usr/bin/env python

"""
Mailroom.py refactored to use Peewee
"""

from peewee import *

sqlite_db = SqliteDatabase('mailroom.db', pragmas={'journal_mode': 'wal', 'cache_size': -1024 * 64})

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class Donor(BaseModel):

    name = CharField(primary_key = True, max_length = 30)

class Donation(BaseModel):

    donation_id = AutoField()
    donation_amount = DecimalField(decimal_places = 2)
    name = ForeignKeyField(Donor, related_name='was_donated_by', null = False)

def addDonor(searchName):
    new_donor = Donor.create(name = searchName)
    new_donor.save()
    return new_donor

def findDonor(searchName):
    donor = Donor.get(Donor.name == searchName)
    return donor

def getDonorsList():
    query = Donor.select()
    return query

def addDonation(searchName, donationAmount):
    new_donation = Donation.create(name = searchName, donation_amount = donationAmount)
    new_donation.save()
    return new_donation

def getDonationsList(searchName):
    query = Donation.select().where(Donation.name == searchName)
    return [x.donation_amount for x in query]

def getNumDonations(dlist):
    """ Get the number of donations in a donation list """
    return len(dlist)

def getAvgDonation(dlist):
    """ Get the average value of the donations in a donation list """
    try:
        return getTotDonation(dlist)/getNumDonations(dlist)
    except ZeroDivisionError:
        return 0.0

def getTotDonation(dlist):
    """ Get the total value of the donations in a donation list """
    return sum(dlist)

def createThankYouEmail(searchName):
    """ Return donation thank you e-mail text based on the donor name and the donated amount """
    donor = findDonor(searchName)
    donationsList = getDonationsList(searchName)
    result = ("\nDear {:s},\n\n"
        "\tThank you so much for your generous donation of ${:,.2f}!\n\n"
        "\tIt will be put to very good use.\n\n"
        "\t\tSincerely,\n\t\t\t- The Team".format(donor.name, getTotDonation(donationsList))
        )
    return result

def storeThankYouLetters():
    """ Save each thank you e-mail text to a file on disk """
    query = getDonorsList()
    for donor in query:
        f = open("{:s}.txt".format(donor.name).replace(" ", "_"), 'w')
        f.write(createThankYouEmail(donor.name))
        f.close()

def getReport():
    """ Create a report of all the donors in the database """
    query = getDonorsList()
    result = ("\nDonor Name          | Total Given | Num Gifts | Average Gift"
        "\n------------------------------------------------------------")
    for donor in query:
        donationsList = getDonationsList(donor)
        result += "\n{:20s}| ${:10.2f} |{:10d} | ${:10.2f}".format(donor.name, getTotDonation(donationsList), getNumDonations(donationsList), getAvgDonation(donationsList))
    return result

def menu_selection(prompt, dispatch_dict):
    """ Run the basic menu(s) of the program """
    while True:
        response = input(prompt).lower()
        if dispatch_dict[response]() == 'quit':
            break

def sendThankYou():
    """ Adds donors and donations and prints out donation thank you e-mails """
    while True:
        nameEntry = input("Enter a full name (or list to view a list of existing names): ")
        if nameEntry.strip() == 'list':
            ''' show list of donor names '''
            for donor in getDonorsList():
                print(donor.name)
        elif nameEntry.strip() == '':
            break
        else:
            currentDonor = findDonor(nameEntry)
            if currentDonor is None:
                currentDonor = addDonor(nameEntry)
                print(f"Created a new donor named {currentDonor.name}")
            else:
                print(f"Found existing donor named {currentDonor.name}")
            amountEntry = float(input("Enter donation amount: "))
            addDonation(nameEntry, amountEntry)
            print(createThankYouEmail(nameEntry))
            break

def viewReport():
    print(getReport())

def quit():
    """ Quits the main menu """
    return 'quit'

main_prompt = ("\nWelcome to the MongoDB Mailroom.py prompt:\n"
    "1. Send a Thank You\n"
    "2. View a Report\n"
    "3. Send letters to everyone\n"
    "q. Quit\n"
    ">-> "
    )
main_dispatch = {"1": sendThankYou,
    "2": viewReport,
    "3": storeThankYouLetters,
    "q": quit,
    }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)






