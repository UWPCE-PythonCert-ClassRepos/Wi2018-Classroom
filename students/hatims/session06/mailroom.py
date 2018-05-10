#!/usr/bin/env python3

import sys
"""
It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
"""

donors = dict()
donors.update({'William Gates': [7897100.00, 5000.00, 12000000.00]})
donors.update({'Mark Zuckerberg': [19000.00, 8900000.00]})
donors.update({'Jeff Bezos': [1000.00, 1445600.00]})
donors.update({'Paul Allen': [9000.00, 29000000.00, 5690000000.00]})


"""
Creating the Report
"""

"""function will print the report header and details for the donors"""
def create_report():
    print_header()
    print_details()

"""function will print the report header"""	
def print_header():
    print("{:<20}{:5}{:15}{:5}{:10}{:5}{:15}".format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    print("-" * 77)

"""function will print the report details for each donor"""		
def print_details():
    total_given=0
    num_gifts=0
    average_gift=0
    for donor_name in donors:
        for val in donors[donor_name]:
            total_given = total_given+val
        num_gifts = len(donors[donor_name])
        average_gift = total_given / (num_gifts)
        print("{:<22}${:>15.2f}{:^20}${:>15.2f}".format(donor_name, total_given, num_gifts, average_gift)) 	
        total_given = 0		

"""
Sending a Thank You
"""
def send_thankyou():
    full_name = propmpt_fullname()
    if full_name.upper() == 'LIST':
        print([donor for donor in donors])
    elif not name_exists(full_name):
        donation_amount = propmpt_donation()
        donors.update({full_name: [float(donation_amount)]})		
    elif name_exists(full_name):
        donation_amount = propmpt_donation()
        donors[full_name].append(float(donation_amount))
		

"""
Write a full set of letters to everyone to individual files on disk.
"""
def send_letters_to_donors():
    print("sending letters to every one")
    compose_letter()


def compose_letter():
    for donor in donors:
        letter ="Dear " + donor + ",\n\n\t\tThank you for your very kind donation of $" + str(get_total_gift(donors[donor])) + ".\n\n\t\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\n\t\t\t\t-The Team"
        outfile = open(donor + '.txt', 'w')
        outfile.write(letter)
        outfile.close()		

def get_total_gift(donor_gift):
    total_given = 0
    for val in donor_gift:
            total_given = total_given+val
    return total_given
						  
"""Function will return a boolean to indicate a donor name already exists or not"""
def name_exists(full_name):
    name_found = False
    for donor in donors:
        if full_name == donor:
            name_found = True
    return name_found			

"""Function will return the index for donor in data structure"""
def get_index(full_name):
    index = 0
    for idx, donor in enumerate(donors):
        if full_name.upper() == str(donor[0]).upper():
            index = idx
    return index
	
"""function will prompt user to select an action from the menu"""   
def propmpt_fullname():
    return input("\nPlease enter a full name or type list (to list the donors):  \n\n")

"""function will prompt user to select an action from the menu"""   
def propmpt_donation():
    return input("\nPlease enter a donation amount:  \n\n")
	
"""function will user to select an action from the menu"""   
def propmpt_menu():
    return input("\nPlease choose one of the following actions:  \n1. Send a Thank You\n2. Create a Report\n3. Send letters to everyone\n4. quit(q)\n\n")

	
def quit():
    sys.exit()
	
switch_func_dict = {'1': send_thankyou, '2': create_report, '3': send_letters_to_donors}
	

response = propmpt_menu()
try:
    if not response.isnumeric():
        raise TypeError
    if int(response) < 0 or int(response) > 4:
        raise IndexError
except (TypeError, IndexError):
    print("You entered invalid value\n")
    input("\nPlease enter a donation amount:  \n\n")
else:
    while response != str(4):
        switch_func_dict.get(response)()
        response = propmpt_menu()
