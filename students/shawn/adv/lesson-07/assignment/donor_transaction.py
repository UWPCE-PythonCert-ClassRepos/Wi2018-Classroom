from peewee import *
from assignment.donor import Donation,Donor
import datetime

def seed():
    players=[
        ('Bill','Buckner', [1000.25,2300,300,950,250.25]),
        ('Don', 'Baylor', [1141.5,350.33]),
        ('Wade', 'Boggs', [5000.15,125.55, 1000]),
        ('Ted', 'Williams', [333.45]),
        ('Jim', 'Rice', [225.98,125.19,352.76])]

    try:

        database = SqliteDatabase('../assignment/data/donor.db')
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        # Clear the database
        for i in Donor.select():
            i.delete_instance()
        for i in Donation.select():
            i.delete_instance()

        # load the database
        for player in players:
            with database.transaction():
                new_donor = Donor.create(
                    fnam=player[0],
                    lnam=player[1],
                )
                new_donor.save()

                for d in player[2]:
                    new_donation=Donation.create(
                        donation_amount=d,
                        donation_date=datetime.datetime.now(),
                        donor=new_donor
                    )
                    new_donation.save()

        # Dislay the contents of the database and aggregate by total donation
        display()

        #Update a single record
        bill=Donor.get(Donor.fnam=="Bill")
        bill.fnam="William"
        bill.save();

        q=Donor.update(fnam='Billy').where(Donor.fnam=='William')
        q.execute()

        #update muliptle records
        for d in bill.donation:
            if d.donation_amount <1000:
                d.donation_amount *= 500;
                d.save()

        display()

        # qry=Donor.delete().where(sum(Donor.donation.donation_amount) < 2000)
        # qry.execute()

        # delete records
        donor=Donor.get(Donor.fnam=='Wade')
        donor.delete_instance()


        display()


    except Exception as e:
        print(e.args)

    finally:
        database.close()



def display():
    print("\n======= Select All ========")
    qry = (Donor.select( (Donor.fnam + " " + Donor.lnam).alias('name'),
                        Donation.donation_amount,
                        Donation.donation_date)
           .join(Donation)
           .order_by(Donor.fnam)
           )

    [print(f"{i.name} has the following donations: {i.donation.donation_amount} on {i.donation.donation_date}") for i in qry]

    print("\n======= Select by descending donation total ========")
    qry2 = (
            Donor.select( (Donor.fnam + " "+ Donor.lnam).alias("donor"),fn.SUM(Donation.donation_amount).alias("total"))
           .join(Donation)
           .group_by(Donor.fnam , Donor.lnam)
           .order_by(fn.SUM(Donation.donation_amount).desc())
           )

    [print(f"{i.donor} total donation: {i.total}") for i in qry2]

if __name__ == '__main__':
    seed()
