#!/usr/bin/env python3

def add_new_donor(name):
    """   """
    pass


def add_donation_to_history():
    """   """
    pass


def list_donor_names():
    """ Print current list of donors to screen  """
    [print(k) for k in donors.keys()]


def hor_bar():
    """   """
    print("-----------------------------------")


def main_menu_prompt():
    """   """
    response = input("   (1) Send a 'Thank You'\n"
                     "   (2) Create a Report\n"
                     "   (3) quit\n"
                     "--> ")

    return response


def direct_from_main_menu(response):
    """   """
    
    

def thank_you_prompt(donors):
    """   """
    hor_bar()
    print("[Send 'Thank You' menu]\n"
          "Type 'menu' to return to main menu.")
    
    while True:
        response = input('--> ')

        if response in ['list', 'l']:
            list_donor_names()

        # import pdb; pdb.set_trace()

        if response.lower() not in [k.lower() for k in donors.keys()]:
            # TODO see if I need to return add_new_donor to donors object
            # here or if global namespace donors will get updated in
            # add_new_donor function
            add_new_donor(response)

        if response.lower() in [k.lower() for k in donors.keys()]:
            new_amount = donation_prompt()
            donors = add_donation_to_history(new_amount)

        if response in ['m', 'menu']: break

    return
    # TODO see if I need to return donors to get any updates back into
    # the donors object in the global namespace
    # return donors

def donation_prompt():
    """   """
    pass


def report_prompt():
    """   """
    pass


def main():
    """ Show main menu, prompting user for selection.  """
    while True:
        hor_bar()
        print('[Main menu]\n'
              'What would you like to do? (Select one):')

        while True:
            response = main_menu_prompt()

            if response.lower() in ['1', 'send', 'send a thank you', 'thank you']:
                thank_you_prompt(donors)
                break

            if response.lower() in ['2', 'create', 'report', 'create a report']:
                report_prompt()
                break

            if response.lower() in ['3', 'q', 'quit', 'exit']: return

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
