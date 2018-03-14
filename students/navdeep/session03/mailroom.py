def menu(donor_list):
    """This function will print out a menu of options for
    the user to choose from
    :param: the list of donors and how much they have donated"""
    user_option = ""
    while user_option.lower() != 'exit':
        displayMenu()
        user_option = input("Select an option from the menu: ")
        if user_option.lower() == 'send a thank you':
            addNewDonation(donor_list)
        elif user_option.lower() == 'create a report':
            createReport(donor_list)
        elif user_option.lower() == 'exit':
            print("Thank you for all of the donations!")
        else:
            print("That is not a valid option you chose")

def displayMenu():
    """
    displays the menu of options to the user
    :return:
    """
    str_menu = "1. Type 'Send a Thank You' to add name and donation\n"  \
               "2. Type 'Create a Report' to see list of donors\n" \
               "3. Type 'exit' to exit the program"
    print(str_menu)
    print()

def addNewDonation(donor_list):
    """
    Allows user to add a new donor and their donation to the list
    :param donor_list: the list of donors and their donations
    """
    new_donor = input("Enter the name of a new donor: ")
    while new_donor.lower() == 'list':
        showDonorNames(donor_list)
        new_donor = input("Please enter a donor name: ")
    new_donation = float(input("Enter a new donation amount: "))
    while new_donation < 1:
        new_donation = float(input("Enter something greater than 0: "))
    donor_list.append(new_donor.strip())
    donor_list.append(new_donation)
    printThankYou(new_donor, new_donation)

def showDonorNames(donor_list):
    """
    will show the unique names of donors
    :param donor_list: the list of donors and their donations
    """
    print("Here are the list of donors: ")
    unique_list = []
    for donor in donor_list[::2]:
        if donor not in unique_list:
            unique_list.append(donor)
            print(donor)

def printThankYou(newest_donor, newest_donation):
    """
    Prints out a thank you message after someone has donated
    :param newest_donor: the name of the newest donor
    :param newest_donation: the amount the new donor donated
    """
    thank_you_message = "Thank you {} for you generous donation " \
                        "of ${:.2f}.".format(newest_donor.title(), round(newest_donation,2))
    print(thank_you_message)
    print()

def reportHeader():
    """
    The header of the report
    """
    header = '{0:<15}\t\t\t{1:<20}  {2:<20}  {3:<20}\n' \
             '-------------------------------------------------------------------------------------'.format(
                                                                                        'Donor',
                                                                                        'Total Given',
                                                                                        'Num Gifts',
                                                                                        'Average Gift')
    print(header)

def createReport(donor_list):
    """
    Creates a table of the report that shows the donor names, how many times they donated
    the average donation and total donations
    :param donor_list: the list of donors and their donation amounts
    """
    total_give = 0.00
    num_gifts = 0
    avg_gift = 0
    str_report = ""
    unique_list = []
    for donor in donor_list[::2]:
        if donor not in unique_list:
            unique_list.append(donor.strip())
    reportHeader()
    for name in unique_list:
        num_gifts = 0
        total_give = 0
        avg_gift = 0
        for index,donor in enumerate(donor_list):
            if name == donor:
                num_gifts = num_gifts + 1
                total_give = total_give + donor_list[index + 1]
        avg_gift = total_give / num_gifts
        str_report += "{0:<15}\t\t\t$ {1:<20} {2:<20} $ {3:<20}\n".format(name.title(),
                                                                          round(total_give, 2),
                                                                          num_gifts,
                                                                          round(avg_gift, 2))
    print(str_report)


donors = ["Navdeep", 1000, "Nick", 5, "Henry", 100, "Nick", 2,
          "Lorenzo", 1000, "Torin", 200.5]

menu(donors)
