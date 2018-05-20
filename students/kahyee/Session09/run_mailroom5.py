#!/usr/bin/env python3

import os
import mailroom5 as mr

donation_dict = {
"Bob": [1.00, 2.00],
"Jon": [1.50, 100.00],
"Sally": [1000.00],
"Barry": [50.00],
"Ellen": [1.25]
}

donors = mr.Donor_group(donation_dict)

donors.add_donor("test", [1.00])

def default_prompt():
    return int(input("Select Action \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letters to Everyone \n 4. Quit \n"))
    
def thank_you():
    donor_name = input("Donor's Full Name: ")
    while donor_name.lower() == "list":
        donors.list()
        donor_name = input("Donor's Full Name: ")
    donation_amt = float(input("How much did they donate?"))
    donors.add_donor(donor_name, [donation_amt])
    #print(donors.find_donor(donor_name).email())

user_prompt = default_prompt()

switch_prompt_dict = {
    1: thank_you,
    2: donors.create_report,
    3: donors.all_email
}

while user_prompt != 4:
    try:
        switch_prompt_dict[user_prompt]()
    except KeyError:
        print("Enter a value from 1 to 4")
    finally:
        user_prompt = default_prompt()
