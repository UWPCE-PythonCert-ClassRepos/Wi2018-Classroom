#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4192822?module_item_id=8336629
"""

import json_save.json_save.json_save_dec as js
import json

# Format of thank-you notes
THANK_YOU = "Thank you, {}, for your donation(s) of ${}!\n"

# Destination filename for thank-yous
OUTFILE = "{}.txt"

# Persistent DB filename
DB_FILE = "db.json"


@js.json_save
class DonorDB(object):
    db = js.Dict()


    def __init__(self):
        try:
            with open(DB_FILE, 'r') as f:
                contents = f.read()
            self.db = js.from_json(contents)
            print(f"Read db contents from {DB_FILE}")
        except json.decoder.JSONDecodeError:
            print(f"Could not load database from {DB_FILE}, is it corrupt?")
            raise
        except IOError:
            print(f"Didn't find db in {DB_FILE}; using defaults")
            self.db["alice"] = [5]
            self.db["bob"] = [1, 2]
            self.db["carol"] = [1, 5, 100]
            self.db["dan"] = [5]
            self.db["erin"] = [2, 1]

    
    def persist(self):
        try:
            with open(DB_FILE, 'w') as f:
                f.write(self.to_json())
        except IOError:
            print(f"IOError writing to {DB_FILE}")
            raise



def persist_db(donor_list):
    donor_list.persist()


def get_action():
    try:
        action = input(("Select an action and press return:\n"
                        "[S]end a thank-you (add users and donations)\n"
                        "[W]rite thank-you letters to file\n"
                        "[C]reate a report\n"
                        "[E]rase donor database\n"
                        "[P]ersist donor database to disk (./db.json)\n"
                        "[Q]uit\n"
                        "> ")).lower()

    except EOFError:  # Catch ^D
        return None
    except KeyboardInterrupt:  # Catch ^C
        return None

    return action


def do_action(action, donor_list):
    """ Call appropiate action function.  Return false if action is quit. """
    if action == "c":
        create_report(donor_list.db)
    elif action == "s":
        add_donations(donor_list.db)
    elif action == "w":
        write_thankyous(donor_list.db)
    elif action == "e":
        clear_db(donor_list)
    elif action == "q":
        return False
    elif action == "p":
        persist_db(donor_list)
    else:
        raise NotImplementedError(f"Action {action} not implemented")

    return True


def build_thankyou(name, donor_list):
    """ Apply thankyou format string to name """
    if not donor_list.db.get(name):
        raise NameError(f"{name} not in database")

    return (THANK_YOU.format(name, sum(donor_list.db[name])))


def list_donors(donor_list):
    """ return list donor names """
    donors = ""
    for n in donor_list.db:
        print(f"{n}")


def driver(donor_list):
    """ Main loop for mailroom """
    done = False
    while not done:
        action = get_action()
        if not action:
            done = True
        if not do_action(action, donor_list):
            done = True


def add_donation(name, amount, donor_list):
    """ Add donation for name.  Add name if it doesn't exist """
    if not donor_list.db.get(name):
        print("Adding new donor: " + name)
        donor_list.db[name] = []

    donor_list.db[name].append(amount)


def add_donations(donor_list):
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
            print(list_donors(donor_list))
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

            add_donation(name, donation_amount, donor_list)

        done = True
        print(build_thankyou(name, donor_list))


def write_thankyous(donor_list):
    """ Write thankyou strings to files, one per donor """
    for d in donor_list.db:
        with open(OUTFILE.format(d), 'w') as outfile:
            outfile.write(build_thankyou(d, donor_list))


def generate_stats(name, donor_list):
    """ Return total given, number of gifts, average gift for name """
    total = sum(donor_list.db[name])
    number = len(donor_list.db[name])
    average = total / number
    return total, number, average


def create_report(donor_list):
    """ Display table: Donor Name | Total Given | Num Gifts | Average Gift """
    print("Donor Name | Total Given | Num Gifts | Average Gift")
    for d in donor_list.db:
        total, number, average = generate_stats(d, donor_list)
        print(f"{d:10} | "
              f"{total:11.2f} | "
              f"{number:9d} | "
              f"{average:12.2f}")


def get_db():
    """ Return donor list to external caller """
    return myDonorDB.donor_db


def clear_db(donor_list):
    """ Clear donor_list """
    donor_list.db = {}


donor_list = DonorDB()
if __name__ == '__main__':

    # Start main loop
    driver(donor_list)
