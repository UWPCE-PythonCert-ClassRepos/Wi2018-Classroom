from peewee import *
import os.path

database = SqliteDatabase('donor_database.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database

class Donor(BaseModel):
    """
    This class defines the donor.  Their name and ID will
    be stored in this class
    """
    donor_email = CharField(primary_key = True, max_length = 100)
    first_name = CharField(max_length = 100)
    last_name = CharField(max_length = 100)
    combined_name = CharField(max_length = 200)

class Donation(BaseModel):
    invoice = IntegerField(primary_key = True)
    donor_email = ForeignKeyField(Donor, related_name = 'belongs_to', null = False)
    amount = FloatField()

database.create_tables([Donor, Donation])
database.close()
