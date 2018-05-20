import os.path
from donor_classes_fp import Donor, DonorCollection

def initializeDonorDB(donor_collection_obj):
    """
    Initializes the dictionary of donor objects and their donation  amounts. The donor names are the keys for the dictionary, while their donation amounts are the values. The donation amounts are stored in lists. Each donor is stored only once in the dictionary.
    :param donor_collection_obj: The database of donor objects
    :return: the initialized dictionary of donors and their donation amounts
    """
    d1 = Donor("Navdeep", "Gill",[500.00])
    d2 = Donor("Lorenzo", "Braden", [1000.00, 300.00])
    d3 = Donor("Torin", "Stetina", [200.75])
    d4 = Donor("Henry", "Chipman", [6000.00, 600.00])
    donor_collection_obj.append_collection_dict(d1)
    donor_collection_obj.append_collection_dict(d2)
    donor_collection_obj.append_collection_dict(d3)
    donor_collection_obj.append_collection_dict(d4)

def initializeOptionsDB():
    """
    Initializes the options the user can select from. A dictionary where the key is the option the user can select and the values are the functions that are called based off of the user's selection
    :return: The options dictionary.
    """
    options_dict = {'t': askUserForDonor, 's': writeToFile, 'r': createReport, 'f': challengeList, 'e': exitMessage}
    return options_dict

def displayMenu():
    """
    displays the menu of options to the user
    """
    str_menu = "\n1. Type 't' to add a name, donation and thank you card\n"+\
    "2. Type 'r' to Create a Report and see a list of the donors\n"+\
    "3. Type 's' to Send letters to everyone\n4. Type 'f' to multiply all donations by a factor\n"+\
    "5. Type 'e' to exit the program\n"
    #for testing purposes to determine menu is returned correctly
    #return str_menu
    print(str_menu)

def menu(donor_collection_obj, menu_dict):
    """
    This function will print out a menu of options for the user to choose from,
    ask the user what action they would like to perform and then call the function that performs that action
    :param donor_collection_obj: The database of donor objects
    :param menu_dict: The dictionary of user options
    """
    user_option = ""
    while user_option.lower() != 'e':
        displayMenu()
        user_option = input("Select an option from the menu: ")
        user_option = user_option.lower().strip()
        #user_option = 't' #for testing purposes
        #return user_option #used to test menu produces correct user input
        try:
            menu_dict[user_option](donor_collection_obj)
        except KeyError as e:
            print(e)
            print("Invalid option selected. Please try again")

def askUserForDonor(donor_collection_obj):
    """
    Allows user to add a new donor object to the database or print out
    the names of the current donors or exit back to the main menu.
    The user can also type in the name of a donor that already
    exists to append a new donation to that donor object
    :param donor_collection_obj: the database of donor objects
    """
    user_donor_option = ""
    while user_donor_option != 'Exit':
        user_donor_option = input("1. Type 'New' of a new donor\n"
                                  "2. Type 'List' to list the donor names\n"
                                  "3. Type 'Exit' to return to main menu\n"
                                  "\nYour Selection:  ")

        user_donor_option = donor_collection_obj.clean_text(user_donor_option)
        if user_donor_option == 'New':
            addNewDonor(donor_collection_obj)
        elif user_donor_option == 'List':
            showDonorNames(donor_collection_obj)
        elif user_donor_option == 'Exit':
            return
        else:
            print("Please select a valid option:")
            print()

def addNewDonor(donor_collection_obj):
    """
    Prompts the user for a first and last name for the donor object, regardless of whether or not the donor currently exists. The user cannot enter in a blank string as a name.
    :param donor_collection_obj: The database of donor objects
    """
    first_name = None
    last_name = None
    invalid = True
    while invalid == True:
        try:
            first_name = input("Enter first name for donor: ")
            last_name = input("Enter last name for donor: ")
            #first_name = "Kelly" used for testing
            #last_name = "Pratt" used for testing
            if first_name == "" or last_name == "":
                raise ValueError
        except ValueError as e:
            print("The name you entered is invalid. Enter proper first/last name")
        else:
            first_name, last_name = donor_collection_obj.clean_text(first_name),donor_collection_obj.clean_text(last_name)
            invalid = False
    #Return statement used for testing purposes
    #return full_name
    addNewDonation(donor_collection_obj, first_name, last_name)

