#!/usr/bin/env python3

donate = {'Merv': [10, 500, 100], 'Linda': [300, 62, 7], 'Larry': [25, 50, 100], 'Sue': [20, 50, 1000]}

def thankYou():
    """Add new donations to record and display a thank you note when provided a name and donation amount."""

    resp = input("Type 'list' to see donor list, otherwise, type a name or leave blank to quit:  ")
    if resp == "":
        quit()
    if resp == 'list':
        print(donate.keys())
    else:
        for name, gifts in donate.items():
            countMatches = 0
            if resp in donate:
                amount = input("Please input the donation amount or leave blank to quit:  ")
                if amount == "":
                    quit()
                donate[name].append(int(amount))
                countMatches += 1
                break
        if countMatches == 0:
            amount = input("Please input the donation amount or leave blank to quit:  ")
            if amount == "":
                quit()
            donate[resp] = [(int(amount))]
        print(f"{resp} - Thank you for your gift of {amount} dollars.")


def createReport():
    donateReport = []
    """Print donors names, total donations, # of donations, and avg donation- sorted highest to lowest total donation"""

    # Calculate donation summary for each donor and add to the report
    for name, gifts in donate.items():
        dName = name
        donations = gifts
        total = sum(donations)
        count = len(donations)
        avg = total // count
        donateReport.append([dName, total, count, avg])

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

# Prompt with menu
switcher = {'1': thankYou, '2': createReport, '0': quit}
while True:
    res = input("Type '1' to send a thank you. \nType '2' to create a report. \nType '0' to quit:  ")
    switcher[res]()
