#!/usr/bin/env python3


"""
Session09 - Make mailroom Object Oriented


https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom

Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a history of the
    amounts they have donated. This structure should be populated at first with at least
    five donors, with between 1 and 3 donations each.

    You can store that data structure in the global namespace.

    The script should prompt the user (you) to choose from a menu of 3 actions:
    “Send a Thank You”, “Create a Report” or “quit”)


### Finally, use only functions and the basic Python data types you’ve learned about so far.
There is no need to go any farther than that for this assignment.

"""

import oop_mailroom_db
import oop_mailroom_letter

ddb=oop_mailroom_db.DonorDB()
ltr=oop_mailroom_letter.LetterOop()

donor_db = {"william gates, iii":[326888.82, 326895.67],
            "mark zuckerberg":[5565.37, 5465.37, 5365.36],
            "jeff bezos":[877.33],
            "paul allen":[236.14, 236.14, 236.14],
            "jose gonzalez" : [123.45, 678.90, 101.11]
            }


def print_menu():
    getInputVar=(input('''Choose an action:

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        4 - Add additional contribution
        5 - Quit

        '''))

    return getInputVar.strip()



if __name__ == '__main__':
    running = True
    while running:
        selection=print_menu()
        if selection == "1":
            ltr.send_thank_you(ddb.donor_db)
        elif selection == "2":
            ddb.print_donor_report(ddb.donor_db)
        elif selection == "3":
            ltr.send_letters_to_all(ddb.donor_db)
        elif selection == "4":
            ddb.add_new_donor(ddb.donor_db)
        elif selection == "5":
            running = False
        else:
            print("Please select an option 1-5 from the menu")
