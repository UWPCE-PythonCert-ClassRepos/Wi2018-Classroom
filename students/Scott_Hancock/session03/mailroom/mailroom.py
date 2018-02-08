class Donor:
    """ Class to keep track of donors with a donor name and list of donation amounts """

    def __init__(self, name=''):
        """ """
        self.name = name
        self.donationList = list()

    def addDonation(self, amount):
        """ Add a donation amount to the list """
        self.donationList.append(amount)

    def getNumDonations(self):
        """ Get the number of donations the donor has made """
        return len(self.donationList)

    def getAvgDonation(self):
        """ Get the average value of the donations the donor has made"""
        if self.getNumDonations() > 0:
            return self.getTotDonation()/self.getNumDonations()
        else:
            return 0.0

    def getTotDonation(self):
        """ Get the total value of the donations the donor has made """
        total = 0.0
        for donation in self.donationList:
            total += donation
        return total

def menu_selection(prompt, dispatch_dict):
    """ Run the basic menu(s) of the program """
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == 'quit':
            break

def findDonor(searchList, searchName):
    """ Search for a donor in the given list (searchList) by their name (searchName) and return the donor """
    result = None
    for donor in searchList:
        if donor.name == searchName:
            result = donor
            break
    return result

def createThankYouEmail(name, amount):
    """ Return donation thank you e-mail text based on the donor name and the donated amount """
    result = ("\nDear {:s},\n\n"
        "Thank you so much for your generous donation of ${:,.2f}!\n\nWarmly,\n\nScott Hancock".format(name, amount)
        )
    return result


donorList = list()

def sendThankYou():
    """ Adds donors and donations and prints out donation thank you e-mails """
    while True:
        response = input("Enter a full name (or list to view a list of existing names): ")
        if response.strip() == 'list':
            ''' show list of donor names '''
            for donor in donorList:
                print(donor.name)
        else:
            ''' use name and ask for donation amount '''
            currentDonor = findDonor(donorList, response)
            if currentDonor is None:
                currentDonor = Donor(response)
                donorList.append(currentDonor)
                print("Created a new donor")
            else:
                print("Found donor named " + response)
            response = input("Enter donation amount: ")
            amount = float(response)
            currentDonor.addDonation(amount)
            print(createThankYouEmail(currentDonor.name, amount))
            break

def createReport():
    """ Prints out a summary report of all the donors """
    print("\nDonor Name          | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------")
    for donor in donorList:
        print("{:20s}| ${:10.2f} |{:10d} | ${:10.2f}".format(donor.name, donor.getTotDonation(), donor.getNumDonations(), donor.getAvgDonation()))
    return

def quit():
    """ Quits the main menu """
    return 'quit'

main_prompt = ("\nWelcome to the Mailroom.py prompt:\n"
    "1. Send a Thank You\n"
    "2. Create a Report\n"
    "q. Quit\n"
    ">-> "
    )
main_dispatch = {"1": sendThankYou,
    "2": createReport,
    "q": quit,
    }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)






