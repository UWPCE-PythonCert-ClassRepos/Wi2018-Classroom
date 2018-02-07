#!/usr/bin/env python3
"""
"""

# In memory representation of the donor database
# using a tuple for each donor
# -- kind of like a record in a database table
# the donations are in a list -- so you can add to them
# Note the mutable inside an immutable

donor_data = [("Allen, Paul", [1000000, 50000, 300000]), 
                    ("Gates, Bill", [5000000, 80000, 700000]), 
                    ("Bezos, Jeff", [30000]), 
                    ("Musk, Elon", [1000000, 30000]), 
                    ("Zuckerberg, Mark",[10000, 50000, 12000, 400000])
                    ]


def show_list():
    for donor in donor_data:
        print(donor[0])


def get_donor(name):
    for donor in donor_data:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


def init_prompt():
    response = input('''\n
        Would you like to: 
        '1' - Send a Thank You 
        '2' - Create a Report 
        '3' - Quit
        > ''')
    return response.strip()


def make_donor_email(donor):
    return f'''\n
        Dear {donor[0]}, 
        Thank you for your donation of ${donor[1][-1]:.2f}. 
        You are a good person.
                            Sincerely,
                            -Me
        '''
        #.format(donor[0], donor[1][-1])


def send_donor_email():
    while True:
        name = input("Please enter a donor's name in the form of 'Last name, First name'"
            "(or 'list' to see a list of all donors, or 'menu' to exit)> ").strip()
        if name == "list":
            show_list()
        elif name == "menu":
            return None
        else:
            break
    while True:
        amount_str = input("Please enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return None
        else:
            amount = float(amount_str)
        donor = get_donor(name)
        if donor is None:
            donor = (name, [])
            donor_data.append(donor)
        donor[1].append(amount)
        break
    print(make_donor_email(donor))


#def sort_key(donor):
    #return donor[1]


def make_report():
    #donor_data.sort(key=sort_key)
    donor_sort = sorted(donor_data, key=lambda donor: sum(donor[1]), reverse=True)
    #print(donor_sort)
    col_names = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    headers = f'{col_names[0]:20}{col_names[1]:>15}{col_names[2]:^15}{col_names[3]:20}'
    print(" ")
    print(headers)
    print(("_")*65)
    print((" "))
    for n in range(len(donor_sort)):
        columns = f'{donor_sort[n][0]:20}{sum(donor_sort[n][1]):15.2f}{len(donor_sort[n][1]):^15}{(sum(donor_sort[n][1])/len(donor_sort[n][1])):12.2f}'
        print(columns)


if __name__ == "__main__":
    running = True
    while running:
        selection = init_prompt()
        if  selection == "1":
            send_donor_email()
        elif selection == "2":
            make_report()
        elif selection == "3":
            running = False
        else:
            print("error: please make a valid selection!")


