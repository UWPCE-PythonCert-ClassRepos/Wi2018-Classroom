import csv
from peewee import *
from data.db import Category
import os


def seed_db():
    """
    Read the source data CSV file into the SQLite database
    :return: none
    """
    dbf = os.path.join(os.path.dirname(__file__), 'fmt.db')
    database = SqliteDatabase(dbf)
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    for i in Category.select():
        i.delete_instance()

    file=os.path.join(os.path.dirname(__file__),'format.csv')
    with open(file, 'rU') as f:
        reader = csv.reader(f)
        next(reader, None)
        for r in reader:
            new_fmt=Category(
                category=r[0].strip(),
                inval=r[1].strip(),
                outval=r[2].strip(),
                desc=r[3].strip()
            )
            new_fmt.save()
seed_db()


def fmt_dict():
    """
    Program template data for generation of format.sas program file
    :return: Contents of the category table as dictionary
    """
    fmt={}

    dbf = os.path.join(os.path.dirname(__file__), 'fmt.db')
    database = SqliteDatabase(dbf)
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    for r in Category.select():
        fmt[r.category.strip()]=(r.inval.strip(),r.outval.strip(),r.desc.strip())
    return fmt











