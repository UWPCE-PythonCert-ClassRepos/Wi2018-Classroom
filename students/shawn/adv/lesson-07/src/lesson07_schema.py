from peewee import *


database = SqliteDatabase('../src/data/personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    person_name = CharField( max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)

class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """

    job_name = CharField( max_length = 30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
    person = ForeignKeyField(Person,backref="jobs")

class Dept(BaseModel):
    """

    """
    dept_num = CharField( max_length = 4)
    dept_name = CharField(max_length = 30)
    job = ForeignKeyField(Job,backref="depts")

database.create_tables([
        Job,
        Person,
        Dept
    ])

database.close()
