import os
import json_save_meta as js 

class JsonMailroom(js.JsonSaveable):
    donor_json_dict = js.Dict()

    def __init__(self, donor_db):
        self.donor_json_dict = donor_db 

def save_json(donor_list):
    json_obj = JsonMailroom(donor_list)
    json_compat = json_obj.to_json()
    try:
        with open('mailroom_json.json', 'w') as f:
            f.write(json_compat)
    except IOError:
        print("Unable to save donor database")

def load_json():
    try:
        with open('mailroom_json.json', 'r') as f:
            contents = f.read()
    except IOError:
        print("Unable to load donor database")

    if contents:
        json_donor = js.from_json(contents)
    print(json_donor)

def menu(donor_list):
    """This function will print out a menu of options for
    the user to choose from
    :param: the list of donors and how much they have donated"""
    user_option = ""
    while user_option.lower() != 'e':
        displayMenu()
        user_option = input("Select an option from the menu: ")
        if user_option.lower() == 't':
            addNewDonation(donor_list)
        elif user_option.lower() == 'r':
            createReport(donor_list)
        elif user_option.lower() == 's':
            writeToFile(donor_list)
        elif user_option.lower() == 'e':
            print("Thank you for all of the donations!")
        elif user_option.lower() == 'j':
            save_json(donor_list)
        elif user_option.lower() == 'l':
            load_json()
        else:
            print("That is not a valid option you chose")

def displayMenu():
    """
    displays the menu of options to the user
    :return:
    """
    print()
    str_menu = "1. Type 't' to Send a Thank You to add a name, donation and thank you card\n"  \
               "2. Type 'r' to Create a Report and see a list of the donors\n" \
               "3. Type 's' to Send letters to everyone\n" \
               "4. Type 'j' to save as JSON\n" \
               "5. Type 'l' (lowercase 'L') to load JSON\n" \
               "6. Type 'e' to exit the program"
    print(str_menu)
    print()

def addNewDonation(donor_list):
    """
    Allows user to add a new donor and their donation to the list
    :param donor_list: the list of donors and their donations
    """
    new_donor = input("1. Enter the name of a new donor\n"
                      "2. Type 'list' to list the donor names\n"
                      "3. Type 'exit' to return to main menu\n"
                      "Your Selection:  ")
    print()
    if new_donor.lower() == 'list':
        showDonorNames(donor_list)
    elif new_donor.lower() == 'exit':
        return
    else:
        try:
            new_donation = float(input("Enter a new donation amount: "))
        except ValueError as e:
            print("The amount you entered is an invalid value.")
        else:
            while new_donation < 1:
                new_donation = float(input("Enter something greater than 0: "))
            if new_donor.strip() in donor_list:
                donor_list[new_donor].append(new_donation)
            else:
                donor_list[new_donor.strip()] = [new_donation]
            printThankYou(new_donor, new_donation)

def showDonorNames(donor_list):
    """
    will show the unique names of donors.  Will use comprehension to print
    out the donor names
    :param donor_list: the list of donors and their donations
    """
    print("Here are the list of donors: ")
    [print(donor) for donor in donor_list.keys()]
    #for donor in donor_list.keys():
     #   print(donor)

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
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)

def createReport(donor_list):
    """
    Creates a table of the report that shows the donor names, how many times they donated
    the average donation and total donations
    :param donor_list: the list of donors and their donation amounts
    """
    total_give = 0.00
    num_gifts = 0
    avg_gift = 0
    report_dict = {}
    for donor, donations in donor_list.items():
        num_gifts = len(donations)
        total_give = sum(donations)
        avg_gift = total_give / num_gifts
        report_dict[donor] = [round(total_give,2), num_gifts, round(avg_gift, 2)]
    reportHeader()
    for donor, metrics in report_dict.items():
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(donor, metrics[0], metrics[1], metrics[2]))

def writeToFile(donor_list):
    """
    Writes thank you letters for each individual that has donated and saves the file
    in the current working directory.
    :param donor_list: the dictionary of donors and the values each donor has donated
    """
    letter = None
    filename = None
    donor_file_name = None
    complete_file_name = None
    #path = 'C:\\Users\\navgill\Wi2018-Classroom\students\\navdeep\session04\Letters'
    for donor,donations in donor_list.items():
        donor_file_name = donor.replace(" ", "_")
        full_file_name = "{}.txt".format(donor_file_name)
        complete_file_name = os.path.join(os.getcwd(), full_file_name)
        letter = letterToSend(donor,donations)
        with open(complete_file_name,'w+') as f:
            f.write(letter)
        f.close()

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

donors = {"Navdeep Gill": [1000], "Nick Garzon": [5, 2], "Henry Chipman": [100],
          "Lorenzo B": [1000], "Torin Stetina": [200.75]}

menu(donors)