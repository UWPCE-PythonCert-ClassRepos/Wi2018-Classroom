"""It should have a data structure that holds a list of your donors and a history of the
amounts they have donated. This structure should be populated at first with at least five donors,
with between 1 and 3 donations each.

You can store that data structure in the global namespace.

The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”,
“Create a Report” or
“quit”)"""
import os
import datetime

donors = ["Ann Annson","Bill Billson","Cal Calson","Dan Danson", "Elle Elleson"]
donation_amounts = []
donation_amounts.append([30.50, 10,9])
donation_amounts.append([1, 99.25])
donation_amounts.append([302.33])
donation_amounts.append([3000, 1000, 9000])
donation_amounts.append([105.60])

donors_directory = dict()

"""Using existing list data to create dictionary of donors"""
donors_directory = {donor: donation_amounts[donors.index(donor)] for donor in donors}

print(donors_directory)


def thanks():
    while True:
        name = input("Please enter Full Name\n")
        if name == "list" or name == "List":
            for key in donors_directory.keys():
                print(key)
            name = input("Please enter Full Name\n")
        if any(name not in n for n in donors):
            donors_directory[name] = []

        donation = input("Please enter donation amount\n")
        print()
        donors_directory[name].append(float(donation))
        print(donors_directory[name])
        print("\n\n")
        write_letter(name)
        return 0


def write_letter(donor_name):

        print(f'Dearest {donor_name}\n\n'
              f'Thank you for your kind donation of {float(donors_directory[donor_name][-1])} dollars.\n'
              f'This will help us continue to provide\n'
              f'valuable services to the community.\n'
              f'Thanks,\n'
              f'Charitable Giving Department')
        return 0



def report():

    print("Donor Name         |Total Given   |Num Gifts|Average Gift")

    for donor in donors_directory:
        print(f'{donor:<20}{sum(donors_directory[donor]):<14}'
              f'{len(donors_directory[donor]):<10}'
              f'{sum(donors_directory[donor])/len(donors_directory[donor]):<12}')
    return 0


def save_letters():

    if not os.path.exists('letters'):
        os.makedirs('letters')

    today = datetime.datetime.now().strftime("%y%m%d")

    for donor in donors_directory:

        with open('letters\\'+donor.replace(' ','_')+today+'.txt', 'w')as f:
            f.write(f'Dearest {donor}\n\n'
                    f'Thank you for your kind donation of {float(donors_directory[donor][-1])} dollars.\n'
                    f'This will help us continue to provide\n'
                    f'valuable services to the community.\n'
                    f'Thanks,\n'
                    f'Charitable Giving Department')
            f.close()

    return 0

while True:
        print ("""
            Please select from the following commands:
            1.Send a Thank You
            2.Create a Report
            3.Save letters to disk
            4.Exit/Quit
            """)

        response = input("Enter 1 through 4 \n")
        if response == '1':
            thanks()
        elif response == '2':
            report()
        elif response == '3':
            save_letters()
        elif response == '4':
            print("\n Goodbye")
            exit()
        else:
            print("Please enter a number 1, 2, 3 or 4")



