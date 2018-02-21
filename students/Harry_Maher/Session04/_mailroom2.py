#!/usr/bin/env python3
'''
You work in the mail room at a local charity. Part of your job is to write incredibly boring, repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again, so you’ve decided to let Python help you out of a jam and do your work for you.
The program

Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

    You can store that data structure in the global namespace.

    The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)


if the user (you) selects ‘Send a Thank You’, prompt for a Full Name.

    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of the selected user.
    Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.


    If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
        Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
        Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
        After printing this report, return to the original prompt.
    At any point, the user should be able to quit their current task and return to the original prompt.
    From the original prompt, the user should be able to quit the script cleanly.

Your report should look something like this:

Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14



'''

import os

# Just gonna make these global cuz lazy. Eventually this will be less bad.
# Name of donor is key. Value is list w/ 2 values: total amount donated (float), number of gifts (int)
donor_dict = {"Bill":[2.75,3], "Bob": [52.75,15], "Jim": [27.36,2] , "Ann": [12.76,1], "Beth": [31245.75,1]}
donors = [donor for donor in donor_dict.keys()]


def mailroom():
    """automate mail sending and report generation"""
    choice = " "
    arg_dict = {"1":send_ty, "2":generate_report, "3": send_letters, "4":quit}
    while choice != "4":
        choice = input("Pick a number: \n1. Send thank you \n2. Create report \n3. Send letters to all donors \n4. Quit\n")
        arg_dict.get(choice)()
            
def send_ty():
    """Prints out a thank you letter to specified person, or to new person. Doesn't save new person to globally defined dict. We'll wait for oop to do that?"""
    name = input("Pick or add a name!\n")
    if name == "list":
        print("\n".join(donors))
        name = input("Pick or add a name!")
    if name not in donors and (name !="list"):
        donor_dict[name] = [0,0]
        donation = input("How much did they donate?\n")
        donor_dict[name][0]+=float(donation)
        donor_dict[name][1]+=1
    print(thank_you_txt(name))


def thank_you_txt(name):
        return "Dear {0},\n\n \tThanks so much for your generous donation of ${1:.2f}.\n \tWe are all incredibly grateful because blah blah. \n\n-NGO".format(name, donor_dict[name][0])

def generate_report():
    print("{:16}|{:^13}|{:^11}|{:>13}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for name in donors:
        print("{:17}${:>12.2f} {:>11} ${:>12.2f}".format(name, donor_dict[name][0], donor_dict[name][1],(donor_dict[name][0]/donor_dict[name][1])))

def send_letters():
    for name in donors:
        output_dir = "letters"
        filename = output_dir+"/"+name+".txt"
        try:
            with open(filename, "w+") as f:
                f.write(thank_you_txt(name))
        except FileNotFoundError:
            os.mkdir(output_dir)
            with open(filename, "w+") as f:
                f.write(thank_you_txt(name))



if __name__ == "__main__":
    mailroom()