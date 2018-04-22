#!/usr/bin/env python3
import functools

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom
"""

@functools.total_ordering
class Donor:
    """ A record of a donor and their donations """
    def __init__(self, name):
        self.donations = []
        self.name = name


    def __eq__(self, other):
        return self.name == other.name


    def __lt__(self, other):
        return self.name < other.name


    def add_donation(self, donation):
        self.donations.append(donation)


class DonorList:
    """ Create and use a list of donors and their donations """
    # Format of thank-you notes
    THANK_YOU = "Thank you, {}, for your donation(s) of ${}!\n"
    # Destination file
    OUTFILE = "{}.txt"


    def __init__(self):
        self.donors = {}  # Donor.name : Donor  -- is this idiom OK?


    def get_donors(self):
        return self.donors


    def get(self, name):
        return self.donors.get(name)


    def get_action(self):
        try:
            action = input(("Select an action and press return:\n"
                            "[S]end a thank-you (add users and donations)\n"
                            "[W]rite thank-you letters to file\n"
                            "[C]reate a report\n"
                            "[E]rase donor database\n"
                            "[Q]uit\n"
                            "> ")).lower()

        except EOFError:  # Catch ^D
            return None
        except KeyboardInterrupt:  # Catch ^C
            return None

        return action


    def do_action(self, action):
        """ Call action function.  Return false if action is quit. """
        if action == "c":
            self.create_report()
        elif action == "s":
            self.add_donations()
        elif action == "w":
            self.write_thankyous()
        elif action == "e":
            self.clear_db()
        elif action == "q":
            return False
        else:
            raise NotImplementedError(f"Action {action} not implemented")

        return True


    def build_thankyou(self, name):
        """ Apply thankyou format string to name """
        if not self.donors.get(name):
            raise NameError(f"{name} not in database")

        return (self.THANK_YOU.format(name,
                                      sum(self.donors[name].donations)))


    def list_donors(self):
        """ return list donor names """
        ds = []
        for n in self.donors:
            ds.append(f"{self.donors[n].name}")  # Clunky, name == n
        return ds


    def driver(self):
        """ Main loop for mailroom """
        done = False
        while not done:
            action = self.get_action()
            if not action:
                done = True
            if not self.do_action(action):
                done = True


    def add_donation(self, name, amount):
        """ Add donation for name.  Add name if it doesn't exist """
        if not self.donors.get(name):
            print("Adding new donor: " + name)
            self.donors[name] = Donor(name)

        self.donors.get(name).add_donation(amount)


    def add_donations(self):
        """ Add donation history for a(n optionally new) user """
        done = False
        while not done:
            try:
                name = input("Enter donor name (or \"list\" for list): ").lower()
            except EOFError:
                return
            except KeyboardInterrupt:
                return

            if name == "list":
                for d in self.list_donors():
                    print(f"{d}\n")
                continue

            moredonations = True
            while moredonations:
                try:
                    value = input("Enter donation amount or [enter] finished: ")
                except EOFError:
                    break
                except KeyboardInterrupt:
                    break
                if not donation_amount:
                    break

                try:
                    donation_amount = int(value)
                except ValueError:
                    print("Invalid input, reenter.")
                    continue

                add_donation(name, donation_amount)

            done = True
            print(self.build_thankyou(name))


    def write_thankyous(self):
        """ Write thankyou strings to files, one per donor """
        for d in self.donors:
            with open(OUTFILE.format(d.name), 'w') as outfile:
                outfile.write(build_thankyou(d.name))


    def generate_stats(self, donor):
        """ Return total given, number of gifts, average gift for name """
        total = sum(self.donors[donor].donations)
        number = len(self.donors[donor].donations)
        average = total / number
        return total, number, average


    def create_report(self):
        """ Display: Donor Name | Total Given | Num Gifts | Average Gift """
        print("Donor Name | Total Given | Num Gifts | Average Gift")
        for d in self.donors:
            total, number, average = generate_stats(d)
            print(f"{d:10} | "
                  f"{total:11.2f} | "
                  f"{number:9d} | "
                  f"{average:12.2f}")


    def clear_db(self):
        """ Clear donor_list """
        self.donors = {}  # Need global?


    def prepopulate_db(self):
        """
        donor_list["alice"] = [5]
        donor_list["bob"] = [1, 2]
        donor_list["carol"] = [1, 5, 100]
        donor_list["dan"] = [5]
        donor_list["erin"] = [2, 1]
        """
        self.donors["alice"] = Donor("alice")
        self.donors["alice"].add_donation(5)
        self.donors["bob"] = Donor("bob")
        self.donors["bob"].add_donation(1)
        self.donors["bob"].add_donation(2)
        self.donors["carol"] = Donor("carol")
        self.donors["carol"].add_donation(1)
        self.donors["carol"].add_donation(5)
        self.donors["carol"].add_donation(100)
        self.donors["dan"] = Donor("dan")
        self.donors["dan"].add_donation(5)
        self.donors["erin"] = Donor("erin")
        self.donors["erin"].add_donation(2)
        self.donors["erin"].add_donation(1)


if __name__ == '__main__':
    donor_list = DonorList()
    # Store donors/history in dictionary
    donor_list.prepopulate_db()
    # Start main loop
    donor_list.driver()
