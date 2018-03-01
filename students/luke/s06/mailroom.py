#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom
"""

# List of donors -- global but not const
donor_list = {}

# Format of thank-you notes
THANK_YOU = "Thank you, {}, for your donation(s) of ${}!\n"

# Destination file
OUTFILE = "{}.txt"


def get_action():
    try:
        action = input(("Select an action and press return:\n"
                        "[S]end a thank-you (add users and donations)\n"
                        "[W]rite thank-you letters to file\n"
                        "[C]reate a report\n"
                        "[Q]uit\n"
                        "> ")).lower()

    except EOFError:  # Catch ^D
        return None
    except KeyboardInterrupt:  # Catch ^C
        return None

    return action


def do_action(action):
    """ Call appropiate action function.  Return false if action is quit. """
    if action == "c":
        create_report()
    elif action == "s":
        add_donations()
    elif action == "w":
        write_thankyous()
    elif action == "q":
        return False
    else:
        raise NotImplementedError(f"Action {action} not implemented")

    return True


def build_thankyou(name):
    """ Apply thankyou format string to name """
    if not donor_list.get(name):
        raise NameError(f"{name} not in database")

    return (THANK_YOU.format(name, sum(donor_list[name])))


def list_donors():
    """ return list donor names """
    donors = ""
    for n in donor_list:
        print(f"{n}")


def driver():
    """ Main loop for mailroom """
    done = False
    while not done:
        action = get_action()
        if not action:
            done = True
        if not do_action(action):
            done = True


def add_donation(name, amount):
    """ Add donation for name.  Add name if it doesn't exist """
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
                break

            try:
                donation_amount = int(value)
            except ValueError:
                print("Invalid input, reenter.")
                continue

            add_donation(name, donation_amount)

        done = True
        print(build_thankyou(name))


def write_thankyous():
    """ Write thankyou strings to files, one per donor """
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


def get_db():
    """ Return donor list. """
    return donor_list


if __name__ == '__main__':
    # Store donors/history in dictionary
    donor_list["alice"] = [5]
    donor_list["bob"] = [1, 2]
    donor_list["carol"] = [1, 5, 100]
    donor_list["dan"] = [5]
    donor_list["erin"] = [2, 1]

# Non-interactive unit tests
    assert(build_thankyou("dan") == "Thank you, dan, for your donation(s) of $5!\n")
    assert(generate_stats("carol") == (106, 3, 106/3))

    # Start main loop
    driver()
