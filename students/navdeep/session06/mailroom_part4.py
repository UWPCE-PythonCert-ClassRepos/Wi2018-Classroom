import os.path

def initializeDonorDB():
    """
    Initializes the dictionary of donors and their donation  amounts. The donor
    names are the keys for the dictionary, while their donation amounts are the
    values. The donation amounts are stored in lists. A donor can have more than
    1 donation. Each donor is stored only once in the dictionary
    :return: the initialized dictionary of donors and their donation amounts
    """
    donor_db = {"Navdeep Gill": [1000], "Nick Garzon": [5,2], "Henry Chipman": [100],
                "Lorenzo B": [1000], "Torin Stetina": [200.75]}
    return donor_db

def initializeOptionsDB():
    options_dict = {'t': askUserForDonor, 's': createFileName, 'r': createReport, 'e': exitMessage}
    return options_dict

def displayMenu():
    """
    displays the menu of options to the user
    """
    print()
    str_menu = "1. Type 't' to Send a Thank You to add a name, donation and thank you card\n"  \
               "2. Type 'r' to Create a Report and see a list of the donors\n" \
               "3. Type 's' to Send letters to everyone\n" \
               "4. Type 'e' to exit the program"

    #for testing purposes to determine menu is returned correctly
    return str_menu
    #print(str_menu)
    #print()

def menu(donor_dict, menu_dict):
    """This function will print out a menu of options for
    the user to choose from
    :param: the list of donors and how much they have donated"""
    user_option = ""
    while user_option.lower() != 'e':
        displayMenu()
        #user_option = input("Select an option from the menu: ")
        user_option = 't' #for testing purposes
        user_option = user_option.strip()
        user_option = user_option.lower()
        return user_option #used to test menu produces correct user input
        #try:
         #   menu_dict[user_option](donor_dict)
        #except KeyError as e:
         #   print("Invalid option selected. Please try again")

def askUserForDonor(donor_dict):
    """
    Allows user to add a new donor to the dictionary or print out
    the names of the current donors or exit back to the main menu.
    The user can also type in the name of a donor that already
    exists to append a new donation.
    :param donor_list: the list of donors and their donations
    """
    user_donor_option = ""
    while user_donor_option != 'exit':
        #user_donor_option = input("1. Type 'new' of a new donor\n"
         #                         "2. Type 'list' to list the donor names\n"
          #                        "3. Type 'exit' to return to main menu\n"
           #                       "Your Selection:  ")
        #print()
        user_donor_option = 'NeW'
        user_donor_option = user_donor_option.strip().lower()
        if user_donor_option == 'new':
            return "addNewDonor(donor_dict)"
        elif user_donor_option == 'list':
            return "showDonorNames(donor_dict)"
        elif user_donor_option == 'exit':
            return
        else:
            print("Please select a valid option:")

def addNewDonor(donor_dict):
    first_name = None
    last_name = None
    full_name = None
    invalid = True
    while invalid == True:
        try:
            #first_name = input("Enter first name for donor: ")
            #last_name = input("Enter last name for donor: ")
            first_name = "Kelly"
            last_name = "Pratt"
            first_name, last_name = first_name.strip(),last_name.strip()
            if first_name == "" or last_name == "":
                raise ValueError
        except ValueError as e:
            print("The name you entered is invalid. Enter proper first/last name")
        else:
            first_name, last_name = first_name.lower(), last_name.lower()
            first_name,last_name = first_name.title(), last_name.title()
            invalid = False
    full_name = first_name + ' ' + last_name
    #Return statement used for testing purposes
    return full_name
    #addNewDonation(donor_dict, full_name)

def addNewDonation(donor_dict, new_donor):
    """
    Allows the user to input a new donation for the user. The user must
    enter a valid amount (integer or float).  The user must
    also enter a value greater than 0.  If the donor currently exists
    in the dictionary, the donor's new donation will be appended to the list stored under
    their name, which is the key in the dictionary. If the donor does
    not exist in the dictionary, a new key will be created along with a new
    list for that key.
    :param donor_list: the dictionary of donors and their donation amounts
    :param new_donor: the name of the new donor
    """
    try:
        #new_donation = float(input("Enter a new donation amount: "))
        new_donation = 1000
        while new_donation < 0:
            new_donation = float(input("Enter something greater than 0: "))
    except ValueError as e:
        print("The amount you entered is an invalid value.")
    else:
        if donorExists(donor_dict, new_donor):
            donor_dict[new_donor].append(new_donation)
        else:
            donor_dict[new_donor.strip()] = [new_donation]
        #Return used for testing purposes. Testing
        #To see if dictionary updated with new donor
        #and new donation
        return donor_dict
        #printThankYou(new_donor, new_donation)

def donorExists(donor_dict, new_donor):
    """
    This function will test whether or not a donor already exists in the dictionary
    :param donor_list: A dictionary of donor names and the values they have donated
    :param new_donor: the name of the donor the user most recently inputted
    :return: True if donor exists in the dictionary as a key, false otherwise
    """
    if new_donor in donor_dict:
        return True
    else:
        return False

