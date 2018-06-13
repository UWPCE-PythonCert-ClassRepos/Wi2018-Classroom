import os
import sys
import json_save_dec as js
from json_save_meta import *


DONOR_DICT = {"Bill":[2.75,3.10], "Bob": [52.75,15.00], "Jim": [27.36,22] , "Ann": [12.76,1.24], "Beth": [31245.75,14.53]}

#################################################
"""
# This is from mailroom 3, slightly modified to work with @js.json_save
# Only real modifications are from lines 14 to 34, and mailroom().
"""
@js.json_save
class Donors_as_json:
    donor_dict = Dict()
    def __init__(self, donor_dict):
        self.donor_dict = donor_dict


def write_to_json():
    """ write it to, or read it from my_saved.json"""
    global DONOR_DICT
    write_or_read = input("Write or read? w/r\n").lower().strip()

    if write_or_read[0] == "w":
        my_donors = Donors_as_json(DONOR_DICT)
        my_donors = my_donors.to_json()
        with open("my_saved.json", "w+") as fh:
            fh.write(str(my_donors))
    elif write_or_read[0] == "r":
        with open("my_saved.json") as fh:
            new_donor_dict = js.from_json(fh)
            DONOR_DICT = new_donor_dict.donor_dict

##################################################

def send_ty():
    """Prints out a thank you letter to specified person, or to new person. Doesn't save new person to globally defined dict. We'll wait for oop to do that?"""
    while True:
        name = input("Pick or add a name! or 'list'\n")
        name = name.title()
        if name == "List":
            print("\n".join([donor for donor in DONOR_DICT.keys()]))
            continue
        if name not in [donor for donor in DONOR_DICT.keys()] and (name != "List"):
            DONOR_DICT[name] = []
            donation = input("How much did they donate?\n")
            DONOR_DICT[name].append(float(donation))
        else:
            donation = input("How much did they donate?\n")
            DONOR_DICT[name].append(float(donation))
        print(thank_you_txt(name))
        break


def thank_you_txt(name):
        return f"Dear {name},\n\n \tThanks so much for your generous donation of ${DONOR_DICT[name][-1]:.2f}.\n \tWe are all incredibly grateful because blah blah. \n\n-NGO"


def generate_report():
    print("{:16}|{:^13}|{:^11}|{:>13}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for name in DONOR_DICT:
        print("{:17}${:>12.2f} {:>11} ${:>12.2f}".format(name, sum(DONOR_DICT[name]),len(DONOR_DICT[name]), sum(DONOR_DICT[name])/len(DONOR_DICT[name])))


def send_letters():
    for name in [donor for donor in DONOR_DICT.keys()]:
        name = "_".join(name.split()) # For people with two names
        output_dir = "letters"
        filename = output_dir+"/"+name+".txt"
        try:
            with open(filename, "w+") as fh:
                fh.write(thank_you_txt(name))
        except FileNotFoundError:
            os.mkdir(output_dir)
            with open(filename, "w+") as fh:
                fh.write(thank_you_txt(name))


def quit():
    sys.exit()


def mailroom():
    """automate mail sending and report generation"""
    choice = " "
    arg_dict = {"1":send_ty, "2":generate_report, "3": send_letters, "4":quit, "5":write_to_json}
    while choice != "4":
        choice = input("Pick a number: \n1. Send thank you \n2. Create report \n3. Send letters to all donors \n4. Quit\n5. JSONify\n")
        try:
            arg_dict.get(choice)()
        except TypeError:
            print('Type "1", "2", "3", "5", or "4", without the quotes.')


if __name__ == "__main__":
    mailroom()
