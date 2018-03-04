#!/usr/bin/env python3.6
import datetime as dt


def prompt_for_amount(name):
    """ Prompt user for donation amount and return value. """
    amount = input(f"How much did {name} donate? ")

    return ''.join(amount.split('$')[-1].split(','))


def add_new_donor(name, amount):
    """ Add new donor and donation amount to donor database. """
    donors[name] = dict([('donations', [float(amount)])])


def add_donation_to_history(name, amount):
    """ Add new donation to existing donor's records """
    donors[name]['donations'].append(amount)


def verify_add_donor(name):
    """   """
    while True:
        response = input(f"Are you sure you want to add {name}? [Y/n] ")

        # 'Y' is default response.
        if response == '': response = 'y'
        
        if response.lower() in ['y', 'n', 'yes', 'no']: return response.lower()


def list_donor_names():
    """ Print current list of donors to screen.  """
    [print(k) for k in donors.keys()]

    return


def blank_lines(number_lines=1):
    """ Return number_lines '\n' as string """
    return '\n' * (number_lines + 1)
    

def compose_letter(name, amount):
    """ Print donation Thank You letter to screen. """
    letter = letter_preamble(name)
    letter += letter_body(name, amount)
    letter += letter_closing()

    print(letter)

    return


def letter_preamble(name):
    """ Return Thank You letter preamble. """
    preamble = dt.datetime.now().strftime('%d %B %Y')
    preamble += blank_lines(2)
    preamble += f"Dear {name},"
    preamble += blank_lines()

    return preamble


def letter_body(name, amount):
    """ Return body of Thank You letter. """
    body = (
        f'Thank you for your generous donation of ${float(amount):,.2f}. Your gracious support '
        'helps us continue our important work doing what we do. We look forward to continuing to '
        'partner with you in the future. Please contact us if you have any questions or have any '
        'interest in arranging a visit.'
        )

    return body


def letter_closing():
    """ Return closing and signature of Thank You letter. """
    closing = blank_lines()
    closing += 'Sincerely,'
    closing += blank_lines(2)
    closing += 'Mr. F\nActing Director\n(800) 555-1234'

    return closing
    

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


def thank_you_prompt(donors):
    """   """
    hor_bar()
    print("[Send 'Thank You' menu]\n"
          "Type 'menu' to return to main menu.")
    
    while True:
        response = input('--> ')

        if response in ['list', 'l']:
            list_donor_names()

        elif response in ['m', 'menu']: break

        elif response.lower() not in [k.lower() for k in donors.keys()]:
            # TODO see if I need to return add_new_donor to donors object
            # here or if global namespace donors will get updated in
            # add_new_donor function
            new_donor = response
            verify = verify_add_donor(new_donor)

            if verify[0] == 'y':
                amount = prompt_for_amount(new_donor)
                add_new_donor(new_donor, amount)

                compose_letter(new_donor, amount)
                
                return

        elif response.lower() in [k.lower() for k in donors.keys()]:
            donor = response
            new_amount = prompt_for_amount(donor)
            add_donation_to_history(donor, new_amount)

            compose_letter(donor, amount)

            return

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
    donors = dict([('William Gates, III', {'donations': [1, 5, 100000000]}),
                   ('Mark Zuckerberg', {'donations': [378000, 5000, 20.01]}),
                   ('Jeff Bezos', {'donations': [29000000, 34000, 709000]}),
                   ('Paul Allen', {'donations': [750000, 513895, 30592.50]}),
                   ('John Ferrell', {'donations': [520000000000]})])

    print('\nWelcome to the Mailroom applicaton.')

    main()

    print('\nThank you for using Mailroom. Have a nice day!')
