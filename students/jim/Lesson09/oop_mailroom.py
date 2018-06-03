class Donor:

    def __init__(self, donor_name, *args):
        self.name = donor_name
        self.donations = []
        self.add_donations(*args)

    def add_donations(self, *args):
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                self.donations.append(arg)
                print(self.__str__() + ": added donation of " + str(arg))

    def list_donations(self):
        print(self.donations)

    def donation_total(self):
        return sum(self.donations)

    def num_donations(self):
        return len(self.donations)

    def avg_donation(self):
        return self.donation_total / self.num_donations

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Donor(" + self.name + ")"


class DonorCollection:

    def __init__(self):
        self.d_list = list()

    def append_donors(self, *args):
        for item in args:
            if type(item) is Donor:
                self.list.append(item)

    def num_donors(self):
        return len(self.list)

    def generate_report(self):
        print("Donor Name\t\tTotal Given\t\tNum Gifts\t\tAvg Gift")
        print("-"*60)
        for d in self.d_list:
            pass

def generate_thanks(donor, mode="recent"):

    if mode == "total":
        # TODO: this could be reduced
        donation_val = sum(donor.donations)
    else:
        donation_val = donor.donations[-1]

    print("Dear {}:\n".format(donor))
    print("Thank you for your kind donation of ${:03.2f}.".format(donation_val))
    print("Rest assured that it will be put to good use.\n")
    print("Sincerely,")
    print("The Management")


d = Donor("Turanga Leela", 26, 73, 59, 67.23)
print(d)
d.list_donations()
dcoll = DonorCollection()
dcoll.append_donors(d)
dcoll.generate_report()