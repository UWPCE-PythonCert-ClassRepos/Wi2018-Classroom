#Mailroom.py

donors = ["Jeff Bezons","Mark Zuckerberg","Paul Allen","William Gates"]
donation_amounts = []
donation_amounts.append([877.33, 10.00,9.00])
donation_amounts.append([16396.10, 99.25])
donation_amounts.append([708.42])
donation_amounts.append([653784.49, 1000.00, 10000.00])



def thanks():
    while True:
        name = input("Please enter your Full Name\n")
        if name == "list" or name == "List":
            print(donors)
            name = input("Please enter your Full Name\n")
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
              f'This will help save the children to provide\n'
              f'valuable services to the needy children.\n'

              f'Thanks,\n'
              f'Save the children,\n'
              f'Management')
        return 0



def report():

    print("Donor Name       |Amount  |number of donations |Total amounts")

    for person in donors:
        donations = donation_amounts[donors.index(person)]
        print(f'{person:<20}{sum(donations):<14}'
              f'{len(donations):<10}'
              f'{sum(donations)/len(donations):<12}')
    return 0



while True:
        print ("""
            Please select from the following menus:
            1.Send a Thank You
            2.Create a Report
            3.Quit
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