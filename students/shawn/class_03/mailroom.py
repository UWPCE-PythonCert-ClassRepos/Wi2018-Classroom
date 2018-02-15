import statistics as stat
import math as m
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
        :return: return formatted string
        """
        return f"{self.fnam} {self.lnam} has {len([i for i in self.donation if i>0])} donations totalling {sum([i for i in self.donation])}"

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
        Writes report to console
        :return: None
        """
        result=[]
        for i,v in self.donors.items():
            line=[]
            line.append(v.fnam)
            line.append(v.lnam)
            line.append(v.donation)
            result.append(line)

        print(f"{'{:<20}'.format('Donor')}{'{:<15}'.format('Total')}{'{:<15}'.format('Donations')}"
              f"{'{:>10}'.format('Average')}")
        print(f"{63*'-'}")
        for r in result:
            print(f"{'{:<20}'.format(r[0] + ' ' + r[1])}",end=" ")
            print(f"{'{:<15.2f}'.format(sum(r[2]))}", end=" ")
            print(f"{'{:<15.0f}'.format( len([i for i in r[2] if i>0])  )}", end=" ")
            print(f"{'{:>10.2f}'.format(stat.mean(r[2]))}")
        print(f"{63*'-'}")

#-----------------------------------------------------------------------*
# dummy function to load a collection of donors
#-----------------------------------------------------------------------*
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
            ['Wade','Boggs',5000.15],
            ['Wade','Boggs',125.55],
            ['Wade','Boggs',1000.00],
            ['Ted','Williams',333.45],
            ['Jim','Rice',225.98],
            ['Jim', 'Rice', 125.19],
            ['Jim', 'Rice', 352.76] ]
    for i in data:
        donors.read_data(i[0],i[1],i[2])



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
            return donor_list.read_data(donor[1].fnam, donor[1].lnam, amt[1])
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
                              f"bringing your total donations to {sum([i for i in donor[1].donation])}.\n\nSincerly,\nmanagment\n"
                              f"{'-'*100}")

                    return True


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
def main_menu():
    """
    Entry point into app.
    :return: Bool - true to continue, False to quit
    """
    msg="**Welcome to MailRoom**\nPlease select from the following actions\n\n\t(1)Send a thank you\n\t(2)Create a report\n\t(3)Quit\n\nSelect"
    action=prompt_user(msg)
    if action[0]:
        if action[1] in ['1','2','3']:
            if action[1]=='1':
                ty=send_thankyou()
                return ty
            elif action[1]=='2':
                rc=report(donor_list)
                return rc
            else:
                print("Closing...")
                return False


if __name__ == '__main__':
    # -----------------------------------------------------------------------*
    # seed the database
    # -----------------------------------------------------------------------*
    donor_list=Donors()
    load_default(donor_list)

    # -----------------------------------------------------------------------*
    # Prompt for action
    # -----------------------------------------------------------------------*
    status=True
    while status==True:
        status=main_menu()




