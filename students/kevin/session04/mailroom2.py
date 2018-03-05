#!/usr/bin/env python3.6
import datetime as dt


def prompt_for_amount(name):
    """ Prompt user for donation amount and return value. """
    amount = input(f"How much did {name} donate? ")

    return ''.join(amount.split('$')[-1].split(','))


def add_new_donor(name, amount):
    """ Add new donor and donation amount to donor database. """
    donors[name] = dict([('name', name), ('donations', [float(amount)]),
                         ('latest_don', float(amount))])


def add_donation_to_history(name, amount):
    """ Add new donation to existing donor's records """
    donors[name]['donations'].append(float(amount))
    donors[name]['latest_don'] = float(amount)


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
    

def print_letter(letter_content):
    """ Style beginning and end of letter and print to console. """
    print(f'<BEGIN EMAIL>\n{letter_content}\n<END EMAIL>')


def compose_letter(name, amount):
    """ Print donation Thank You letter to screen. """
    letter = letter_preamble(name)
    letter += letter_body(name, amount)
    letter += letter_closing()

    return letter


def send_letters_all():
    """  """
    pass


def letter_date():
    """ Return today's date, formatted for letter preamble. """
    return dt.datetime.now().strftime('%d %B %Y')


def letter_preamble(name):
    """ Return Thank You letter preamble. """
    preamble = letter_date()
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


def compose_letter_dict(name):
    """ Return Thank You letter composed from single template, filled with dict. """
    letter = (
        f'{letter_date()}'
        f'{blank_lines(2)}'
        'Dear {name},\n\nThank you for your generous donation of ${latest_don:,.2f}. '
        'Your gracious support helps us continue our important work doing what we do. '
        'We look forward to continuing to partner with you in the future. Please contact '
        'us if you have any questions or have any interest in arranging a visit.'
        f'{blank_lines()}Sincerely,{blank_lines(2)}Mr. F\nActing Director\n'
        '(800) 555_1234'.format(**donors[name])
        )

    return letter
    

def hor_bar(count=35):
    """   """
    return "-" * count


def main_menu_prompt():
    """   """
    response = input("   (1) Send a 'Thank You'\n"
                     "   (2) Create a Report\n"
                     "   (3) quit\n"
                     "--> ")

    if response.lower() in ['1', 'send', 'send a thank you', 'thank you']:
        return 0

    elif response.lower() in ['2', 'create', 'report', 'create a report']:
        return 1

    elif response.lower() in ['3', 'q', 'quit', 'exit']:
        return 3


def thank_you_prompt():
    """ Direct Thank You letter menu user input """
    print(hor_bar())
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

                # letter = compose_letter(new_donor, amount)
                letter = compose_letter_dict(new_donor)
                print_letter(letter)
                
                return

        elif response.lower() in [k.lower() for k in donors.keys()]:
            donor = response
            new_amount = prompt_for_amount(donor)
            add_donation_to_history(donor, new_amount)

            letter = compose_letter(donor, new_amount)
            print_letter(letter)

            return

    return
    # TODO see if I need to return donors to get any updates back into
    # the donors object in the global namespace
    # return donors


def report_prompt():
    """ Direct report menu user input. """
    print(hor_bar())
    print("[Donor Summary Report]\n")

    print(assemble_report())

    return
    # return donors


def assemble_report():
    """ Return nicely formatted donor report. """
    col_widths = [25, 20, 12, 20]
    headers = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']

    header_row = assemble_header(headers, col_widths)
    hor_line = hor_bar(len(header_row))
    table_body = assemble_table(col_widths)

    return f'{header_row}\n{hor_line}\n{table_body}'


def assemble_header(headers, col_widths):
    """ Return header row for donor report table. """
    header = f'{headers[0]:<{col_widths[0]-1}}'

    count = 1
    for field in headers[1:]:
        header += f'|{headers[count]:^{col_widths[count]+1}}'
        count+=1

    return header


def assemble_table(col_widths):
    """ Return table body, fetching all computed values from other functions. """
    table = ''

    for k, v in donors.items():
        total = get_total(k)
        num_gifts = get_num_gifts(k)
        avg_gift = get_avg_gift(k)
        # import pdb; pdb.set_trace()
        table += (f'{k:<{col_widths[0]}}${total:{col_widths[1]},.2f}'
                  f'{num_gifts:{col_widths[2]}d}   ${avg_gift:{col_widths[3]},.2f}\n')

    return table


def get_total(name):
    """ Return total donations for supplied donor name """
    return sum(donors[name]['donations'])


def get_num_gifts(name):
    """ Return total number of gifts given by supplied donor name. """
    return len(donors[name]['donations'])


def get_avg_gift(name):
    """ Return the average of all of the supplied donor's donations. """
    return get_total(name) / get_num_gifts(name)
    

def main():
    """ Show main menu, prompting user for selection.  """
    while True:
        print(hor_bar())
        print('[Main menu]\n'
              'What would you like to do? (Select one):')

        switch_func_dict = {
            0: thank_you_prompt,
            1: report_prompt,
            2: send_letters_all
        }

        response = None

        while response not in switch_func_dict.keys():
            response = main_menu_prompt()

            if response == 3: return

            if response in switch_func_dict.keys():
                switch_func_dict.get(response)()
                break

            print("Invalid input. Please select one:")

    return


if __name__ == '__main__':
    # Initialize 5 donors and at least 1 donation for each.
    donors = dict([('William Gates, III', {'name': 'William Gates, III',
                                           'donations': [1, 5, 100000000],
                                           'latest_don': 100000000}),
                   ('Mark Zuckerberg', {'name': 'Mark Zuckerberg',
                                        'donations': [378000, 5000, 20.01],
                                        'latest_don': 20.01}),
                   ('Jeff Bezos', {'name': 'Jeff Bezos',
                                   'donations': [29000000, 34000, 709000],
                                   'latest_don': 709000}),
                   ('Paul Allen', {'name': 'Paul Allen',
                                   'donations': [750000, 513895, 30592.50],
                                   'latest_don': 30592.50}),
                   ('John Ferrell', {'name': 'John Ferrell',
                                     'donations': [520000000000],
                                     'latest_don': 520000000000})])

    print('\nWelcome to the Mailroom applicaton.')

    main()

    print('\nThank you for using Mailroom. Have a nice day!')
