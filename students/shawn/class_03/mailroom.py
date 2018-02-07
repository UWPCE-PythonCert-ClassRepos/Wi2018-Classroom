# data
class Donor(object):
    def __init__(self, fname,lname,donation):
        self.fname = fname
        self.lname = lname
        self.donation = [donation]

    def __str__(self):
        return self.fname

    def add_donation(self,donation):
        self.donation.append(donation)

    @property
    def keyval(self):
        return self.fname + self.lname

class Donors(object):
    def __init__(self):
        self.donors={}

    def get_or_create(self,donor):
        k=donor.keyval
        if k not in self.donors:
            self.donors[k]=donor
            return donor,True
        return self.donors[k],False

    def read_data(self,fnam,lnam,donation):
        d=Donor(fnam,lnam,donation)
        donor,created=self.get_or_create(d)

        if created:
            return f"{donor.fname} was added to the database"
        else:
            donor.add_donation(donation)
            return f"Donation recorded for {donor.fname}"

#------------------------------------------------------------------------*
#
#------------------------------------------------------------------------*
       # ['Bill', 'Buckner', 300.33],
       #      ['Bill', 'Buckner', 950.00],
       #      ['Bill', 'Buckner', 250.25],

def load_default(donors):
    """Load the default list of users in Donor collection"""
    data = [['Bill', 'Buckner', 1000.25],
            ['Don', 'Baylor', 1141]]
    for i, v in enumerate(data):
        print(v)


ds = Donors()
ds.read_data("a","b",200)

print(ds)







# for k,v in ds.donors.items():
#     print(k,v)
# print(test)
# donors.read_data((v[0], v[1], v[2]))

#-----------------------------------------------------------------------*
# Prompt user for arg
#-----------------------------------------------------------------------*
def prompt_user(msg,limit=3):
    """Return console input from the user"""
    counter=0
    while True:
        counter+=1
        arg=input(f"{msg} >>")
        if len(arg)>0:
            return [True,arg]
        if counter==limit:
            print("We are done here")
            return [False, ""]

#-----------------------------------------------------------------------*
# Lookup user or call add user for new user
#-----------------------------------------------------------------------*
def get_user(user):


    if user in data:
        return user
    else:
        prompt_user(f"{user} is not in database. Do you wish to add {user}?")
        # add_user(user)
#-----------------------------------------------------------------------*
# Prompt user for arg
#-----------------------------------------------------------------------*
def add_user(user):
    is_yn,yn=prompt_user(f"Do you really want to add {user} to the database? (Y/N)")
    if is_yn[0]:
        if str(is_yn[1]).upper()=="Y":
            val=prompt_user(f"How much is {is_yn[1]} donating?")
            if val[0]:
                print(f"{user} added to the database")




# -----------------------------------------------------------------------*
# Prompt user for arg
# -----------------------------------------------------------------------*
def send_thankyou():
    user=prompt_user("Who would you like to thank?")
    if user[0]:
        get_user(user[1])



#
# if __name__ == '__main__':
#
#     msg="\t(1)Send a thank you\n\t(2)Create a report\n\t(3)Quit\nSelect an action"
#     action=prompt_user(msg)
#     if action[0]:
#         if action[1] in ['1','2','3']:
#             if action[1]=='1':
#                 ty=send_thankyou()
#
