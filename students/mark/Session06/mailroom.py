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

# donor_db = {"William Gates, III":[326888.82, 326895.67],
#             "Mark Zuckerberg":[5565.37, 5465.37, 5365.36],
#             "Jeff Bezos":[877.33],
#             "paul allen":[236.14, 236.14, 236.14],
#             "jose gonzalez" : [123.45, 678.90, 101.11]
#             }

donor_db = {"william gates, iii":[326888.82, 326895.67],
            "mark zuckerberg":[5565.37, 5465.37, 5365.36],
            "jeff bezos":[877.33],
            "paul allen":[236.14, 236.14, 236.14],
            "jose gonzalez" : [123.45, 678.90, 101.11]
            }

def format_donor_name(donor_names):
    if ',' in donor_names:
        name_title=donor_names.split(',')
        i_var=name_title[0].title() + ','
        donor_names=i_var.replace(',', "," + name_title[1].upper())
        return(donor_names)
    else:
        name_title=donor_names
        return(donor_names.title())


def print_donor_name(donor_db):
    """
    Output the donor name(s)
    :param: donor_db dict
    :returns: zero for success
    """
    print("Donor list: \n")
    for donor_names in donor_db.keys():
        if ',' in donor_names:
            name_title=donor_names.split(',')
            i_var=name_title[0].title() + ','
            donor_names=i_var.replace(',', "," + name_title[1].upper())
            print(donor_names)
        else:
            name_title=donor_names
            print(donor_names.title())
    return 0


def get_donor(name):
    """
    get a donor out of the donor "structure"
    """
    for donor in donor_db:
        if name.strip().lower() == donor[0].lower():
            """ get the name in lowercase, makes matching names easier later"""
            return donor

    return None # or should this be donor?

def send_thank_you():
    """
    Record a donation, create a thank you letter.
    """

    # use a while loop to get the user input and execute a function
    # basic input checking, strip whitespace
    while True:
        name = input("Enter a donor's name "
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print_donor_name(donor_db)
        elif name == "menu":
            return
        else:
            if name.lower() in donor_db.keys():
                print("name: ", format_donor_name(name), "found.")
                print(create_letter(name, donor_db))
            break

def print_menu():
    getInputVar=(input('''Choose an action:

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        4 - Quit
        '''))

    return getInputVar.strip()


def report_sort_key(item):
    """list.sort(key="<thing>") thing must be a function
    """
    return item[1]


def print_donor_report(donor_database):
    """
    Output report of donors
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_database.items():
        name = format_donor_name(name)
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=report_sort_key)
    # print it out in with a nice format.
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)  # Make 66 little '-'s
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))


def create_letter(donor, donor_db):
    """
    Create a thank you letter for the donor
    :param: donor/string, donor_db dict/string:tuple
    :returns: string with letter
    """
    print('debug')
    return '''\n
          Dear {}
          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.
          Your generous contributions to date totaling ${:.2f} 
          allow us continue our mission and achive our joint goals.
                         Sincerely,
                            -The Team
          '''.format(format_donor_name(donor), donor_db[donor][-1], sum(donor_db[donor]))

def send_letters_to_all(donor_db):
    """

    :params: donor_db/dict,
    :returns: 0 if completes

    :description:
    In this version, add a function (and a menu item to invoke it),
    that goes through all the donors in your donor data structure,
    generates a thank you letter, and writes it to disk as a text file.

    menu_item, menu #3

    """

    for k in donor_db.keys():

        file_name=format_donor_name(k).replace(',','').replace(" ","_") + ".txt"
        with open(file_name, 'w') as fh1:
            fh1.write(create_letter(k, donor_db))

    return 0





if __name__ == '__main__':
    print("this is the main section")

    # #donor=['w golf',(200.02)]
    # #donor='Paul Allen'
    # menuValue=print_menu()
    # print_eg_letter()
    # print_donor_report()
    # print('debug')
    # print(create_letter('jeff bezos', donor_db))


    ### code below works, need work on called functions (works)
    running = True
    while running:
#       selection = main_menu_selection()
        selection=print_menu()
        if selection == "1":
            send_thank_you()
        elif selection == "2":
            print_donor_report(donor_db)
        elif selection == "3":
            send_letters_to_all(donor_db)
        elif selection == "4":
            running = False
        else:
            print("Please select an option 1-4 from the menu")
