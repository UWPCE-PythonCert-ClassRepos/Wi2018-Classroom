from peewee import *


database = SqliteDatabase('../assignment/data/donor.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

class BaseModel(Model):
    class Meta:
        database = database

class Donor(BaseModel):
    """
    Donor
    """
    fnam=CharField(max_length=50)
    lnam=CharField(max_length=50)

class Donation(BaseModel):
    """
    Donatations
    """

    donation_amount= DecimalField(max_digits = 7, decimal_places = 2)
    donation_date = DateField(formats = 'YYYY-MM-DD')
    donor = ForeignKeyField(Donor,backref="donation")


database.create_tables([
        Donor,
        Donation
    ])

database.close()