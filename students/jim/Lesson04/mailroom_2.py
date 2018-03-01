import sys

# Pre-populated data structure in the global namespace
donor_data = {}
donor_data["Eric Idle"] = [500, 300, 100]
donor_data["John Cleese"] = [750, 400, 50]
donor_data["Michael Palin"] = [1000, 150, 25]
donor_data["Terry Gilliam"] = [200, 200, 10]
donor_data["Graham Chapman"] = [375, 42, 7]


def init_script():
    print("Welcome to the Boring Task Automator!")
    print("-"*37)
    print("(1) Send a thank you")
    print("(2) Create a report")
    print("(3) Quit")

    menu_dict = {"1" : send_thanks,\
                 "2" : create_report,\
                 "3" : sys.exit }

    user_input = input("> ")

    menu_dict[user_input]()


def send_thanks():
    print("Enter the full name of the donor to thank.")
    print("Type 'list' for a list of active donors.")
    donor_name = input("> ")

    if donor_name == "list":
        list_donors()

    elif donor_name not in donor_data.keys():
        donor_data[donor_name] = []
        print("Donor", donor_name, "not found; added to donor list.")

    donation_amt = int(input("How much is the donation? "))
    donor_data[donor_name].append(donation_amt)
    print_letter(donor_name, donation_amt)

    # Back to the menu
    init_script()


def list_donors():
    for donor_name in donor_data.keys():
        print(donor_name)
    send_thanks()


def create_report():
    print("Donor Name\t| Total Given \t| Num Gifts \t| Average Gift")
    print("-"*62)
    for donor in donor_data.keys():
        donation_total = round(sum(donor_data[donor]), 2)
        donation_number = len(donor_data[donor])
        donation_avg = round((donation_total / donation_number), 2)
        print(donor, "\t\t", donation_total, "\t\t", donation_number, "\t", donation_avg)

    # Back to the  menu
    init_script()


def print_letter(donor_name, donation_amt):
    print("Dear {}:\n".format(donor_name))
    print("Thank you so much for your kind donation of {} dollars.".format(donation_amt))
    print("It will be put to great use. Give yourself a big pat on the back.\n")
    print("Sincerely,")
    print("The Management.")
    return


if __name__ == '__main__':
    init_script()
