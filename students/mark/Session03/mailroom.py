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
    return('''
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

def sendThankYou():
    """
    Record a donation, create a thank you letter.
    """

    # use a while loop to get the user input and execute a function
    # basic input checking, strip whitespace
    while True:
        name = input("Enter a donor's name "
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            printDonorName()
        elif name == "menu":
            return
        else:
            break

def printMenu():
    getInputVar=(input('''Choose an action:

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        4 - Quit
        '''))

    return getInputVar.strip()


def reportSortKey(item):
    return item[1]

    """not really clear on how this little piece of magic works yet, but it's needed.
    used to print the printDonorReport

    this is the "item column" which we will sort on, but why in a function?
    """

    return item[1]

def printDonorReport():
    """
    Output report of donors
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donorDB:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    print('debug')
    report_rows.sort(key=reportSortKey)
    # print it out in with a nice format.
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

def createLetter(donor):
    """
    Create a thank you letter for the donor
    :param: donor tuple
    :returns: string with letter
    """
    return '''\n
          Dear {}
          Thank you for your very kind donation of ${}.
          It will be put to very good use.
                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1])

          #           Thank you for your very kind donation of ${:.2f}.



if __name__ == '__main__':
    print("this is the main section")

    #donor=['w golf',(200.02)]
    #donor='Paul Allen'
    printMenu()
    printEgLetter()
    printDonorReport()
    print('debug')
    print(createLetter(donorDB))
