#!/usr/bin/env python3
import os
from datetime import datetime

donate = {'Merv': [10, 500, 100], 'Linda': [300, 62, 7], 'Larry': [25, 50, 100], 'Sue': [20, 50, 1000]}

def sendThankYou(name=False, amount=False):
    """Add new donations to record and displays a thank you note when provided a NAME and donation AMOUNT."""
    if not name:
        name = promptForName()
    if not amount:
        amount = promptForAmount()
    recordDonation(name, amount)
    print(thankYouNote(name, amount))


def recordDonation(name, amount):
    try:
        donate[name].append(amount)
    except KeyError:
        donate[name] = [amount]


def thankYouNote(name, amount):
    """Return string containing thank you note message which is customized for given NAME and donation AMOUNT"""
    return f"{name},\n\nThank you for your gift of {amount} dollars. Your donation will be put to good use.\n\n - The Team"



def promptForName():
    name = input("\nPlease enter the donor's name. Type 'list' to display all donors or leave blank to quit.\n")

    if name == "":
        quit()
    elif name == 'list':
        print(donate.keys())
        promptForName()
    else:
        return name


def promptForAmount():
    try:
        amount = input("\nPlease enter the donation amount or leave blank to quit:\n")
        if amount == "":
            quit()
        amount = int(amount)
        return amount
    except ValueError:
        print('Donation amount must be a number.')
        promptForAmount()


###############


def createReport():
    """Print donors names, total donations, # of donations, and avg donation- sorted highest to lowest total donation"""

    # Calculate donation summary for each donor and add to the report
    donateReport = [[name, sum(gifts), len(gifts), sum(gifts) // len(gifts)] for name, gifts in donate.items()]

    # get total donations for sort
    def totalDonations(elem):
        return elem[1]

    # sort donations report for highest total donations
    sortedDonateReport = sorted(donateReport, key=totalDonations, reverse=True)

    # format row (left align - column 10 wide, right align - column 20 wide, right align - column 20 wide)
    row = '{:<10}{:>20}{:>20}{:>20}'

    def printLine():
        line = ['-' * 10, '-' * 20, '-' * 20, '-' * 20]  # line break (multipliers set to match width defined above)
        print(row.format(*line))

    def printHeader():
        header = ['Donor Name', 'Total ($)', 'Count', 'Average ($)']
        print(row.format(*header))

    # print report header with column titles
    printLine()
    printHeader()
    printLine()

    # print donation summary sorted
    for record in sortedDonateReport:
        print(row.format(*record))

    # print report footer
    printLine()

def letters():
    """For all the donors in the donor data structure, generate a thank you letter, and write it to disk as a text file."""

    response = input("Type the directory where these letters should be saved:  ")
    os.chdir(response)
    for donor, gifts in donate.items():
        with open(donor + '_' + str(datetime.now().date()) + '.txt', 'w+') as f:
            f.write(thankYouNote(donor, sum(gifts)))
    print(f"\nLetters have been saved to the {response} directory.\n")



# Prompt with menu
switcher = {'1': sendThankYou, '2': createReport, '3': letters, '0': quit}
"""
while True:
    res = input("\nType '1' to send a thank you. \nType '2' to create a report. \nType '3' to send letters. \nType '0' to quit.\n")
    switcher[res]()
"""
