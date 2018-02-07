#!/usr/bin/env python3


"""
Session03 - Part I


https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom

Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

    You can store that data structure in the global namespace.

    The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)



### Finally, use only functions and the basic Python data types you’ve learned about so far. There is no need to go any farther than that for this assignment.

/*
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14
*/

/*


*/
"""

donorDB = [("William Gates, III", [326888.82, 326895.67]),
            ("Mark Zuckerberg", [5565.37, 5465.37, 5365.36]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [236.14, 236.14, 236.14]),
            ]

def printDonorName():
    print("Donor list: \n")
    for donor in donorDB:
        print(donor[0])

def printEgLetter():
    print('''
    Dear Jeff Bezos,

        Thank you for your very kind donation of $877.33.

        It will be put to very good use.

                       Sincerely,
                          -The Team
    ''')

def getDonor(name):
    """
    get a donor out of the donor "structure"
    """
    for donor in donorDB:
        if name.strip().lower() == donor[0].lower():
            """ get the name in lowercase, makes matching names easier later"""
            return donor

    return None # or should this be donor?

def printMenu():
    getInputVar=(input('''Choose an action:

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        4 - Quit
        '''))

    return getInputVar.strip()


if __name__ == '__main__':
    print("this is the main section")

    printMenu()
    printEgLetter()
    printDonorName()
