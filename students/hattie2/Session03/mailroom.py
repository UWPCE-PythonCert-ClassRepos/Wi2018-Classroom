"""It should have a data structure that holds a list of your donors and a history of the
amounts they have donated. This structure should be populated at first with at least five donors,
with between 1 and 3 donations each.

You can store that data structure in the global namespace.

The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”,
“Create a Report” or
“quit”)"""

donors = ["Ann Annson","Bill Billson","Cal Calson","Dan Danson", "Elle Elleson"]

donation_amounts = []
donation_amounts.append([30.50, 10,9])
donation_amounts.append([1, 99.25])
donation_amounts.append([302.33])
donation_amounts.append([3000, 1000, 9000])
donation_amounts.append([105.60])


def thanks():
    while True:
        name = input("Please enter Full Name\n")
        if name == "list" or name == "List":
            print(donors)
            name = input("Please enter Full Name\n")
        if any(name not in n for n in donors):
            donors.append(name)
            donation_amounts.append([])

        donation = input("Please enter donation amount\n")
        print()
        donation_amounts[donors.index(name)].append(float(donation))
        print(donation_amounts[donors.index(name)])
        print("\n\n")
        write_letter(name, donation)
        return 0


def write_letter(donor_name, donor_amount):

        print(f'Dearest {donor_name}\n\n'
              f'Thank you for your kind donation of {donor_amount} dollars.\n'
              f'This will help us continue to provide\n'
              f'valuable services to the community.\n'
              f'Thanks,\n'
              f'Charitable Giving Department')
        return 0



def report():

    print("Donor Name         |Total Given   |Num Gifts|Average Gift")

    for person in donors:
        donations = donation_amounts[donors.index(person)]
        print(f'{person:<20}{sum(donations):<14}'
              f'{len(donations):<10}'
              f'{sum(donations)/len(donations):<12}')
    return 0



while True:
        print ("""
            Please select from the following commands:
            1.Send a Thank You
            2.Create a Report
            3.Exit/Quit
            """)

        response = input("Enter 1 through 3 \n")
        if response == '1':
            thanks()
        elif response == '2':
            report()
        elif response == '3':
            print("\n Goodbye")
            exit()
        else:
            print("Please enter a number 1, 2 or 3")



