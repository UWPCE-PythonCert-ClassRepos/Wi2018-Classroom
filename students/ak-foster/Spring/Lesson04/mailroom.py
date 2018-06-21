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
    """Record donation as an entry in the data structure."""
    try:
        donate[name].append(amount)
    except KeyError:
        donate[name] = [amount]


def thankYouNote(name, amount):
    """Return string containing thank you note message which is customized for given NAME and donation AMOUNT"""
    return f"{name},\n\nThank you for your gift of {amount} dollars. Your donation will be put to good use.\n\n - The Team"

class Prompt:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount




def promptForAmount(amount=False):
    if not amount:
        amount = input("\nPlease enter the donation amount or leave blank to quit:\n")
    try:
        if amount == "":
            quit()
        amount = int(amount)
        return amount
    except ValueError:
        print('Donation amount must be a number.')
        promptForAmount()


def createReport(test=False):
    """Print donors names, total donations, # of donations, and avg donation- sorted highest to lowest total donation"""

    # Calculate donation summary for each donor and add to the report
    donateReport = [[name, sum(gifts), len(gifts), sum(gifts) // len(gifts)] for name, gifts in donate.items()]

    # sort donations report for highest total donations
    sortedDonateReport = sorted(donateReport, key=lambda i: i[1], reverse=True)

    # format row (left align - column 10 wide, right align - column 20 wide, right align - column 20 wide)
    row = '{:<10}{:>20}{:>20}{:>20}'

    line = ['-' * 10, '-' * 20, '-' * 20, '-' * 20]  # line break (multipliers set to match width defined above)
    line = row.format(*line)

    header = ['Donor Name', 'Total ($)', 'Count', 'Average ($)']
    header = row.format(*header)

    # print report header with column titles
    print(line)
    print(header)
    print(line)

    # print donation summary sorted
    for record in sortedDonateReport:
        print(row.format(*record))

    # print report footer
    print(line)
    if test:
        return sortedDonateReport


def letters(filePath=False):
    """For all the donors, generate a thank you letter and write it to disk as a text file."""
    if not filePath:
        filePath = promptForDir()
    promptForDir(filePath)
    saveLetters()
    print(f"\nLetters have been saved to the {filePath} directory.\n")


def promptForDir(filePath=False):
    """Get directory from user and create if directory doesn't exist, then change to the directory."""

    if not filePath:
        filePath = input("Please enter the directory where these letters should be saved:\n")
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    os.chdir(filePath)
    return filePath


def saveLetters():
    """Write a thank you letter for each donor to a file in the current working directory."""
    for donor, gifts in donate.items():
        with open(donor + '_' + str(datetime.now().date()) + '.txt', 'w+') as f:
            f.write(thankYouNote(donor, sum(gifts)))

# Prompt with menu
switcher = {'1': sendThankYou, '2': createReport, '3': letters, '0': quit}
"""
while True:
    res = input("\nType '1' to send a thank you. \nType '2' to create a report. \nType '3' to send letters. \nType '0' to quit.\n")
    switcher[res]()
"""
import logging

logging.critical("This is a critical error!")
logging.error("I'm an error.")
logging.warning("Hello! I'm a warning!")
logging.info("This is some information.")
logging.debug("Perhaps this information will help you find your problem?")
