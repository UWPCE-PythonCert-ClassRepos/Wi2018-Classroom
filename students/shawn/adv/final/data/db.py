from peewee import *
import os

dbf=os.path.join(os.path.dirname(__file__),'fmt.db')
database = SqliteDatabase(dbf)
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

class BaseModel(Model):
    class Meta:
        database = database

class Category(BaseModel):
    """
    Table to hold the SAS program template details
    """
    category=CharField(max_length=3)
    inval=CharField(max_length=32)
    outval=CharField(max_length=32)
    desc=CharField(max_length=1000)

database.create_tables([
        Category
    ])
database.close()