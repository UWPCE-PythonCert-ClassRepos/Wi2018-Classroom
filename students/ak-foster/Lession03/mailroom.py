#!/usr/bin/env python3

donate = [['Merv', 1], ['Linda', 3], ['Larry', 2], ['Sue', 2]]

while True:
    res = input('Type \'1\' to send a thank you. Type \'2\' to create a report. Type \'3\' to quit:  ')
    if res == '1':
        resp = input('Type \'list\' to see donor list, otherwise, type a name:  ')
        if resp == 'list':
            print(donate)
        else:
            for name in donate:
                countMatches = 0
                if name[0] == resp:
                    amount = input('Please input the donation amount:  ')
                    name.append(int(amount))
                    countMatches =+ 1
                    break
            if countMatches == 0:
                donate.append([resp, ])
                amount = input('Please input the donation amount:  ')
                donate[-1].append(int(amount))
            print(f'{resp} - Thank you for your gift of {amount} bitcoin.')
    if res == '2':
        # TODO: If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
            # TODO: Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
            # TODO: Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
            # TODO: After printing this report, return to the original prompt.
        # TODO: At any point, the user should be able to quit their current task and return to the original prompt.
        # TODO: From the original prompt, the user should be able to quit the script cleanly.
        donateReport = []
        for name in donate:
            dName = name[0]
            donations = name[1:]
            total = sum(donations)
            avg = total / (len(donations))
            donateReport.append([dName, str(total), str(avg)])
        # TODO: figure out a better way to pretty print...some thoughts below
        row = '{:<10}' * len(donateReport)
        for record in zip(*donateReport):
            print(row.format(*record))

    if res == '3':
        break
