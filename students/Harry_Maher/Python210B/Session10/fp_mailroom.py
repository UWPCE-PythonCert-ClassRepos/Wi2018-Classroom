#!/usr/bin/env python3

"""
Functional version of mailroom
"""

import os

donor_dict = {"Bill":[2.75,3.12], "Bob": [52.75,15.11], \
"Jim": [27.36,2.07] , "Ann": [12.76,1.01], "Beth": [31245.75]}
donors = [donor for donor in donor_dict.keys()] 


def pick_ty_recipient(name = None):
    if name == None: 
        name = input("Pick or add a name (or type list)!\n")
    if name.strip().lower() == "list":
        print("\n".join(donors))
        # If some fool wants to keep typing "list" for some reason:
        name = pick_ty_recipient() 
    return name.title().strip()


def thank_you_txt(name):
        return f"Dear {name},\n\n \tThanks so much for your generous\
 donations totaling ${sum(donor_dict[name]):.2f}.\n \tWe are\
 all incredibly grateful because blah blah. \n\n-NGO"


def send_ty(name = None):
    """Prints out a thank you letter to specified person, or to new person."""
    name = pick_ty_recipient(name)
    if name not in donors and (name !="list"):
        donor_dict[name] = [0,0]
        donation = input("How much did they donate?\n")
        try:
            donor_dict[name].append(float(donation))
        except ValueError:
            donation = input("Donation needs to be a number")
        donor_dict[name].append(float(donation))
    print(thank_you_txt(name))
    return thank_you_txt(name)


def generate_report():
    """print a report of donation averages by donor."""
    report = "{:16}|{:^13}|{:^11}|{:>13}\n".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    for name in donors:
        report+="{:17}${:>12.2f} {:>11} ${:>12.2f}\n".format(name, sum(donor_dict[name]), len(donor_dict[name]),(sum(donor_dict[name])/len(donor_dict[name])))
    print(report)
    return report


def send_letters():
    """Send written letters to folder."""
    for name in donors:
        name = "_".join(name.split()) # For people with multiple names
        filename = "letters/"+name+".txt"
        try:
            with open(filename, "w+") as f:
                f.write(thank_you_txt(name))
        except FileNotFoundError:
            os.mkdir(output_dir)
            with open(filename, "w+") as f:
                f.write(thank_you_txt(name))
    # Return "sent!" upon sucessful completion. For pytest
    return "sent!" 


def challenge():
    # shorter with a list comp:
    # return sum([factor * donation for donations in donor_dict.values() for donation in donations if donation > min_donation and donation < max_donation])
    try:
        factor = int(input("By what factor do you wanna increase donations?\n"))
        min_donation = int(input("What's the min donation to increase by that factor?\n"))
        max_donation = int(input("What's the max donation to increase by that factor?\n"))
    except ValueError:
        print("Not a number, start over.")
        return challenge()
    
    all_donations = [donation for donations in donor_dict.values() for donation in donations]
    filtered_list = filter(lambda x: x > min_donation and x < max_donation, all_donations)
    multiplier = lambda donation: donation * 2
    tot_donation = sum(list(map(multiplier, filtered_list)))
    print(f"""Total contribution, 
        multiplying all donations less than {max_donation} 
        and greater than {min_donation} by a factor of {factor} 
        would be: {tot_donation}""")


def mailroom(choice = None):
    """automate mail sending and report generation"""
    choices = """Pick a number: 
    1. Send thank you 
    2. Create report 
    3. Send letters to all donors 
    4. Increase donations by a factor
    5. Quit\n"""
    arg_dict = {"1":send_ty, "2":generate_report, "3": send_letters, "4": challenge,"5":quit}
    if choice == None:
        choice = input(choices)
    while choice != "5":
        arg_dict.get(choice, 'Type "1", "2", "3", or "4", without the quotes.')()
        choice = input(choices)


if __name__ == "__main__":
    mailroom()