def addNewDonation(donor_collection_obj, first_name, last_name):
    """
    Allows the user to input a new donation for the user. The user must
    enter a valid amount (integer or float).  The user must
    also enter a value greater than 0.  If the donor currently exists
    in the dictionary, the donor's new donation will be appended to the list stored under their name, which is the key in the dictionary. If the donor does not exist in the database, a new donor object will be created
    :param donor_collection_obj: the database of donor objects
    :param first_name: first name of the new donor, a string
    :param last_name: last name of the new donor
    """
    new_donation = [getUserValue("Donation Amount")]
    donor_collection_obj.new_donor(first_name, last_name, new_donation)
    print(donor_collection_obj.get_thank_you(first_name, last_name))

def challengeList(donor_collection_obj):
    """
    Allows the user to project how much their total contributions would be if they factored the donations by a certain amount.  For example, the user can multiply each donation that is over $500 by a factor of 2.
    :param donor_collection_obj: the donor database
    """
    factor = getUserValue("Factor")
    boundaryType = askForMinMax(donor_collection_obj)
    new_collection = None
    boundaryAmount = getUserValue("{} Boundary Type".format(boundaryType))
    if boundaryType == "Min":
        new_collection = donor_collection_obj.challenge(factor, min_donation = boundaryAmount)
    else:
        new_collection = donor_collection_obj.challenge(factor, max_donation = boundaryAmount)
    getTotalDonation(factor, new_collection)

def getTotalDonation(factor, donor_collection_obj):
    """
    Shows the user what the total donations would come to if they factored donations within a certain boundary.  The user will also see what their personal contribution is.  A detailed report of the donors whose donations could potentially be matched will also be shown.
    :param factor: The factor by which the user could multiply the current donations by
    :param donor_collection_obj: the donor database
    """
    print("\nIf each current donation within the boundary you set was multipled by {},\nthe total sum of donations would be: {}.\nYour personal contribution would be: {}.\nA detailed report of the final donations can be seen below:\n".format(factor, donor_collection_obj.sum_all_donations(), round(donor_collection_obj.sum_all_donations() / factor, 2)))
    createReport(donor_collection_obj)

def getUserValue(str_reason = "value"):
    """
    This function will ask the user for a numeric value.  This function is used when the user is entering in a new donation amount, entering a factor they would like to multiply the current donations by or setting the boundary for the specific donations they want to factor.
    :param str_reason: The reason why the user is being asked to enter in a number.  For example, str_reason will equal "donation" when the user is supposed to enter in a new donation amount.
    :return: Returns the value the user entered
    """
    invalid = True
    while invalid == True:
        try:
            user_value = float(input("Enter number for {}: ".format(str_reason)))
            if type(user_value) != float or user_value < 1:
                raise ValueError
        except ValueError:
            print("\nThe value you entered was illegal\n")
        else:
            invalid = False
    return user_value

def askForMinMax(donor_collection_obj):
    """
    Determines whether or not the user wants to include a minimum/maximum donation amount to factor
    :return: the users answer, a string
    """
    invalid = True
    while invalid == True:
        try:
            MinOrMax = input("1. Type 'min' to factor donations below a specified amount\n2. Type 'max' to factor donations above a specified amount: ")
            MinOrMax = donor_collection_obj.clean_text(MinOrMax)
            if MinOrMax != "Min" and MinOrMax != "Max":
                raise ValueError
        except ValueError:
            print("The option you entered was illegal\n")
        else:
            invalid = False
    return MinOrMax

def showDonorNames(donor_collection_obj):
    """
    Prints out the full names of each donor
    :param donor_collection_obj: The database of donors
    """
    print(donor_collection_obj.show_donors())


def writeToFile(donor_collection_obj):
    """
    Allows user to save a letter written to each donor and their donation amounts to the current working directory
    :param donor_collection_obj: The database of donor objects
    """
    donor_collection_obj.write_to_file()

def createReport(donor_collection_obj):
    """
    Allows user to create a report that shows each donor's name, total donated, number of times donated and average donations. This function calls the donor collection objects create report method, which generates the report.
    :param donor_collection_obj: The database of donor objects
    """
    print(donor_collection_obj.report_header())
    print(donor_collection_obj.create_report())

def exitMessage(donor_collection_obj):
    """
    Exit message once the user decides to end the entire program
    All of the donors stored in the donor_collection object will be printed
    a final time
    :param donor_collection_obj:The database of donor objects
    """
    print("\nThank you to the following donors for all of your donations: \n")
    showDonorNames(donor_collection_obj)
    print("\nCome back anytime to donate more!")

all_donors = DonorCollection()
initializeDonorDB(all_donors)
menu_dict = initializeOptionsDB()
menu(all_donors, menu_dict)
