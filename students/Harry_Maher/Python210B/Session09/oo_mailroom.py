#!/usr/env/bin python3
"""
object oriented version of mailroom. 
"""
import os

class Donors:
    """Class that stores Donor instances in dict like: {donor name: Donor_instance} W/ related methods"""
    def __init__(self, donor_dict = None):
        if donor_dict == None:
            self.donor_dict = {}
        else:
            self.donor_dict = donor_dict


    def new_donor(self, donor_name, donor):
        self.donor_dict[donor_name] = donor


    @property
    def list_of_names(self):
        return [donor.name for donor in self.donor_dict.values()]


    def generate_report(self):
        """print a report of donation averages by donor."""
        report = "{:16}|{:^13}|{:^11}|{:>13}\n"\
        .format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        for donor in self.donor_dict.values():
            report+="{:17}${:>12.2f} {:>11} ${:>12.2f}\n"\
            .format(donor.formatted, donor.total_donated, donor.number_donations, donor.average_donation)
        print(report)
        return report


    def pick_ty_recipient(self):
        name = input("Pick or add a name (or type list)!\n").strip().title().replace(" ", "_")
        if name.lower() == "list":
            print("\n".join([donor.formatted for donor in self.donor_dict.values()]))
            # If some fool wants to keep typing "list" for some reason:
            name = self.pick_ty_recipient() 
        return name


    def send_letters(self):
        for donor in self.donor_dict.values():
            output_dir = "letters"
            filename = output_dir+"/"+donor.name+".txt"
            print(donor.thank_you_txt)
            try:
                with open(filename, "w+") as f:
                    f.write(donor.thank_you_txt)
            except FileNotFoundError:
                os.mkdir(output_dir)
                with open(filename, "w+") as f:
                    f.write(donor.thank_you_txt)


class Donor:
    """Class that's a list of donations for each donor w/ related property/methods"""
    def __init__(self, name):
        self.name = name
        self.donations = []

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def total_donated(self):
        return sum(self.donations)

    @property
    def number_donations(self):
        return len(self.donations)

    @property
    def average_donation(self):
        return self.total_donated / self.number_donations

    @property
    def formatted(self):
        return self.name.replace("_", " ")

    @property
    def thank_you_txt(self):
        return f"""Dear {self.formatted},\n\n \tThanks so much for your generous
        donations totaling ${self.total_donated:.2f}.  We are
        all incredibly grateful because blah blah. 
        -NGO"""


donors = Donors()

def send_ty(name = None): #ideally break this up, but whatever.
    """Prints out a thank you letter to specified person, or to new person."""
    if name == None:
        name = donors.pick_ty_recipient()
    try:
        donation = float(input("How much did they donate?\n"))
    except ValueError:
        print("Donation needs to be a number.")
        send_ty(name)
    if name not in donors.list_of_names:
        new_donor_instance = Donor(name)
        new_donor_instance.add_donation(donation)
        donors.new_donor(name, new_donor_instance)
        print(new_donor_instance.thank_you_txt)
    else:
        donors.donor_dict[name].add_donation(float(donation))
        print(donors.donor_dict[name].thank_you_txt)
   

def generate_report():
    donors.generate_report()


def send_letters():
    donors.send_letters()


def quit():
    pass


def print_error():
    print("pick a number from 1 to 4!")


def main():
    choice, choices = "", "Pick a number: \n\
    1. Send thank you \n\
    2. Create report \n\
    3. Send letters to all donors \n\
    4. Quit\n"
    arg_dict = {"1":send_ty, "2":generate_report, "3": send_letters, "4":quit}
    while choice != "4":
        choice = input(choices)
        arg_dict.get(choice, print_error)()     


if __name__ == "__main__":
    main()