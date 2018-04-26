#!/usr/bin/env python
import donor as dr
import reporting as rp


# Programming in python B Winter 2018
# March 17, 2018
# Mailroom Session 9 - Reporting
# Refactored
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# -- Processing --#
def get_user_choice():
    '''Generates a main menu selection (1-4) for user actions.'''
    print("""
    MailRoom OOP Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Send Letters To Everyone
    4) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 4]: ")
    return (user_choice.strip())


def process_menu(menu_item):
    '''Process the main menu selection from user action.
    Item-1 continues into the thank you letter prompts, Item-2 creates a list
    of donors and a donation report on the screen, Item-3 saves individual
    giving reports to disk as text files.'''
    if menu_item == '1':
        send_thanks()
    elif menu_item == '2':
        dr.Donor_object.print_screen_report(donor_obj)
    elif menu_item == '3':
        print(dr.Donor_object.create_individual_letters(donor_obj))


def send_thanks():
    '''Prompts the user for a donor name, pre-existing or new.'''
    while (True):
        name = input("Please enter FULL NAME, enter 'LIST' for names, or 'MAIN' for menu: ")
        if name.lower() == "list":
            print(str(donor_obj) + "\n")
        elif name.lower() == "main":
            return
        else:
            process_thank_you(name)


def process_thank_you(name):
    '''Prompt the user for a donation amount following the prompt for
     donor name.'''
    try:
        gift_amount = int(input("Please enter donation $ AMOUNT for " + name
                                + ":"))
        if name in donor_dict.keys():
            original_list = donor_dict.get(name)
            original_list.append(gift_amount)
            donor_dict[name] = original_list
            rp.Reports.thank_you_printing(name, gift_amount)
        else:
            # new name
            donor_dict[name] = [gift_amount]
            rp.Reports.thank_you_printing(name, gift_amount)

    except ValueError as e:
        print("\n Error: " + str(e) + "\nPlease enter a number amount:\n ")
        process_thank_you(name)


# -- Presentation (Input/Output) --#
if __name__ == '__main__':

    donor_dict = {
        'Paul Allen': [1000000.00, 50000.00, 300000.00],
        'Bill Gates': [500000.00, 80000.00, 70000.00],
        'Warren Buffett': [30000.00, 30000.00, 40000.00],
        'Elon Musk': [1000000.00, 30000.00],
        'Mark Zuckerberg': [10000.00, 50000.00, 12000.00, 400000.00]}
    donor_obj = dr.Donor_object(donor_dict)

    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "4":
            print("Goodbye!")
            break
        else:
            process_menu(get_user_action)
