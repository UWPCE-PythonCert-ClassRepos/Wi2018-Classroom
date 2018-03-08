#!/usr/bin/env python3

"""
It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
"""

donors = list()
donor1 = ['William Gates', 7897100.00, 5000.00, 12000000.00]
donor2 = ['Mark Zuckerberg', 19000.00, 8900000.00]
donor3 = ['Jeff Bezos', 1000.00, 1445600.00]
donor4 = ['Paul Allen', 9000.00, 29000000.00, 5690000000.00]

donors.append(donor1)
donors.append(donor2)
donors.append(donor3)
donors.append(donor4)

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
    for row in donors:
        donor_name = row[0]
        for val in row[1:len(row)]:
            total_given = total_given+val
        num_gifts = len(row) - 1 
        average_gift = total_given / (len(row) - 1)
        print("{:<22}${:>15.2f}{:^20}${:>15.2f}".format(donor_name, total_given, num_gifts, average_gift)) 		

"""
Sending a Thank You
"""
def send_thankyou():
    full_name = propmpt_fullname()
    if full_name.upper() == 'LIST':
        for donor in donors:
            print(donor[0])
    elif not name_exists(full_name):
        donation_amount = propmpt_donation()
        donor_record = [full_name, int(donation_amount)]
        donors.append(donor_record)		
    elif name_exists(full_name):
        index = get_index(full_name)
        donation_amount = propmpt_donation()
        donors[index].append(float(donation_amount))        
		
"""Function will return a boolean to indicate a donor name already exists or not"""
def name_exists(full_name):
    name_found = False
    for donor in donors:
        if full_name.upper() == str(donor[0]).upper():
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
    return input("\nPlease choose one of the following actions:  \n1. Send a Thank You\n2. Create a Report\n3. quit(q)\n\n")

if __name__ == '__main__':
    response = propmpt_menu()
    while response != str(3):
        if response == str(1):
            send_thankyou()
        if response == str(2):
            create_report()
        response = propmpt_menu()
        