import json
import pdb

class DonorDatabase():
    
    def __init__(self):
        self.data = {}
    
    def send_thanks_to(self, name):
    # Prints a thank you note sent to <name>
        print("Dear {}:\n".format(name))
        print("Thank you kindly for your recent donation of {} dollars."\
            .format(self.data[name][-1]))
        print("Rest assured that it will be put to good use.\n")
        print("Respectfully,\n")
        print("The Management")

    #def create_report

    def total_donations_from(self, name):
        return sum(self.data[name])

    def num_donations_from(self, name):
        return len(self.data[name])
    
    def average_donation_from(self, name):
        return self.total_donations_from(name) / self.num_donations_from(name)

    def new_donation(self, name, amount):
        if name not in self.data.keys():
            self.data[name] = []
        for a in amount:
            self.data[name].append(a)
        return

    def user_menu(self):
        print("Donations database manager")
        print("1) View dononation information")
        print("2) Add donation information")
        print("3) Load")
        print("4) Save")
        print("5) Exit")
        user_selection = input(">")
        user_selection = int(user_selection)

        if user_selection == 1:
            print(self.data)
            self.user_menu()

        elif user_selection == 2:
            donor_name = input("Name of this donor? ")
            donations = input("Dollar amount of {}'s donations? ".format(donor_name))
            donations = donations.split(",")
            donations = [int(d) for d in donations]
            self.new_donation(donor_name, donations)
            self.user_menu()
            
        elif user_selection == 3:
            # load database from json
            pass

        elif user_selection == 4:
            # save database to jason
            pass

        else:
            exit(0)

if __name__ == "__main__":
    ddb = DonorDatabase()
    ddb.user_menu()