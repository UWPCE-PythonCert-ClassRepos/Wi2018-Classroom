from mailroom import Donors,Donor

def ui(msg,limit=3):
    """
    Display the prompt to user for [limit] times then cancels
    :param msg: (str) Message to display to user
    :param limit: number of times to accept null repsonse before terminating
    :return: (list) [0](bool) -if response was provided [1](str) the user response
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

def send_thankyou(donors):
    """
    Accepts arguments and sends to donor.thankyou method
    :param donors: Donor
    :return: None
    """
    recipient=ui("Enter the name of the donor to thank")
    if recipient[0]:
        k=Donor.make_key(recipient[1])
        donor=donors.get(k)
        if donor:
            print(donor.send_message())
        else:
            add_new=ui("Would you like to add this new donor to the database and send a thank you? (Y/N)")
            if add_new[0]:
                if add_new[1].lower()=="y":
                    add_new_donor(donors,recipient[1])
    call_main()

def add_new_donor(donors,name):
    """
    Accepts arguments for the add new donor method
    :param donors: Donor
    :param name: (str) Name of the new donor
    :return: None
    """
    if not name:
        recipient = ui("Enter the name of the donor to thank")
        if recipient[0]:
            name=recipient[1]
        else:
            return None

    donation=ui(f"Enter a donation amount for {name}")
    if donation[0]:
        full_name = name.split()
        fnam = " ".join(full_name[:1])
        lnam = " ".join(full_name[1:])
        donor=Donor(fnam,lnam,float(donation[1]))
        Donors.new_or_append(donors,donor)
        print(donor.send_message())
    call_main()

def challenge(donors):
    """
    Mutiplies donor.donations in range [ll-ul] by [factor] and calls report to display new donations stats
    :param donors: Donors
    :return: None
    """
    factor=ui("Enter a factor by which to jack up your donation")
    if factor[0]:
        don_range=ui("Enter the range for donations in format [upper]-[lower] or 'all' to include all values")
        if don_range[0]:
            if don_range[1]=="all":
                report(Donors.challenge(donors,int(factor[1])),title=f"All donations increased by a factor of {factor[1]}")
            else:
                vals=don_range[1].split("-")
                ll=int(vals[0])
                ul=int(vals[1])
                report(Donors.challenge(donors,int(factor[1]),ll,ul),f"Donations between {ll} and {ul} increased by {factor[1]}")

def report(donors,title=None):
    """
    CAlls the Donors.report method
    :param donors:  Donors
    :param title: (str) Optional title for report
    :return: (str) message about results
    """
    if title:
        print(donors.send_report(title=title))
    else:
        print(donors.send_report())
    call_main()

def call_main():
    dd = {"1": send_thankyou,"2": report,"3":challenge,"4":close}
    main_menu("**Welcome to MailRoom**\nPlease select from the following actions\n\n\t(1)Send a thank you\n\t(2)Create a report\n\t(3)Jack up the donations\n\t(4)Quit\n\nSelect",dd)

def main_menu(msg,disp,testarg=0):

        selection=ui(msg)
        if selection[0]:
            return disp[selection[1]](donors)

def close(*args,**kwargs):
    print("Closing...")
    return False
import datetime

if __name__ == '__main__':

    donors = Donors()
    Donors.load(donors, "data.csv")
    call_main()



