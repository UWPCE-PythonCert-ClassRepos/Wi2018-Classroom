#!/usr/bin/env python3
import os
from datetime import datetime

donate = {'Merv': [10, 500, 100], 'Linda': [300, 62, 7], 'Larry': [25, 50, 100], 'Sue': [20, 50, 1000]}


def thankYou():
    """Add new donations to record and display a thank you note when provided a name and donation amount."""

    resp = input("Type 'list' to see donor list, otherwise, type a name or leave blank to quit:  ")
    if resp == "":
        quit()
    if resp == 'list':
        print(donate.keys())
    else:
        name = resp
        try:
            amount = input("Please input the donation amount or leave blank to quit:  ")
            if amount == "":
                quit()
            amount = int(amount)
            donate[name].append(int(amount))
        except ValueError:
            print('Donation amount must be a number. Restarting...')
            thankYou()
        except KeyError:
            donate[name] = [int(amount)]
            print(
                f"{resp},\n\nThank you for your gift of {amount} dollars. Your donation will be put to good use.\n\n - The Team")
    return True


def createReport():
    donateReport = []
    """Print donors names, total donations, # of donations, and avg donation- sorted highest to lowest total donation"""

    # Calculate donation summary for each donor and add to the report
    for name, gifts in donate.items():
        donateReport.append([name, sum(gifts), len(gifts), total // count])

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
        total = sum(gifts)
        with open(donor + '_' + str(datetime.now().date()) + '.txt', 'w+') as f:
            f.write(
                f"{donor},\n\nThank you for your gift of {total} dollars. Your donation will be put to good use.\n\n - The Team")
    print(f"\nLetters have been saved to the {response} directory.\n")


# Prompt with menu
switcher = {'1': thankYou, '2': createReport, '3': letters, '0': quit}
while True:
    res = input(
        "Type '1' to send a thank you. \nType '2' to create a report. \nType '3' to send letters. \nType '0' to quit:  ")
    switcher[res]()
