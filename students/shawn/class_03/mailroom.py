import statistics as stat
from collections import  namedtuple



#-----------------------------------------------------------------------*
# Classes to manage the interactions with database
#-----------------------------------------------------------------------*
class Donor(object):
    """Class to hold instances of each donor"""

    def __init__(self, fnam,lnam,donation=0):
        self.fnam = fnam
        self.lnam = lnam
        self.donation = [donation]

    def __str__(self):
        """
        :return: return formatted string for report
        """
        return f"{'{:<20}'.format(self.fnam + ' ' + self.lnam)}" \
               f"{'{:>20.2f}'.format( sum([i for i in self.donation]))}" \
               f"{'{:>20}'.format(len([i for i in self.donation if i>0]))}" \
               f"{'{:>20.2f}'.format(stat.mean([i for i in self.donation if i>0]))}"

    def add_donation(self,donation):
        """
        Append a donation to an existing donor
        :param donation: string
        :return: none
        """
        self.donation.append(float(donation))

    @property
    def keyval(self):
        """
        :return: key of dictionary item
        """
        return self.fnam.lower() + self.lnam.lower()

class Donors(object):

    """Class to hold dictionary of instances of Donor
     """
    def __init__(self):
        self.donors={}

    def get_or_create(self,donor):
        """
        Returns donor if exists, otherwise add donor to collection
        :param donor: instance of Donor
        :return: Donor, Bool - True if new donor
                            -  False if existing donor
        """
        k=donor.keyval
        if k not in self.donors:
            self.donors[k]=donor
            return donor,True
        return self.donors[k],False

    def read_data(self,fnam,lnam,donation=0):
        """
        Parse arguments into instance of Donor
        :param fnam: str - first name
        :param lnam: str - Last name
        :param donation:  str/float - donation amount
        :return: Bool - True if new, False if existing
                 Donor
        """
        d=Donor(fnam,lnam,donation)
        donor,created=self.get_or_create(d)
        if created:
            return True,donor
        else:
            donor.add_donation(donation)
            return False,donor

    def get(self,k):
        """
        Returns Donor by Key
        :param k: dictionary key
        :return: Donor
        """
        return k in self.donors,self.donors.get(k)

    def report(self):
        """
        Writes report to console.
        :return: None
        """
        print(f"{'{:<20}'.format('Donor')}{'{:>20}'.format('Total')}{'{:>20}'.format('Donations')}"f"{'{:>20}'.format('Average')}")
        print(f"{90*'-'}")
        [print(i) for i in self.donors.values()]
        print(f"{90*'-'}")
        return self

    def load_default(donors):
        """
        Load the default list of users in Donor collection
        :param donors: global list of Donor instances
        :return: None
        """

        data = [['Bill', 'Buckner', 1000.25],
                ['Bill', 'Buckner', 2300.00],
                ['Bill', 'Buckner', 300.33],
                ['Bill', 'Buckner', 950.00],
                ['Bill', 'Buckner', 250.25],
                ['Don', 'Baylor', 1141.50],
                ['Wade', 'Boggs', 5000.15],
                ['Wade', 'Boggs', 125.55],
                ['Wade', 'Boggs', 1000.00],
                ['Ted', 'Williams', 333.45],
                ['Jim', 'Rice', 225.98],
                ['Jim', 'Rice', 125.19],
                ['Jim', 'Rice', 352.76]]

        [donors.read_data(i[0],i[1],i[2]) for i in data]

        # data = [['Bill', 'Buckner', [1000.25,2300.00,300.33,950.00,250.25]],
        #         ['Don', 'Baylor', [1141.50]],
        #         ['Wade', 'Boggs', [5000.15,125.55,1000.00]],
        #         ['Ted', 'Williams', [333.45]],
        #         ['Jim', 'Rice', [225.98,125.19,352.76]]]
        #

#-----------------------------------------------------------------------*
# Prompt user for arg
#-----------------------------------------------------------------------*
def prompt_user(msg,limit=3):
    """
    Capture user input
    :param msg: Text string to display to the user
    :param limit: number of times to request valid input before terminating dialog
    :return: bool - True if valid arg, False if invalid
             str - user input
    """
    counter=0
    while True:
        counter+=1
        arg=input(f"{msg} >>")
        if len(arg)>0:
            return [True,arg]
        if counter==limit:
            print("We are done here")
            return [False, ""]

# -----------------------------------------------------------------------*
#  get user
# -----------------------------------------------------------------------*
def get_user(user):
    """
    Lookup donor from global collection. Recursively calls self when
    after adding a new user to prompt for donation amount
    :param user: str - full name of donor
    :return: Donor - Instance of donor
             amount - return donation for existing donor
    """
    k=user.replace(" ","").lower()
    donor=donor_list.get(k)
    if donor_list.get(k)[0]:
        amt=prompt_user(f"Enter the donation amount for {user}")
        if amt[0]:
            if amt[1].lower()!="quit":
                return donor_list.read_data(donor[1].fnam, donor[1].lnam, amt[1])
            else:
                return None
    else:
        is_add=prompt_user(f"Would you like to add '{user}' to the database? (Y/N)")
        if is_add[0]:
            if is_add[1].upper()=="Y":
                new_donor=donor_list.read_data(user.split(" ")[0], user.split(" ")[1])
                return get_user(new_donor[1].fnam + new_donor[1].lnam)

# -----------------------------------------------------------------------*
# Prompt user for arg
# -----------------------------------------------------------------------*
def send_thankyou():
    """
    If user exists, generates message in console.
    :return: True
    """
    while True:
        user=prompt_user("Enter the full name of the donor you with to thank (type 'list' to view donors)")
        if user[0]:
            if user[1].lower()=="list":
                for i, v in donor_list.donors.items():
                    print(v)
                print("\n")
            else:
                if user[1].lower()=='quit':
                    return True
                else:
                    donor=get_user(user[1])
                    if donor != None:
                        print(f"{'-'*100}"
                              f"\n\nDearest {donor[1].fnam},\n\nThank for your latest donation of {donor[1].donation[-1]}, "
                              f"bringing your total donations to {sum([i for i in donor[1].donation])}.\n\nSincerly,\nManagement\n"
                              f"{'-'*100}")

                    return True
        else:
            break
            return False



# -----------------------------------------------------------------------*
# Write report
# -----------------------------------------------------------------------*
def report(donors):
    """
    Calls the Donors.Report method to generate a report in the console
    :param donors: global instance of Donors collection
    :return: True
    """
    report=donors.report()
    return True

# -----------------------------------------------------------------------*
# Main menu
# -----------------------------------------------------------------------*
def main(msg,disp_dict,testarg=0):
    if msg == "test":
        return disp_dict.get(testarg)
    else:
        action = prompt_user(msg)
        if action[0]:
            if action[1] in ("1","2","3"):
                if action[1]=="2":
                    return disp_dict[action[1]](donor_list)
                else:
                    return disp_dict[action[1]]()
        else:
            print("Invalid selection\n")
            return True

def close():
    print("Closing...")
    return False

if __name__ == '__main__':
    # -----------------------------------------------------------------------*
    # seed the database
    # -----------------------------------------------------------------------*


    donor_list=Donors()
    donor_list.load_default()

    dd = {"1":send_thankyou, "2":report, "3":close}

    # -----------------------------------------------------------------------*
    # Prompt for action
    # -----------------------------------------------------------------------*
    status=True
    while status==True:
        status=main("**Welcome to MailRoom**\nPlease select from the following actions\n\n\t(1)Send a thank you\n\t(2)Create a report\n\t(3)Quit\n\nSelect",dd)





