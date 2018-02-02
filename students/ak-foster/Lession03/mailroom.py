#!/usr/bin/env python3

donate = [['Merv', 10, 500, 100], ['Linda', 300, 62, 7], ['Larry', 25, 50, 100], ['Sue', 20, 50, 1000]]

def thankYou():
    """Adds new donations to record and displays a thank you note when provided a name and donation amount."""
    resp = input('Type \'list\' to see donor list, otherwise, type a name:  ')
    if resp == 'list':
        print(donate)
    else:
        for name in donate:
            countMatches = 0
            if name[0] == resp:
                amount = input('Please input the donation amount:  ')
                name.append(int(amount))
                countMatches = + 1
                break
        if countMatches == 0:
            donate.append([resp, ])
            amount = input('Please input the donation amount:  ')
            donate[-1].append(int(amount))
        print(f'{resp} - Thank you for your gift of {amount} dollars.')


def createReport():
    donateReport = []
    """Print report with donors names, total donations, and avg donation- sorted by highest to lowest total donations"""
    # Calculate donation summary for each donor and add to the report
    for name in donate:
        dName = name[0]
        donations = name[1:]
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
        line = ['-' * 10, '-' * 20, '-' * 20, '-' * 20]  # line break (multipliers to match width set above)
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
while True:
    res = input('Type \'1\' to send a thank you. Type \'2\' to create a report. Type \'0\' to quit:  ')
    if res == '1':
        thankYou()

    if res == '2':
        createReport()

    if res == '0':
        break
