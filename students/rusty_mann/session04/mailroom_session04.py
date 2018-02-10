#!/usr/bin/env python3


#List of tuples, donor at index 0 in each tuple
#and list of donations at index 1 in each tuple
donor_data = {"Allen, Paul": [1000000.00, 50000.00, 300000.00], 
                    "Gates, Bill": [5000000.00, 80000.00, 700000.00], 
                    "Bezos, Jeff": [30000.00], 
                    "Musk, Elon": [1000000.00, 30000.00], 
                    "Zuckerberg, Mark":[10000.00, 50000.00, 2000.00, 400000.00]
                    }


def show_donor_list():
    donor_list = []
    for donor in donor_data:
        donor_list.append(donor)
    sort_donors = sorted(donor_list)
    for donor in sort_donors:
        print(donor)


def get_donor(name):
    """
    retieve donor form donor_data list
    :param: name of donor
    :returns: donor tuple
    """
    for donor in donor_data:
        if name.strip().lower() == donor.lower():
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
    """
    Make a thank you email for the donor
    :param: donor tuple
    returns: string containing text of email
    """
    #for donor, amt in donor_data.items():
    return '''\n
        Dear {0}, 
        Thank you for your donation of ${1:.2f}.
        You are a good person.
                            Sincerely,
                            -Me
        '''.format(donor, donor_data[donor][-1])


def send_donor_email():
    while True:
        name = input("Please enter a donor's name in the form of 'Last name, First name'"
            "(or 'list' to see a list of all donors, or 'menu' to exit)> ").strip()
        if name == "list":
            show_donor_list()
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
        #print(donor)
        if donor is None:
            donor = (name)
            donor_data.setdefault(name, [])
        #print(donor_data)
            #donor = {name: []}
            #donor_data.update(donor)
        donor_data[name].append(amount)
        #print(donor_data)
        break
    #print(donor_data)
    #print(donor)
    print(make_donor_email(donor))


def sort_key(donor):
    return donor[1]


def make_report():
    rows = []
    for donor in donor_data:
        total = sum(donor_data[donor])
        num = len(donor_data[donor]
        avg = total / num
        rows.append((donor, total, num, avg))
    rows.sort(key=sort_key, reverse=True)
    for row in rows:
        print('{:20s}{:15.2f}{:^15d}{:12.2f}'.format(*row))



'''
def make_report():
    donor_data.sort(key=sort_key)
    #donor_sort = sorted(donor_data, key=lambda donor: sum(donor[1]), reverse=True)
    print(donor_sort)
    col_names = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    headers = f'{col_names[0]:20}{col_names[1]:>15}{col_names[2]:^15}{col_names[3]:20}'
    print(" ")
    print(headers)
    print(("_")*65)
    print((" "))
    for n in range(len(donor_sort)):
        columns = f'{donor_sort[n][0]:20}{sum(donor_sort[n][1]):15.2f}{len(donor_sort[n][1]):^15}{(sum(donor_sort[n][1])/len(donor_sort[n][1])):12.2f}'
        print(columns)
'''

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


