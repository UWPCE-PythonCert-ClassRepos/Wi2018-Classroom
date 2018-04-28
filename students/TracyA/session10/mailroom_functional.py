#!/usr/bin/env python

# Programming in python B Winter 2018
# March 22, 2018
# Mailroom Session 10 Functional mailroom
# Refactored
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# -- Data --#
donor_dict = {
    'Paul Allen': [1000000.00, 50000.00, 300000.00],
    'Bill Gates': [500000.00, 80000.00, 70000.00],
    'Warren Buffett': [30000.00, 30000.00, 40000.00],
    'Elon Musk': [1000000.00, 30000.00],
    'Mark Zuckerberg': [10000.00, 50000.00, 12000.00, 400000.00],
}


# -- Processing --#
def get_user_choice():
    print("""
    MailRoom Functional Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Send Letters To Everyone
    4) Double Donations (map)
    5) Double Donations over $500 (filter, map)
    6) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 6]: ")
    return (user_choice.strip())


def process_menu(menu_item):
    if menu_item == '1':
        send_thanks()
    elif menu_item == '2':
        format_charity_structure()
    elif menu_item == '3':
        create_individual_letters()
    elif menu_item == '4':
        factor_name()
    elif menu_item == '5':
        filter_name()


def send_thanks():
    '''Prompts the user for a donor name, pre-existing or new.'''
    while (True):
        name = input("Please enter FULL NAME, enter 'LIST' for names, or 'MAIN' for menu: ")
        if name.lower() == "list":
            print_donors()
            print(' ')
        elif name.lower() == "main":
            return
        else:
            process_thank_you(name)


def process_thank_you(name):
    '''Prompt the user for a donation amount following the prompt for donor name.'''
    try:
        gift_amount = int(input("Please enter $$ donation $$ amount for " + name + ":"))
        if name in donor_dict.keys():
            # We found the name so update the giving values
            original_list = donor_dict.get(name)
            original_list.append(gift_amount)
            donor_dict[name] = original_list
            thank_you_printing(name, gift_amount)
        else:
            # We didn't find the name so create a new key value pair
            donor_dict[name] = [gift_amount]
            thank_you_printing(name, gift_amount)
    except ValueError as e:
        print("\n Error: " + str(e) + " Please enter a number amount.\n ")
        process_thank_you(name)


def thank_you_printing(name, amount):
    line_divider = "*" * 50
    print(f'''
    {line_divider}
    {name}

    Dear {name},
    Thank you for your charitable gift of ${amount}.
    {line_divider}
    ''')


def print_donors():
    comp = {key for key in donor_dict.keys()}
    print(comp)


def format_charity_structure():
    print('')
    print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
    print('-' * 55)
    for key in donor_dict:
        donor_list = donor_dict.get(key)
        sum_values = "{:.2f}".format(sum(donor_list))
        ave_values = "{:.2f}".format(sum(donor_list) / len(donor_list))
        print('{:20}{:>15}{:>10}{:>10}'.format(key, sum_values, len(donor_list), ave_values))


def create_individual_letters():
    try:
        for key in donor_dict:
            donor_list = donor_dict.get(key)
            sum_values = "{:.2f}".format(sum(donor_list))
            key.replace(" ", "_")
            objFileName = key.replace(" ", "_") + ".txt"
            objMyFile = open(objFileName, "w")
            objMyFile.write(gen_letter_body(key, sum_values))
            objMyFile.close()
            print(objFileName + " file saved.")
    except IOError:
        print("\n" + "File error!")


def gen_letter_body(name, amount):
    report_text = (f'''Dear {name},
    Thank you for your charitable gift of ${amount}.
            It will be put to very good use.
                        Sincerely,
                              --The Cool Team''')
    return (report_text)


def factor_name():
    '''Prompts the user for a donor name for factoring up.'''
    print("\nThis feature will factor up a donor's contributions by two. Donor names:")
    print(donor_dict)
    name = input("\nPlease enter FULL NAME (Jane Doe): ")
    if name.lower() == "main":
        return
    else:
        process_factor(name)


def process_factor(name):
    '''Factor (map) donations.'''
    if name in donor_dict.keys():
        original_list = donor_dict.get(name)
        print("Original donation list: " + str(original_list))
        new_list = list(map(fun, original_list))
        donor_dict[name] = new_list
        print("New donation list: " + str(new_list))
    else:
        print("Sorry, that name is not on record, try again.")
        factor_name()


def filter_name():
    '''Prompts the user for a donor name for filtering AND factoring up.'''
    print("\nThis feature will factor up a donor's contributions by two if over $500. Donor names:")
    print(donor_dict)
    name = input("\nPlease enter FULL NAME (John Doe): ")
    if name.lower() == "main":
        return
    else:
        process_filter(name)


def process_filter(name):
    '''Filter and Factor (map) donations.'''
    if name in donor_dict.keys():
        original_list = donor_dict.get(name)
        print("Original donation list: " + str(original_list))
        new_list = list(map(fun, filter(lambda x: x >= 500, original_list)))
        donor_dict[name] = original_list + new_list
        print("New donation list: " + str(donor_dict[name]))
    else:
        print("Sorry, that name is not on record, try again.")
        filter_name()


def fun(x):
    return x * 2


# -- Presentation (Input/Output) --#
if __name__ == '__main__':

    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "6":
            print("Goodbye!")
            break
        else:
            process_menu(get_user_action)
