#!/usr/bin/env python3

def add_new_donor():
    """   """
    pass


def add_donation_to_history():
    """   """
    pass


def list_donor_names():
    """   """
    pass


def main_menu_prompt():
    """   """
    response = input("  (1) Send a 'Thank You'\n"
                     "  (2) Create a Report\n"
                     "  (3) quit\n"
                     "  --> ")

    return response
    

def thank_you_prompt():
    """   """

    while True:
        response = ('--> ')

        if reponse in ['list', 'l']:
            list_donor_names()


def report_prompt():
    """   """
    pass


def main():
    """ Show main menu, prompting user for selection.  """
    print('\nWhat would you like to do? (Select one):')

    while True:
        response = main_menu_prompt()

        if response.lower() in ['1', 'send', 'send a thank you', 'thank you']:
            thank_you_prompt()

        if response.lower() in ['2', 'create', 'report', 'create a report']:
            report_prompt()

        if response.lower() in ['3', 'q', 'quit', 'exit']: break

        else:
            print("Invalid input. Please select one:")

    return



if __name__ == '__main__':
    # Initialize 5 donors and at least 1 donation for each.
    donors = dict([('William Gates, III', {'donations': (1, 5, 100000000)}),
                   ('Mark Zuckerberg', {'donations': (378000, 5000, 20.01)}),
                   ('Jeff Bezos', {'donations': (29000000, 34000, 709000)}),
                   ('Paul Allen', {'donations': (750000, 513895, 30592.50)}),
                   ('John Ferrell', {'donations': (520000000000)})])

    print('\nWelcome to the Mailroom applicaton.')

    main()

    print('\nThank you for using Mailroom. Have a nice day!')
