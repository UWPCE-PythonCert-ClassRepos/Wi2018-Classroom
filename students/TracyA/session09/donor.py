#!/usr/bin/env python
import reporting as rp

# Programming in python B Winter 2018
# March 17, 2018
# Mailroom Session 9 - Reporting
# Refactored
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class Donor_object(object):
    '''Turns a dictionary into a class'''

    # --Constructor--
    def __init__(self, dictionary):
        '''Constructor'''
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __str__(self):
        """"""
        attrs = str([x for x in self.__dict__])
        return "Donor Names: %s" % attrs

    def print_screen_report(self):
        print('')
        print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name',
                                               '| Total Gifts', '| Num Gifts', '| Ave Gift'))
        print('-' * 55)
        for key in self.__dict__:
            donor_list = self.__dict__.get(key)
            sum_values = "{:.2f}".format(sum(donor_list))
            ave_values = "{:.2f}".format(sum(donor_list) / len(donor_list))
            print('{:20}{:>15}{:>10}{:>10}'.format(key, sum_values, len(donor_list), ave_values))

    def create_individual_letters(self):
        try:
            for key in self.__dict__:
                donor_list = self.__dict__.get(key)
                sum_values = "{:.2f}".format(sum(donor_list))
                key.replace(" ", "_")
                file_name = key.replace(" ", "_") + ".txt"
                my_file = open(file_name, "w")
                my_file.write(rp.Reports.gen_letter_body(key, sum_values))
                my_file.close()
        except IOError:
            return("\n" + "File error!")
        return ("*** Files saved! ***")
