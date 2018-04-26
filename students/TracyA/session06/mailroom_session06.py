#!/usr/bin/env python
import sys

# Programming in python B Winter 2018
# February 12, 2017
# Mailroom Session 5
# Refactored
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


donor_data = {"Allen, Paul": [1000000.00, 50000.00, 300000.00],
              "Gates, Bill": [5000000.00, 80000.00, 700000.00],
              "Warren, Buffett": [30000.00, 30000.00, 40000.00],
              "Musk, Elon": [1000000.00, 30000.00],
              "Zuckerberg, Mark": [10000.00, 50000.00, 12000.00, 400000.00]}


# Donor data comprehension
def show_list():
    donor_list = [donor for donor in donor_data]
    sort_donors = sorted(donor_list)
    [print(donor) for donor in sort_donors]


def get_donor(name):
    """retieve donor form donor_data list
    :param: name of donor
    :returns: donor tuple
    """
    for donor in donor_data:
        if name.strip().lower() == donor.lower():
            return donor


# Find Donor
# def find_donor(name):
#     key = name.title().strip()
#     donations = donor_data.get(key)
#     print("{} has donated the following: {}".format(key, total))
#     print(total)


# Add donor
def add_donor(name, amount):
    """add donor to donor database"""
    donor = get_donor(name)
    if donor is None:
        donor_data.setdefault(name, [])
    donor_data[name].append(amount)


def make_donor_dict(name, amount):
    """First name, last name and donation amount"""
    donor_dict = {}
    donor = get_donor(name)
    donor_dict["first name"], donor_dict["last name"] = split_name(donor)
    donor_dict["amt"] = amount
    return donor_dict


def donor_selection():
    name = input("Please enter a donor's name in the form "
                 "of 'Last Name, First name'. \n Enter 'list' to see a list of "
                 "donors or 'menu' to exit > ").title()
    return name


def get_donor_name():
    """Attempt to break up and handle exceptions"""
    while True:
        name = donor_selection()
        if name == "List":
            show_list()
        elif name == "Menu":
            return None
        else:
            try:
                first, last = split_name(name)
                name = last + ", " + first
            except IndexError:
                print("Please enter a full name: ""Last name"", ""First name "": ")
            else:
                return name


def donation_selection():
    amount_str = str(input("Please enter a donation amount (or 'menu' to exit) > "))
    return amount_str


def get_donation_amount():
    """ Attempt to break out donations """
    while True:
        donation = donation_selection()
        if donation == "menu".strip().lower():
            return None
        else:
            try:
                amount = float(donation)
            except ValueError:
                print("Error: Please enter a number")
            else:
                return amount


def split_name(name):
    """ I can now split the names into first and last name"""
    first_name = name.split(",")[1].strip()
    last_name = name.split(",")[0].strip()
    return first_name, last_name


def create_letter_files():
    """This will write the letter as a text file for the donors"""
    letter_dict = {}
    for donor in donor_data:
        letter_dict["first name"], letter_dict["last name"] = split_name(donor)
        letter_dict["amt"] = donor_data[donor][-1]
        with open('{last name}_{first name}.txt'.format
                  (**letter_dict), 'w') as outfile:
            outfile.write(make_donor_email(letter_dict))


def make_donor_email(dct):
    """
    Make a thank you email for the donor
    :param: donor tuple
    returns: string containing text of email1
    """
    return '''\n
        Dear {first name} {last name},
        Thank you for you1r donation of ${amt: .2f}.
        You will be blessed.
                    Sincerely,
                    -Director
                    '''.format(**dct)


def send_donor_email():
    """Print thank you message to the screen"""
    name = get_donor_name()
    if name is None:
        return None
    amount = get_donation_amount()
    if amount is None:
        return None
    add_donor(name, amount)
    donor_dict = make_donor_dict(name, amount)
    print(make_donor_email(donor_dict))


def sort_key(item):
    """ key function used to sort the list by first (not zeroth) item"""
    return item[1]


def quit_program():
    print("Thank you, come again!")
    sys.exit(0)


def make_report():
    """Generate the report of the donors and amounts donated.
    :returns: the donor report as a string.
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for donor in donor_data:
        total = sum(donor_data[donor])
        num = len(donor_data[donor])
        avg = total / num
        report_rows.append((donor, total, num, avg))

    # sort the report data
    report_rows.sort(key=sort_key, reverse=True)
    report = []
    report.append("{:20s} | {:11s} | {:15s} | {:12s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))

    report.append("-" * 67)
    for row in report_rows:
        report.append("{:20s}${:15.2f}{:^15d}${:12.2f}".format(*row))
    return "\n".join(report)


def print_donor_report():
    print(make_report())


def init_prompt():
    answer = input('''\n
        Would you like to:
        '1' - Send a Thank You
        '2' - Create a Report
        '3' - Send letters to everyone
        '4' - Quit
        > ''')
    return answer


if __name__ == "__main__":
    running = True

    dispatch_dictionary = {"1": send_donor_email,
                           "2": print_donor_report,
                           "3": create_letter_files,
                           "4": quit_program}
    while running:
        response = init_prompt()
        try:
            dispatch_dictionary[response]()
        except KeyError:
            print("error: please make a valid selection!")
