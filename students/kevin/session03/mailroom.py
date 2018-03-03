#!/usr/bin/env python3

def add_new_donor():
    """   """
    pass


def add_donation_to_history():
    """   """
    pass



if __name__ == '__main__':

    donors = dict([('William Gates, III', {'donations': (1, 5, 100000000)}),
                   ('Mark Zuckerberg', {'donations': (378000, 5000, 20.01)}),
                   ('Jeff Bezos', {'donations': (29000000, 34000, 709000)}),
                   ('Paul Allen', {'donations': (750000, 513895, 30592.50)}),
                   ('John Ferrell', {'donations': (520000000000)})])

    print('\nWelcome to the Mailroom applicaton.\n\n'
          'What would you like to do? (Select one):')
    
    while True:
        response = input("  (1) Send a 'Thank You'\n"
                         "  (2) Create a Report\n"
                         "  (3) quit\n"
                         "  --> ")

        if response.lower() in ['1', 'send', 'send a thank you', 'thank you']:
            pass

        if response.lower() in ['2', 'create', 'report', 'create a report']:
            pass
        
        if response.lower() in ['3', 'q', 'quit', 'exit']: break

        else:
            print("I didn't understand your input.\n"
                  "Please select one of the following options:")


    print('\nThank you for using Mailroom. Have a nice day!')
