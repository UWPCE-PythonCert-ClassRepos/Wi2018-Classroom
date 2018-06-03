import json


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
        if name in self.data.keys():
            self.data[name].append(amount)
        else:
            self.data[name] = [amount]
    

if __name__ == "__main__":
    print("Donations database manager")
    print("1) View dononation information")
    print("2) Add donation information")
    print("3) Load")
    print("4) Save")
    print("5) Exit")
    user_selection = input(">")
    print(user_selection)