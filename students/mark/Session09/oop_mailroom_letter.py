#!/usr/bin/env python3


"""

Session09
Import this class into oop_mailroom.py

"""

class LetterOop(object):


    def format_donor_name(self, donor_names):
        if ',' in donor_names:
            name_title=donor_names.split(',')
            i_var=name_title[0].title() + ','
            donor_names=i_var.replace(',', "," + name_title[1].upper())
            return(donor_names)
        else:
            name_title=donor_names
            return(donor_names.title())


    def send_thank_you(self, donor_db):
        """
        Record a donation, create a thank you letter.
        """

        # use a while loop to get the user input and execute a function
        # basic input checking, strip whitespace
        while True:
            name = input("Enter a donor's name "
                         "(or 'list' to see all donors or 'menu' to exit)> ").strip()
            if name == "list":
                self.print_donor_name(donor_db)
            elif name == "menu":
                return
            else:
                if name.lower() in donor_db.keys():
                    print("name: ", self.format_donor_name(name), "found.")
                    print(self.create_letter(name, donor_db))
                else:
                    if name.lower() not in donor_db.keys():
                        print("name: ", self.format_donor_name(name), "is NOT found.")
                        print("debug: adding a function call to add donor.")
                        add_donor_info(name, donor_db)
                break


    def create_letter(self, donor, donor_db):
        """
        Create a thank you letter for the donor
        :param: donor/string, donor_db dict/string:tuple
        :returns: string with letter
        """
        return '''\n
              Dear {},

              Thank you for your very kind donation of ${:.2f}.
              It will be put to very good use.
              Your generous contributions to date totaling ${:.2f}
              allow us continue our mission and achive our joint goals.

                             Sincerely,
                                -The Team
              '''.format(self.format_donor_name(donor), donor_db[donor][-1], sum(donor_db[donor]))


    def send_letters_to_all(self, donor_db):
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

            file_name=self.format_donor_name(k).replace(',','').replace(" ","_") + ".txt"
            with open(file_name, 'w') as fh1:
                fh1.write(self.create_letter(k, donor_db))

            print(self.create_letter(k, donor_db))

        return 0

    def print_donor_name(self, donor_db):
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



if __name__ == '__main__':
    print("this is the main section")

    ### code below works, need work on called functions (works)
    running = True
    while running:
        selection=print_menu()
        if selection == "1":
            send_thank_you()
        elif selection == "2":
            super.print_donor_report(donor_db)
        elif selection == "3":
            send_letters_to_all(donor_db)
        elif selection == "4":
            running = False
        elif selection == "5":
            add_new_donor(donor_db)
        else:
            print("Please select an option 1-5 from the menu")
