#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom
"""

# Store donors/history in dictionary
donor_list = {"alice": [5],
              "bob": [1, 2],
              "carol": [1, 5, 100],
              "dan": [5],
              "erin": [2, 1]}

# Format of thank-you notes
THANK_YOU = "Thank you, {}, for your donation(s) of ${}!\n"

# Destination file
OUTFILE = "{}.txt"


def driver():
    """ Main loop for mailroom """
    done = False
    while not done:
        try:
            action = input(("Select an action and press return:\n"
                            "[S]end a thank-you (add users and donations)\n"
                            "[W]rite thank-you letters to file\n"
                            "[C]reate a report\n"
                            "[Q]uit\n"
                            "> ")).lower()
            while action not in "swcq":
                action = input("Bad option, reenter > ").lower()

            if action == "s":
                add_donations()
            elif action == "w":
                write_thankyous()
            elif action == "c":
                create_report()
            else:
                done = True
        except EOFError:
            done = True
        except KeyboardInterrupt:
            done = True
    return


def build_thankyou(name):
    """ Apply thankyou format string to name """
    return (THANK_YOU.format(name, sum(donor_list[name])))


def list_donors():
    """ return list donor names """
    donors = ""
    for n in donor_list:
        donors += n + "\n"
    return donors[:-1]  # Trim trailing newline


def add_donation(name, amount):
    """ add donation for name.  add name if it doesn't exist """
    if not donor_list.get(name):
        print("Adding new donor: " + name)
        donor_list[name] = []

    donor_list[name].append(donation_amount)


def add_donations():
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
            print(list_donors())
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
                break;

            try:
                donation_amount = int(value)
            except ValueError:
                print("Invalid input, reenter.")
                continue

            add_donation(name, donation_amount)

        done = True
        print(build_thankyou(name))
    return


def write_thankyous():
    """ write thankyou strings to files, one per donor """
    for d in donor_list:
        with open(OUTFILE.format(d), 'w') as outfile:
            outfile.write(build_thankyou(d))


def generate_stats(name):
    """ Return total given, number of gifts, average gift for name """
    total = sum(donor_list[name])
    number = len(donor_list[name])
    average = total / number
    return total, number, average

def create_report():
    """ Display table: Donor Name | Total Given | Num Gifts | Average Gift """
    print("Donor Name | Total Given | Num Gifts | Average Gift")
    for d in donor_list:
        total, number, average = generate_stats(d)
        print(f"{d:10} | "
              f"{total:11.2f} | "
              f"{number:9d} | "
              f"{average:12.2f}")
    return


# Non-interactive unit tests
assert(build_thankyou("dan") == "Thank you, dan, for your donation(s) of $5!\n")
assert(generate_stats("carol") == (106, 3, 106/3))


if __name__ == '__main__':
    driver()
