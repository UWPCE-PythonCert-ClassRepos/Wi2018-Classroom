import os.path
from populate_mailroom_redis import ManipulateDBRedis

def initializeOptionsDB():
    """
    Initializes the options the user can select from. A dictionary where the key is the option the user can select and the values are the functions that are called based off of the user's selection
    :return: The options dictionary.
    """
    options_dict = {'t': askUserForDonor, 's': writeToFile, 'r': createReport, 'd': delete_instance, 'e': exitMessage}
    return options_dict

def displayMenu():
    """
    displays the menu of options to the user
    """
    str_menu = "\n1. Type 't' to add a name, donation and thank you card\n"+\
    "2. Type 'r' to Create a Report and see a list of the donors\n"+\
    "3. Type 's' to Send letters to everyone\n"+\
    "4. Type 'd' to delete a donor and their donations\n"+\
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

        user_donor_option = clean_text(user_donor_option)
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
    Prompts the user for a first name, last name, email for the donor object, regardless of whether or not the donor currently exists. The user cannot enter in a blank string as a name.
    :param donor_collection_obj: The database of donor objects
    """
    first_name = None
    last_name = None
    email = None
    invalid = True
    while invalid == True:
        try:
            first_name = input("Enter first name for donor: ")
            last_name = input("Enter last name for donor: ")
            email = input("Enter email for donor: ")
            if first_name == "" or last_name == "" or email == "":
                raise ValueError
        except ValueError as e:
            print("The name you entered is invalid. Enter proper first/last name")
        else:
            first_name, last_name = clean_text(first_name), clean_text(last_name)
            email = email.strip()
            invalid = False
    addNewDonation(donor_collection_obj, first_name, last_name, email)

def addNewDonation(donor_collection_obj, first_name, last_name, email):
    """
    Allows the user to input a new donation for the user. The user must
    enter a valid amount (integer or float).  The user must
    also enter a value greater than 0.  If the donor currently exists
    in the dictionary, the donor's new donation will be appended to the list stored under their name, which is the key in the dictionary. If the donor does not exist in the database, a new donor object will be created
    :param donor_collection_obj: the database of donor objects
    :param first_name: first name of the new donor, a string
    :param last_name: last name of the new donor
    """
    new_donation = getUserValue("Donation Amount")
    donor_collection_obj.add_donor_redis(first_name, last_name, email, new_donation)
    print(donor_collection_obj.thank_you_message(first_name, new_donation))

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

def clean_text(name):
    """
    Eliminates text of whitespace, lowercase all letters and capitalize the first letter
    """
    name = name.strip()
    name = name.lower() 
    name = name.title()
    return name

def delete_instance(donor_collection_obj):
    invalid = True
    while invalid == True:
        try:
            del_email = input("Enter email of donor you would like to delete: ")
            if del_email == "" or not donor_collection_obj.donor_exists_redis(del_email):
                raise ValueError
        except ValueError:
            print("\nEmail does not exist in database.\n")
        else:
            invalid = False
    donor_collection_obj.delete_donation_redis(del_email)



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
    report_header()
    print(donor_collection_obj.create_report())

def report_header():
    str_header = ('\n{:25s} | {:25s} | {:11s} | {:9s} | {:12s}'.format("Donor Name", "Donor Email", "Total Given", "Num Gifts", "Average Gift"))
    str_header = str_header + '\n' + ("-"*95)
    print(str_header)

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

store_donors = ManipulateDBRedis()
menu_dict = initializeOptionsDB()
menu(store_donors, menu_dict)
