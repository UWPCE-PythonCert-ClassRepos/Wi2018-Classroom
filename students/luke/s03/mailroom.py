#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom
"""

class donor:
    """Donor class holds donor name and list of donations"""
    def __init__(self, name, donations=None):
        self.name = name
        if donations is None:
            self.donations = [ ]
        else:
            self.donations = donations


def driver():
    """ Main loop for mailroom """
    done = False
    while not done:
        action = input(("Select an action and press return:\n"
            "[S]end a thank-you (add users and donation entries)\n"
            "[C]reate a report\n"
            "[Q]uit\n"
            "> "))
        action = action.lower()
        while not action in "scq": action = input("Bad option, reenter > ")

        if action == "s":
            add_donations()
        elif action == "c":
            create_report()
        else:
            done = True;
    return


def add_donations():
    """ Add donation history for a(n optionally new) user """
    done = False
    while not done:
        name = input("Enter donor name (or \"list\" for list): ")
        if name == "list":
            # list donor names
            for d in donor_history: print(d.name)
            continue
        for thisdonor in donor_history:
            if name == thisdonor.name:
                break
        if thisdonor == None:
            thisdonor = donor(name)
            donor_history.append(thisdonor)
            print("Adding new donor: " + name)
        moredonations = True
        while moredonations:
            value = input("Enter donation amount or -1 when finished: ")
            try:
                donation_amount = int(value)
            except ValueError:
                print("Invalid input, reenter.")
                continue
            if donation_amount == -1: break
            thisdonor.donations.append(donation_amount)
        done = True
        if thisdonor: print(f"Thank you, {name}, for your donation(s)!")
        print()
    return

def create_report():
    """ Display table: Donor Name | Total Given | Num Gifts | Average Gift """
    print("Donor Name | Total Given | Num Gifts | Average Gift")
    for d in donor_history:
        total = 0
        for amt in d.donations: total += amt
        print(f"{d.name:10} | {total:11.2f} | {len(d.donations):9d} | {total/len(d.donations):12.2f}")
    print()
    return


if __name__ == '__main__':
    donor_history = [ donor("alice", [5]) ]
    donor_history.append(donor("bob", [1, 2]))
    donor_history.append(donor("carol", [1, 5, 100]))
    donor_history.append(donor("dan", [5]))
    donor_history.append(donor("erin", [2, 1]))

    driver()