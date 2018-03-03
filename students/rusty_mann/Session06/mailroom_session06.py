#!/usr/bin/env python3

import sys

#Dictionary: keys are donors and values are lists of donations
donor_data = {"Allen, Paul": [1000000.00, 50000.00, 300000.00], 
                    "Gates, Bill": [5000000.00, 80000.00, 700000.00], 
                    "Bezos, Jeff": [30000.00], 
                    "Musk, Elon": [1000000.00, 30000.00], 
                    "Zuckerberg, Mark": [10000.00, 50000.00, 2000.00, 400000.00]
                    }


def show_donor_list():
    """print list of donors to terminal."""
    donor_list = [donor for donor in donor_data]
    sort_donors = sorted(donor_list)
    [print(donor) for donor in sort_donors]


def get_donor(name):
    """
    retieve donor form donor_data list
    :param: name of donor
    :returns: donor tuple
    """
    for donor in donor_data:
        if name.strip().lower() == donor.lower():
            return donor
    return None


def split_name(name):
    '''
    split donor name and reverse the order
    param: donor name
    return: donor name in the form of "First name, Last name"
    '''
    first_name = name.split(",")[1].strip()
    last_name = name.split(",")[0].strip()
    return first_name, last_name


def make_letter_files():
    '''write thank you letter as text files for each donor and save to disk'''
    letter_dict = {}
    for donor in donor_data:
        letter_dict["first name"], letter_dict["last name"] = split_name(donor)
        letter_dict["amt"] = donor_data[donor][-1]
        with open('{last name}_{first name}.txt'.format(**letter_dict), 'w') as outfile:
            outfile.write(make_donor_email(letter_dict))


def make_donor_email(dct):
    """
    make a thank you email for the donor
    param: donor tuple
    returns: string containing text of email
    """
    return '''\n
        Dear {first name} {last name}, 
        Thank you for your donation of ${amt:.2f}.
        You are a good person.
                            Sincerely,
                            -Me
        '''.format(**dct)


def make_donor_dict(name, amount):
    """
    return dictionary containing first name, last name, and donation amount
    params: name of donor and donation amount
    """
    donor_dict = {}
    donor = get_donor(name)
    donor_dict["first name"], donor_dict["last name"] = split_name(donor)
    donor_dict["amt"] = amount
    return donor_dict


def add_donor(name, amount):
    """add donor to donor_data database"""
    donor = get_donor(name)
    if donor is None:
        donor_data.setdefault(name, [])
    donor_data [name].append(amount)
    return donor_data


def donor_selection(name=False):
    if not name:
        name = input("Please enter a donor's name in the form of 'Last name, First name' "
        "(or 'list' to see a list of all donors, or 'menu' to exit)> ")
    return name.title()


def get_donor_name(name=False):
    """handle exceptions and return donor name"""
    while True:
        if not name:
            name = donor_selection()
        if name.strip().lower() == "list":
            show_donor_list()
            break
        elif name.strip().lower() == "menu":
            return None
        else:
            try:
                first, last = split_name(name)
                name = last + ", " + first
            except IndexError:
                print("Error: Please enter a last name and first name seperated by a comma!")
                #break
            else:
                return name


def donation_selection(amount_str):
    if not amount_str:
        amount_str = str(input("Please enter a donation amount (or 'menu' to exit)> ")) 
    return amount_str


def get_donation_amount(donation=False):
    """handle exceptions and return donation amount"""
    while True:
        if not donation:
            donation = donation_selection()
        if donation.strip().lower() == "menu":
            return None
        else:
            try:
                amount = float(donation)
            except ValueError:
                print("Error: Please enter a number")
                #break
            else:
                return amount


def send_donor_email(name=False, amount=False):
    """print thank you message to terminal"""
    if not name:
        name = get_donor_name()
        if name == None:
            return None
    if not amount:
        amount = get_donation_amount()
        if amount == None:
            return None
    add_donor(name, amount)
    donor_dic = make_donor_dict(name, amount)
    print(make_donor_email(donor_dic))


def sort_key(item):
    """return second item in sequence for sorting donor report"""
    return item[1]


def make_report():
    """print full donor report to terminal"""
    rows = []
    for donor in donor_data:
        total = sum(donor_data[donor])
        num = len(donor_data[donor])
        avg = total / num
        rows.append((donor, total, num, avg))
    rows.sort(key=sort_key, reverse=True)
    print("{:20s}{:15s}{:15s}{:12s}".format(
        "Donor Name", "|  Total Given", "|  Num Gifts", "|  Average Gift"))
    print("_" * 67)
    [print('{:20s}{:15.2f}{:^15d}{:12.2f}'.format(*row)) for row in rows]


def quit_program():
    print("Thank you, come again!")
    sys.exit(0)


def menu_selection():
    selection = input('''\n

                Would you like to:

                '1' - Send a Thank You 
                '2' - Create a Report
                '3' - Send letters to everyone 
                '4' - Quit
                > ''')
    return selection


if __name__ == "__main__":

    running = True

    dispatch_dict = {"1": send_donor_email,
                           "2": make_report,
                           "3": make_letter_files,
                           "4": quit_program
                           }

    while running:
        response = menu_selection()
        try:
            dispatch_dict[response]()
        except KeyError:
            print("Error: Please select a valid menu option")


