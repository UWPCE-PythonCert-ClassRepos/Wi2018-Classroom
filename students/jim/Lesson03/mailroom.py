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

    user_input = input("> ")
    user_input = int(user_input)

    if user_input == 1:
        send_thanks()
    elif user_input == 2:
        create_report()
    elif user_input == 3:
        exit(0)

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

    donor_data[donor_name] = donor_data[donor_name].append(donation_amt)

    print("Dear {}:".format(donor_name))
    print("\n")
    print("Thank you so much for your kind donation of {} dollars.".format(donation_amt))
    print("It will be put to great use. Give yourself a big pat on the back.")
    print("\n")
    print("Sincerely,")
    print("The Management.")

    init_script()

def list_donors():
    for donor_name in donor_data.keys():
        print(donor_name)
    send_thanks()

init_script()
