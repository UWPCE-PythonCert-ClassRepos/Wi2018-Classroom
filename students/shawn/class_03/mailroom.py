import statistics as stat
import math as m
#-----------------------------------------------------------------------*
# Classes to manage the interactions with database
#-----------------------------------------------------------------------*
class Donor(object):
    """Class to hold instances of each donor
        Methods:
         str - override default behavior to return a formatted string
         add_donation - append a donation to donation list for existing donor
        Properties:
         keyval - return unique key for Donor
    """
    def __init__(self, fnam,lnam,donation=0):
        self.fnam = fnam
        self.lnam = lnam
        self.donation = [donation]

    def __str__(self):
        return f"{self.fnam} {self.lnam} has {len([i for i in self.donation if i>0])} donations totalling {sum([i for i in self.donation])}"

    def add_donation(self,donation):
        self.donation.append(float(donation))

    @property
    def keyval(self):
        return self.fnam.lower() + self.lnam.lower()

class Donors(object):
    """Class to hold dictionary of instances of edonor
         Methods:
          get_or_create - accept: instance of Donor and either add to dictionary for new or append donation for existing
                          return: Donor, bool (true if added)
          read_data - accept: arguments for Donor, passes to call get_or_create
                      return: status message string
          get - accept: dictionary key
              - return: true if exist, else false
     """
    def __init__(self):
        self.donors={}

    def get_or_create(self,donor):
        k=donor.keyval
        if k not in self.donors:
            self.donors[k]=donor
            return donor,True
        return self.donors[k],False

    def read_data(self,fnam,lnam,donation=0):
        d=Donor(fnam,lnam,donation)
        donor,created=self.get_or_create(d)
        if created:
            return True,donor
        else:
            donor.add_donation(donation)
            return False,donor

    def get(self,k):
        return k in self.donors,self.donors.get(k)

    def report(self):
        result=[]
        for i,v in self.donors.items():
            line=[]
            line.append(v.fnam)
            line.append(v.lnam)
            line.append(v.donation)
            result.append(line)

        print(f"{'{:<25}'.format('Donor')}{'{:^10}'.format('Total')}{'{:>20}'.format('Average')}")
        print(f"{57*'-'}")
        for r in result:
            print(f"{'{:<25}'.format(r[0] + ' ' + r[1])}",end=" ")
            print(f"{'{:^10.2f}'.format(sum(r[2]))}", end=" ")
            print(f"{'{:>20.2f}'.format(stat.mean(r[2]))}")


#-----------------------------------------------------------------------*
# dummy function to load a collection of donors
#-----------------------------------------------------------------------*
def load_default(donors):
    """Load the default list of users in Donor collection
            donors  - List of Donor class.
    """
    data = [['Bill', 'Buckner', 1000.25],
            ['Bill', 'Buckner', 2300.00],
            ['Bill', 'Buckner', 300.33],
            ['Bill', 'Buckner', 950.00],
            ['Bill', 'Buckner', 250.25],
            ['Don', 'Baylor', 1141.50]]
    for i in data:
        donors.read_data(i[0],i[1],i[2])



#-----------------------------------------------------------------------*
# Prompt user for arg
#-----------------------------------------------------------------------*
def prompt_user(msg,limit=3):
    """Return console input from the user
       msg - message to display to the user
       limit - number of times to prompt user before terminating
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
    k=user.replace(" ","").lower()
    donor=dlist.get(k)
    if dlist.get(k)[0]:
        amt=prompt_user(f"Enter the donation amount for {user}")
        if amt[0]:
            return dlist.read_data(donor[1].fnam,donor[1].lnam,amt[1])
    else:
        is_add=prompt_user(f"Would you like to add '{user}' to the database? (Y/N)")
        if is_add[0]:
            if is_add[1].upper()=="Y":
                new_donor=dlist.read_data(user.split(" ")[0],user.split(" ")[1])
                return get_user(new_donor[1].fnam + new_donor[1].lnam)

# -----------------------------------------------------------------------*
# Prompt user for arg
# -----------------------------------------------------------------------*
def send_thankyou():
    while True:
        user=prompt_user("Enter the full name of the donor you with to thank (type 'list' to view donors)")
        if user[0]:
            if user[1].lower()=="list":
                for i, v in dlist.donors.items():
                    print(v)
            else:
                donor=get_user(user[1])
                if donor != None:
                    print(f"\n\nDearest {donor[1].fnam},\n\nThank for your latest donation of {donor[1].donation[-1]}, bringing your total donations to {sum([i for i in donor[1].donation])}.\n\nSincerly,\nmanagment")

                break

# -----------------------------------------------------------------------*
# Write report
# -----------------------------------------------------------------------*
def report(donors):
    report=donors.report()




if __name__ == '__main__':
    # -----------------------------------------------------------------------*
    # seed the database
    # -----------------------------------------------------------------------*
    dlist=Donors()
    load_default(dlist)

    # -----------------------------------------------------------------------*
    # Prompt for action
    # --------------------------------------------------------------------
    msg="\t(1)Send a thank you\n\t(2)Create a report\n\t(3)Quit\nSelect an action"
    action=prompt_user(msg)
    if action[0]:
        if action[1] in ['1','2','3']:
            if action[1]=='1':
                ty=send_thankyou()
            elif action[1]=='2':
                report(dlist)
