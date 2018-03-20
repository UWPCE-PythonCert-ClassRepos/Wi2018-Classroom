from mailroom import Donors,Donor
import numbers

def ui(msg,limit=3):
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
    recipient=ui("Enter the name of the donor to thank")
    if recipient[0]:
        k=Donor.make_key(recipient[1])
        donor=donors.get(k)
        if donor:
            try:
                donor.send_message()
            except Exception as e:
                return e.args
        else:
            add_new=ui("Would you like to add this new donor to the database? (Y/N)")
            if add_new[0]:
                if add_new[1].lower()=="y":
                    add_new_donor(donors,recipient[1])
    call_main()

def add_new_donor(donors,name):
    if not name:
        recipient = ui("Enter the name of the donor to thank")
        if recipient[0]:
            name=recipient[1]
        else:
            return

    donation=ui(f"Enter a donation amount for {name}")
    if donation[0]:
        try:
            full_name = name.split()
            fnam = " ".join(full_name[:1])
            lnam = " ".join(full_name[1:])
            donor=Donor(fnam,lnam,float(donation[1]))
            Donors.new_or_append(donors,donor)
            print("Message sent...\n\n")
            donor.send_message()
        except Exception as e:
            print("ERROR: message not sent: " + e.args)
    call_main()


def report(donors):
    donors.send_report()

def call_main():
    dd = {"1": send_thankyou,"2": report,"3":close}
    main_menu("**Welcome to MailRoom**\nPlease select from the following actions\n\n\t(1)Send a thank you\n\t(2)Create a report\n\t(3)Quit\n\nSelect",dd)

def main_menu(msg,disp,testarg=0):

        selection=ui(msg)
        if selection[0]:
            return disp[selection[1]](donors)

def close(*args,**kwargs):
    print("Closing...")
    return False


if __name__ == '__main__':
    donors = Donors()
    Donors.load(donors, "data.csv")
    call_main()



