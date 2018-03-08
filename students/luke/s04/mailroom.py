#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom
"""

# Store donors/history in dictionary
donor_list = {"alice": [5],
              "bob": [1, 2],
              "carol": [1, 5, 100],
              "dan": [5],
              "erin": [2, 1]}

# Format of thank-you notes
THANK_YOU = "Thank you, {}, for your donation(s) of ${}!\n"

# Destination file
OUTFILE = "{}.txt"


def driver():
    """ Main loop for mailroom """
    done = False
    while not done:
        action = input(("Select an action and press return:\n"
                        "[S]end a thank-you (add users and donation entries)\n"
                        "[W]rite thank-you letters to file\n"
                        "[C]reate a report\n"
                        "[Q]uit\n"
                        "> "))
        while not action.lower() in "swcq":
            action = input("Bad option, reenter > ")

        if action == "s":
            add_donations()
        elif action == "w":
            write_thankyous()
        elif action == "c":
            create_report()
        else:
            done = True
    return


def add_donations():
    """ Add donation history for a(n optionally new) user """
    done = False
    while not done:
        name = input("Enter donor name (or \"list\" for list): ")

        if name == "list":
            # list donor names
            for n in donor_list:
                print(n)
            continue

        if not donor_list.get(name):
            print("Adding new donor: " + name)
            donor_list[name] = []

        moredonations = True
        while moredonations:
            value = input("Enter donation amount or [enter] when finished: ")
            if (value == ""):
                break
            try:
                donation_amount = int(value)
            except ValueError:
                print("Invalid input, reenter.")
                continue
            donor_list[name].append(donation_amount)
        done = True
        print(THANK_YOU.format(name, sum(donor_list[name])))
    return


def write_thankyous():
    for d in donor_list:
        with open(OUTFILE.format(d), 'w') as outfile:
            outfile.write(THANK_YOU.format(d, sum(donor_list[d])))


def create_report():
    """ Display table: Donor Name | Total Given | Num Gifts | Average Gift """
    print("Donor Name | Total Given | Num Gifts | Average Gift")
    for d in donor_list:
        total = 0
        d_list = donor_list[d]
        for amt in d_list:
            total += amt
        print(f"{d:10} | "
              f"{total:11.2f} | "
              f"{len(d_list):9d} | "
              f"{total/len(d_list):12.2f}")
    print()
    return


if __name__ == '__main__':
    driver()
