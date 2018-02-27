#!/usr/bin/env python
# Programming in python B Winter 2018
# February 12, 2017
# Mailroom Session 4
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


donor_data = {"Allen, Paul": [1000000, 50000, 300000],
              "Gates, Bill": [5000000, 80000, 700000],
              "Warren, Buffett": [30000, 30000, 40000],
              "Musk, Elon": [1000000, 30000],
              "Zuckerberg, Mark": [10000, 50000, 12000, 400000]}


def show_list():
    donor_data = []
    for donor in donor_data:
        donor_data.append(donor)
    sort_donors = sorted(donor_data)
    for donor in sort_donors:
        print(donor[0])


def get_donor(name):
    """retieve donor form donor_data list
    :param: name of donor
    :returns: donor tuple
    """
    for donor in donor_data:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None

# Find Donor
# def find_donor(name):
#     key = name.title().strip()
#     donations = donor_data.get(key)
#     print("{} has donated the following:".format(key))
#     print(total)


# # Add donor
# def add_donor(name):
#     name = name.title().strip()
#     donor_data[name] = []
#     return name


def add_donor_info(name, donor_db):
    """ Add donor info or add a new donor
    :params: name/string/name of donor db key, donor_db: dictionary of
    donor names/amts.
        :return:
    """
    if name == "list" or name == "menu":
        print('Please select a name other than list or menu.')
        return 12
    if name not in donor_db:
        "create a name in the donor_db if it does not already exist"
        donor_db.update({name.lower(): []})

    try:
        amount = input("Enter amount of donor's contribution "
                       "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        donor_db[name].append(float(amount))
    except ValueError:
        print("\nPlease resubmit a the donor amount information in \
            dollars and cents with a format matching: 10.11\n")
    return


def init_prompt():
    response = input('''\n
        Would you like to:
        '1' - Send a Thank You
        '2' - Create a Report
        '3' - Send letters to everyone
        '4' - Quit
        > ''')
    return response.strip()


def split_name(donor):
    """ I can now split the names into first and last name"""
    first_name = donor.split(",")[1].strip()
    last_name = donor.split(",")[0].strip()
    return first_name, last_name


def create_letter_files():
    """This will write the letter as a text file for the donors"""
    letter_dict = {}
    for donor in donor_data:
        letter_dict["first name"], letter_dict["last name"] = split_name(donor)
        letter_dict["amt"] = donor_data[donor][-1]
        with open('{last name}_{first name}.txt'.format(**letter_dict), 'w') as outfile:
            outfile.write(make_donor_email(letter_dict))


def make_donor_email(d):
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
                    '''.format(**d)


def send_donor_email():
    donor_dict = {}
    while True:
        name = input("Please enter a donor's name in the form of \
         'Last name, First name' "
                     "(or 'list' to see a list of all donors, \
                     or 'menu' to exit)> ").strip()
        if name == "list":
            show_list()
        elif name == "menu":
            return None
        else:
            break
    while True:
        amount_str = input("Please enter a donation amount \
         (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return None
        else:
            amount = float(amount_str)
        donor = get_donor(name)
        if donor is None:
            donor_data.setdefault(name, [])
            donor_dict["first name"], donor_dict["last name"] = split_name(name)
        donor_data[name].append(amount)
        donor_dict["amt"] = amount
        break
    print(make_donor_email(donor_dict))


def sort_key(item):
    """ key function used to sort the list by first (not zeroth) item"""
    return item[1]


def make_report():
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
    for row in rows:
        print('{:20s}{:15.2f}{:^15d}{:12.2f}'.format(*row))


if __name__ == "__main__":
    running = True
    while running:
        selection = init_prompt()
        if selection == "1":
            send_donor_email()
        elif selection == "2":
            make_report()
        elif selection == "3":
            create_letter_files()
        elif selection == "4":
            running = False
        else:
            print("error: please make a valid selection!")
