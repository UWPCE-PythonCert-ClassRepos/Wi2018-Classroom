class Donor:
    """ Class to keep track of a donor with a donor name and list of donation amounts """

    def __init__(self, name=''):
        self.name = name.strip()
        self.donationList = list()

    def addDonation(self, amount):
        """ Add a donation amount to the list """
        self.donationList.append(amount)

    # CHANGE INTO A PROPERTY
    def getNumDonations(self):
        """ Get the number of donations the donor has made """
        return len(self.donationList)

    def getAvgDonation(self):
        """ Get the average value of the donations the donor has made"""
        try:
            return self.getTotDonation()/self.getNumDonations()
        except ZeroDivisionError:
            return 0.0

    def getTotDonation(self):
        """ Get the total value of the donations the donor has made """
        return sum(self.donationList)

    def createThankYouEmail(self):
        """ Return donation thank you e-mail text based on the donor name and the donated amount """
        result = ("\nDear {:s},\n\n"
            "\tThank you so much for your generous donation of ${:,.2f}!\n\n"
            "\tIt will be put to very good use.\n\n"
            "\t\tSincerely,\n\t\t\t- The Team".format(self.name, self.getTotDonation())
            )
        return result


class DonorCollection:
    """ Keeps track of the collection of donors as well as writing thank you letters and the donor report """
    """ To add: read and write donor collection as a JSON """

    def __init__(self):
        self.donorList = list()

    def addDonor(self, donor):
        """ Add a donor to the list """
        self.donorList.append(donor)

    def findDonor(self, searchName):
        """ Search for a donor in the list by the donor's name """
        result = None
        for donor in self.donorList:
            if donor.name.lower() == searchName.strip().lower():
                result = donor
                break
        return result

    def listDonors(self):
        """ List all the donors """
        for donor in self.donorList:
            print(donor.name)

    def storeThankYouLetters(self):
        """ Save each thank you letter to a file by the donor's name """
        for donor in self.donorList:
            f = open("{:s}.txt".format(donor.name).replace(" ", "_"), 'w')
            f.write(donor.createThankYouEmail())
            f.close()

    def getReport(self):
        """ Return a report of all the donors and donation roll-up """
        result = ("\nDonor Name          | Total Given | Num Gifts | Average Gift"
            "\n------------------------------------------------------------")
        for donor in self.donorList:
            result += "\n{:20s}| ${:10.2f} |{:10d} | ${:10.2f}".format(donor.name, donor.getTotDonation(), donor.getNumDonations(), donor.getAvgDonation())
        return result


donors = DonorCollection()

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
        response = input("Enter a full name (or list to view a list of existing names): ")
        if response.strip() == 'list':
            ''' show list of donor names '''
            donors.listDonors()
        else:
            ''' use name and ask for donation amount '''
            currentDonor = donors.findDonor(response)
            if currentDonor is None:
                currentDonor = Donor(response)
                donors.addDonor(currentDonor)
                print("Created a new donor")
            else:
                print("Found donor named " + currentDonor.name)
            response = input("Enter donation amount: ")
            amount = float(response)
            currentDonor.addDonation(amount)
            print(currentDonor.createThankYouEmail())
            break

def createReport():
    print(donors.getReport())

def quit():
    """ Quits the main menu """
    return 'quit'

# CAPITALIZE THESE
MAIN_PROMPT = ("\nWelcome to the Mailroom.py prompt:\n"
    "1. Send a Thank You\n"
    "2. Create a Report\n"
    "3. Send letters to everyone\n"
    "q. Quit\n"
    ">-> "
    )
MAIN_DISPATCH = {"1": sendThankYou,
    "2": createReport,
    "3": donors.storeThankYouLetters,
    "q": quit,
    }

if __name__ == '__main__':
    menu_selection(MAIN_PROMPT, MAIN_DISPATCH)






