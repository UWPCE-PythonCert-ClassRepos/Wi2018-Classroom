#!/usr/bin/env python

# Programming in python B Winter 2018
# March 17, 2018
# Mailroom Session 9 - Reporting
# Refactored
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class Reports(object):
    """ Process data using files """

    # --Constructor--
    def __init__(self, id=""):
        # Attributes
        self.id = id

    # --Methods--
    @staticmethod
    def thank_you_printing(name, amount):
        line_divider = "*" * 50
        print(f'''
        {line_divider}
        {name}
        Dear {name},
        Thank you for your charitable gift of ${amount}.
        {line_divider}
        ''')

    @staticmethod
    def gen_letter_body(name, amount):

        report_text = (f'''Dear {name},
        Thank you for your charitable gift of ${amount}.
                    It will be put to very good use.
                                    Sincerely,
                                            --The Cool Team''')
        return (report_text)
