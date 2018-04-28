#!/usr/bin/env python3

import sys

# Dictionary: keys are donors and values are lists of donations
#donor_data = {"Allen, Paul": [1000000.00, 50000.00, 300000.00],
#              "Gates, Bill": [5000000.00, 80000.00, 700000.00],
#              "Bezos, Jeff": [30000.00],
#              "Musk, Elon": [1000000.00, 30000.00],
#              "Zuckerberg, Mark": [10000.00, 50000.00, 2000.00, 400000.00]
#              }


class Donor():

    def __init__(self, name=''):
        self.name = name.strip()
        self.donation_list = list()

    def add_donation(self, amount):
        self.donation_list.append(amount)

    def get_num_donations(self):
        return len(self.donation_list)

    def get_tot_donations(self):
        return sum(self.donation_list)

    def get_last_donation(self):
        return self.donation_list[-1]

    def get_avg_donation(self):
        try:
            return self.get_tot_donations() / self.get_num_donations()
        except ZeroDivisionError:
            return 0.0

    @staticmethod
    def split_name(name):
        '''
        split donor name and reverse the order
        param: donor name
        return: donor name in the form of "First name, Last name"
        '''
        first_name = name.split(",")[1].strip()
        last_name = name.split(",")[0].strip()
        return first_name, last_name

    def make_donor_dict(self):
        """
        return dictionary containing first name, last name, and donation amount
        params: name of donor and donation amount
        """
        donor_dict = {}
        donor = self.name
        donor_dict["first name"], donor_dict["last name"] = self.split_name(donor)
        donor_dict["amt"] = self.get_last_donation()
        return donor_dict

    def make_donor_email(self, dct):
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


class DonorCollection():

    def __init__(self):
        self.donor_list = list()

    def add_donor(self, donor):
        self.donor_list.append(donor)

    def find_donor(self, searchName):
        result = None
        for donor in self.donor_list:
            if donor.name.lower() == searchName.strip().lower():
                result = donor
                break
        return result

    def make_donor_list(self):
        """makes alphabetical list of donors."""
#        return sorted(self.donor_list)
        donor_sort = []
        for donor in self.donor_list:
            donor_sort.append(donor.name)
        donor_sort = sorted(donor_sort)
        for donorname in donor_sort:
            print(donorname)
#        print(sorted([donorname for donorname in donor_sort]))

    def make_letter_files(self):
        '''write thank you letter as text files for each donor and save to disk'''
        letter_dict = {}
        for donor in self.donor_list:
            letter_dict["first name"], letter_dict["last name"] = Donor.split_name(donor.name)
            letter_dict["amt"] = donor.get_last_donation()
            with open('{last name}_{first name}.txt'.format(**letter_dict), 'w') as outfile:
                outfile.write(donor.make_donor_email(letter_dict))
        print("Thank you letter have been sent!")

#    def sort_key(item):
#        """return second item in sequence for sorting donor report"""
#        return item[1]

    def make_report(self):
        """print full donor report to terminal"""
        report = []
        report.append("{:20s}{:14s} {:14s}{:15s}".format(
            "Donor Name", "|  Total Given", "|  Num Gifts", "|  Average Gift"))
        report.append("_" * 67)
        report_lst = []
        for donor in self.donor_list:
            report_lst.append('{:20s} ${:12.2f}{:^15d}  ${:11.2f}'.format(donor.name, donor.get_tot_donations(), donor.get_num_donations(), donor.get_avg_donation()))
            report_lst = sorted(report_lst)
        for donor_info in report_lst:
            report.append(donor_info)
        return "\n".join(report)


donors = DonorCollection()


def donor_selection(name=False):
    if not name:
        name = input("Please enter a donor's name in the form of 'Last name, First name' "
        "(or 'list' to see a list of all donors, or 'menu' to exit)> ")
    return name.title()


def get_donor_name(name=None):
    """handle exceptions and return donor name"""
    while True:
        if not name:
            name = donor_selection()
        if name.strip().lower() == "list":
            donors.make_donor_list()
            #[print(donor) for donor in show_list]
            #break
            name = None
        elif name.strip().lower() == "menu":
            return None
        else:
            try:  # test for two names separated by comma
                first, last = Donor.split_name(name)
                name = last + ", " + first
            except IndexError:
                print("Error: Please enter a last name and first name seperated by a comma!")
                name = None
            else:
                return name


def donation_selection(amount_str=False):
    if not amount_str:
        amount_str = input("Please enter a donation amount (or 'menu' to exit)> ") 
    return str(amount_str)


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
                donation = None
            else:
                return amount


def send_donor_email(name=False, amount=False):
    """print thank you message to terminal"""
    if not name:
        name = get_donor_name()
    if name is None:
        return None
    if not amount:
        amount = get_donation_amount()
    if amount is None:
        return None
    current_donor = donors.find_donor(name)
    if current_donor is None:
        current_donor = Donor(name)
        donors.add_donor(current_donor)
    current_donor.add_donation(amount)
    donor_dic = current_donor.make_donor_dict()
    email = current_donor.make_donor_email(donor_dic)
    #return email
    print(email)
    #print(make_donor_email(donor_dic))


def print_report():
    print(donors.make_report())


def quit_program():
    print("Tha come again!")
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
                     "2": print_report,
                     "3": donors.make_letter_files,
                     "4": quit_program
                     }

    while running:
        response = menu_selection()
        try:
            dispatch_dict[response]()
        except KeyError:
            print("Error: Please select a valid menu option")