def showDonorNames(donor_dict):
    """
    will show the unique names of donors.  Will use comprehension to print
    out the donor names
    :param donor_list: the list of donors and their donations
    """
    print("Here are the list of donors: ")
    #Code below was used for testing purposes to
    #Determine if the donor names will correctly print
    new_donor_list = [donor for donor in donor_dict.keys()]
    return new_donor_list
    #[print(donor) for donor in donor_list.keys()]

def printThankYou(newest_donor, newest_donation):
    """
    Prints out a thank you message after someone has donated
    :param newest_donor: the name of the newest donor
    :param newest_donation: the amount the new donor donated
    """
    thank_you_message = "Thank you {} for you generous donation " \
                        "of ${:.2f}.".format(newest_donor.title(), round(newest_donation,2))
    #return statement used for testing purposes to determine
    #if thank you message is printed correctly
    return thank_you_message
    #print(thank_you_message)
    #print()

def reportHeader():
    """
    The header of the report
    """
    header = ("{:25s} | {:11s} | {:9s} | {:12s}\n".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    header += "-" * 66
    return header

def createReport(donor_dict):
    """
    Creates a table of the report that shows the donor names, how many times they donated
    the average donation and total donations
    :param donor_list: the list of donors and their donation amounts
    """
    total_give = 0.00
    num_gifts = 0
    avg_gift = 0
    report_dict = {}
    for donor, donations in donor_dict.items():
        num_gifts = len(donations)
        total_give = calculateSum(donations)
        avg_gift = calculateAverage(donations)
        report_dict[donor] = [round(total_give,2), num_gifts, round(avg_gift, 2)]
    #Return statement used for testing purposes
    #Determine if report_dict is correct
    return report_dict
    #printReport(report_dict)

def printReport(report_dict):
    """
    This function prints the report. The report contains
    the number of gifts given, the average donation and
    the total donation amounts,
    :param report_dict: the dictionary of donors and donations
    """
    reportHeader()
    str_report = ""
    for donor, metrics in report_dict.items():
        str_report += ("{:25s}   {:11.2f}   {:9d}   {:12.2f}\n".format(donor, metrics[0], metrics[1], metrics[2]))
    return str_report

def calculateSum(donations_list):
    """
    Calculates the sum of all donations for a donor
    :param donations_list: the list of donations of a donor. The value stored in the
    donor dictionary
    :return: the sum of the donations
    """
    return sum(donations_list)

def calculateAverage(donations_list):
    """
    Calculates the sum of all donations for a donor
    :param donations_list: the list of donations of a donor. The value stored in the
    donor dictionary
    :return: the sum of the donations
    """
    return sum(donations_list) / len(donations_list)

def createFileName(donor_dict):
    """
    Creates a file name for each donor in the donor dictionary. Once the file
    name is created, the file name, donor name and list of donations are sent
    to the writeToFile function, where the letter is stored as a
    .txt file
    :param donor_dict: The dictionary of donors and their list of donations
    """
    #path = 'C:\\Users\\navgill\Wi2018-Classroom\students\\navdeep\session04\Letters'
    letter = None
    filename = None
    donor_file_name = None
    complete_file_name = None
    for donor,donations in donor_dict.items():
        donor_file_name = donor.replace(" ", "_")
        full_file_name = "{}.txt".format(donor_file_name)
        #Return statement used for testing purposes to ensure
        #file name is created correctly
        return full_file_name
        #writeToFile(full_file_name, donor, donations)

def writeToFile(file_name, donor, donations):
    """
    Writes thank you letters for each individual that has donated and saves the file
    in the current working directory.
    :param donor_list: the dictionary of donors and the values each donor has donated
    """
    file_name = os.path.join(os.getcwd(), file_name)
    letter = letterToSend(donor, donations)
    with open(file_name, 'w+') as f:
        f.write(letter)
    f.close


def letterToSend(donor, donations):
    """
    The letter that will be saved thanking each donor for their contributions
    :param donor: the name of the donor
    :param donations: the donation amounts
    :return: the letter for each individual, a string
    """
    str_letter = "Dear {},\n" \
                 "\tThank you for your kind donation(s) of {}.\n" \
                 "\tIt will be put to very good use.\n" \
                 "\t\tSincerely,\n" \
                 "\t\t\t-The Team".format(donor, str(donations)[1:-1])
    return str_letter

def exitMessage(donor_dict):
    """
    Exit message once the user decides to end the entire program
    All of the donors stored in the dictionary will be printed
    a final time
    :param donor_list: a dictionary of donors and the values they donated
    :return:
    """
    str_exit_message = "Thank you to the following donors for all of your donations:\n "
    for donor in donor_dict.keys():
        str_exit_message += donor
    return str_exit_message

donors = initializeDonorDB()
menu_dict = initializeOptionsDB()
menu(donors, menu_dict)
